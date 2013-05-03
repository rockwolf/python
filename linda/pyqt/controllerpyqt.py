#!/usr/env/python
"""
    See LICENSE file for copyright and license details.					
"""

import sys
from PyQt4 import QtCore, QtGui
from decimal import Decimal

from pyqt.viewpyqt import Ui_MainWindow
from pyqt_generic.tablemodel import TableModel
from modules.function import *

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
        self.gui.cmb_market_code.connect(
            self.gui.cmb_market_code, 
            QtCore.SIGNAL('currentIndexChanged(int)'), 
            self.cmb_market_code_changed)
        self.gui.cmb_stock_name.connect(
            self.gui.cmb_stock_name, 
            QtCore.SIGNAL('currentIndexChanged(int)'), 
            self.cmb_stock_name_changed)
        self.gui.btn_exit.connect(
            self.gui.btn_execute, 
            QtCore.SIGNAL("clicked()"), 
            self.btn_execute_clicked)
        self.gui.btn_reset.connect(
            self.gui.btn_reset, 
            QtCore.SIGNAL("clicked()"), 
            self.btn_reset_clicked)
        self.gui.btn_update.connect(
            self.gui.btn_update, 
            QtCore.SIGNAL("clicked()"), 
            self.btn_update_clicked)
        self.gui.btn_remove.connect(
            self.gui.btn_remove, 
            QtCore.SIGNAL("clicked()"), 
            self.btn_remove_clicked)
        self.gui.btn_removelast.connect(
            self.gui.btn_removelast, 
            QtCore.SIGNAL("clicked()"), 
            self.btn_removelast_clicked)

    # Button Events
    def btn_exit_clicked(self):
        """ Exit """
        self.clear_inputbuffer()
        sys.exit(0)

    def btn_reset_clicked(self):
        """ Clear the input buffer. """
        self.clear_inputbuffer()
    
    def btn_update_clicked(self):
        """ Update the selected record in the table. """
        selected_index = self.table.selectionModel().selectedRows()
        print('Test:', str(selected_index))
        self.table.update_row(self.table, selected_index)

    # Events
    def init_tbl_summary(self):
        """ Initialize tbl_summary. """
        # set the table header
        # TODO: set header values in mdlconstants and use the constants
        header = ['account', 'date_start', '', '', '',
                'date_created', 'date_modified']
        self.table = TableModel(header, [], 0, len(header))
        # takeAt(0) removes the default empty table that's there and addWidget
        # adds a newly created one.
        self.gui.vl_table.takeAt(0)
        self.gui.vl_table.addWidget(self.table)

    def init_gui(self):
        """ Initialise fields """
        # Info labels
        self.gui.lbl_infofinance.clear()
        self.gui.lbl_infofinance.setText('>> ' + self.config.exportdir)
        self.gui.lbl_infodetails.clear()
        self.set_lbl_check(self.ctl.get_check_info([]))
        # fill all combo boxes
        self.ctl.init_display_data()
        # default values
        self.set_default_account()
        # Init tbl_summary
        self.init_tbl_summary()

    # Getters and setters
    def get_account(self):
        """ Returns the account name from the cmb_account combobox. """
        return str(self.gui.cmb_account.currentText())

    def add_account(self, value):
       """ Add a new item to cmb_account. """
       self.gui.cmb_account.addItem(value)
