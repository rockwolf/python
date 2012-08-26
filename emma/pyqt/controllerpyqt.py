#!/usr/env/python
"""
Author: Andy Nagels
Date: 2012-08-26
Lisa: Pyqt gui frontend for a postgresql db, used to store financial data.

Copyright (C) 2010 Andy Nagels

This file is part of Emma.

Lisa is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Emma is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Emma. If not, see <http://www.gnu.org/licenses/>.
					
"""
from PyQt4 import QtCore, QtGui

from pyqt.viewpyqt import Ui_MainWindow
from pyqt_generic.tablemodel import TableModel

class ControllerPyqt(QtGui.QMainWindow):
    """ Controller that also contains pyqt related code. """
    
    def __init__(self, config, controller):
        """ Construct basic QApplication, add widgets and start exec_loop """
        # initialise special vars
        self.config = config
        # initialize gui
        QtGui.QMainWindow.__init__(self)

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self) 
        self.connectslots()
        self.ctl = controller

    def connectslots(self):
        """ Connect methods to the signals the gui emits """
        self.gui.btn_exit.connect(
            self.gui.btn_exit, 
            QtCore.SIGNAL("clicked()"), 
            self.btn_exit_clicked)

    # Button Events
    def btn_exit_clicked(self):
        """ Exit """
        exit(0)
        
    # Events
    #def cmb_category_changed(self, selstr):
    #    """ When the category combo selection changes. """
    #    self.process_category_changed(selstr)

    def init_tbl_division(self):
        """ Initialize table division. """
        # set the table header
        # TODO: set header values in mdlconstants and use the constants
        header = ['total', 'defense', 'offense', 'invest']
        self.table_division = TableModel(header, [], 0, len(header))
        for i in range(self.gui.grd_tables.count()):
            print(self.gui.grd_tables.itemAt(i), i, self.gui.grd_tables.itemAt(i).widget())
        #self.gui.grd_tables.takeAt(0)
        #self.gui.grd_tables.addWidget(self.table_division)

    def init_gui(self):
        """ Initialise fields """
        # Init tables
        self.init_tbl_division()
