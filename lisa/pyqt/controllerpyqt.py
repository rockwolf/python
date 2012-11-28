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
        self.gui.btn_clear.connect(
            self.gui.btn_clear, 
            QtCore.SIGNAL("clicked()"), 
            self.btn_clear_clicked)
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
    def btn_execute_clicked(self):
        """ Write given input lines from table to database. """
        self.ctl.write_to_database(self.table.tablecontent)
        self.table.clear()
        
    def btn_exit_clicked(self):
        """ Exit """
        self.clear_inputbuffer()
        sys.exit(0)

    def btn_clear_clicked(self):
        """ Clear the command buffer. """
        self.clear_inputbuffer()
    
    def btn_add_clicked(self):
        """ Create the command to send to clipf and add it to the buffer. """
        self.ctl.add_tbl_summary(self.table, self.ctl.get_input_line(self.table))
        self.clear_fields()
        self.gui.cmb_subcategory.setCurrentIndex(0)

    def btn_update_clicked(self):
        """ Update the selected record in the table. """
        selected_index = self.table.selectionModel().selectedRows()
        print('Test:', str(selected_index))
        self.table.update_row(self.table, selected_index)

    def btn_remove_clicked(self):
        """ Remove the selected record in the table. """
        #TODO: get the table row to get the index
        selected_index = -1
        self.ctl.remove_selected(self.table, selected_index) 
    
    def btn_removelast_clicked(self):
        """ Remove the last added record from the table. """
        self.ctl.remove_last(self.table)

    # Events
    def cmb_category_changed(self, selstr):
        """ When the category combo selection changes. """
        self.process_category_changed(selstr)

    def cmb_subcategory_changed(self, selstr):
        """ When the subcategory combo selection changes. """
        self.process_subcategory_changed(selstr)
        
    def process_category_changed(self, selstr):
        """ When the category combo selection changes. """
        #TODO: limit the cominations = also need to improve the gui behaviour
        subcategory = self.gui.cmb_subcategory.currentText()
        self.toggle_stockinputs()
    
    def process_subcategory_changed(self, selstr):
        """ When the subcategory combo selection changes. """
        self.gui.txt_comment.setEnabled(True)
        self.toggle_stockinputs()

    def toggle_stockinputs(self):
        """ Enable/disable all inputs related to stock information """
        category = self.gui.cmb_category.currentText()
        subcategory = self.gui.cmb_subcategory.currentText()
        if deals_with_stocks(category, subcategory):
            # enable stock inputs
            self.gui.cmb_market_code.setEnabled(True)
            self.gui.txt_market_description.setEnabled(True)
            self.gui.cmb_stock_name.setEnabled(True)
            self.gui.txt_stock_description.setEnabled(True)
            self.gui.spn_quantity.setEnabled(True)
            self.gui.spn_price.setEnabled(True)
            self.gui.spn_commission.setEnabled(True)
            self.gui.spn_tax.setEnabled(True)
            if is_a_trade(category, subcategory):
                self.gui.spn_risk.setEnabled(True)
                self.gui.dt_expiration.setEnabled(True)
            else:
                self.gui.spn_risk.setEnabled(False)
                self.gui.dt_expiration.setEnabled(False)
            # set inputfields
            self.gui.spn_tax.setValue(Decimal(self.config.default_tax))
            if is_a_trade(category, subcategory):
                self.gui.spn_risk.setValue(Decimal(self.config.default_risk))
            else:
                self.gui.spn_risk.setValue(0.0)
            #TODO: automatic calculation of commission temporarily disabled
            self.gui.chk_manual_commission.setEnabled(False)
        else:
            # disable stock inputs
            self.gui.cmb_market_code.setEnabled(False)
            self.gui.txt_market_description.setEnabled(False)
            self.gui.cmb_stock_name.setEnabled(False)
            self.gui.txt_stock_description.setEnabled(False)
            self.gui.spn_quantity.setEnabled(False)
            self.gui.spn_price.setEnabled(False)
            self.gui.spn_commission.setEnabled(False)
            self.gui.spn_tax.setEnabled(False)
            self.gui.spn_risk.setEnabled(False)
            self.gui.dt_expiration.setEnabled(False)
            # reset input fields
            self.gui.spn_quantity.setValue(0.0)
            self.gui.spn_price.setValue(0.0)
            self.gui.spn_tax.setValue(0.0)
            self.gui.spn_commission.setValue(0.0)
            self.gui.spn_risk.setValue(0.0)
            self.gui.chk_manual_commission.setEnabled(False)
        self.ctl.set_infodetails()

    def cmb_stock_name_changed(self):
        """ When the stock name selection changes. """    
        self.ctl.filltxt_stock_description()
        self.ctl.set_infodetails()        
        
    def cmb_market_code_changed(self):
        """ When the market_code combo selection changes. """
        self.ctl.fillcmb_stock_name()
        self.ctl.filltxt_market_description()
    
    def init_tbl_summary(self):
        """ Initialize tbl_summary. """
        # set the table header
        # TODO: set header values in mdlconstants and use the constants
        header = ['date', 'account', 'category', 'subcategory', 'amount',
                'comment', 'stock', 'stock_description', 'market',
                'market_description', 'quantity', 'price',
                'commission', 'tax', 'risk', 'currency', 'exchange_rate',
                'manual_flag', 'expires_on']
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
        # fill all combo boxes
        self.ctl.fillcombos()
        # default values
        self.set_default_account()
        self.set_default_exchange_rate()
        self.set_default_currency()
        # Init tbl_summary
        self.init_tbl_summary()

    # Clear fields
    def clear_inputbuffer(self):
        """ Clears the table that contains the data. """
        self.table.clear()

    def clear_fields(self):
        """ Clear the main input fields. """
        self.gui.txt_comment.clear()
        self.gui.spn_amount.setValue(0)

    def clear_cmb_stock_name(self):
        """ Clear the cmb_stock_name combobox. """
        self.gui.cmb_stock_name.clear()

    # Getters and setters
    def get_date(self):
        """ Returns the date from the date-picker. """
        return str(self.gui.dt_date.date().toString(QtCore.Qt.ISODate))

    def get_account(self):
        """ Returns the account name from the cmb_account combobox. """
        return str(self.gui.cmb_account.currentText())

    def get_category(self):
        """ Returns the category name from the cmb_category combobox. """
        return str(self.gui.cmb_category.currentText())
    
    def get_subcategory(self):
        """ Returns the subcategory name from the cmb_subcategory combobox. """
        return str(self.gui.cmb_subcategory.currentText())
    
    def get_amount(self):
        """ Returns the amount from the spn_amount spinedit. """
        return str(self.gui.spn_amount.textFromValue( \
                self.gui.spn_amount.value()))

    def get_comment(self):
        """ Returns the comment text. """
        return str(self.gui.txt_comment.text())

    def get_market_code(self):
        """ Returns the market_code. """
        return str(self.gui.cmb_market_code.currentText())
    
    def get_market_description(self):
        """ Returns the market description. """
        return str(self.gui.txt_market_description.text())

    def get_stock_name(self):
        """ Returns the stock_name. """
        return str(self.gui.cmb_stock_name.currentText())

    def get_stock_description(self):
        """ Returns the stock description. """
        return str(self.gui.txt_stock_description.text())

    def get_quantity(self):
        """ Returns the quantity from the spn_quantity spinedit. """
        return str(self.gui.spn_quantity.textFromValue( \
                self.gui.spn_quantity.value()))

    def get_price(self):
        """ Returns the price from the spn_price spinedit. """
        return str(self.gui.spn_price.textFromValue( \
                self.gui.spn_price.value()))

    def get_commission(self):
        """ Returns the commission from the spn_commission spinedit. """
        return str(self.gui.spn_commission.textFromValue( \
                self.gui.spn_commission.value()))

    def get_tax(self):
        """ Returns the tax from the spn_tax spinedit. """
        return str(self.gui.spn_tax.textFromValue( \
                self.gui.spn_tax.value()))

    def get_risk(self):
        """ Returns the risk from the spn_risk spinedit. """
        return str(Decimal(self.gui.spn_risk.textFromValue( \
                self.gui.spn_risk.value()))/100)
                
    def get_currency(self):
    	""" Returns the currency used. """
    	return str(self.gui.cmb_currency.currentText())
    	
    def get_exchange_rate(self):
    	""" Returns the exchange rate used. """
    	return str(self.gui.spn_exchange_rate.textFromValue( \
    		self.gui.spn_exchange_rate.value()))

    def get_manual_commission(self):
        """ Returns the value of the manual commission calc. checkbox """
        return '0' if self.gui.chk_manual_commission.isChecked() else '1' 
        
    def get_date_expiration(self):
    	""" Returns the value of the dt_expiration date picker. """
    	return str(self.gui.dt_expiration.date().toString(QtCore.Qt.ISODate))

    def set_infodetails(self, value):
       """ Sets new info on the lbl_infodetails label. """
       self.gui.lbl_infodetails.setText(value)

    def set_market_description(self, value):
       """ Sets new info on txt_market_description. """
       self.gui.txt_market_description.clear()
       self.gui.txt_market_description.setText(value)

    def set_stock_description(self, value):
       """ Sets new info on txt_stock_description. """
       self.gui.txt_stock_description.clear()
       self.gui.txt_stock_description.setText(value)
   
    def add_stock_name(self, value):
       """ Add a new item to cmb_stock_name. """
       self.gui.cmb_stock_name.addItem(value)

    def add_category(self, value):
       """ Add a new item to cmb_category. """
       self.gui.cmb_category.addItem(value)

    def add_subcategory(self, value):
       """ Add a new item to cmb_subcategory. """
       self.gui.cmb_subcategory.addItem(value)

    def add_account(self, value):
       """ Add a new item to cmb_account. """
       self.gui.cmb_account.addItem(value)

    def add_market_code(self, value):
       """ Add a new item to cmb_market_code. """
       self.gui.cmb_market_code.addItem(value)
       
    def set_default_account(self):
        """ Select the default account. """
        index = int(self.config.default_account)-1
        self.set_combo_selection(index, self.gui.cmb_account)

    def set_default_currency(self):
        """ Set the default currency value at startup. """
        index = int(self.config.default_currency)-1
        self.set_combo_selection(index, self.gui.cmb_currency)

    def set_default_exchange_rate(self):
        """ Set the default exchange rate value at startup. """
        self.gui.spn_exchange_rate.setValue(Decimal(self.config.default_exchange_rate))

    def set_combo_selection(self, index, combobox):
        """ Sets a combobox selection. """
        if index > 0:
            combobox.setCurrentIndex(index)

    def add_currency(self, value):
        """ Add a new item to cmb_currency. """ 
        self.gui.cmb_currency.addItem(value)

