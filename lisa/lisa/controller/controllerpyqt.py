#!/usr/bin/env python
"""
    See LICENSE file for copyright and license details.					
"""

import sys
from PyQt4 import QtCore, QtGui
from decimal import Decimal

import view.viewpyqt
import view.viewpyqt_dialog_emma
import view.viewpyqt_dialog_parameters
from generic.pyqt.tablemodel import TableModel
from generic.modules.function import *
from modules.emma import *
from modules.function import *
from modules.constant import *

class DialogEmma(QtGui.QDialog):
    """
        Subclassing the DialogEmma dialog
        to define the accept.
    """
    def __init__(self, data_general, data_buy, data_sell, parent=None):
        super(DialogEmma, self).__init__(parent)
        self.ui = view.viewpyqt_dialog_emma.Ui_DialogEmma()
        self.ui.setupUi(self)
        # use new style signals
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.txt_general.setText('\n'.join(data_general))
        self.ui.txt_buy.setText('\n'.join(data_buy))
        self.ui.txt_sell.setText('\n'.join(data_sell))
        
    def accept(self):
        super(DialogEmma, self).accept() # call the accept method of QDialog.
                                           # super is needed
                                           # since we just override the accept method

class DialogParameters(QtGui.QDialog):
    """
        Subclassing the DialogParameters dialog
        to define the accept.
    """
    def __init__(self, parent=None):
        super(DialogParameters, self).__init__(parent)
        self.ui = view.viewpyqt_dialog_parameters.Ui_DialogParameters()
        self.ui.setupUi(self)
        # use new style signals
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        header = ['parameter_id', 'name', 'value', 'description']
        table = TableModel(header, [], 0, len(header))
        # takeAt(0) removes the default empty table that's there and addWidget
        # adds a newly created one.
        self.ui.vl_parameters.takeAt(0)
        self.ui.vl_parameters.addWidget(table)

    def accept(self):
        super(DialogParameters, self).accept()


class ControllerPyqt(QtGui.QMainWindow):
    """
        Controller that also contains pyqt related code.
    """
    
    def __init__(self, config, controller):
        """
            Construct basic QApplication, add widgets and start exec_loop
        """
        # initialise special vars
        self.config = config
        # initialize gui
        QtGui.QMainWindow.__init__(self)

        self.gui = view.viewpyqt.Ui_MainWindow()
        self.gui.setupUi(self) 
        self.connectslots()
        self.ctl = controller
        self.model_data = None

    def connectslots(self):
        """
            Connect methods to the signals the gui emits
        """
        self.gui.btn_exit.clicked.connect(self.btn_exit_clicked)
        self.gui.btn_add.clicked.connect(self.btn_add_clicked)
        self.gui.cmb_market_code.currentIndexChanged[int].connect(self.cmb_market_code_changed)
        self.gui.cmb_commodity_name.currentIndexChanged[int].connect(self.cmb_commodity_name_changed)
        #self.gui.cmb_commodity_name.keyPressed.connect(self.cmb_commodity_name_key_pressed)
        self.gui.btn_execute.clicked.connect(self.btn_execute_clicked)
        self.gui.btn_clear.clicked.connect(self.btn_clear_clicked)
        self.gui.btn_update.clicked.connect(self.btn_update_clicked)
        self.gui.btn_remove.clicked.connect(self.btn_remove_clicked)
        self.gui.btn_removelast.clicked.connect(self.btn_removelast_clicked)
        self.gui.btn_emma.clicked.connect(self.btn_emma_clicked)
        self.gui.btn_gnucash.clicked.connect(self.btn_gnucash_clicked)
        self.gui.btn_parameters.clicked.connect(self.btn_parameters_clicked)

    # Button Events
    def btn_execute_clicked(self):
        """
            Write given input lines from table to database.
        """
        self.ctl.write_to_database(self.model_data)
        self.set_lbl_check(self.ctl.get_check_info([]))
        self.model_data.clear()
        
    def btn_exit_clicked(self):
        """
            Exit
        """
        self.clear_inputbuffer()
        sys.exit(0)

    def btn_clear_clicked(self):
        """
            Clear the input buffer.
        """
        self.clear_inputbuffer()
    
    def btn_add_clicked(self):
        """
            Add new input to the input_fields table.
        """
        # Init tbl_data
        input_line = self.ctl.get_input_line()
        if self.model_data == None:
            print '1b_0: init_tbl_data'
            self.init_tbl_data(input_line)
        else: 
            print '1b_1: add_tbl_data'
            self.ctl.add_tbl_data(self.model_data, [input_line])
        print "-1c- test [btn_add_clicked], model_data :", self.model_data.get_values()
        self.clear_fields()
        #self.set_lbl_check(self.ctl.get_check_info(self.model_data.tablecontent))

    def btn_update_clicked(self):
        """
            Update the selected record in the table.
        """
        selected_index = self.gui.tbldata.selectionModel().selectedRows()
        print 'Test:', str(selected_index)
        self.gui.tbl_data.update_row(self.model_data, selected_index)

    def btn_remove_clicked(self):
        """
            Remove the selected record in the table.
        """
        #TODO: get the table row to get the index
        #This currently gets the last row.
        selected_index = self.model_data.rowCount(None)
        self.ctl.remove_selected(self.model_data, selected_index)
        print "-3a- test [btn_remove_clicked], model_data :", self.model_data.get_values()
    
    def btn_removelast_clicked(self):
        """ Remove the last added record from the table. """
        self.ctl.remove_last(self.model_data)
        
    def btn_emma_clicked(self):
        """
            Equations for money management.
        """
        input_line = self.ctl.get_input_line()
        buying = we_are_buying(
            input_line[Input.ACCOUNT_FROM],
            input_line[Input.ACCOUNT_TO])
        #TODO: make sure that price and amount are filled in, to avoid division by zero
        if not (Decimal(input_line[Input.AMOUNT]) == DEFAULT_DECIMAL
            or Decimal(input_line[Input.PRICE]) == DEFAULT_DECIMAL):
            emma = Emma(
                Decimal(input_line[Input.POOL]), #TODO:incorporate a margin entry part (see parameter table!) 
                #
                Decimal(input_line[Input.AMOUNT]),
                Decimal(input_line[Input.TAX]),
                Decimal(input_line[Input.COMMISSION]),
                0, #input_line[Input.SHARES], #TODO: SHARES DOES NOT EXIST
                Decimal(input_line[Input.PRICE]),
                buying,
                input_line[Input.MARKET],
                input_line[Input.COMMODITY],
                input_line[Input.ACCOUNT_FROM],
                Decimal(input_line[Input.RISK]),
                input_line[Input.CURRENCY_FROM],
                Decimal(input_line[Input.EXCHANGE_RATE]),
                #input_line[Input.ESTIMATE])
                0) #TODO: ESTIMATE does not exist
            emma.calculate()
            
            dlg = DialogEmma(
                dict_to_list_sorted(emma.result_general),
                dict_to_list_sorted(emma.result_buy),
                dict_to_list_sorted(emma.result_sell))
            dlg.exec_() # exec_() for modal, show() for non-modal dialog
            
    def btn_gnucash_clicked(self):
        """
            What to enter in GnuCash?
        """
        #TODO: show gnucash entries for all the lines in the table.
        # OR show gnucash info for all lines in the db that have not been entered yet.
        # => add extra column: gnucash with value 0 or 1 (1 = already entered in gnucash)
        pass

    def btn_parameters_clicked(self):
        """
            Equations for money management.
        """
        dlg = DialogParameters()
        dlg.exec_()

    #def cmb_commodity_name_key_pressed(self, qKeyEvent):
    #    """
    #        keyPressed event in combo
    #    """
    #    print 'test:', str(qKeyEevnt)
    #    if qKeyEvent.key() == QtCore.Qt.Key_Return: 
    #        self.ctl.update_accounts_for_commodities(str(self.gui.cmb_commodity_name.currentText()))

    # Events
    def toggle_commodity_inputs(self):
        """
            Enable/disable all inputs related to commodity information
        """
        account_from = self.gui.cmb_account_from.currentText()
        account_to = self.gui.cmb_account_to.currentText()
        is_commodity = deals_with_commodities(account_from, account_to)
        # enable commodity labels
        self.gui.lbl_market_code.setEnabled(is_commodity)
        self.gui.lbl_commodity_name.setEnabled(is_commodity)
        self.gui.lbl_quantity.setEnabled(is_commodity)
        self.gui.lbl_price.setEnabled(is_commodity)
        self.gui.lbl_commission.setEnabled(is_commodity)
        self.gui.lbl_tax.setEnabled(is_commodity)
        self.gui.lbl_risk.setEnabled(is_commodity)
        self.gui.lbl_pool.setEnabled(is_commodity)
        self.gui.lbl_risk.setEnabled(is_commodity)
        self.gui.lbl_expiration.setEnabled(is_commodity)
        # enable commodity inputs
        self.gui.cmb_market_code.setEnabled(is_commodity)
        self.gui.txt_market_description.setEnabled(is_commodity)
        self.gui.cmb_commodity_name.setEnabled(is_commodity)
        self.gui.txt_commodity_description.setEnabled(is_commodity)
        self.gui.spn_quantity.setEnabled(is_commodity)
        self.gui.spn_price.setEnabled(is_commodity)
        self.gui.spn_commission.setEnabled(is_commodity)
        self.gui.spn_tax.setEnabled(is_commodity)
        self.gui.spn_pool.setEnabled(is_commodity)
        #TODO: automatic calculation of commission temporarily disabled
        self.gui.chk_manual_commission.setEnabled(is_commodity)
        self.gui.spn_risk.setEnabled(is_commodity)
        self.gui.dt_expiration.setEnabled(is_commodity)
        # set inputfields
        self.gui.spn_tax.setValue(Decimal(self.config.default_tax))
        self.gui.spn_risk.setValue(Decimal(self.config.default_risk))
        # reset input fields
        self.gui.spn_quantity.setValue(0.0)
        self.gui.spn_price.setValue(0.0)
        self.gui.spn_tax.setValue(0.0)
        self.gui.spn_commission.setValue(0.0)
        self.gui.spn_risk.setValue(0.0)
        self.gui.chk_manual_commission.setEnabled(False)
        self.set_current_pool() #reset pool to current value
        self.ctl.set_info_details()

    def cmb_commodity_name_changed(self):
        """
            When the commodity selection changes.
        """
        self.ctl.filltxt_commodity_description()
        self.ctl.set_info_details()        
        
    def cmb_market_code_changed(self):
        """
            When the market_code combo selection changes.
        """
        self.ctl.fillcmb_commodity_name()
        self.ctl.filltxt_market_description()
    
    def init_tbl_data(self, input_line):
        """
            Initialize tbl_data, with the first input_line
            already added to the model.
        """
        headers = ['date', 'account_from', 'account_to', 'amount',
                'comment', 'commodity', 'commodity_description', 'market',
                'market_description', 'quantity', 'price',
                'commission', 'tax', 'risk', 'currency_from', 'currency_to', 'exchange_rate',
                'automatic_flag', 'expires_on']
        self.model_data = TableModel([input_line], headers)
        self.gui.tbl_data.setModel(self.model_data)

    def init_gui(self):
        """
            Initialise fields
        """
        # Info labels
        self.gui.lbl_infofinance.clear()
        self.gui.lbl_infofinance.setText('[<< ' + self.ctl.get_parameter_value(8) + ' >> ' + self.ctl.get_parameter_value(9) + ']')
        self.gui.lbl_infodetails.clear()
        self.set_lbl_check(self.ctl.get_check_info([]))
        # fill all combo boxes
        self.ctl.init_display_data()
        # default values
        self.set_default_commission()
        self.set_default_tax()
        self.set_default_market()
        self.set_default_commodity()
        self.set_default_account_from()
        self.set_default_account_to()
        self.set_default_exchange_rate()
        self.set_default_currency_from()
        self.set_default_currency_to()
        self.set_default_risk()

    # Clear fields
    def clear_inputbuffer(self):
        """
            Clears the table that contains the data.
        """
        #TODO: clear when possible
        if self.model_data != None:
            self.model_data.clear()

    def clear_fields(self):
        """
            Clear the main input fields.
        """
        print '2a- clear fields: comment and amount cleared'
        self.gui.txt_comment.clear()
        self.gui.spn_amount.setValue(0)

    def clear_cmb_commodity_name(self):
        """
            Clear the cmb_commodity_name combobox.
        """
        self.gui.cmb_commodity_name.clear()

    # Getters and setters
    def get_date(self):
        """
            Returns the date from the date-picker.
        """
        return str(self.gui.dt_date.date().toString(QtCore.Qt.ISODate))

    def get_account_from(self):
        """
            Returns the account name from the cmb_account_from combobox.
        """
        return str(self.gui.cmb_account_from.currentText())

    def get_account_to(self):
        """
            Returns the account name from the cmb_account_to combobox.
        """
        return str(self.gui.cmb_account_to.currentText())
    
    def get_amount(self):
        """
            Returns the amount from the spn_amount spinedit.
        """
        return str(self.gui.spn_amount.textFromValue(self.gui.spn_amount.value()))

    def get_comment(self):
        """
            Returns the comment text.
        """
        return str(self.gui.txt_comment.text())

    def get_market_code(self):
        """
            Returns the market_code.
        """
        return str(self.gui.cmb_market_code.currentText())
    
    def get_market_description(self):
        """
            Returns the market description.
        """
        return str(self.gui.txt_market_description.text())

    def get_commodity_name(self):
        """
            Returns the commodity_name.
        """
        return str(self.gui.cmb_commodity_name.currentText())

    def get_commodity_description(self):
        """
            Returns the commodity description.
        """
        return str(self.gui.txt_commodity_description.text())

    def get_quantity(self):
        """
            Returns the quantity from the spn_quantity spinedit.
        """
        return str(self.gui.spn_quantity.textFromValue(self.gui.spn_quantity.value()))

    def get_price(self):
        """
            Returns the price from the spn_price spinedit.
        """
        return str(self.gui.spn_price.textFromValue(self.gui.spn_price.value()))

    def get_pool(self):
        """
            Returns the pool from the spn_pool spinedit.
        """
        return str(self.gui.spn_pool.textFromValue(self.gui.spn_pool.value()))

    def get_commission(self):
        """
            Returns the commission from the spn_commission spinedit.
        """
        return str(self.gui.spn_commission.textFromValue(self.gui.spn_commission.value()))

    def get_tax(self):
        """
            Returns the tax from the spn_tax spinedit.
        """
        return str(self.gui.spn_tax.textFromValue(self.gui.spn_tax.value()))

    def get_risk(self):
        """
            Returns the risk from the spn_risk spinedit.
        """
        return str(Decimal(str(self.gui.spn_risk.textFromValue(self.gui.spn_risk.value()))))
                
    def get_currency_from(self):
    	"""
            Returns the from currency used.
        """
    	return str(self.gui.cmb_currency_from.currentText())
 
    def get_currency_to(self):
    	"""
            Returns the to currency used.
        """
    	return str(self.gui.cmb_currency_to.currentText())
    	
    def get_exchange_rate(self):
    	"""
            Returns the exchange rate used.
        """
    	return str(self.gui.spn_exchange_rate.textFromValue(self.gui.spn_exchange_rate.value()))

    def get_manual_commission(self):
        """
            Returns the value of the manual commission calc. checkbox
        """
        return '0' if self.gui.chk_manual_commission.isChecked() else '1' 
        
    def get_date_expiration(self):
    	"""
            Returns the value of the dt_expiration date picker.
        """
    	return str(self.gui.dt_expiration.date().toString(QtCore.Qt.ISODate))

    def set_info_details(self, value):
        """
            Sets new info on the lbl_infodetails label.
        """
        self.gui.lbl_infodetails.setText(value)

    def set_lbl_check(self, value):
        """
            Sets new info on the lbl_infodetails label.
        """
        self.gui.lbl_check.setText(value)

    def set_market_description(self, value):
        """
            Sets new info on txt_market_description.
        """
        self.gui.txt_market_description.clear()
        self.gui.txt_market_description.setText(value)

    def set_commodity_description(self, value):
        """
            Sets new info on txt_commodity_description.
        """
        self.gui.txt_commodity_description.clear()
        self.gui.txt_commodity_description.setText(value)
   
    def add_commodity_name(self, value):
        """
            Add a new item to cmb_commodity_name.
        """
        self.gui.cmb_commodity_name.addItem(value)

    def add_account_from(self, value):
        """
            Add a new item to cmb_account_from.
        """
        self.gui.cmb_account_from.addItem(value)

    def add_account_to(self, value):
        """
            Add a new item to cmb_account_to.
        """
        self.gui.cmb_account_to.addItem(value)

    def add_market_code(self, value):
        """
            Add a new item to cmb_market_code.
        """
        self.gui.cmb_market_code.addItem(value)
       
    def set_default_commission(self):
        """
            Select the default commission.
        """
        self.gui.spn_commission.setValue(Decimal(self.ctl.get_parameter_value(12)))
        
    def set_default_tax(self):
        """
            Select the default tax.
        """
        self.gui.spn_tax.setValue(Decimal(self.ctl.get_parameter_value(13)))
        
    def set_default_market(self):
        """
            Select the default market.
        """
        index = int(self.ctl.get_parameter_value(14))-1
        self.set_combo_selection(index, self.gui.cmb_market_code)

    def set_default_commodity(self):
        """
            Select the default commodity.
        """
        index = int(self.ctl.get_parameter_value(15))-1
        self.set_combo_selection(index, self.gui.cmb_commodity_name)

    def set_default_account_from(self):
        """
            Select the default account.
        """
        index = int(self.ctl.get_parameter_value(6))-1
        self.set_combo_selection(index, self.gui.cmb_account_from)

    def set_default_account_to(self):
        """
            Select the default account.
        """
        index = int(self.ctl.get_parameter_value(7))-1
        self.set_combo_selection(index, self.gui.cmb_account_to)

    def set_default_currency_from(self):
        """
            Set the default from currency value at startup.
        """
        index = int(self.ctl.get_parameter_value(3))-1
        self.set_combo_selection(index, self.gui.cmb_currency_from)

    def set_default_currency_to(self):
        """
            Set the default to currency value at startup.
        """
        index = int(self.ctl.get_parameter_value(4))-1
        self.set_combo_selection(index, self.gui.cmb_currency_to)
 
    def set_default_exchange_rate(self):
        """
            Set the default exchange rate value at startup.
        """
        self.gui.spn_exchange_rate.setValue(Decimal(self.ctl.get_parameter_value(5)))

    def set_default_risk(self):
        """
            Set the default risk.
        """
        self.gui.spn_risk.setValue(Decimal(self.ctl.get_parameter_value(2)))

    def set_combo_selection(self, index, combobox):
        """
            Sets a combobox selection.
        """
        if index > 0:
            combobox.setCurrentIndex(index)

    def set_current_pool(self):
        """
            Resets the trading pool to the most current value.
        """
        self.ctl.fill_spn_pool()

    def set_pool(self, value):
        """
            Sets the trading pool to the given value.
        """
        self.gui.spn_pool.setValue(value)

    def add_currency_from(self, value):
        """
            Add a new item to cmb_currency_from.
        """ 
        self.gui.cmb_currency_from.addItem(value)
 
    def add_currency_to(self, value):
        """
            Add a new item to cmb_currency_to.
        """ 
        self.gui.cmb_currency_to.addItem(value)
        
    #TODO: reactivate the checkbox manual flag
    #TODO: add event so that when clicked, the commission and tax are
    #automatically calculated.
    #TODO: when automatic is checked, the commission and tax fields
    #should no longer be editable, and vice versa.
    #TODO: when the market or amount or category or subcategory (<> buy or sell) is changed, this also should be refreshed!
    #The goal is to make tax and commission dependent on the values in t_parameter
