#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.					
"""
from datetime import datetime

from database.databaseaccess import DatabaseAccess
from modules.function import *

class Finance(CoreModule):
    """
        Finance class.
    """
        
    def create_statements_TABLE_FINANCE(self, input_fields):
        """
            Creates the records needed for TABLE_FINANCE
            and returns them as a Statement object.
        """
        #TODO: move all create statements tot their own module?
        #This code here is already way to big to my liking.
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            statement_finance = Statement(TABLE_FINANCE)
            records = 0
            currency_exchange_id = self.first_currency_exchange_id_from_latest()
            rate_id = self.first_rate_id_from_latest()
            for fields in input_fields:
                subcategory_id = self.subcategory_id_from_subcategory(fields['subcategory'])
                account_id = self.account_id_from_account(fields['account'])
                category_id = self.category_id_from_category(fields['category'])
               
                #NOTE: in the database, the first values in the tables of the
                #below id's, are empty/dummy values, used for when we are not
                #dealing with stocks.
                market_id = 1
                stock_name_id = 1
                rate_id = 1
                if deals_with_stocks(fields['category'], fields['subcategory']):
                    if fields['market_name'] != '':
                        market_id = self.market_id_from_market(fields['market_name'])
                    if fields['stock_name'] != '':
                        stock_name_id = self.stock_name_id_from_stock_name(
                                fields['stock_name'], market_id)
                    rate_id = self.get_latest_rate_id()
                first_obj = session.query(T_FINANCE).filter_by(
                            date=fields['date'],
                            account_id=account_id,
                            category_id=category_id,
                            subcategory_id=subcategory_id,
                            amount=Decimal(fields['amount']),
                            comment=fields['comment'],
                            stock_name_id=stock_name_id,
                            shares=int(fields['shares']),
                            price=Decimal(fields['price']),
                            tax=Decimal(fields['tax']),
                            commission=Decimal(fields['commission']),
                            active=1
                            ).first()
                if first_obj is None:
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
            session.rollback()
            session = None
