#!/usr/env/python
"""
    See LICENSE file for copyright and license details.					
"""

from os.path import isfile
import shutil
import os, sys
from decimal import getcontext

from database.databaseaccess import DatabaseAccess
from controllerpyqt import ControllerPyqt
from PyQt4 import QtGui
from modules.constant import *
from modules.function import *
from decimal import Decimal
from generic.modules.function import *
from modules.currency_exchange import CurrencyExchange
from modules.rate import Rate
from modules.finance import Finance
from modules.trade import Trade
from modules.emma import Emma

class ControllerMain():
    """
        Contains the bussiness logic of the application.
    """
    
    def __init__(self, config):
        """
            Construct basic QApplication, add widgets and start exec_loop
        """
        # initialise special vars
        self.config = config

    # Methods
    ## General
    def run(self):
        """
            Start the gui.
        """
        app = QtGui.QApplication(sys.argv)
        app.setStyle("cleanLooks")
        #TODO: play with the different styles
        # "windows", "motif", "cde", "plastique" and "cleanlooks"
        window = ControllerPyqt(self.config, self)
        self.gui = window
        window.init_gui()
        window.show()
        sys.exit(app.exec_())

    def write_to_database(self, table_model):
        """
            Write the records to write to the database.
        """
        try:
            currency_exchange = CurrencyExchange(self.config)
            rate = Rate(self.config)
            finance = Finance(self.config)
            trade = Trade(self.config)
            
            input_fields = table_model.get_values()
            # Note: The order of execution below is important!
            # t_currency_exchange
            print 'test1: input_fields = ', input_fields
            var_currency_exchange = currency_exchange.create_statements(input_fields)
            var_currency_exchange.print_statements()
            currency_exchange.write_to_database(var_currency_exchange)
            # t_rate
            var_rate = rate.create_statements(input_fields)
            var_rate.print_statements()
            rate.write_to_database(var_rate)
            # t_finance
            var_finance = finance.create_statements(input_fields)
            var_finance.print_statements()
            finance.write_to_database(var_finance)
            if deals_with_commodities(
                input_fields[Input.ACCOUNT_FROM]
                , input_fields[Input.ACCOUNT_TO]):
                # t_trade
                var_trade = trade.create_statements(
                                input_fields,
                                var_finance)
                var_trade.print_statements()
                trade.write_to_database(var_trade)
            #test = dba.create_statements_TABLE_INVESTMENT(input_fields)
            #test.print_statements()
            #if self.is_an_investment():
            #    dba.write_to_database(dba.create_statements_TABLE_INVESTMENT(input_fields))
            currency_exchange = None
            rate = None
            finance = None
            trade = None
        except  Exception as ex:
            print Error.WRITE_TO_DATABASE_MAIN, ex

    ## Init of gui
    def init_display_data(self):
        """
            fill in the combo boxes with values.
        """
        dba = DatabaseAccess(self.config)
        # Accounts
        for acc in dba.get_account_list():
            self.gui.add_account_from(acc)
            self.gui.add_account_to(acc)
        # Market codes
        for mcd in dba.get_markets():
            self.gui.add_market_code(mcd)
        # Currencies
        for currency in dba.get_currencies():
            self.gui.add_currency_from(currency)
            self.gui.add_currency_to(currency)
        # Commodity names
        self.fillcmb_commodity_name()
        self.filltxt_market_description()
        self.filltxt_commodity_description()
        # Pool
        self.fill_spn_pool()
        dba = None

    def get_check_info(self, table_model):
        """
            Gets the account check info.
        """
        #TODO: fix this later
        pass
        #dba = DatabaseAccess(self.config)
        #values = []
        #for entry in dba.get_rep_check_totals():
        #    values.append(entry) 
        #for entry in self.get_account_totals_from_input_fields(
        #        table_model.get_values()):
        #    for saved_entry in values:
        #        if saved_entry[0] == entry[0]: 
        #            saved_entry[1] = saved_entry[1] + entry[1]
        #info = dba.get_rep_check_total(values)
        #if info == '':
        #    info == 'Error retrieving info...'
        #dba = None
        #return info

    def get_account_total_from_input_fields(self,
            account_name, input_fields):
        """ 
            Returns the account total for the given
            account, only taking into consideration
            what's in the input_fields.
        """
        #TODO: fix this, see the calling function
        value = Decimal(0.0)
        for fields in input_fields:
            if fields['i_account'] == account_name:
                value = value + Decimal(fields['i_amount'])
        return value

    def get_account_totals_from_input_fields(self, input_fields):
        """
            Returns a list with the account name / total pairs,
            only taking into consideration what's in
            the input_fields.
        """
        #TODO: this was for V_rep_cheCK I think, this needs to be fixed!
        # So create a new V_REP_CHECK view!
        values = []
        dba = DatabaseAccess(self.config)
        for account in dba.get_accounts():
            values.append([account, self.get_account_total_from_input_fields(
                    account, input_fields)])
        dba = None
        return values

    def get_input_line(self):
        """
            Get the input values, but add basic extra calculations.
        """
        return self.get_input_line_extra(
            self.gui.get_date()
            , self.gui.get_account_from()
            , self.gui.get_account_to()
            , self.gui.get_amount()
            , self.gui.get_comment()
            , self.gui.get_commodity_name()
            , self.gui.get_commodity_description()
            , self.gui.get_market_code()
            , self.gui.get_market_description()
            , self.gui.get_quantity()
            , self.gui.get_price()
            , self.gui.get_commission()
            , self.gui.get_tax()
            , self.gui.get_risk()
            , self.gui.get_currency_from()
            , self.gui.get_currency_to()
            , self.gui.get_exchange_rate()
            , self.gui.get_manual_commission()
            , self.gui.get_date_expiration()
            , self.gui.get_pool())
            
    
    def get_input_line_extra(self
        , date
        , account_from
        , account_to
        , amount
        , comment
        , commodity
        , commodity_description
        , market
        , market_description
        , quantity
        , price
        , commission
        , tax
        , risk
        , currency_from
        , currency_to
        , exchange_rate
        , manual_commission
        , date_expiration
        , pool):
        """
            Add calculated fields to the input line,
            to end up with what the application will process.
            The values in the list are also cast to the correct type.
        """
        # initialize
        str_list = []
        for i in range(0,Input.SIZE):
            str_list.append('')
        
        # When not needed, values for trading will be cleared.
        if not (deals_with_commodities(self.gui.get_account_from(), self.gui.get_account_to())):
            market = ''
            commodity = ''
            market_description = ''
            commodity_description = ''
            pool = DEFAULT_DECIMAL
            shares = DEFAULT_INT
            price = DEFAULT_DECIMAL
            commission = DEFAULT_DECIMAL
            tax = DEFAULT_DECIMAL
            risk = DEFAULT_DECIMAL
        # Check if it needs to be a negative amount
        if (is_negative_amount(account_from)
            and Decimal(amount) != DEFAULT_DECIMAL):
            amount = '-' + amount
        str_list[Input.DATE] = string_to_date(date)
        str_list[Input.ACCOUNT_FROM] = account_from
        str_list[Input.ACCOUNT_TO] = account_to
        str_list[Input.AMOUNT] = Decimal(amount)
        str_list[Input.COMMENT] = comment
        str_list[Input.COMMODITY_NAME] = commodity
        str_list[Input.COMMODITY_DESCRIPTION] = commodity_description
        str_list[Input.MARKET_CODE] = market
        str_list[Input.MARKET_DESCRIPTION] = market_description
        str_list[Input.QUANTITY] = int(quantity)
        str_list[Input.PRICE] = Decimal(price)
        str_list[Input.COMMISSION] = Decimal(commission)
        str_list[Input.TAX] = Decimal(tax)
        str_list[Input.RISK] = Decimal(risk)
        str_list[Input.CURRENCY_FROM] = currency_from
        str_list[Input.CURRENCY_TO] = currency_to
        str_list[Input.EXCHANGE_RATE] = Decimal(exchange_rate)
        str_list[Input.MANUAL_COMMISSION] = int(manual_commission)
        str_list[Input.DATE_EXPIRATION] = string_to_date(date_expiration)
        str_list[Input.POOL] = Decimal(pool)
        return str_list

    def remove_selected(self, table_model, selected_index):
        """
            Removes the selected record from the input buffer.
        """
        table_model.removeRows(selected_index - 1, 1)

    def remove_last(self, table_model):
        """
            Removes the most recently added record from the input buffer.
        """
        table_model.removeRows(table_model.rowCount(None) - 1, 1)

    def set_info_details(self):
        """
            Update infolabel details.
        """
        dba = DatabaseAccess(self.config)
        account_from = self.gui.get_account_from()
        account_to = self.gui.get_account_to()
        commodity = self.gui.get_commodity_name()
        if deals_with_commodities(account_from, account_to) and not commodity:
            info = dba.get_commodity_info(commodity)
            self.gui.set_info_details(
                '{} ({}): {}'.format(
                    info[1]
                    ,''.join(info[2].split())
                    ,info[0]))
        else:
            self.gui.set_info_details('')
        dba = None

    def fillcmb_commodity_name(self):
        """
            fill cmb function
        """
        dba = DatabaseAccess(self.config)
        self.gui.clear_cmb_commodity_name()
        for name in dba.get_commodity_names(self.gui.get_market_code()):
            self.gui.add_commodity_name(name)
        dba = None
    
    def filltxt_market_description(self):
        """
            fill market description
        """
        dba = DatabaseAccess(self.config)
        self.gui.set_market_description(
                dba.get_market_description(self.gui.get_market_code()))
        dba = None

    def filltxt_commodity_description(self):
        """
            fill commodity description
        """
        dba = DatabaseAccess(self.config)
        self.gui.set_commodity_description(
                dba.get_commodity_description(self.gui.get_commodity_name()))
        dba = None

    def fill_spn_pool(self):
        """
            fill pool value
        """
        dba = DatabaseAccess(self.config)
        self.gui.set_pool(dba.get_pool())
        dba = None

    def add_tbl_data(self, model_data, rows):
        """
            Add or remove rows from the table view
        """
        model_data.insertRows(len(model_data.get_values()), len(rows), rows)

    def convert_to_base_currency(self, currency_base, currency_new, value):
        """
            Convert a new currency to the base currency.
        """
        pass
    
    def update_accounts_for_commodities(self, market, new_commodity):
        """
           Create a long and short account for a new commodity.
        """
        dba = DatabaseAccess(self.config)
        dba.save_new_account('assets:current_assets:commodities:' + new_commodity.lower() + ' (long)')
        dba.save_new_account('assets:current_assets:commodities:' + new_commodity.lower() + ' (short)')
        dba = None

    def get_parameter_value(self, parameter_index):
        """
            Get the parameter value from T_PARAMETER.
            Note: A final conversion needs to be done to
            the correct type, as this returns a string!
        """
        dba = DatabaseAccess(self.config)
        result = dba.get_parameter_value(parameter_index)
        dba = None
        return result
