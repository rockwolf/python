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
from os.path import isfile
from subprocess import call
from PyQt4 import QtCore, QtGui
from databaseaccess import DatabaseAccess
from tablemodel import TableModel
import shutil
import os
from decimal import *

class Controller():
    """ Contains the bussiness logic of the application. """
    
    def __init__(self, gui, config):
        """ Construct basic QApplication, add widgets and start exec_loop """
        # initialise special vars
        self.gui = gui #QtGui.QDialog 
        self.config = config #object
        # initialise the command buffer
        self.inputbuffer = []
        # Decimal precision
        getcontext().prec = 4

    # Methods
    ## General
    
    ## Init of gui
    def fillcombos(self):
        """ fill in the combo boxes with values. """
        #dba = DatabaseAccess(self.config)
        #TODO: write code for getting the views (views should be definable in the db or better: the rc
        # = specify which columns to show
        ## Products
        #for prod in dba.get_products():
        #    self.gui.cmb_product.addItem(prod)
        dba = None
        # Init tbl_summary
        self.init_tbl_summary()

    def install(self):
        """ Setup the database through an external script. """
        try:
            call(["sh", "install.sh"])
        except:
            print('Error: could not load install.sh script.')

    def uninstall(self):
        """ Remove all from database through an external script. """
        try:
            call(["sh", "uninstall.sh"])
        except:
            print('Error: could not load uninstall.sh script.')

    def init_tbl_summary(self):
        """ Initialize tbl_summary. """
        # set the table header
        header = ['date', 'account', 'product', 'object', 'amount', 'comment', 'stock', 'market', 'quantity', 'price', 'commission', 'tax']
        data = self.inputbuffer
        self.table = TableModel(header, data, len(data), len(header))
        self.gui.tbl_summary = self.table
        # can't seem to get existing table updating to work,
        # so takeAt(0) removes the table that's there and addWidget
        # adds a newly created one.
        self.gui.glo_summary.takeAt(0)
        self.gui.glo_summary.addWidget(self.table)
