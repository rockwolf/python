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
            # put code here
            #TODO: create constant.py with the correct error messages.
        except Exception as ex:
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
                    'i_pool':Decimal(pool)
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
            self.gui.add_account(acc)
            #TODO: do we need an account? Probably yes: whsi/binb drawdown support
        dba = None

    def get_input_line(self, table):
        """ Get the input values. """
        #TODO: make this much simpler
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
            pool
            ]
        return str_list

    def set_infodetails(self):
        """ Update infolabel details. """
        dba = DatabaseAccess(self.config)
        #TODO: write some info about total active trades etc. to a label
        dba = None

    def add_tbl_summary(self, table, row):
        """ Add or remove a row from the table view """
        #TODO: display active trades in a table view
        table.add_row(row)
