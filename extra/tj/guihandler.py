#!/usr/env/python
"""
Author: Andy Nagels
Date: 2012-03-11
Pyqt gui for showing a trading journal.

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
from guicode import Ui_Dialog
from databaseaccess import DatabaseAccess
from subprocess import Popen, PIPE
from mainhandler import Controller
from tablemodel import TableModel

class GuiHandler(QtGui.QDialog, Ui_Dialog):
    """ Trading Journal, main class """
    
    def __init__(self, config, parent=None):
        """ Construct basic QApplication, add widgets and start exec_loop """
        # initialise special vars
        self.config = config
        # initialize gui
        QtGui.QDialog.__init__(self, parent)
        self.gui = Ui_Dialog()
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
        self.gui.cmb_view.connect(
            self.gui.cmb_view, 
            QtCore.SIGNAL('currentIndexChanged(const QString&)'), 
            self.cmb_view_changed)
        self.gui.btn_update.connect(
            self.gui.btn_update, 
            QtCore.SIGNAL("clicked()"), 
            self.btn_update_clicked)

    # Button Events
    def btn_exit_clicked(self):
        """ Exit """
        sys.exit(0)

    def btn_update_clicked(self):
        """ Update t_trading_journal if necessary and execute. """
        self.ctl.add_inputline()
        self.gui.cmb_object.setCurrentIndex(0)

    # Events
    def cmb_view_changed(self, selstr):
        """ When the product combo selection changes. """
        print('test cmb_view_changed') 

    def initgui(self):
        """ Initialise fields """
