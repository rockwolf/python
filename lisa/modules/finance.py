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
from modules_generic.function import *

class Finance(CoreModule):
    """
        Finance class.
    """
        
    def create_statements(self, input_fields):
        """
            Creates the records needed for TABLE_FINANCE
            and returns them as a Statement object.
        """
        #TODO: move all create statements tot their own module?
        #This code here is already way to big to my liking.
        try:
            dba = DatabaseAccess(self.config)
            date_created = current_date()
            date_modified = current_date()
            statement_finance = Statement(TABLE_FINANCE)
            records = 0
            currency_exchange_id = dba.first_currency_exchange_id_from_latest()
            rate_id = dba.first_rate_id_from_latest()
            for fields in input_fields:
                subcategory_id = dba.subcategory_id_from_subcategory(fields['subcategory'])
                account_id = dba.account_id_from_account(fields['account'])
                category_id = dba.category_id_from_category(fields['category'])
               
                #NOTE: in the database, the first values in the tables of the
                #below id's, are empty/dummy values, used for when we are not
                #dealing with stocks.
                market_id = 1
                stock_name_id = 1
                rate_id = 1
                if deals_with_stocks(fields['category'], fields['subcategory']):
                    if fields['market_name'] != '':
                        market_id = dba.market_id_from_market(fields['market_name'])
                    if fields['stock_name'] != '':
                        stock_name_id = dba.stock_name_id_from_stock_name(
                                fields['stock_name'], market_id)
                    rate_id = dba.get_latest_rate_id()
                finance_record = dba.get_specific_finance_record(
                    fields['date'],
                    account_id,
                    category_id,
                    subcategory_id,
                    Decimal(fields['amount']),
                    fields['comment'],
                    stock_name_id,
                    int(fields['shares']),
                    Decimal(fields['shares']),
                    Decimal(fields['tax']),
                    Decimal(fields['commission']))
                if finance_record is None:
                        records = records + 1
                        statement_finance.add(
                            records,
                            {
                                'finance_id':None,
                                'date':fields['date'],
                                'year':fields['date'].year,
                                'month':fields['date'].month,
                                'day':fields['date'].day,
                                'account_id':account_id,
                                'category_id':category_id,
                                'subcategory_id':subcategory_id,
                                'amount':Decimal(fields['amount']),
                                'comment':fields['comment'],
                                'stock_name_id':stock_name_id,
                                'shares':int(fields['shares']),
                                'price':Decimal(fields['price']),
                                'tax':Decimal(fields['tax']),
                                'commission':Decimal(fields['commission']),
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
            print(ERROR_CREATE_STATEMENTS_TABLE_FINANCE, ex)
        finally:
            dba = None
