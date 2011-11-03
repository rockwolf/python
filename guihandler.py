#!/usr/env/python
"""
Author: Andy Nagels
Date: 2010-08-24
Lisa: Pyqt gui for clipf, with extra functionality.

Copyright (C) 2010 Andy Nagels

This file is part of Lisa.

Lisa is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lisa is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Lisa. If not, see <http://www.gnu.org/licenses/>.
					
"""
import sys
import shutil
import os
from PyQt4 import QtCore, QtGui
from guicode import Ui_frm_main
from databaseaccess import DatabaseAccess
from subprocess import Popen, PIPE
from mainhandler import Controller
from tablemodel import TableModel

class GuiHandler(QtGui.QDialog, Ui_frm_main):
    """ Less Interaction Saves Arbeit Main Class """
    
    def __init__(self, config, parent=None):
        """ Construct basic QApplication, add widgets and start exec_loop """
        # initialise special vars
        self.config = config
        # initialize gui
        QtGui.QDialog.__init__(self, parent)
        self.gui = Ui_frm_main()
        self.gui.setupUi(self) 
        self.connectslots()
        self.ctl = Controller(self.gui, self.config)
        self.initgui()

    def connectslots(self):
        """ Connect methods to the signals the gui emits """
        self.gui.btn_exit.connect(
            self.gui.btn_exit, 
            QtCore.SIGNAL('clicked()'), 
            self.btn_exit_clicked)
        self.gui.cmb_product.connect(
            self.gui.cmb_product, 
            QtCore.SIGNAL('currentIndexChanged(const QString&)'), 
            self.cmb_product_changed)
        self.gui.cmb_object.connect(
            self.gui.cmb_object, 
            QtCore.SIGNAL('currentIndexChanged(const QString&)'), 
            self.cmb_object_changed)
        self.gui.tab_details.connect(
            self.gui.tab_details, 
            QtCore.SIGNAL('currentChanged(int)'), 
            self.tab_details_changed)
        self.gui.btn_add.connect(
            self.gui.btn_add, 
            QtCore.SIGNAL("clicked()"), 
            self.btn_add_clicked)
        self.gui.cmb_marketcode.connect(
            self.gui.cmb_marketcode, 
            QtCore.SIGNAL('currentIndexChanged(int)'), 
            self.cmb_marketcode_changed)
        self.gui.cmb_stockname.connect(
            self.gui.cmb_stockname, 
            QtCore.SIGNAL('currentIndexChanged(int)'), 
            self.cmb_stockname_changed)
        self.gui.btn_exit.connect(
            self.gui.btn_execute, 
            QtCore.SIGNAL("clicked()"), 
            self.btn_execute_clicked)
        self.gui.btn_clear.connect(
            self.gui.btn_clear, 
            QtCore.SIGNAL("clicked()"), 
            self.btn_clear_clicked)

    # Button Events
    def btn_execute_clicked(self):
        """ Pipe commands to clipf. """
        self.ctl.write_commands()
        
    def btn_exit_clicked(self):
        """ Exit """
        self.ctl.clear_inputbuffer() # dummy pylint test
        sys.exit(0)

    def btn_clear_clicked(self):
        """ Clear the command buffer. """
        self.ctl.clear_inputbuffer()
    
    def btn_add_clicked(self):
        """ Create the command to send to clipf and add it to the buffer. """
        self.ctl.add_inputline()
        self.gui.cmb_object.setCurrentIndex(0)

    # Events
    def cmb_product_changed(self, selstr):
        """ When the product combo selection changes. """
        self.process_product_changed(selstr)

    def cmb_object_changed(self, selstr):
        """ When the object combo selection changes. """
        self.process_object_changed(selstr)
        
    def process_product_changed(self, selstr):
        """ When the product combo selection changes. """
        object_ = self.gui.cmb_object.currentText()
        if((selstr == 'invest.tx' or selstr == 'invest.rx' or selstr == 'trade.tx' or selstr == 'trade.rx') and ( object_ == 'buystocks' or object_ == 'sellstocks')):
            self.gui.tab_details.currentTabName = \
            self.gui.tab_details.setCurrentIndex(1)
            self.ctl.update_info_details()
        else:
            self.gui.tab_details.currentTabName = \
            self.gui.tab_details.setCurrentIndex(0)
    
    def process_object_changed(self, selstr):
        """ When the object combo selection changes. """
        self.gui.txt_comment.setEnabled(True)
        product = self.gui.cmb_product.currentText()
        if((product == 'invest.tx' or product == 'invest.rx' or product == 'trade.tx' or product == 'trade.rx') and ( selstr == 'buystocks' or selstr == 'sellstocks')):
            self.gui.tab_details.currentTabName = \
            self.gui.tab_details.setCurrentIndex(1)
            self.ctl.update_info_details()
            self.gui.spn_tax.setValue(0.17)
        else:
            self.gui.tab_details.currentTabName = \
            self.gui.tab_details.setCurrentIndex(0)

    def tab_details_changed(self, index):
        """ What to do if you change a tab. """
        self.cmb_product_changed(self.gui.cmb_product.currentText())

    def cmb_stockname_changed(self):
        """ When the stock name selection changes. """    
        self.ctl.filltxt_stockdescription()
        self.ctl.update_info_details()        
        
    def cmb_marketcode_changed(self):
        """ When the marketcode combo selection changes. """
        self.ctl.fillcmb_stockname()
        self.ctl.filltxt_marketdescription()
    
    def initgui(self):
        """ Initialise fields """
        # Info labels
        self.gui.lbl_infofinance.clear()
        self.gui.lbl_infofinance.setText('>> ' + self.config.exportfile)
        self.gui.lbl_infodetails.clear()
        # fill all combo boxes
        self.ctl.fillcombos()
        self.gui.cmb_account.setCurrentIndex(0)
