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

from database.mappings import *
from database.mappings_views import *
from modules_generic.function import *
from modulesn_generic.messagehandler import *

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
                    'T_FINANCE': Table('t_finance', self.metadata, autoload=True),
                    'T_STOCK': Table('t_stock', self.metadata, autoload=True),
                    'T_MARKET': Table('t_market', self.metadata, autoload=True),
                    'T_STOCK_NAME': Table('t_stock_name', self.metadata, autoload=True),
                    'T_CATEGORY': Table('t_category', self.metadata, autoload=True),
                    'T_SUBCATEGORY': Table('t_subcategory', self.metadata, autoload=True),
                    'T_ACCOUNT': Table('t_account', self.metadata, autoload=True),
                    'T_CURRENCY': Table('t_currency', self.metadata, autoload=True),
                    'T_CURRENCY_EXCHANGE': Table('t_currency_exchange', self.metadata, autoload=True),
                    'T_FORMULA': Table('t_formula', self.metadata, autoload=True),
                    'T_TRADE': Table('t_trade', self.metadata, autoload=True),
                    'T_RATE': Table('t_rate', self.metadata, autoload=True),
                    'T_DRAWDOWN': Table('t_drawdown', self.metadata, autoload=True),
                    'T_MARGIN': Table('t_margin', self.metadata, autoload=True),
                    'T_MARGIN_TYPE': Table('t_margin_type', self.metadata,
                        autoload=True),
                    'V_FINANCE': Table('v_finance', self.metadata,
                        Column('finance_id', Integer, primary_key=True),
                        autoload=True),
                    'V_STOCK': Table('v_stock', self.metadata,
                        Column('stock_id', Integer, primary_key=True),
                        autoload=True),
                    'V_MARKET': Table('v_market', self.metadata,
                        Column('market_id', Integer, primary_key=True),
                        autoload=True),
                    'V_STOCK_NAME': Table('v_stock_name', self.metadata,
                        Column('stock_name_id', Integer, primary_key=True),
                        autoload=True),
                    'V_CATEGORY': Table('v_category', self.metadata,
                        Column('category_id', Integer, primary_key=True),
                        autoload=True),
                    'V_SUBCATEGORY': Table('v_subcategory', self.metadata,
                        Column('subcategory_id', Integer, primary_key=True),
                        autoload=True),
                    'V_ACCOUNT': Table('v_account', self.metadata,
                        Column('account_id', Integer, primary_key=True),
                        autoload=True),
                    'V_CURRENCY': Table('v_currency', self.metadata,
                        Column('currency_id', Integer, primary_key=True),
                        autoload=True),
                    'V_CURRENCY_EXCHANGE': Table('v_currency_exchange', self.metadata,
                        Column('currency_exchange_id', Integer, primary_key=True),
                        autoload=True),
                    'V_FORMULA': Table('v_formula', self.metadata,
                        Column('formula_id', Integer, primary_key=True),
                        autoload=True),
                    'V_TRADE': Table('v_trade', self.metadata,
                        Column('trade_id', Integer, primary_key=True),
                        autoload=True),
                    'V_RATE': Table('v_rate', self.metadata,
                        Column('rate_id', Integer, primary_key=True),
                        autoload=True),
                    'V_DRAWDOWN': Table('v_drawdown', self.metadata,
                        Column('drawdown_id', Integer, primary_key=True),
                        autoload=True),
                    'V_MARGIN': Table('v_margin', self.metadata,
                        Column('margin_id', Integer, primary_key=True),
                        autoload=True),
                    'V_MARGIN_TYPE': Table('v_margin_type', self.metadata,
                        Column('margin_type_id', Integer, primary_key=True), autoload=True)
            }
            self.map_tables()
            self.map_views()
            self.tables = [x for x in self.metadata.tables.keys() if
                    self.remove_views_from(x) ]
            self.statementFinance = StatementFinance()
            self.statementStock = StatementStock()
        except Exception as ex:
            print("Error in initialisation of DatabaseAccess: ", ex)
   
    def remove_views_from(self, key):
        """ Removes all dictionary entries starting with v_ """
        if key.lower()[0:2] == 't_':
            return True
        else:
            return False

    def map_tables(self):
        """ Create mappers for the tables on the db and the table classes. """
        mapper(T_FINANCE, self.loaded_objects['T_FINANCE'])
        mapper(T_STOCK, self.loaded_objects['T_STOCK'])
        mapper(T_MARKET, self.loaded_objects['T_MARKET'])
        mapper(T_STOCK_NAME, self.loaded_objects['T_STOCK_NAME'])
        mapper(T_CATEGORY, self.loaded_objects['T_CATEGORY'])
        mapper(T_SUBCATEGORY, self.loaded_objects['T_SUBCATEGORY'])
        mapper(T_ACCOUNT, self.loaded_objects['T_ACCOUNT'])
        mapper(T_TRADE, self.loaded_objects['T_TRADE'])
        mapper(T_RATE, self.loaded_objects['T_RATE'])
        mapper(T_CURRENCY, self.loaded_objects['T_CURRENCY'])
        mapper(T_CURRENCY_EXCHANGE, self.loaded_objects['T_CURRENCY_EXCHANGE'])
        mapper(T_FORMULA, self.loaded_objects['T_FORMULA'])
        mapper(T_DRAWDOWN, self.loaded_objects['T_DRAWDOWN'])
        mapper(T_MARGIN, self.loaded_objects['T_MARGIN'])
        mapper(T_MARGIN_TYPE, self.loaded_objects['T_MARGIN_TYPE'])
 
    def map_views(self):
        """ Create mappers for the views on the db and the view classes. """
        mapper(V_FINANCE, self.loaded_objects['V_FINANCE'])
        mapper(V_STOCK, self.loaded_objects['V_STOCK'])
        mapper(V_MARKET, self.loaded_objects['V_MARKET'])
        mapper(V_STOCK_NAME, self.loaded_objects['V_STOCK_NAME'])
        mapper(V_CATEGORY, self.loaded_objects['V_CATEGORY'])
        mapper(V_SUBCATEGORY, self.loaded_objects['V_SUBCATEGORY'])
        mapper(V_ACCOUNT, self.loaded_objects['V_ACCOUNT'])
        mapper(V_TRADE, self.loaded_objects['V_TRADE'])
        mapper(V_RATE, self.loaded_objects['V_RATE'])
        mapper(V_CURRENCY, self.loaded_objects['V_CURRENCY'])
        mapper(V_CURRENCY_EXCHANGE, self.loaded_objects['V_CURRENCY_EXCHANGE'])
        mapper(V_FORMULA, self.loaded_objects['V_FORMULA'])
        mapper(V_DRAWDOWN, self.loaded_objects['V_DRAWDOWN'])
        mapper(V_MARGIN, self.loaded_objects['V_MARGIN'])
        mapper(V_MARGIN_TYPE, self.loaded_objects['V_MARGIN_TYPE'])
        
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
            print("Error in get_categories: ", ex)
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
            print("Error in get_accounts: ", ex)
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
            print("Error in get_subcategories: ", ex)
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
                    active == 1)
            for instance in query: 
                values.append(instance.code)
        except Exception as ex:
            print("Error in get_markets: ", ex)
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
            print("Error in get_marketdescription: ", ex)
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
            print("Error in get_stockinfo: ", ex)
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
            print("Error in get_currencies: ", ex)
        finally:
            session.rollback()
            session = None
        return values

    def file_import_lines(self, fields_db):
        """ Convert general financial information. """
        #TODO: put this in the inherited class
        try:
            session = self.Session()
            try:
                date_created = current_date()
                date_modified = current_date()
                
                print("GENERAL")
                print("_______")
                print("Preparing statements...")
                self.statementFinance = StatementFinance()
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
                              market=fields['market'],
                              stock=fields['stock'],
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
                        self.statementFinance.Add(
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
                print("Executing statements all at once...")
                session.add_all(statements)
            finally:
                session.commit()
                session = None
                print("{0} records added.".format(str(records)))
                print("Done.")
        except Exception as ex:
            print("Error in file_import_lines: ", ex)
   
    def file_import_stocks(self, fields_db, fields_stock):
        """ Import stock information. """
        #TODO: put this in the inherited class
        try:
            session = self.Session()
            try:
                date_created = current_date()
                date_modified = current_date()
                print("STOCKS")
                print("______")
                print("Preparing statements...")
                self.statementStock = StatementStock()
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
                print("Executing statements all at once...")
                statements.Execute(session)
            except Exception as ex:
                print("Error in file_import_stocks: ", ex)
            finally:
                session.commit()
                session = None
                print("{0} records added.".format(str(records)))
                print("Done.")
        except Exception as ex:
            print("Error creating session in file_import_stocks: ", ex)

    def update_finance(self, fields_db, session, i, finance_id, recordid):
        """ Add a new finance entry or update an existing one. """
        pass

    def update_stock(self, fields_stock, session, i, finance_id, recordid):
        """ Add a new stock entry or update an existing one. """
        try:
            date_created = current_date()
            date_modified = current_date()
            # Get stock_name_id from T_STOCK_NAME if it exists (a new entry will be made in T_STOCK_NAME if it doesn't)
            #TODO: add descriptions to market_id_from_market and to stock_name_id_from_stockname)
            market_id = self.market_id_from_market(fields_stock[i]['market'], date_created, date_modified)
            stock_name_id = self.stock_name_id_from_stockname(fields_stock[i]['name'], market_id, date_created, date_modified)
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
                self.statementStock.Add(
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
           print("Error in update_stock: ", ex)
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
        pass

    def subcategory_id_from_subcategory(self, subcategory, date_created, date_modified):
        """ Get the subcategory_id from a subcategory. """
        result = -1
        session = self.Session()
        try:
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
            print("Error retrieving subcategory_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def account_id_from_account(self, account, date_created, date_modified):
        """ Get the account_id from an account. """
        result = -1
        session = self.Session()
        try:
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
            print("Error retrieving account_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def category_id_from_category(self, category, date_created, date_modified):
        """ Get the category_id from a category. """
        result = -1
        session = self.Session()
        try:
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

    def stock_name_id_from_stockname(self, stockname, market_id, date_created, date_modified):
        """ Get the stock_name_id from T_STOCK_NAME. """
        result = -1
        session = self.Session()
        try:
            # Get stock_name_id, based on stockname
            # but first check if the account already exists
            # in T_ACCOUNT. If not, add it to the t_account table.
            obj = session.query(T_STOCK_NAME).filter_by(name=stockname, market_id=market_id).first() is not None
            if not obj: 
                session.add(T_STOCK_NAME(stockname, market_id, '', date_created, date_modified))
                session.commit()
                for instance in session.query(func.max(T_STOCK_NAME.stock_name_id).label('stock_name_id')):
                    result = instance.stock_name_id
            else:
                for instance in session.query(T_STOCK_NAME).filter_by(name=stockname, market_id=market_id):
                    result = str(instance.stock_name_id)
        except Exception as ex:
            print("Error retrieving stock_name_id: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def market_id_from_market(self, code, date_created, date_modified):
        """ Get the market_id from T_MARKET. """
        result = -1
        session = self.Session()
        try:
            obj = session.query(T_MARKET).filter_by(code=code).first() is not None
            if not obj: 
                # NOTE: this code means that when new market records have been added
                # during normal usage, a new uninstall/install/import will not be able
                # to fill in the name and country of the market.
                # For now, assume no new ones are added. If there are, add them to the
                # init_tables script!
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

class Statement():
    """ A class to contain statements to be executed within the orm session. """

    def __init__(self):
        """ Init """
        try:
            self.statements = []
        except Exception as ex:
            print("Error in initialisation of Statements: ", ex)
 
    def Add(self, recordid, tablerow_object, tablename='table'):
        """ Add a statement with recordid and tablerow object. """
        try:
            # Add a statement
            # recordid
            self.statements[recordid-1].append(recordid)
            # tablerow object (statement)
            self.statements[recordid-1].append(tablerow_object)
        except Exception as ex:
            print("Error adding statement for ", tablename, ": ", ex)
   
    def Remove(self, index=-1):
        """ Remove statement added on specified index """
        try:
            self.statements.pop(index)
        except Exception as ex:
            print("Error removing statement from the list: ", ex)
    
    def Execute(self, session):
        """ Execute list of statements for given session """
        try:
            # First collect the statements, without the recordid.
            tablerow_objects = []
            for line in self.statements:
                tablerow_objects.append(line[1])
            # Now add the tablerows to the database, all at once.
            session.add_all(self.statements)
        except Exception as ex:
            print("Error executing statements: ", ex)

    def Print(self, tablename):
        """ Method that actually prints the statement info and text on the screen. """
        print('Statements for ', tablename)
        print('________________________','\n')
        for s in self.statements:
            print(s)

class StatementFinance(Statement):
    """ A derived Statement class for T_FINANCE. """
    
    def Add(self, recordid, tablerow_object):
        """ Add a statement with recordid and tablerow object for T_FINANCE. """
        super(StatementFinance, self).Add(
            recordid,
            tablerow_object,
            'T_FINANCE'
        )

    def Print(self):
        """ Prints the currently held statements for T_FINANCE. """
        super(StatementFinance, self).Print('T_FINANCE')

class StatementStock(Statement):
    """ A derived Statement class for T_STOCK. """
 
    def Add(self, recordid, tablerow_object):
        """ Add a statement with recordid and tablerow object for T_STOCK. """
        super(StatementStock, self).Add(
            recordid,
            tablerow_object,
            'T_STOCK'
        )
   
    def Print(self):
        """ Prints the currently held statements for T_STOCK. """
        super(StatementStock, self).Print('T_STOCK')
