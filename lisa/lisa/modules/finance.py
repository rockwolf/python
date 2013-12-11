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

class Finance(CoreModule):
    """
        Finance class.
    """
        
    def create_statements(self, input_fields):
        """
            Creates the records needed for Table.FINANCE
            and returns them as a Statement object.
        """
        try:
            dba = DatabaseAccess(self.config)
            date_created = current_date()
            date_modified = current_date()
            statement_finance = Statement(Table.FINANCE)
            records = 0
            currency_exchange_id = dba.first_currency_exchange_id_from_latest()
            rate_id = dba.first_rate_id_from_latest()
            for fields in input_fields:
                account_from_id = dba.account_id_from_account(fields[Input.ACCOUNT_FROM])
                account_to_id = dba.account_id_from_account(fields[Input.ACCOUNT_TO])
               
                #NOTE: in the database, the first values in the tables of the
                #below id's, are empty/dummy values, used for when we are not
                #dealing with stocks.
                market_id = 1
                commodity_name_id = 1
                rate_id = 1
                if deals_with_stocks(fields[Input.ACCOUNT_FROM], fields[Input.ACCOUNT_TO]):
                    if fields[Input.MARKET] != '':
                        market_id = dba.market_id_from_market(fields[Input.MARKET])
                    if fields[Input.COMMODITY] != '':
                        commodity_name_id = dba.commodity_name_id_from_commodity_name(
                                fields[Input.COMMODITY], market_id)
                    rate_id = dba.get_latest_rate_id()
                    
                amount_value = fields[Input.AMOUNT])
                if is_negative_amount(amount_value):
                    amount_value = -1.0 * amount_value
                    
                records = records + 1
                statement_finance.add(
                    records,
                    {
                        'finance_id':None,
                        'date':fields[Input.DATE],
                        'year':fields[Input.DATE].year,
                        'month':fields[Input.DATE].month,
                        'day':fields[Input.DATE].day,
                        'account_from_id':account_from_id,
                        'account_to_id':account_to_id,
                        'amount': amount_value,
                        'comment':fields[Input.COMMENT],
                        'stock_name_id':commodity_name_id,
                        'shares':fields[Input.QUANTITY],
                        'price':fields[Input.PRICE],
                        'tax':fields[Input.TAX],
                        'commission':fields[Input.COMMISSION],
                        'active':1,
                        'rate_id':rate_id,
                        'currency_exchange_id':currency_exchange_id,
                        'date_created':date_created,                            
                        'date_modified':date_modified
                    }
                )
                currency_exchange_id = currency_exchange_id + 1
            return statement_finance
        except Exception as ex:
            print(Error.CREATE_STATEMENTS_TABLE_FINANCE, ex)
        finally:
            dba = None
