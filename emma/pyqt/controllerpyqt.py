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
        self.gui.grd_tables.addWidget(self.table_division, 1, 0)
        self.table_division.add_row(['test1', 'test2', 'test3', 'test4'])

    def init_tbl_set_trading(self):
        """ Initialize table division. """
        # set the table header
        # TODO: set header values in mdlconstants and use the constants
        header = ['total', 'defense', 'offense', 'invest']
        self.table_set_trading = TableModel(header, [], 0, len(header))
        self.gui.grd_tables.addWidget(self.table_set_trading, 5, 3)
        self.table_set_trading.add_row(['test1', 'test2', 'test3', 'test4'])

    def print_objects_in_grid(self):
        """ Used for testing. """
        # The below code prints the objects in the grid.
        print('Per row/column:')
        print('---------------')
        rows = self.gui.grd_tables.rowCount()
        columns = self.gui.grd_tables.columnCount()
        for i in range(rows):
            for j in range(columns):
                print(self.gui.grd_tables.itemAtPosition(i,j), i, j)
        print('Per item:')
        print('---------')
        for i in range(self.gui.grd_tables.count()):
            print(self.gui.grd_tables.itemAt(i), i,
                    self.gui.grd_tables.itemAt(i).widget())

    def delete_table_widgets(self, gridlayout):
        """ Deletes table widgets at a certain index in a given gridlayout. """
        print('Delete shit')
        print('-----------')
        for i in range(gridlayout.count()):
            print(i)
            if gridlayout.itemAt(i) is not None:
                if isinstance(gridlayout.itemAt(i).widget(), QtGui.QTableWidget):
                    self.gui.grd_tables.takeAt(i)

    def init_gui(self):
        """ Initialise fields """
        self.gui.tab_main.setCurrentIndex(4)
        self.print_objects_in_grid()
        # Delete tables
        self.delete_table_widgets(self.gui.grd_tables)
        # Init tables
        self.init_tbl_division()
        #self.init_tbl_set_trading()
