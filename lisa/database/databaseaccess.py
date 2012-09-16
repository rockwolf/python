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
from sqlalchemy import create_engine, Table, MetaData, Column, Integer
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
                    TABLE_STOCK: Table(TABLE_STOCK, self.metadata, autoload=True),
                    TABLE_MARKET: Table(TABLE_MARKET, self.metadata, autoload=True),
                    TABLE_STOCK_NAME: Table(TABLE_STOCK_NAME, self.metadata, autoload=True),
                    TABLE_CATEGORY: Table(TABLE_CATEGORY, self.metadata, autoload=True),
                    TABLE_SUBCATEGORY: Table(TABLE_SUBCATEGORY, self.metadata, autoload=True),
                    TABLE_ACCOUNT: Table(TABLE_ACCOUNT, self.metadata, autoload=True),
                    TABLE_CURRENCY: Table(TABLE_CURRENCY, self.metadata, autoload=True),
                    TABLE_CURRENCY_EXCHANGE: Table(TABLE_CURRENCY_EXCHANGE, self.metadata, autoload=True),
                    TABLE_FORMULA: Table(TABLE_FORMULA, self.metadata, autoload=True),
                    TABLE_TRADE: Table(TABLE_TRADE, self.metadata, autoload=True),
                    TABLE_RATE: Table(TABLE_RATE, self.metadata, autoload=True),
                    TABLE_DRAWDOWN: Table(TABLE_DRAWDOWN, self.metadata, autoload=True),
                    TABLE_MARGIN: Table(TABLE_MARGIN, self.metadata, autoload=True),
                    TABLE_MARGIN_TYPE: Table(TABLE_MARGIN_TYPE, self.metadata,
                        autoload=True),
                    VIEW_FINANCE: Table(VIEW_FINANCE, self.metadata,
                        Column('finance_id', Integer, primary_key=True),
                        autoload=True),
                    VIEW_STOCK: Table(VIEW_STOCK, self.metadata,
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
                        Column('margin_type_id', Integer, primary_key=True), autoload=True)
            }
            self.map_tables()
            self.map_views()
            self.tables = [x for x in self.metadata.tables.keys() if
                    self.is_a_table(x) ]
            self.statementFinance = Statement(TABLE_FINANCE)
            self.statementStock = Statement(TABLE_STOCK)
        except Exception as ex:
            print("Error in initialisation of DatabaseAccess: ", ex)
   
    def is_a_table(self, key):
        """ Used to ignore all dictionary entries that don't start with t_ """
        if key.lower()[0:2] == 't_':
            return True
        else:
            return False

    def map_tables(self):
        """ Create mappers for the tables on the db and the table classes. """
        mapper(T_FINANCE, self.loaded_objects[TABLE_FINANCE])
        mapper(T_STOCK, self.loaded_objects[TABLE_STOCK])
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
        mapper(T_DRAWDOWN, self.loaded_objects[TABLE_DRAWDOWN])
        mapper(T_MARGIN, self.loaded_objects[TABLE_MARGIN])
        mapper(T_MARGIN_TYPE, self.loaded_objects[TABLE_MARGIN_TYPE])
 
    def map_views(self):
        """ Create mappers for the views on the db and the view classes. """
        mapper(V_FINANCE, self.loaded_objects[VIEW_FINANCE])
        mapper(V_STOCK, self.loaded_objects[VIEW_STOCK])
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
        mapper(V_DRAWDOWN, self.loaded_objects[VIEW_DRAWDOWN])
        mapper(V_MARGIN, self.loaded_objects[VIEW_MARGIN])
        mapper(V_MARGIN_TYPE, self.loaded_objects[VIEW_MARGIN_TYPE])
        
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
 
    def get_stocknames(self, code):
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
            print("Error in get_stocknames: ", ex)
        finally:
            session.rollback()
            session = None
        return values

    def get_marketdescription(self, market):
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

    def get_stockdescription(self, stock):
        """ Get the stock description """
        value = ''
        try:
            session = self.Session()
            query = session.query(T_STOCK_NAME).filter(T_STOCK_NAME.name == stock)
            for instance in query:
                value = instance.description
                break
        except Exception as ex:
            print("Error in get_stockdescription: ", ex)
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
                T_STOCK_NAME.name.label("stockname"), 
                T_MARKET.name.label("marketname"), 
                T_MARKET.country
            ).join(
                T_MARKET, 
                T_STOCK_NAME.market_id == T_MARKET.market_id
            ).filter(
                T_STOCK_NAME.name == sname
            )
            for instance in query: 
                values.append(instance.stockname)
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

    def create_statements(self, input_fields, table_name):
        """ Creates the record statements for a given table. """
        if table_name == TABLE_FINANCE:
            return self.create_statements_TABLE_FINANCE(input_fields)
        elif table_name == TABLE_STOCK:
            return self.create_statements_TABLE_STOCK(input_fields)
        elif table_name == TABLE_TRADE:
            return self.create_statements_TABLE_TRADE(input_fields)

    def create_statements_TABLE_FINANCE(self, input_fields):
        """ Creates the records needed for TABLE_FINANCE. """
        try:
            session = self.Session()
            date_created = current_date()
            date_modified = current_date()
            statement_finance = Statement(TABLE_FINANCE)
            records = 0
            for fields in input_fields:
                #TODO: only retrieve these id values when needed.
                subcategory_id = self.subcategory_id_from_subcategory(fields['subcategory'])
                account_id = self.account_id_from_account(fields['account'])
                category_id = self.category_id_from_category(fields['category'])
                if fields['market_name'] != '':
                    market_id = self.market_id_from_market(fields['market_name'])
                else:
                    market_id = 0
                if fields['stock_name'] != '':
                    stock_name_id = self.stock_name_id_from_stock_name(
                            fields['stock_name'], market_id)
                else:
                    stock_name_id = 0
                #TODO: when trading, the rate_id should be determined somehow.
                #rate_id = ? (default 0)
                rate_id = 0
                obj = session.query(T_FINANCE).filter_by(
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
                if obj is None: 
                        print(fields)
                        print(fields['date'])
                        print(string_to_date(fields['date']))
                        records = records + 1
                        statement_finance.add(
                            records,
                            T_FINANCE(
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
                                date_created,
                                date_modified
                            )
                        )
            session = None
            return statement_finance
        except Exception as ex:
            print(ERROR_CREATE_STATEMENTS_TABLE_FINANCE, ex)

    def create_statements_TABLE_STOCK(self):
        """ Creates the records needed for TABLE_STOCK. """
        pass
    
    def create_statements_TABLE_TRADE(self):
        """ Creates the records needed for TABLE_TRADE. """
        pass

    def write_to_database(self, statements):
        """ Writes the records of a given statements list to the database.
        """
        try:
            session = self.Session()
            try:
                print(MESSAGE_EXEC_ALL)
                session.add_all(statements)
                session.commit()
                session = None
                print("{0} records added.".format(str(len(statements))))
            except Exception as ex:
                session.rollback()
                print(ERROR_WRITE_TO_DATABASE, ex)
        except Exception as ex:
            print(ERROR_WRITE_TO_DATABASE_SESSION, ex)

    def file_import_lines(self, fields_db):
        """ Convert general financial information. """
        #TODO: this will become the statements(..., TABLE_FINANCE) function.
        # This will completely change.
        try:
            session = self.Session()
            try:
                date_created = current_date()
                date_modified = current_date()
                
                print("GENERAL")
                print("_______")
                print(MESSAGE_PREPARING)
                self.statementFinance = Statement(TABLE_FINANCE)
                records = 0
                for fields in fields_db:
                    subcategory_id = self.subcategory_id_from_subcategory(fields['subcategory'], date_created, date_modified)
                    account_id = self.account_id_from_account(fields['account'], date_created, date_modified)
                    category_id = self.category_id_from_category(fields['category'], date_created, date_modified)
                                            
                    obj = session.query(T_FINANCE).filter_by(
                              date=fields['date'],
                              account_id=account_id,
                              category_id=category_id,
                              subcategory_id=subcategory_id,
                              amount=Decimal(fields['amount']),
                              comment=fields['comment'],
                              market=fields['market_name'],
                              stock=fields['stock_name'],
                              shares=int(fields['shares']),
                              price=Decimal(fields['price']),
                              tax=Decimal(fields['tax']),
                              commission=Decimal(fields['commission']),
                              risk=Decimal(fields['risk'])
                          ).first()
                    if obj is None: 
                        #TODO: Change the list to contain both an id and the
                        # T_FINANCE(... object. Then also search in the
                        # lists if the current id is already present or not
                        # and change it? => can't work, because it's gonna
                        # be a new id.
                        # Updating can only be done on a count record (see
                        # the one below, and then only when triggered from
                        # a rowclick or something.
                        # Aha: input field + press an update button, but
                        # make sure that at least one row is always selected
                        # in the table
                        # Then the rownumber can act as the recordid to
                        # search for in the statement-list.
                        # e.g.: StatementsFinance.statements =
                        # [[1,''],[2,''],[3,'']] 
                        # and StatementsStock.statements = 
                        # [[2,''],[3,'']]  (in this ex., only the last 2
                        # entries are stocks.
                        # NEW
                        records = records + 1
                        self.statementFinance.add(
                            records,
                            T_FINANCE(
                                fields['date'],
                                account_id,
                                category_id,
                                subcategory_id,
                                Decimal(fields['amount']),
                                fields['comment'],
                                fields['stock'],
                                fields['market'],
                                int(fields['shares']),
                                Decimal(fields['price']),
                                Decimal(fields['tax']),
                                Decimal(fields['commission']),
                                1,
                                date_created,
                                date_modified,
                                Decimal(fields['risk']),
                                fields['date'].year,
                                fields['date'].month,
                                fields['date'].day
                            )
                        )
                print(MESSAGE_EXEC_ALL)
                session.add_all(statements)
            finally:
                session.commit()
                session = None
                print("{0} records added.".format(str(records)))
                print("Done.")
        except Exception as ex:
            print(ERROR_FILE_IMPORT_LINES, ex)
   
    def file_import_stocks(self, fields_db, fields_stock):
        """ Import stock information. """
        #TODO: this will become the statements(..., TABLE_STOCK) function
        # It will completely change too.
        try:
            session = self.Session()
            try:
                date_created = current_date()
                date_modified = current_date()
                print("STOCKS")
                print("______")
                print(MESSAGE_PREPARING)
                self.statementStock = Statement(TABLE_STOCK)
                records = 0
                i = 0
                for fields in fields_db:
                    if (not fields['stock'] == '') :
                        subcategory_id = self.subcategory_id_from_subcategory(fields['subcategory'], date_created, date_modified)
                        account_id = self.account_id_from_account(fields['account'], date_created, date_modified)
                        category_id = self.category_id_from_category(fields['category'], date_created, date_modified)
                        # Get id from T_FINANCE (to import in T_STOCK)
                        for instance in session.query(T_FINANCE).filter_by(
                            date=fields['date'],
                            account_id=account_id,
                            category_id=category_id,
                            subcategory_id=subcategory_id,
                            amount=Decimal(fields['amount']),
                            comment=fields['comment'],
                            market=fields['market'],
                            stock=fields['stock'],
                            shares=int(fields['shares']),
                            price=Decimal(fields['price']),
                            tax=Decimal(fields['tax']),
                            commission=Decimal(fields['commission']),
                            risk=Decimal(fields['risk'])
                        ):
                            finance_id = instance.finance_id
                        if fields_stock[i] != {}:
                            # Add new entry if it doesn't already exist
                            if self.update_stock(fields_stock, session, i,
                                    finance_id, i):
                                records = records + 1
                    # fields_db and fields_stock are the same size,
                    # so we use an integer in the fields_db loop as an index
                    # to get the corresponding fields_stock value
                    i = i + 1
                print(MESSAGE_EXEC_ALL)
                statements.Execute(session)
            except Exception as ex:
                print(ERROR_FILE_IMPORT_STOCKS, ex)
            finally:
                session.commit()
                session = None
                print("{0} records added.".format(str(records)))
                print(DONE)
        except Exception as ex:
            print(ERROR_FILE_IMPORT_STOCKS_SESSION, ex)

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
            obj = session.query(T_STOCK).filter_by(
                      finance_id=finance_id,
                      price=Decimal(fields_stock[i]['price']),
                      shares=int(fields_stock[i]['shares']),
                      tax=vartax,
                      commission=varcommission
                  ).first()
            if obj is None: 
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
        #TODO: use either this or the export_lines function
        records = None
        try:
            session = self.Session()
            records = session.query(name).all()
        except Exception as ex:
            print("Error in export_records: ", ex)
        finally:
            session.rollback()
            session = None
            return records
        
    def remove_line(self, rownumber):
        """ Removes a line from the table. """
        #TODO: when trade.tx, tr... etc. (= stock), remove from both
        #classes.
        #TODO: make the Statement-classes accessible from this function?
        #NOTE: I don't think this one is necessary, because we always make
        #sure the information is correct before we press execute.
        pass

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
            obj = session.query(T_ACCOUNT).filter_by(name=account).first() is not None
            if not obj: 
                session.add(T_ACCOUNT(account, date_created, date_modified))
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
                raise Exception("Wrong category in input-file: {0}".format(category))
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
                session.add(T_MARKET(code, 'TBD', '??', date_created, date_modified))
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
        try:
            session = self.Session()
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
        try:
            session = self.Session()
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
