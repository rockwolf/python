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
        self.config = config #object
        # Decimal precision
        getcontext().prec = 4

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
            
            input_fields = self.get_input_fields(tablecontent)
            # Note: The order of execution below is important!
            test = currency_exchange.create_statements(input_fields)
            test.print_statements()
            currency_exchange.write_to_database(currency_exchange.create_statements(input_fields))
            test = rate.create_statements(input_fields)
            test.print_statements()
            rate.write_to_database(rate.create_statements(input_fields))
            statements_finance = finance.create_statements(input_fields)
            statements_finance.print_statements()
            statements_finance = finance.create_statements(input_fields)
            finance.write_to_database(statements_finance)
            
            test = trade.create_statements(input_fields,
                    statements_finance)
            test.print_statements()
            trade.write_to_database(trade.create_statements(input_fields,
                statements_finance))
            #test = dba.create_statements_TABLE_INVESTMENT(input_fields)
            #test.print_statements()
            #if self.is_an_investment():
            #    dba.write_to_database(dba.create_statements_TABLE_INVESTMENT(input_fields))
            currency_exchange = None
            rate = None
            finance = None
            trade = None
            investment = None
        except  Exception as ex:
            print(ERROR_WRITE_TO_DATABASE_MAIN, ex)

    def get_input_fields(self, tablecontent):
        """ Gets input, adds extra info and puts this in a list. """
        input = []
        try:
            for field in tablecontent:
                category = field[2]
                subcategory = field[3]
                if(category[-3:] == '.rx'):
                    flg_income = 1
                elif(category[-3:] == '.tx'):
                    flg_income = 0
                if deals_with_stocks(category, subcategory) :
                    shares = field[10]
                    price = field[11]
                    commission = field[12]
                    tax = field[13]
                    risk = field[14]
                    pool = field[20]
                else:
                    shares = DEFAULT_INT
                    price = DEFAULT_DECIMAL
                    commission = DEFAULT_DECIMAL
                    tax = DEFAULT_DECIMAL
                    risk = DEFAULT_DECIMAL
                    pool = DEFAULT_DECIMAL
                input.append({
                    'i_date':string_to_date(field[0]),
                    'i_account':field[1], #Note: Get account_id from T_ACCOUNT for final insert
                    'i_category':field[2], #Note: Get category_id from T_CATEGORY for final insert
                    'i_subcategory':field[3], #Note: Get subcategory_id from T_SUBCATEGORY for final insert
                    'i_amount':Decimal(field[4]),
                    'i_flag':int(flg_income),
                    'i_comment':field[5],
                    'i_stock_name':field[6],
                    'i_stock_description':field[7],
                    'i_market_name':field[8],
                    'i_market_description':field[9],
                    'i_shares':int(shares),
                    'i_price':Decimal(price),
                    'i_commission':Decimal(commission),
                    'i_tax':Decimal(tax),
                    'i_risk_input':Decimal(risk),
                    'i_currency_from':field[15], #Note: Get currency_id from T_CURRENCY for final insert
                    'i_currency_to':field[16], #Note: Get currency_id from T_CURRENCY for final insert
                    'i_exchange_rate':Decimal(field[17]),
                    'i_manual_flag':int(field[18]),
                    'i_date_expiration':string_to_date(field[19]),
                    'i_pool':Decimal(pool),
                    'i_spread':Decimal(field[21])
                })
        except Exception as ex:
            print(ERROR_GET_INPUT_FIELDS, ex)
        finally:
            return input 

    ## Init of gui
    def init_display_data(self):
        """ fill in the combo boxes with values. """
        dba = DatabaseAccess(self.config)
        # Accounts
        for acc in dba.get_accounts():
            self.gui.add_account(acc)
        # Categories 
        for category in dba.get_categories():
            self.gui.add_category(category)
        # Subcategories. 
        for subcategory in dba.get_subcategories():
            self.gui.add_subcategory(subcategory)
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
        """ Gets the account check info. """
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
        value = Decimal(0.0)
        for fields in input_fields:
            if fields['account'] == account_name:
                value = value + Decimal(fields['amount'])
        return value

    def get_account_totals_from_input_fields(self, input_fields):
        """
            Returns a list with the account name / total pairs,
            only taking into consideration what's in
            the input_fields.
        """
        values = []
        dba = DatabaseAccess(self.config)
        for account in dba.get_accounts():
            values.append([account, self.get_account_total_from_input_fields(
                    account, input_fields)])
        dba = None
        return values

    def get_input_line(self, table):
        """ Get the input values. """
        #TODO: check cat/subcat combo, instead of only subcat
        if(deals_with_stocks(self.gui.get_category(),
            self.gui.get_subcategory())):
            market = self.gui.get_market_code()
            stock = self.gui.get_stock_name()
            market_description = self.gui.get_market_description()
            stock_description = self.gui.get_stock_description()
            pool = self.gui.get_pool()
        else:
            market = ''
            stock = ''
            market_description = ''
            stock_description = ''
            pool = '0.0'
        category = self.gui.get_category()
        if category[-3:] == '.tx':
            amount = '-' + self.gui.get_amount()
        else:
            amount = self.gui.get_amount()
        str_list = [
            self.gui.get_date(),
            self.gui.get_account(),
            category,
            self.gui.get_subcategory(),
            amount,
            self.gui.get_comment(),
            stock,
            stock_description,
            market,
            market_description,
            self.gui.get_quantity(),
            self.gui.get_price(),
            self.gui.get_commission(),
            self.gui.get_tax(),
            self.gui.get_risk(),
            self.gui.get_currency_from(),
            self.gui.get_currency_to(),
            self.gui.get_exchange_rate(),
            self.gui.get_manual_commission(),
            self.gui.get_date_expiration(),
            pool,
            self.gui.get_spread()
            ]
        return str_list

    def remove_selected(self, table, selected_index):
        """ Removes the selected record from the input buffer. """
        table.delete_row(selected_index)

    def remove_last(self, table):
        """ Removes the most recently added record from the input buffer. """
        table.delete_row()

    def set_infodetails(self):
        """ Update infolabel details. """
        dba = DatabaseAccess(self.config)
        prod = self.gui.get_category()
        stock = self.gui.get_stock_name()
        #TODO: make entire program dependent on cids, so there are no longer
        #hardcoded strings.
        if(
            prod == 'invest.tx' or
            prod == 'trade.tx' or
            prod == 'invest.rx' or
            prod == 'trade.rx'
        ) and stock != '':
            info = dba.get_stockinfo(stock)
            self.gui.set_infodetails(info[1] + '(' + 
                    ''.join(info[2].split()) +'): ' + info[0])
        else:
            self.gui.set_infodetails('')
        dba = None

    def fillcmb_stock_name(self):
        """ fill cmb function """
        dba = DatabaseAccess(self.config)
        self.gui.clear_cmb_stock_name()
        for name in dba.get_stock_names(self.gui.get_market_code()):
            self.gui.add_stock_name(name)
        dba = None
    
    def filltxt_market_description(self):
        """ fill market description """
        dba = DatabaseAccess(self.config)
        self.gui.set_market_description(
                dba.get_market_description(self.gui.get_market_code()))
        dba = None

    def filltxt_stock_description(self):
        """ fill stock description """
        dba = DatabaseAccess(self.config)
        self.gui.set_stock_description(
                dba.get_stock_description(self.gui.get_stock_name()))
        dba = None

    def fill_spn_pool(self):
        """ fill pool value """
        dba = DatabaseAccess(self.config)
        self.gui.set_pool(dba.get_pool())
        dba = None

    def add_tbl_summary(self, table, row):
        """ Add or remove a row from the table view """
        table.add_row(row)

    def parse_formula(self, formula_id, value_list):
        """ Parse formula for trading, to calculate the commission. """
        dba = DatabaseAccess(self.config)
        formula = dba.get_formula(formula_id)
        #TODO: loop over elements in formula and substitute the values.
        dba = None

    def convert_to_base_currency(self, currency_base, currency_new, value):
        """ Convert a new currency to the base currency. """
        pass
