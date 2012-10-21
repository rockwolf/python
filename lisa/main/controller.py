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
import shutil
import os, sys
from decimal import getcontext

from modules.stock import Stock
from database.databaseaccess import DatabaseAccess
from pyqt.controllerpyqt import ControllerPyqt
from PyQt4 import QtGui
from modules.constant import *
from modules.function import *

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
        #TODO: fix error about must start a QApplication in the init of this
        #class. Perhaps the run function should be executed before this init?
        #Possible solution implemented by putting this code
        #here in the controller.
        app = QtGui.QApplication(sys.argv)
        window = ControllerPyqt(self.config, self)
        self.gui = window
        window.init_gui()
        window.show()
        sys.exit(app.exec_())

    def write_to_database(self, tablecontent):
        """ Write the records to write to the database. """
        try:
            dba = DatabaseAccess(self.config)
            
            input_fields = self.get_input_fields(tablecontent)
            # Note: The order of execution below is important!
            test = dba.create_statements_TABLE_CURRENCY_EXCHANGE(input_fields)
            test.print_statements()
            test = dba.create_statements_TABLE_RATE(input_fields)
            test.print_statements()
            test = dba.create_statements_TABLE_TRADE(input_fields)
            test.print_statements()
            #test = dba.create_statements_TABLE_INVESTMENT(input_fields)
            #test.print_statements()
            test = dba.create_statements_TABLE_FINANCE(input_fields)
            test.print_statements()
            
            dba.write_to_database(dba.create_statements_TABLE_CURRENCY_EXCHANGE(input_fields))
            dba.write_to_database(dba.create_statements_TABLE_RATE(input_fields))
            #if self.is_an_investment():
            #    dba.write_to_database(dba.create_statements_TABLE_INVESTMENT(input_fields))
            #if self.is_a_trade():
            #    dba.write_to_database(dba.create_statements_TABLE_TRADE(input_fields))
            #dba.write_to_database(dba.create_statements_TABLE_FINANCE(input_fields))
            dba = None
        except  Exception as ex:
            print(ERROR_WRITE_TO_DATABASE, ex)

    def get_input_fields(self, tablecontent):
        """ Gets input, adds extra info and puts this in a list. """
        fields_db = []
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
                else:
                    shares = -1
                    price = -1
                    commission = -1
                    tax = -1
                    risk = -1
                fields_db.append({
                    'date':field[0],
                    'account':field[1], #Note: Get account_id from T_ACCOUNT for final insert
                    'category':field[2], #Note: Get category_id from T_CATEGORY for final insert
                    'subcategory':field[3], #Note: Get subcategory_id from T_SUBCATEGORY for final insert
                    'amount':field[4],
                    'flag':flg_income,
                    'comment':field[5],
                    'stock_name':field[6],
                    'stock_description':field[7],
                    'market_name':field[8],
                    'market_description':field[9],
                    'shares':shares,
                    'price':price,
                    'commission':commission,
                    'tax':tax,
                    'risk':risk,
                    'currency':field[15],
                    'exchange_rate':field[16],
                    'manual_flag':field[17]
                })
        except Exception as ex:
            print(ERROR_GET_INPUT_FIELDS, ex)
        finally:
            return fields_db 

            ## import finance info from table data
            #dba = DatabaseAccess(self.config)
            #dba.file_import_lines(fields_db)
            #dba = None
            ## import stock info from table data
            #fields_stock = []
            #stock = Stock(self.config)
            #for field in fields_db:
            #    fields_stock.append(stock.parse_stocks(field))
            #stock.process_stocks(fields_db, fields_stock)
            #stock = None
            ##TODO: process_trades

    def backup(self):
        """ Make a backup of the output file for clipf. """
        # remove old backup
        if isfile(self.config.backupfile):
            try:
                os.remove(self.config.backupfile)
                print(self.config.backupfile + ' removed.')
            #except IOError as strerror:
            except Exception as ex:
                print("Error: ", ex)
        # copy current to .bak
        if isfile(self.config.exportfile) and not isfile(self.config.backupfile):
            try:
                shutil.copy(self.config.exportfile, self.config.backupfile)
                print(self.config.backupfile + ' created.')
            except Exception as ex:
                print('Error: application fucked up while creating backup: ', ex)
        else:
            print('Error: backup file already exists.')

    ## Init of gui
    def fillcombos(self):
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
            self.gui.add_currency(currency)
        # Stock names
        self.fillcmb_stock_name()
        self.filltxt_market_description()
        self.filltxt_stock_description()
        dba = None

    def get_input_line(self, table):
        """ Get the input values. """
        #TODO: check cat/subcat combo, instead of only subcat
        if(self.gui.get_subcategory() == 'buy' or \
                self.gui.get_subcategory() == 'sell'):
            market = self.gui.get_market_code()
            stock = self.gui.get_stock_name()
        else:
            market = ''
            stock = ''
        str_list = [
            self.gui.get_date(),
            self.gui.get_account(),
            self.gui.get_category(),
            self.gui.get_subcategory(),
            self.gui.get_amount(),
            self.gui.get_comment(),
            stock,
            self.gui.get_stock_description(),
            market,
            self.gui.get_market_description(),
            self.gui.get_quantity(),
            self.gui.get_price(),
            self.gui.get_commission(),
            self.gui.get_tax(),
            self.gui.get_risk(),
            self.gui.get_currency(),
            self.gui.get_exchange_rate(),
            self.gui.get_manual_commission()
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

    def add_tbl_summary(self, table, row):
        """ Add or remove a row from the table view """
        table.add_row(row)

    def parse_formula(self, formula_id, value_list):
        """ Parse formula for trading, to calculate the commission. """
        #TODO: create the get_formula function in databaseaccess.
        dba = DatabaseAccess(self.config)
        formula = dba.get_formula(formula_id)
        #TODO: loop over elements in formula and substitute the values.
        dba = None

    def convert_to_base_currency(self, currency_base, currency_new, value):
        """ Convert a new currency to the base currency. """
        pass
