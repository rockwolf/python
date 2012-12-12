#! /usr/local/bin/python
"""
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
from sqlalchemy import create_engine, Table, MetaData, \
        Column, Integer, or_, and_
from sqlalchemy.types import VARCHAR
from sqlalchemy.orm import mapper, clear_mappers
#from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from decimal import Decimal
from datetime import datetime

from database.mappings import *
from database.mappings_views import *
from modules_generic.function import *
from modules_generic.messagehandler import *
from modules.statement import Statement
from modules.constant import *
from modules.function import *

class DatabaseAccess():
    """ Connecting to the database. """ 

    def __init__(self, config):
        """ Initialize object. """
        try:
            self.config = config
            #print('postgresql://' + self.config.dbuser + ':' + self.config.dbpass + '@' + self.config.dbhost + '/' + self.config.dbname)
            self.db = create_engine(
                'postgresql://' 
                + self.config.dbuser
                + ':' 
                + self.config.dbpass 
                + '@' 
                + self.config.dbhost 
                + '/' 
                + self.config.dbname
                ,echo=False
            )
            self.Session = sessionmaker(bind=self.db) 
            # When recreating this object, the previous mappers where remembered by sqlalchemy. We need to clear them first.
            clear_mappers()
            self.metadata = MetaData(self.db)
            self.loaded_objects = {
                    TABLE_FINANCE : Table(TABLE_FINANCE, self.metadata, autoload=True),
                    TABLE_INVESTMENT: Table(TABLE_INVESTMENT, self.metadata, autoload=True),
                    TABLE_MARKET: Table(TABLE_MARKET, self.metadata, autoload=True),
                    TABLE_STOCK_NAME: Table(TABLE_STOCK_NAME, self.metadata, autoload=True),
                    TABLE_CATEGORY: Table(TABLE_CATEGORY, self.metadata, autoload=True),
                    TABLE_SUBCATEGORY: Table(TABLE_SUBCATEGORY, self.metadata, autoload=True),
                    TABLE_ACCOUNT: Table(TABLE_ACCOUNT, self.metadata, autoload=True),
                    TABLE_CURRENCY: Table(TABLE_CURRENCY, self.metadata, autoload=True),
                    TABLE_CURRENCY_EXCHANGE: Table(TABLE_CURRENCY_EXCHANGE, self.metadata, autoload=True),
                    TABLE_FORMULA: Table(TABLE_FORMULA, self.metadata, autoload=True),
                    TABLE_PARAMETER: Table(TABLE_PARAMETER, self.metadata, autoload=True),
                    TABLE_TRADE: Table(TABLE_TRADE, self.metadata, autoload=True),
                    TABLE_RATE: Table(TABLE_RATE, self.metadata, autoload=True),
                    TABLE_DRAWDOWN: Table(TABLE_DRAWDOWN, self.metadata, autoload=True),
                    TABLE_MARGIN: Table(TABLE_MARGIN, self.metadata, autoload=True),
                    TABLE_MARGIN_TYPE: Table(TABLE_MARGIN_TYPE, self.metadata,
                        autoload=True),
                    VIEW_FINANCE: Table(VIEW_FINANCE, self.metadata,
                        Column('finance_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_INVESTMENT: Table(VIEW_INVESTMENT, self.metadata,
                        Column('stock_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_MARKET: Table(VIEW_MARKET, self.metadata,
                        Column('market_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_STOCK_NAME: Table(VIEW_STOCK_NAME, self.metadata,
                        Column('stock_name_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_CATEGORY: Table(VIEW_CATEGORY, self.metadata,
                        Column('category_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_SUBCATEGORY: Table(VIEW_SUBCATEGORY, self.metadata,
                        Column('subcategory_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_ACCOUNT: Table(VIEW_ACCOUNT, self.metadata,
                        Column('account_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_CURRENCY: Table(VIEW_CURRENCY, self.metadata,
                        Column('currency_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_CURRENCY_EXCHANGE: Table(VIEW_CURRENCY_EXCHANGE, self.metadata,
                        Column('currency_exchange_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_FORMULA: Table(VIEW_FORMULA, self.metadata,
                        Column('formula_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_PARAMETER: Table(VIEW_PARAMETER, self.metadata,
                        Column('parameter_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_TRADE: Table(VIEW_TRADE, self.metadata,
                        Column('trade_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_RATE: Table(VIEW_RATE, self.metadata,
                        Column('rate_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_DRAWDOWN: Table(VIEW_DRAWDOWN, self.metadata,
                        Column('drawdown_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_MARGIN: Table(VIEW_MARGIN, self.metadata,
                        Column('margin_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_MARGIN_TYPE: Table(VIEW_MARGIN_TYPE, self.metadata,
                        Column('margin_type_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_REP_CHECK_TOTAL: Table(VIEW_REP_CHECK_TOTAL, self.metadata,
                        Column('account_name', VARCHAR(6), primary_key=True), autoload=True)
            }
            self.map_tables()
            self.map_views()
            self.tables = [x for x in self.metadata.tables.keys() if is_a_table(x) ]
        except Exception as ex:
            print("Error in initialisation of DatabaseAccess: ", ex)
   
    def map_tables(self):
        """ Create mappers for the tables on the db and the table classes. """
        mapper(T_FINANCE, self.loaded_objects[TABLE_FINANCE])
        mapper(T_INVESTMENT, self.loaded_objects[TABLE_INVESTMENT])
        mapper(T_MARKET, self.loaded_objects[TABLE_MARKET])
        mapper(T_STOCK_NAME, self.loaded_objects[TABLE_STOCK_NAME])
        mapper(T_CATEGORY, self.loaded_objects[TABLE_CATEGORY])
        mapper(T_SUBCATEGORY, self.loaded_objects[TABLE_SUBCATEGORY])
        mapper(T_ACCOUNT, self.loaded_objects[TABLE_ACCOUNT])
        mapper(T_TRADE, self.loaded_objects[TABLE_TRADE])
        mapper(T_RATE, self.loaded_objects[TABLE_RATE])
        mapper(T_CURRENCY, self.loaded_objects[TABLE_CURRENCY])
        mapper(T_CURRENCY_EXCHANGE, self.loaded_objects[TABLE_CURRENCY_EXCHANGE])
        mapper(T_FORMULA, self.loaded_objects[TABLE_FORMULA])
        mapper(T_PARAMETER, self.loaded_objects[TABLE_PARAMETER])
        mapper(T_DRAWDOWN, self.loaded_objects[TABLE_DRAWDOWN])
        mapper(T_MARGIN, self.loaded_objects[TABLE_MARGIN])
        mapper(T_MARGIN_TYPE, self.loaded_objects[TABLE_MARGIN_TYPE])
 
    def map_views(self):
        """ Create mappers for the views on the db and the view classes. """
        mapper(V_FINANCE, self.loaded_objects[VIEW_FINANCE])
        mapper(V_INVESTMENT, self.loaded_objects[VIEW_INVESTMENT])
        mapper(V_MARKET, self.loaded_objects[VIEW_MARKET])
        mapper(V_STOCK_NAME, self.loaded_objects[VIEW_STOCK_NAME])
        mapper(V_CATEGORY, self.loaded_objects[VIEW_CATEGORY])
        mapper(V_SUBCATEGORY, self.loaded_objects[VIEW_SUBCATEGORY])
        mapper(V_ACCOUNT, self.loaded_objects[VIEW_ACCOUNT])
        mapper(V_TRADE, self.loaded_objects[VIEW_TRADE])
        mapper(V_RATE, self.loaded_objects[VIEW_RATE])
        mapper(V_CURRENCY, self.loaded_objects[VIEW_CURRENCY])
        mapper(V_CURRENCY_EXCHANGE, self.loaded_objects[VIEW_CURRENCY_EXCHANGE])
        mapper(V_FORMULA, self.loaded_objects[VIEW_FORMULA])
        mapper(V_PARAMETER, self.loaded_objects[VIEW_PARAMETER])
        mapper(V_DRAWDOWN, self.loaded_objects[VIEW_DRAWDOWN])
        mapper(V_MARGIN, self.loaded_objects[VIEW_MARGIN])
        mapper(V_MARGIN_TYPE, self.loaded_objects[VIEW_MARGIN_TYPE])
        mapper(V_REP_CHECK_TOTAL, self.loaded_objects[VIEW_REP_CHECK_TOTAL])
        
    def config(self):
        """ Retrieve config file values """
        config = ConfigParser.RawConfigParser()
        config.read(self.myconf)
        self.dbhost = config.get('database', 'host')[1:-1]
        self.dbname = config.get('database', 'name')[1:-1]
        self.dbuser = config.get('database', 'user')[1:-1]
        self.dbpass = config.get('database', 'password')[1:-1]
 
    def get_categories(self):
        """ Get the categories. """
        values = []
        try:
            session = self.Session()
            query = session.query(T_CATEGORY)
            for instance in query: 
                values.append(instance.name)
        except Exception as ex:
            print(ERROR_GET_CATEGORIES, ex)
        finally:
            session.rollback()
            session = None
        return values
    
    def get_accounts(self):
        """ Get the accounts. """
        values = []
        try:
            session = self.Session()
            query = session.query(T_ACCOUNT)
            for instance in query: 
                values.append(instance.name)
        except Exception as ex:
            print(ERROR_GET_ACCOUNTS, ex)
        finally:
            session.rollback()
            session = None
        return values

    def get_subcategories(self):
        """ Get the subcategories. """
        values = []
        try:
            session = self.Session()
            query = session.query(T_SUBCATEGORY)
            for instance in query: 
                values.append(instance.name)
        except Exception as ex:
            print(ERROR_GET_SUBCATEGORIES, ex)
        finally:
            session.rollback()
            session = None
        return values

    def get_markets(self):
        """ Get the market codes. """
        values = []
        try:
            session = self.Session()
            query = session.query(T_MARKET).filter(
                    T_MARKET.active == 1)
            for instance in query: 
                values.append(instance.code)
        except Exception as ex:
            print(ERROR_GET_MARKETS, ex)
        finally:
            session.rollback()
            session = None
        return values
 
    def get_stock_names(self, code):
        """ Get the stock names. """
        values = []
        try:
            session = self.Session()
            query = session.query(T_STOCK_NAME).join(
                T_MARKET, 
                T_STOCK_NAME.market_id == T_MARKET.market_id
            ).filter(
                T_MARKET.code == code,
                T_STOCK_NAME.active == 1
            )
            for instance in query: 
                values.append(instance.name)
        except Exception as ex:
            print("Error in get_stock_names: ", ex)
        finally:
            session.rollback()
            session = None
        return values

    def get_market_description(self, market):
        """ Get the market description """
        value = ''
        try:
            session = self.Session()
            query = session.query(T_MARKET).filter(T_MARKET.code == market)
            for instance in query:
                value = instance.name
                break
        except Exception as ex:
            print(ERROR_GET_MARKET_DESCRIPTION, ex)
        finally:
            session.rollback()
            session = None
        return value 

    def get_stock_description(self, stock):
        """ Get the stock description """
        value = ''
        try:
            session = self.Session()
            query = session.query(T_STOCK_NAME).filter(T_STOCK_NAME.name == stock)
            for instance in query:
                value = instance.description
                break
        except Exception as ex:
            print("Error in get_stock_description: ", ex)
        finally:
            session.rollback()
            session = None
        return value 

    def get_stockinfo(self, sname):
        """ Get extra stock info. """
        values = []
        try:
            session = self.Session()
            query = session.query(
                T_STOCK_NAME.name.label("stock_name"), 
                T_MARKET.name.label("marketname"), 
                T_MARKET.country
            ).join(
                T_MARKET, 
                T_STOCK_NAME.market_id == T_MARKET.market_id
            ).filter(
                T_STOCK_NAME.name == sname
            )
            for instance in query: 
                values.append(instance.stock_name)
                values.append(instance.marketname)
                values.append(instance.country)
        except Exception as ex:
            print(ERROR_GET_STOCK_INFO, ex)
        finally:
            session.rollback()
            session = None
        return values
     
    def get_currencies(self):
        """ Get the currency codes. """
        values = []
        try:
            session = self.Session()
            query = session.query(T_CURRENCY)
            for instance in query: 
                values.append(instance.code)
        except Exception as ex:
            print(ERROR_GET_CURRENCIES, ex)
        finally:
            session.rollback()
            session = None
        return values

    def create_statements_TABLE_FINANCE(self, input_fields):
        """ Creates the records needed for TABLE_FINANCE. """
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            statement_finance = Statement(TABLE_FINANCE)
            records = 0
            currency_exchange_id = self.first_currency_exchange_id_from_latest()
            print('test: currency_exchange_id (first one)= ',
                    currency_exchange_id)
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
                            T_FINANCE(
                                None,
                                fields['date'],
                                string_to_date(fields['date']).year,
                                string_to_date(fields['date']).month,
                                string_to_date(fields['date']).day,
                                account_id,
                                category_id,
                                subcategory_id,
                                Decimal(fields['amount']),
                                fields['comment'],
                                stock_name_id,
                                int(fields['shares']),
                                Decimal(fields['price']),
                                Decimal(fields['tax']),
                                Decimal(fields['commission']),
                                1,
                                rate_id,
                                currency_exchange_id,
                                date_created,
                                date_modified
                            )
                        )
                        currency_exchange_id = currency_exchange_id + 1
            return statement_finance
        except Exception as ex:
            print(ERROR_CREATE_STATEMENTS_TABLE_FINANCE, ex)
        finally:
            session.rollback()
            session = None

    def create_statements_TABLE_RATE(self, input_fields):
        """ Creates the records needed for TABLE_RATE. """
        try:
            #TODO: session object is for querying if there is a record already,
            # but we don't need it here I think.
            date_created = current_date()
            date_modified = current_date()
            statement_rate = Statement(TABLE_RATE)
            records = 0
            for fields in input_fields:
                if deals_with_stocks(fields['category'], fields['subcategory']):
                    formula_id = self.get_formula_id_to_use(fields)
                    records = records + 1
                    
                    #TODO: get parameter values from parameter table
                    #
                    if fields['manual_flag'] == 1:
                        commission = fields['commission']
                        tax = fields['tax']
                        on_shares = -1.0
                        on_commission = -1.0
                        on_ordersize = -1.0
                        on_other = -1.0
                        calculated = -1.0
                    else:
                        #TODO: calculate something when necessary
                        on_shares = -1.0
                        #TODO: calculate something when necessary
                        on_commission = -1.0
                        #TODO: calculate something when necessary
                        on_ordersize = -1.0
                        #TODO: actually calculate something when necessary
                        on_other = 0.0
                        calculated = self.calculate_commission()
                        #TODO: function to determine which commission we
                        #need to select, at the moment 1 or 2, dependend on
                        #the amount and/or market
                        commission = self.get_parameter_value(1) #9.75
                        #TODO: function to determine...
                        tax = self.get_parameter_value(4) #BE tax
                    
                    statement_rate.add(
                        records,
                        T_RATE(
                            None,
                            Decimal(calculated),
                            Decimal(calculated)/Decimal(100.0),
                            Decimal(on_shares),
                            Decimal(on_commission),
                            Decimal(on_ordersize),
                            Decimal(on_other),
                            Decimal(commission),
                            Decimal(tax),
                            int(formula_id),
                            int(fields['manual_flag']),
                            date_created,
                            date_modified
                        )
                    )
            return statement_rate
        except Exception as ex:
            print(ERROR_CREATE_STATEMENTS_TABLE_RATE, ex)
    
    def create_statements_TABLE_INVESTING(self, input_fields):
        """ Creates the records needed for TABLE_INVESTING. """
        #TODO: this needs to be a portfolio module, but
        #we don't need it at the moment. Will be finished
        #later. T_STOCK is no longer needed, it will be T_INVESTMENT.
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            statement_investment = Statement(TABLE_INVESTMENT)
            records = 0
            for fields in input_fields:
                if is_an_investment(fields['category'], fields['subcategory']):
                    record = records + 1
                    #statement_investment.add(
                    #    records,
                    #    T_INVESTMENT(
                    #        None,
                    #        stock_name_id?,
                    #        action?, #do we need this? the cat. says it already
                    #        fields['price'],
                    #        fields['shares'],
                    #        fields['tax'],
                    #        fields['
                    #        date_created,
                    #        date_modified
                    #     )
                    # )
            return statement_INVESTMENT
        except Exception as ex:
            print(ERROR_CREATE_STATEMENTS_TABLE_INVESTMENT, ex)
        finally:
            session.rollback()
            session = None
   
    #TODO:
    #First do T_FINANCE
    #(Use date_created later to check the recently updated block... ?)
    #query with id_buy or id_sell
    #not found? it's a new entry so create it.
    #found?
    #  if id_buy filled in, we are buying now
    #  if id_sell filled in, we are selling now
    #  update accordingly
    #TODO: get_latest_finance_date_created (like with the currency)
    # -> look for the finance_id in T_TRADE using id_buy and id_sell
    # -> found = update needed so skip to put in update later?
    # -> not found = insert needed, so put in the insert statements
    # Can we update or commit on the fly? date_created and date_modified make this difficult...
    # Nah, we need to retrieve the old values anyway to create the new statement.
    # So creating insert and update statements and joining them later in this function should
    # be sufficient.
    #TODO: rewrite all the statement creation to give back a list of insert/update and delete statements.
    #This can later be used to do seperate insert/update and delete operations.
    #Beware that this also requires the writing of a function in statement.py
    #that returns the values from the statement-object (if this function doesn't already exist).
    #convention: 0 = insert / 1 = update / 3 = delete
    #NOTE: Correct way of updating =  Supplier.query.filter(<your stuff here, or user filter_by, or whatever is in your where clause>).update(values)
    #e.g.: session.query(Supplier).filter_by(id=2).update({"name": u"Mayowa"})
    #TABLE_TRADE.query.filter(market_name=...,stock_name=...).update({"date_...": date_... etc.})
    def create_statements_TABLE_TRADE(self, input_fields, statements_finance):
        """ Creates the records needed for TABLE_TRADE. """
        try:
            session = self.Session()
            date_created = current_date()
            date_modified = current_date()
            statement_trade = Statement(TABLE_TRADE)
            needs_update = 0
            records = 0
        
            finance_id = self.first_finance_id_from_latest()
            #TODO: get the entire line of information from TABLE_FINANCE, because we need the date
            #and price info too.
            if finance_id != -1:
                for fields in input_fields:
                    if is_a_trade(fields['category'], fields['subcategory']):            
                        market_id = self.market_id_from_market(
                                fields['market_name'])
                        stock_name_id = self.stock_name_id_from_stock_name(
                                fields['stock_name'], market_id)
                        
                        finance_record = self.get_finance_record(finance_id)
                        print('test finance_record=', finance_record)
                        trade_record = self.get_trade_record(finance_id)
                        print('test trade_record=', trade_record)

                        if self.trade_already_started(market_id, stock_name_id):
                            #NOTE: This is what we use to determine whether we
                            #need to fill in id_buy or id_sell
                            print('test: subcat=', fields['subcategory'])
                            print('test: cat=', fields['category'])
                            if fields['subcategory'] == 'buy' and \
                                T_TRADE.id_buy == -1:
                                id_buy = finance_id
                            elif fields['subcategory'] == 'sell' and \
                                T_TRADE.id_sell == -1:
                                id_sell = finance_id
                            else:
                                raise Exception(
                                    "{0} already contains a sell or buy record" \
                                    " and you are trying to add one like it again?".format(TABLE_TRADE))
                            #NOTE: When this code is executed, we know that
                            # we'll have to update later, instead of insert.
                            needs_update = 1
                        record = records + 1
                        #NOTE: price_buy will be fields['amount']
                        #When we buy more, it will be overwritten!
                        #Trading without adding to positions is assumed by this code!
                        #
                        #TODO:
                        #- Write seperate code in the main controller for the
                        #  update and the insert?
                        if needs_update == 1:
                            date_created = DEFAULT_DATE #TODO: get the previous date_created from the T_TRADE record.
                            #TODO: this is complex: we need to first check if it
                            #is new. When new, we need to add it in the regular
                            #way, but when it already exists, we need to create
                            #update statements. SQLAlchemy?
                            #TODO: check http://stackoverflow.com/questions/270879/efficiently-updating-database-using-sqlalchemy-orm
                            if we_are_buying(fields['subcategory']):
                                print('test: we are buying')
                                win_flag =
                                self.get_win_flag_value(
                                        price_buy,
                                        trade_record[1].price_sell,
                                        long_flag)
                            else:
                                print('test: we are selling')
                                win_flag =
                                self.get_win_flag_value(
                                        trade_record[1].price_buy,
                                        price_sell,
                                        long_flag)
                            at_work = trade_record[1].at_work
                            currency_id = trade_record[1].currency_id
                            drawdown_id = trade_record[1].drawdown_id
                            #TODO: create seperate application that manages T_DRAWDOWN based on selection
                            #where win_flag = -1
                        else:
                            print('test: we are buying =',
                                    we_are_buying(fields['subcategory']))
                            if we_are_buying(fields['subcategory']):
                                date_buy = date_created
                                year_buy = date_created.year
                                month_buy = date_created.month
                                day_buy = date_created.day
                                date_sell = string_to_date(DEFAULT_DATE)
                                year_sell = date_sell.year
                                month_sell = date_sell.month
                                day_sell = date_sell.day
                                price_buy = fields['amount']
                                price_sell = DEFAULT_PRICE
                            else:
                                date_sell = date_created
                                year_sell = date_created.year
                                month_sell = date_created.month
                                day_sell = date_created.day
                                date_buy = string_to_date(DEFAULT_DATE)
                                year_buy = date_buy.year
                                month_buy = month_buy.month
                                day_buy = day_buy.day
                                price_buy = DEFAULT_PRICE
                                price_sell = fields['amount']
                            risk = 0.0
                            initial_risk = 0.0
                            initial_risk_percent = initial_risk/100.0
                            win_flag = -1 #not yet finished, we can not now it yet.
                            at_work = price_buy*fields['shares']
                            currency_id = self.currency_id_from_currency(fields['currency'])
                            drawdown_id = self.new_drawdown_record()
                            print('test: long_flag =', self.get_long_flag(fields['category'],
                                    fields['subcategory'], trade_record))

                            long_flag = self.get_long_flag_value(fields['category'],
                                    fields['subcategory'], trade_record)
                            #TODO: if needs_update = 1: update else: insert
                            # How? Add update flag or something?
                            # Create seperate statements?
                            # Perhaps it's enough to ADD THE TRADE_ID from
                            # trade_record to T_TRADE(..., date_buy, ...) instead
                            # of None!!!
                            #TODO: check what we need to enter for risk,
                            #win_flag etc.
                            statement_trade.add(
                                records,
                                T_TRADE(
                                    None,
                                    date_buy,
                                    year_buy,
                                    month_buy,
                                    day_buy,
                                    date_sell,
                                    year_sell,
                                    month_sell,
                                    day_sell,
                                    long_flag,
                                    price_buy,
                                    price_sell,
                                    risk,
                                    initial_risk,
                                    initial_risk_percent,
                                    win_flag,
                                    at_work,
                                    id_buy, #how the fuck do I determene these 2
                                            #refs?
                                    id_sell,
                                    currency_id,
                                    drawdown_id,
                                    1, #active
                                    date_created,
                                    date_modified
                                )
                            )
                finance_id = finance_id + 1
            return statement_trade
        except Exception as ex:
            print(ERROR_CREATE_STATEMENTS_TABLE_TRADE, ex)
        finally:
            session.rollback()
            session = None

    def trade_already_started(self, market_id, stock_name_id):
        """
            Check if this trade has already started.
        """
        print('test: in trade already started: market_id=', market_id,
        'stock_name_id=', stock_name_id)
        result = False
        try:
            session = self.Session()
            #NOTE: id_buy or id_sell must be -1
            # but both can't be filled in (= finished trade)
            obj = session.query(T_TRADE).filter(
                    T_TRADE.market_id == market_id,
                    T_TRADE.stock_name_id == stock_name_id,
                    T_TRADE.active == 1).filter(
                        or_(
                            T_TRADE.id_buy == -1,
                            T_TRADE.id_sell == -1
                        )).filter(
                            T_TRADE.id_buy != -1,
                            T_TRADE.id_sell !=  -1
                       )
            for instance in obj:
                print('test:', instance)
                result = True
        except Exception as ex:
            print(ERROR_TRADE_ALREADY_STARTED, ex)
        return result

    #TODO: toroughly test this, especially the faulty trade_record crap
    def get_long_flag_value(self, category, subcategory, trade_record):
        """ Are we long? """
        result = False
        if trade_record == []:
            result = (category == 'buy') 
        else:
            result = (category == 'sell' and trade_record[1]['date_buy'] !=
                    DEFAULT_DATE)
        return 1 if result else 0

    #TODO: toroughly test this
    def get_win_flag_value(self, price_buy, price_sell, long_flag):
        """ Trade finished... did we win? """
        result = False
        if long_flag == 1 then:
            result = (price_buy < price_sell)
        else:
            result = (price_buy > price_sell)
        return 1 if result else 0

    def create_statements_TABLE_CURRENCY_EXCHANGE(self, input_fields):
        """ Creates the records needed for TABLE_CURRENCY_EXCHANGE. """
        try:
            statement_currency_exchange = Statement(TABLE_CURRENCY_EXCHANGE)
            date_created = current_date()
            date_modified = current_date()
            records = 0
            for fields in input_fields:
                records = records + 1
                #NOTE: we don't need to query, because we always add a new
                #currency_exchange line. The same value can be used multiple
                #times, so it's not possible to query if one already exists.
                statement_currency_exchange.add(
                    records,
                    T_CURRENCY_EXCHANGE(
                        None,
                        self.currency_id_from_currency(fields['currency']),
                        Decimal(fields['exchange_rate']),
                        date_created,
                        date_modified
                    )
                )
            return statement_currency_exchange
        except Exception as ex:
            print(ERROR_CREATE_STATEMENTS_TABLE_CURRENCY_EXCHANGE, ex)

    def calculate_commission(self):
        """ Calculation for T_RATE """
        return -1.0
    
    def write_to_database(self, statements):
        """ 
            Writes the records of a given statements list to the database.
        """
        try:
            if statements != []:
                statement_list = statements.get_statement_list()
                #TODO: create statements.get_insert_list()
                #get_update_list() => contains update statements for use in sqlalchemy
                #get_delete_list() => dummy, we won't be needing this
                #TODO: adjust this function to account for the update part.
                session = self.Session()
                try:
                    print(statements.table_name, end=': ')
                    session.add_all(statement_list)
                    session.commit()
                    print("{0} records added.".format(str(len(statement_list))))
                except Exception as ex:
                    print(ERROR_WRITE_TO_DATABASE, ex)
                finally:
                    session.rollback()
                    session = None
        except Exception as ex:
            print(ERROR_WRITE_TO_DATABASE_SESSION, ex)

    #def file_import_stocks(self, fields_db, fields_stock):
    #    """ Import stock information. """
    #    #TODO: this will become the statements(..., TABLE_STOCK) function
    #    # It will completely change too.
    #    try:
    #        session = self.Session()
    #        try:
    #            date_created = current_date()
    #            date_modified = current_date()
    #            print("STOCKS")
    #            print("______")
    #            print(MESSAGE_PREPARING)
    #            self.statementStock = Statement(TABLE_STOCK)
    #            records = 0
    #            i = 0
    #            for fields in fields_db:
    #                if (not fields['stock'] == '') :
    #                    subcategory_id = self.subcategory_id_from_subcategory(fields['subcategory'])
    #                    account_id = self.account_id_from_account(fields['account'])
    #                    category_id = self.category_id_from_category(fields['category'])
    #                    # Get id from T_FINANCE (to import in T_STOCK)
    #                    for instance in session.query(T_FINANCE).filter_by(
    #                        date=fields['date'],
    #                        account_id=account_id,
    #                        category_id=category_id,
    #                        subcategory_id=subcategory_id,
    #                        amount=Decimal(fields['amount']),
    #                        comment=fields['comment'],
    #                        market=fields['market'],
    #                        stock=fields['stock'],
    #                        shares=int(fields['shares']),
    #                        price=Decimal(fields['price']),
    #                        tax=Decimal(fields['tax']),
    #                        commission=Decimal(fields['commission']),
    #                        risk=Decimal(fields['risk'])
    #                    ):
    #                        finance_id = instance.finance_id
    #                    if fields_stock[i] != {}:
    #                        # Add new entry if it doesn't already exist
    #                        if self.update_stock(fields_stock, session, i,
    #                                finance_id, i):
    #                            records = records + 1
    #                # fields_db and fields_stock are the same size,
    #                # so we use an integer in the fields_db loop as an index
    #                # to get the corresponding fields_stock value
    #                i = i + 1
    #            print(MESSAGE_EXEC_ALL)
    #            statements.Execute(session)
    #        except Exception as ex:
    #            print(ERROR_FILE_IMPORT_STOCKS, ex)
    #        finally:
    #            session.commit()
    #            session = None
    #            print("{0} records added.".format(str(records)))
    #            print(DONE)
    #    except Exception as ex:
    #        print(ERROR_FILE_IMPORT_STOCKS_SESSION, ex)

    def update_finance(self, fields_db, session, i, finance_id, recordid):
        """ Add a new finance entry or update an existing one. """
        pass

    def update_stock(self, fields_stock, session, i, finance_id, recordid):
        """ Add a new stock entry or update an existing one. """
        #TODO: figure out what to do with this,
        # after the statement(..., TABLE_NAME) stuff is implemented.
        try:
            date_created = current_date()
            date_modified = current_date()
            # Get stock_name_id from T_STOCK_NAME if it exists (a new entry will be made in T_STOCK_NAME if it doesn't)
            #TODO: add descriptions to market_id_from_market and to
            #stock_name_id_from_stock_name)
            market_id = self.market_id_from_market(fields_stock[i]['market'])
            stock_name_id = self.stock_name_id_from_stock_name(fields_stock[i]['name'], market_id)
            vartax = Decimal(fields_stock[i]['tax'])
            varcommission = Decimal(fields_stock[i]['commission'])
            first_obj = session.query(T_STOCK).filter_by(
                      finance_id=finance_id,
                      price=Decimal(fields_stock[i]['price']),
                      shares=int(fields_stock[i]['shares']),
                      tax=vartax,
                      commission=varcommission
                  ).first()
            if first_obj is None: 
                # NEW
                self.statementStock.add(
                    recordid,
                    T_STOCK(
                        finance_id,
                        stock_name_id,
                        fields_stock[i]['action'],
                        Decimal(fields_stock[i]['price']),
                        int(fields_stock[i]['shares']),
                        vartax,
                        varcommission,
                        0,
                        date_created,
                        date_modified,
                        Decimal(fields_stock[i]['risk'])
                    )
                )
                return True;
        except Exception as ex:
           print(ERROR_UPDATE_STOCK, ex)
        return False;

    def export_records(self, name):
        """ Return the records from the table or view, defined by name. """
        records = None
        session = self.Session()
        try:
            records = session.query(name).all()
        except Exception as ex:
            print("Error in export_records: ", ex)
        finally:
            session.rollback()
            session = None
        return records

    def subcategory_id_from_subcategory(self, subcategory):
        """ Get the subcategory_id from a subcategory. """
        result = -1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            # Get subcategory_id, based on subcategory
            # but first check if the subcategory already exists
            # in T_SUBCATEGORY. If not, add it to the t_sub_categorytable.
            obj = session.query(T_SUBCATEGORY).filter_by(name=subcategory).first() is not None
            if not obj: 
                session.add(T_SUBCATEGORY(subcategory, date_created, date_modified))
                session.commit()
                for instance in session.query(func.max(T_SUBCATEGORY.subcategory_id).label('subcategory_id')):
                    result = instance.subcategory_id
            else:
                for instance in session.query(T_SUBCATEGORY).filter_by(name=subcategory):
                    result = str(instance.subcategory_id)
        except Exception as ex:
            print(ERROR_SUBCATEGORY_ID_FROM_SUBCATEGORY, ex)
        finally:
            session.rollback()
            session = None
        return result

    def account_id_from_account(self, account):
        """ Get the account_id from an account. """
        result = -1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            # Get account id, based on account name
            # but first check if the account already exists
            # in T_ACCOUNT. If not, add it to the t_account table.
            obj  = session.query(T_ACCOUNT).filter_by(name=account).first() is not None
            if not obj:
            	#TODO: add the ability to add a market description (Very low priority!)
                session.add(T_ACCOUNT(account, '', date_created, date_modified))
                session.commit()
                for instance in session.query(func.max(T_ACCOUNT.account_id).label('account_id')):
                    result = instance.account_id
            else:
                for instance in session.query(T_ACCOUNT).filter_by(name=account):
                    result = str(instance.account_id)
        except Exception as ex:
            print(ERROR_ACCOUNT_ID_FROM_ACCOUNT, ex)
        finally:
            session.rollback()
            session = None
        return result

    def category_id_from_category(self, category):
        """ Get the category_id from a category. """
        result = -1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            # Get category_id, based on category name
            # but first check if the category already exists
            # in T_CATEGORY. If not, add it to the t_category table.
            # if category ends with .rx: flg_income = 1, else 0
            if(category[-3:] == '.rx'):
                flg_income = 1
            elif(category[-3:] == '.tx'):
                flg_income = 0
            else:
                raise Exception("Wrong category in input: {0}".format(category))
            obj = session.query(T_CATEGORY).filter_by(name=category).first() is not None
            if not obj: 
                session.add(T_CATEGORY(category, flg_income, date_created, date_modified))
                session.commit()
                for instance in session.query(func.max(T_CATEGORY.category_id).label('category_id')):
                    result = instance.category_id
            else:
                for instance in session.query(T_CATEGORY).filter_by(name=category):
                    result = str(instance.category_id)
        except Exception as ex:
            print("Error retrieving category_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def stock_name_id_from_stock_name(self, stock_name, market_id):
        """ Get the stock_name_id from T_STOCK_NAME. """
        result = -1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            # Get stock_name_id, based on stock_name
            # but first check if the account already exists
            # in T_ACCOUNT. If not, add it to the t_account table.
            obj = session.query(T_STOCK_NAME).filter_by(name=stock_name, market_id=market_id).first() is not None
            if not obj: 
                session.add(T_STOCK_NAME(stock_name, market_id, '', date_created, date_modified))
                session.commit()
                for instance in session.query(func.max(T_STOCK_NAME.stock_name_id).label('stock_name_id')):
                    result = instance.stock_name_id
            else:
                for instance in session.query(T_STOCK_NAME).filter_by(name=stock_name, market_id=market_id):
                    result = str(instance.stock_name_id)
        except Exception as ex:
            print("Error retrieving stock_name_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def market_id_from_market(self, code):
        """ Get the market_id from T_MARKET. """
        result = -1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            obj = session.query(T_MARKET).filter_by(code=code).first() is not None
            if not obj: 
                # NOTE: this code means that when new market records have been added
                # during normal usage, a new uninstall/install/import will not be able
                # to fill in the name and country of the market.
                # For now, assume no new ones are added. If there are, add them to the
                # init_tables script!
                #TODO: add extra field in gui for the country code and country name
                # + add this to the input_fields. This way, we can also add new markets.
                # But: perhaps this makes the input too complex and a new button with a dialog window
                # behind it is needed?
                session.add(T_MARKET(None, code, 'TBD', '??', 1, date_created, date_modified))
                session.commit()
                for instance in session.query(func.max(T_MARKET.market_id).label('market_id')):
                    result = instance.market_id
            else:
                for instance in session.query(T_MARKET).filter_by(code=code):
                    result = str(instance.market_id)
        except Exception as ex:
            print("Error retrieving market_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def subcategory_from_subcategory_id(self, subcategory_id):
        """ Get the subcategory for a given subcategory_id from the T_SUBCATEGORY table. """
        result = ''
        session = self.Session()
        try:
            for instance in session.query(T_SUBCATEGORY).filter_by(subcategory_id=subcategory_id):
                result = instance.name
        except Exception as ex:
            print("Error retrieving subcategory from subcategory_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def accountname_from_account_id(self, account_id):
        """ Get the accountname for a given account_id from the T_ACCOUNT table. """
        result = ''
        session = self.Session()
        try:
            for instance in session.query(T_ACCOUNT).filter_by(account_id=account_id):
                result = instance.name
        except Exception as ex:
            print("Error retrieving accountname from account_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def category_from_category_id(self, category_id):
        """ Get the category for a given category_id from the T_CATEGORY table. """
        result = ''
        try:
            session = self.Session()
            for instance in session.query(T_CATEGORY).filter_by(category_id=category_id):
                result = instance.name
        except Exception as ex:
            print("Error retrieving category from category_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result
    
    def currency_id_from_currency(self, currency):
        """ Get the currency_id from a currency string (e.g.'USD'). """
        result = -1
        session = self.Session()
        try:
            first_obj = session.query(T_CURRENCY).filter_by(code=currency).first()
            if first_obj is not None:
                result = str(first_obj.currency_id)
            else:
                raise Exception("Error: currency {0} not found! -1 used as a currency_id.".format(currency))
        except Exception as ex:
            print(ERROR_ACCOUNT_ID_FROM_ACCOUNT, ex)
        finally:
            session.rollback()
            session = None
        return result

    def get_formula_id_to_use(self, fields):
        """ Gets the formula_id to use for a given trading line of the input fields.
        """
        #TODO: determine the rate_id, based on ???
        # Ah no, we need to create a new rate_id,
        # but determine the formula_id to use
        # fields['currency'] = USD => probably the formula with usd
        # fields['category'] = 'trade.tx'
        # fields['subcategory'] =  => 'buy' or 'sell'
        #TODO: do we need to add a dummy formula that multiplies by 1?
        #NOTE: do it manually for now, we'll fix this later
        formula_id = 1
        #if is_a_trade(fields):
        #       if uppercase(fields['currency']) == 'USD':
        #           formula_id = 2 #TODO: was it 2?      
        #       elif somethingsomething:
        #           formula_id = 1
        return formula_id

    def get_latest_rate_id(self):
        """ Gets the latest rate_id """
        result = -1
        session = self.Session()
        try:
            first_obj = session.query(T_RATE).order_by(T_RATE.rate_id.desc()).first()
            if first_obj is not None:
                result = first_obj.rate_id
            else:
                # We don't have one yet, so by making the last one 0,
                # a get_latest_rate_id() + 1 would become 1
                result = 0
        except Exception as ex:
            print("Error retrieving latest rate_id from T_RATE: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def get_parameter_value(self, parameter_id):
        """ Function to get the value that belongs to the given parameter. """
        result = ''
        session = self.Session()
        try:
            for instance in session.query(T_PARAMETER).filter_by(
                    parameter_id=parameter_id):
                result = instance.value
        except Exception as ex:
            print("Error retrieving parameter value: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def first_currency_exchange_id_from_latest(self):
        """ 
            Gets the first currency_exchange_id from the latest update
            block, which is determined by examining the date_created column.
        """
        result = -1
        session = self.Session()
        try:
            currency_exchange_created = self.get_latest_date_created(TABLE_CURRENCY_EXCHANGE)
            first_obj = session.query(T_CURRENCY_EXCHANGE).filter_by(
                    date_created=currency_exchange_created).first()
            if first_obj is not None:
                result = first_obj.currency_exchange_id
        except Exception as ex:
            print("Error in first_currency_id_from_latest: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def first_rate_id_from_latest(self):
        """ 
            Gets the first rate_id from the latest update
            block, which is determined by examining the date_created column.
        """
        result = -1
        session = self.Session()
        try:
            rate_created = self.get_latest_date_created(TABLE_RATE)
            obj = session.query(T_RATE).filter_by(date_created=rate_created)
            for instance in obj:
                result = instance.rate_id
        except Exception as ex:
            print("Error in first_rate_id_from_latest: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def first_finance_id_from_latest(self):
        """ 
            Gets the first finance_id from the latest update
            block, which is determined by examining the date_created column.
        """
        result = -1
        session = self.Session()
        try:
            finance_created = self.get_latest_date_created(TABLE_FINANCE)
            obj = session.query(T_FINANCE).filter_by(date_created=finance_created)
            for instance in obj:
                result = instance.finance_id
        except Exception as ex:
            print("Error in first_finance_id_from_latest: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def get_latest_date_created(self, tablename):
        """ Get's the latest date_created value that was added. """
        result = current_date()
        session = self.Session()
        try:
            if tablename == TABLE_FINANCE:
                first_obj = session.query(T_FINANCE).order_by(
                    T_FINANCE.finance_id.desc()).first()
            elif tablename == TABLE_RATE:
                first_obj = session.query(T_RATE).order_by(
                    T_RATE.rate_id.desc()).first()
            elif tablename == TABLE_CURRENCY_EXCHANGE:
                first_obj = session.query(T_CURRENCY_EXCHANGE).order_by(
                    T_CURRENCY_EXCHANGE.currency_exchange_id.desc()).first()
            else:
                first_obj = None
            if first_obj is not None:
                result = first_obj.date_created
        except Exception as ex:
            print('Error in get_latest_date_created for table', tablename + ':', ex)
        finally:
            session.rollback()
            session = None
        return result

    def get_finance_record(self, finance_id):
        """ 
            Gets the finance_record with the given finance_id.
        """
        result = []
        session = self.Session()
        try:
            first_obj = session.query(T_FINANCE).filter_by(finance_id =
                    finance_id).first() #finance_id is unique anyway
            if first_obj is not None:
                result = first_obj.get_record()
        except Exception as ex:
            print("Error in get_finance_record: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def get_trade_record(self, finance_id):
        """ 
            Gets the trade_record with the given finance_id set in
            either id_buy or id_sell.
        """
        result = []
        session = self.Session()
        try:
            finance_created = self.get_latest_date_created(TABLE_TRADE)
            first_obj = session.query(T_TRADE).filter(
                    or_(
                        T_TRADE.id_buy == finance_id,
                        T_TRADE.id_sell == finance_id)).first() #finance_id is unique anyway
            if first_obj is not None:
                result = first_obj.get_record()
        except Exception as ex:
            print("Error in get_finance_record: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def get_rep_check_total(self, check_totals):
        """ Returns a string with the totals per account. """
        result = "" 
        i = 0
        for entry in check_totals:
            if i == 0:
                result = entry[0] + \
                    '|' + str(entry[1])
            else:
                result = result + ' ' + entry[0] + \
                '|' + str(entry[1])
            i = i + 1
        return result

    def get_rep_check_totals(self):
        """ Returns a list with the account name and totals. """
        values = []
        session = self.Session()
        try:
            obj = session.query(V_REP_CHECK_TOTAL)
            for instance in obj:
                    values.append([instance.account_name,
                        instance.account_total])
        except Exception as ex:
            print("Error in get_rep_check_totals: ", ex)
        finally:
            session.rollback()
            session = None
        return values
    
    def new_drawdown_record(self):
        """ Creates a new record in T_DRAWDOWN with a default value of 0. """
        result = -1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            session.add(T_DRAWDOWN(None, 0, date_created, date_modified))
            session.commit()
            for instance in session.query(
                    func.max(T_DRAWDOWN.drawdown_id).label(
                        'drawdown_id')):
                result = instance.drawdown_id
        except Exception as ex:
            print(ERROR_NEW_DRAWDOWN_RECORD, ex)
        finally:
            session.rollback()
            session = None
        return result
