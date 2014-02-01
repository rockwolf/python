#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.
"""
from datetime import datetime

from database.databaseaccess import DatabaseAccess
from modules.core_module import CoreModule
from modules.statement import Statement
from modules.constant import *
from modules.function import *
from generic.modules.function import *
from generic.modules.calculator_finance import CalculatorFinance

class Rate(CoreModule):
    """
        Rate class.
    """

    def __init__(self, config):
        """
            Initialisation
        """
        self.config = config
        self.statement_rate = Statement(Table.RATE)
        self.commission = DEFAULT_DECIMAL
        self.tax = DEFAULT_DECIMAL
        self.date_created = DEFAULT_DATE
        self.date_modified = DEFAULT_DATE

    def create_statements(self, input_fields):
        """
            Creates the records needed for Table.RATE
            and returns them as a Statement object.
        """
        try:
            dba = DatabaseAccess(self.config)
            lib = CalculatorFinance()
            self.date_created = current_date()
            self.date_modified = current_date()
            records = 0
            for fields in input_fields:
                if deals_with_commodities(fields[Input.ACCOUNT_FROM], fields[Input.ACCOUNT_TO]):
                    records = records + 1
                    if fields[Input.AUTOMATIC_FLAG] == 0:
                        self.commission = fields[Input.COMMISSION]
                        self.tax = fields[Input.TAX]
                    else:
                        self.commission = lib.calculate_commission(TRADING_ACCOUNTS[0], fields[Input.MARKET_CODE], fields[Input.COMMODITY_NAME], fields[Input.PRICE], fields[Input.QUANTITY])
                        # TODO: make a calculate_tax function in the library?
                        self.tax = fields[Input.TAX]
                    self.add_to_statement(records, fields)
            return self.statement_rate
        except Exception as ex:
            print Error.CREATE_STATEMENTS_TABLE_RATE, ex
        finally:
            dba = None
            lib = None

    def add_to_statement(self, records, fields):
        """
            Add the data to the statement list.
        """
        self.statement_rate.add(
            records,
            {
                'rate_id':None,
                'commission':Decimal(self.commission),
                'tax':Decimal(self.tax),
                'automatic_flag':int(fields[Input.AUTOMATIC_FLAG]),
                'date_created':self.date_created,
                'date_modified':self.date_modified
            }
        )
