#!/usr/env/python
"""
    See LICENSE file for copyright and license details.					
"""

from os.path import isfile
import shutil
import os, sys
from decimal import getcontext

from database.databaseaccess import DatabaseAccess
from pyqt.controllerpyqt import ControllerPyqt
from PyQt4 import QtGui
from modules.constant import *
from modules.function import *
from decimal import Decimal
from modules_generic.function import *
from modules.currency_exchange import CurrencyExchange
from modules.rate import Rate
from modules.finance import Finance
from modules.investment import Investment
from modules.trade import Trade

class ControllerMain():
    """ Contains the bussiness logic of the application. """
    
    def __init__(self, config):
        """ Construct basic QApplication, add widgets and start exec_loop """
        # initialise special vars
        self.config = config

    # Methods
    ## General
    def run(self):
        """ Start the gui. """
        app = QtGui.QApplication(sys.argv)
        window = ControllerPyqt(self.config, self)
        self.gui = window
        window.init_gui()
        window.show()
        sys.exit(app.exec_())

    def write_to_database(self, tablecontent):
        """ Write the records to write to the database. """
        try:
            currency_exchange = CurrencyExchange(self.config)
            rate = Rate(self.config)
            finance = Finance(self.config)
            trade = Trade(self.config)
            investment = Investment(self.config)
            bet = Bet(self.config)
            
            input_fields = self.get_input_fields(tablecontent)
            # Note: The order of execution below is important!
            # t_currency_exchange
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
            # t_bet
            var_bet = bet.create_statements(
                        input_fields,
                        var_finance)
            bet.print_statements()
            #bet.write_to_database(var_finance)
            currency_exchange = None
            rate = None
            finance = None
            trade = None
            investment = None
        except  Exception as ex:
            print(Error.WRITE_TO_DATABASE_MAIN, ex)

    def get_input_fields(self, tablecontent):
        """ Gets input, adds extra info and puts this in a list. """
        input = []
        try:
            for field in tablecontent:
                account_to = field[InputIndex.ACCOUNT_TO]
                if deals_with_stocks(account_from, account_to) :
                    shares = field[InputIndex.SHARES]
                    price = field[InputIndex.PRICE]
                    commission = field[InputIndex.COMMISSION]
                    tax = field[InputIndex.TAX]
                    risk = field[InputIndex.RISK]
                    pool = field[InputIndex.POOL]
                else:
                    shares = DEFAULT_INT
                    price = DEFAULT_DECIMAL
                    commission = DEFAULT_DECIMAL
                    tax = DEFAULT_DECIMAL
                    risk = DEFAULT_DECIMAL
                    pool = DEFAULT_DECIMAL
                input.append({
                    'i_date':string_to_date(field[InputIndex.DATE]),
                    'i_account_from':field[InputIndex.ACCOUNT_FROM], #Note: Get account_id from T_ACCOUNT for final insert
                    'i_account_to':field[InputIndex.ACCOUNT_TO],
                    'i_amount':Decimal(field[InputIndex.AMOUNT]),
                    'i_comment':field[InputIndex.COMMENT],
                    'i_stock_name':field[InputIndex.STOCK],
                    'i_stock_description':field[InputIndex.STOCK_DESCRIPTION],
                    'i_market_name':field[InputIndex.MARKET],
                    'i_market_description':field[InputIndex.MARKET_DESCRIPTION],
                    'i_shares':int(shares),
                    'i_price':Decimal(price),
                    'i_commission':Decimal(commission),
                    'i_tax':Decimal(tax),
                    'i_risk_input':Decimal(risk),
                    'i_currency_from':field[InputIndex.CURRENCY_FROM], #Note: Get currency_id from T_CURRENCY for final insert
                    'i_currency_to':field[InputIndex.CURRENCY_TO], #Note: Get currency_id from T_CURRENCY for final insert
                    'i_exchange_rate':Decimal(field[InputIndex.EXCHANGE_RATE]),
                    'i_automatic_flag':int(field[InputIndex.AUTOMATIC_FLAG]),
                    'i_date_expiration':string_to_date(field[InputIndex.DATE_EXPIRATION]),
                    'i_periodic':int(field[InputIndex.PERIODIC_FLAG]),
                    'i_periodic_start':string_to_date(field[InputIndex.PERIODIC_START]),
                    'i_periodic_end':string_to_date(field[InputIndex.PERIODIC_END]),
                    'i_pool':Decimal(pool)
                })
        except Exception as ex:
            print(Error.GET_INPUT_FIELDS, ex)
        finally:
            return input 

    ## Init of gui
    def init_display_data(self):
        """ fill in the combo boxes with values. """
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
        # Stock names
        self.fillcmb_stock_name()
        self.filltxt_market_description()
        self.filltxt_stock_description()
        # Pool
        self.fill_spn_pool()
        dba = None

    def get_check_info(self, tablecontent):
        """
            Gets the account check info.
        """
        dba = DatabaseAccess(self.config)
        values = []
        for entry in dba.get_rep_check_totals():
            values.append(entry) 
        for entry in self.get_account_totals_from_input_fields(
                self.get_input_fields(tablecontent)):
            for saved_entry in values:
                if saved_entry[0] == entry[0]: 
                    saved_entry[1] = saved_entry[1] + entry[1]
        info = dba.get_rep_check_total(values)
        if info == '':
            info == 'Error retrieving info...'
        dba = None
        return info

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
        values = []
        dba = DatabaseAccess(self.config)
        for account in dba.get_accounts():
            values.append([account, self.get_account_total_from_input_fields(
                    account, input_fields)])
        dba = None
        return values

    def get_input_line(self, table):
        """
            Get the input values.
        """
        # initialize
        market = ''
        stock = ''
        market_description = ''
        stock_description = ''
        pool = '0.0'
    
        str_list = []
        for i in range(0,InputIndex.SIZE):
            str_list.append('')
    
        # get values    
        if(deals_with_stocks(self.gui.get_account_from(), self.gui.get_account_to())):
            market = self.gui.get_market_code()
            stock = self.gui.get_stock_name()
            market_description = self.gui.get_market_description()
            stock_description = self.gui.get_stock_description()
            pool = self.gui.get_pool()
            
        #TODO: check if it needs to be a negative amount
        if is_negative_amount(account_name):
            amount = '-' + self.gui.get_amount()
        else:
            amount = self.gui.get_amount()
        
        str_list[InputIndex.DATE] = self.gui.get_date()
        str_list[InputIndex.ACCOUNT_FROM] = self.gui.get_account_from()
        str_list[InputIndex.ACCOUNT_TO] = self.gui.get_account_to()
        str_list[InputIndex.AMOUNT] = amount
        str_list[InputIndex.COMMENT] = self.gui.get_comment()
        str_list[InputIndex.STOCK] = stock
        str_list[InputIndex.STOCK_DESCRIPTION] = stock_description
        str_list[InputIndex.MARKET] = market
        str_list[InputIndex.MARKET_DESCRIPTION] = market_description
        str_list[InputIndex.QUANTITY] = self.gui.get_quantity()
        str_list[InputIndex.PRICE] = self.gui.get_price()
        str_list[InputIndex.COMMISSION] = self.gui.get_commission()
        str_list[InputIndex.TAX] = self.gui.get_tax()
        str_list[InputIndex.RISK] = self.gui.get_risk()
        str_list[InputIndex.CURRENCY_FROM] = self.gui.get_currency_from()
        str_list[InputIndex.CURRENCY_TO] = self.gui.get_currency_to()
        str_list[InputIndex.EXCHANGE_RATE] = self.gui.get_exchange_rate()
        str_list[InputIndex.MANUAL_COMMISSION] = self.gui.get_manual_commission()
        str_list[InputIndex.DATE_EXPIRATION] = self.gui.get_date_expiration()
        str_list[InputIndex.POOL] = pool
        str_list[InputIndex.PERIODIC_FLAG] = self.gui.get_periodic_flag()
        str_list[InputIndex.PERIODIC_START] = self.gui.get_periodic_start()
        str_list[InputIndex.PERIODIC_END] = self.gui.get_periodic_end()
        return str_list

    def remove_selected(self, table, selected_index):
        """
            Removes the selected record from the input buffer.
        """
        table.delete_row(selected_index)

    def remove_last(self, table):
        """
            Removes the most recently added record from the input buffer.
        """
        table.delete_row()

    def set_infodetails(self):
        """
            Update infolabel details.
        """
        dba = DatabaseAccess(self.config)
        account_from = self.gui.get_account_from()
        account_to = self.gui.get_account_to()
        stock = self.gui.get_stock_name()
        #TODO: get the correct accounts here
        if deals_with_stocks(account_from, account_to) and not stock:
            info = dba.get_stockinfo(stock)
            self.gui.set_infodetails(
                '{} ({}): {}'.format(
                    info[1]
                    ,''.join(info[2].split())
                    ,info[0]))
        else:
            self.gui.set_infodetails('')
        dba = None

    def fillcmb_stock_name(self):
        """
            fill cmb function
        """
        dba = DatabaseAccess(self.config)
        self.gui.clear_cmb_stock_name()
        for name in dba.get_stock_names(self.gui.get_market_code()):
            self.gui.add_stock_name(name)
        dba = None
    
    def filltxt_market_description(self):
        """
            fill market description
        """
        dba = DatabaseAccess(self.config)
        self.gui.set_market_description(
                dba.get_market_description(self.gui.get_market_code()))
        dba = None

    def filltxt_stock_description(self):
        """
            fill stock description
        """
        dba = DatabaseAccess(self.config)
        self.gui.set_stock_description(
                dba.get_stock_description(self.gui.get_stock_name()))
        dba = None

    def fill_spn_pool(self):
        """
            fill pool value
        """
        dba = DatabaseAccess(self.config)
        self.gui.set_pool(dba.get_pool())
        dba = None

    def add_tbl_summary(self, table, row):
        """
            Add or remove a row from the table view
        """
        table.add_row(row)

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
        # TODO: make is_a_trading_market, without having to specify all markets in
        # constant.py
        # Perhaps add a flag to t_market? [I|T] [invest|trade]
        # TODO: add a button to set the flag for the currently selected market
        if is_a_trading_market(market):
            # NOTE: This only works when
            # an account can not be used for trading and investing at the same time
            # NOTE: commodities is used, instead of stocks, to look at trading and investing seperately.
            dba.save_new_account('assets:current_assets:commodities:' + new_commodity.lower() + ' (long)')
            dba.save_new_account('assets:current_assets:commodities:' + new_commodity.lower() + ' (short)')
        dba = None
