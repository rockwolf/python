#!/usr/env/python
"""
Author: Andy Nagels
Date: 2010-08-24
Lisa: Pyqt gui frontend for a postgresql db, used to store financial data.

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
from decimal import Decimal
from subprocess import Popen, PIPE

from gui.guicode import Ui_frm_main
from database.databaseaccess import DatabaseAccess
from mainhandler import Controller
from modules_generic.tablemodel import TableModel

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
        self.gui.cmb_category.connect(
            self.gui.cmb_category, 
            QtCore.SIGNAL('currentIndexChanged(const QString&)'), 
            self.cmb_category_changed)
        self.gui.cmb_subcategory.connect(
            self.gui.cmb_subcategory, 
            QtCore.SIGNAL('currentIndexChanged(const QString&)'), 
            self.cmb_subcategory_changed)
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
        self.gui.cmb_subcategory.setCurrentIndex(0)

    # Events
    def cmb_category_changed(self, selstr):
        """ When the category combo selection changes. """
        self.process_category_changed(selstr)

    def cmb_subcategory_changed(self, selstr):
        """ When the subcategory combo selection changes. """
        self.process_subcategory_changed(selstr)
        
    def process_category_changed(self, selstr):
        """ When the category combo selection changes. """
        subcategory_ = self.gui.cmb_subcategory.currentText()
        self.toggle_stockinputs()
    
    def process_subcategory_changed(self, selstr):
        """ When the subcategory combo selection changes. """
        self.gui.txt_comment.setEnabled(True)
        self.toggle_stockinputs()

    def toggle_stockinputs(self):
        """ Enable/disable all inputs related to stock information """
        category = self.gui.cmb_category.currentText()
        subcategory_ = self.gui.cmb_subcategory.currentText()
        if((category == 'invest.tx' or category == 'invest.rx' or category == 'trade.tx' or category == 'trade.rx') and ( subcategory_ == 'buy' or subcategory_ == 'sell')):
            # enable stock inputs
            self.gui.cmb_marketcode.setEnabled(True)
            self.gui.txt_marketdescription.setEnabled(True)
            self.gui.cmb_stockname.setEnabled(True)
            self.gui.txt_stockdescription.setEnabled(True)
            self.gui.spn_quantity.setEnabled(True)
            self.gui.spn_price.setEnabled(True)
            self.gui.spn_commission.setEnabled(True)
            self.gui.spn_tax.setEnabled(True)
            if(category == 'trade.tx' or category == 'trade.rx'):
                self.gui.spn_risk.setEnabled(True)
            else:
                self.gui.spn_risk.setEnabled(False)
            # set inputfields
            self.gui.spn_tax.setValue(Decimal(self.config.default_tax))
            if(category == 'trade.tx' or category == 'trade.rx'):
                self.gui.spn_risk.setValue(Decimal(self.config.default_risk))
            else:
                self.gui.spn_risk.setValue(0.0)
        else:
            # disable stock inputs
            self.gui.cmb_marketcode.setEnabled(False)
            self.gui.txt_marketdescription.setEnabled(False)
            self.gui.cmb_stockname.setEnabled(False)
            self.gui.txt_stockdescription.setEnabled(False)
            self.gui.spn_quantity.setEnabled(False)
            self.gui.spn_price.setEnabled(False)
            self.gui.spn_commission.setEnabled(False)
            self.gui.spn_tax.setEnabled(False)
            self.gui.spn_risk.setEnabled(False)
            # reset input fields
            self.gui.spn_quantity.setValue(0.0)
            self.gui.spn_price.setValue(0.0)
            self.gui.spn_tax.setValue(0.0)
            self.gui.spn_commission.setValue(0.0)
            self.gui.spn_risk.setValue(0.0)
        self.ctl.update_info_details()

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
