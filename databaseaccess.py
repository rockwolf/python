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
from datetime import datetime
import psycopg2 as dbapi2
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import mapper, clear_mappers
from sqlalchemy.sql import exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from mappings import *
from decimal import Decimal
from datetime import datetime

class DatabaseAccess():
    """ Connecting to the database. """ 

    def __init__(self, config):
        """ Initialize object. """
        try:
            self.config = config
            
            #print('postgresql://' + self.config.dbuser + ':' + self.config.dbpass + '@' + self.config.dbhost + '/' + self.config.dbname)
            self.db = create_engine('postgresql://' + self.config.dbuser + ':' + self.config.dbpass + '@' + self.config.dbhost + '/' + self.config.dbname, echo=False)
            self.Session = sessionmaker(bind=self.db) 
            
            # When recreating this object, the previous mappers where remembered by sqlalchemy. We need to clear them first.
            clear_mappers()

            self.metadata = MetaData(self.db)
            
            self.tblfinance = Table('t_finance', self.metadata, autoload=True)
            self.tblstock = Table('t_stock', self.metadata, autoload=True)
            self.tblstockcurrent = Table('t_stock_current', self.metadata, autoload=True)
            self.tblmarket = Table('t_market', self.metadata, autoload=True)
            self.tblstockname = Table('t_stock_name', self.metadata, autoload=True)
            self.tblproduct = Table('t_product', self.metadata, autoload=True)
            self.tblmargin = Table('t_margin', self.metadata, autoload=True)
            self.tblmargintype = Table('t_margin_type', self.metadata, autoload=True)
            self.tblobject = Table('t_object', self.metadata, autoload=True)
            self.tblaccount = Table('t_account', self.metadata, autoload=True)
            
            self.map_tables()
            
            self.tables = { 
                    'finance': 't_finance',
                    'stock': 't_stock',
                    'stockcurrent': 't_stock_current',
                    'market': 't_market',
                    'stockname': 't_stock_name',
                    'product': 't_product',
                    'margin': 't_margin',
                    'margintype': 't_margin_type',
                    'object': 't_object',
                    'account': 't_account'
                    }

            self.sqlpath = 'sql'
            self.sqldrop = [ 'drop_tables.sql' ]
            self.sqlcreate = [ 'create_tables.sql' ]
            self.sqlinit = [ 'init_tables.sql' ]
            self.msgHandler = __import__('messagehandler')
        except Exception as ex:
            print("Error in initialisation of DatabaseAccess: ", ex)
    
    def map_tables(self):
        """ Create mappers for the tables on the db and the table classes. """
        mapper(T_FINANCE, self.tblfinance)
        mapper(T_STOCK, self.tblstock)
        mapper(T_STOCK_CURRENT, self.tblstockcurrent)
        mapper(T_MARKET, self.tblmarket)
        mapper(T_STOCK_NAME, self.tblstockname)
        mapper(T_PRODUCT, self.tblproduct)
        mapper(T_MARGIN, self.tblmargin)
        mapper(T_MARGIN_TYPE, self.tblmargintype)
        mapper(T_OBJECT, self.tblobject)
        mapper(T_ACCOUNT, self.tblaccount)
        
    def config(self):
        """ Retrieve config file values """
        config = ConfigParser.RawConfigParser()
        config.read(self.myconf)
        
        self.dbhost = config.get('database', 'host')[1:-1]
        self.dbname = config.get('database', 'name')[1:-1]
        self.dbuser = config.get('database', 'user')[1:-1]
        self.dbpass = config.get('database', 'password')[1:-1]

    def get_values(self, query):
        """ Global wrapper for retrieving values. """
        #db = dbapi2.connect(
        #        host=self.dbhost,
        #        database=self.dbname,
        #        user=self.dbuser,
        #        password=self.dbpass)
        #cur = db.cursor()
        #cur.execute (qry)
        #rows = cur.fetchall()
        #values = []
        #for row in rows:
        #    i = 0
        #    for col in row:
        #        values.append(row[i])
        #        i = i+1
        #db.commit()
        #cur.close()
        #db.close()
        values = []
        return values
 
    def get_products(self):
        """ Get the products. """
        values = []
        try:
            session = self.Session()
            query = session.query(T_PRODUCT)
            for instance in query: 
                values.append(instance.name)
        except Exception as ex:
            print("Error in get_products: ", ex)
        finally:
            session.rollback()
            session = None
        return values
    
    def get_products_from_finance(self):
        """ Get the distinct products from the finance table. """
        values = []
        #TODO: fix when function is needed. Was broken when switching to T_FINANCE.pid
        #try:
        #    session = self.Session()
        #    query = session.query(T_FINANCE).distinct(T_FINANCE.product)
        #    for instance in query: 
        #        values.append(instance.product)
        #except Exception as ex:
        #    print("Error in get_products_from_finance: ", ex)
        #finally:
        #    session.rollback()
        #    session = None
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

    def get_objects(self):
        """ Get the objects. """
        values = []
        try:
            session = self.Session()
            query = session.query(T_OBJECT)
            for instance in query: 
                values.append(instance.name)
        except Exception as ex:
            print("Error in get_objects: ", ex)
        finally:
            session.rollback()
            session = None
        return values

    def get_markets(self):
        """ Get the market codes. """
        values = []
        try:
            session = self.Session()
            query = session.query(T_MARKET)
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
            query = session.query(T_STOCK_NAME).join(T_MARKET, T_STOCK_NAME.mid == T_MARKET.mid).filter(T_MARKET.code == code)
            for instance in query: 
                values.append(instance.name)
        except Exception as ex:
            print("Error in get_stocknames: ", ex)
        finally:
            session.rollback()
            session = None
        return values

    def get_stockinfo(self, sname):
        """ Get extra stock info. """
        #str_list = [
        #        'select t1.description, t2.description from',
        #        self.tblstockname,
        #        't1 join',
        #        self.tblmarket,
        #        't2 on t1.mid = t2.mid where t1.name =',
        #        "'" + str(sname) + "';"]
        values = []
        return values
        
    def get_expenses(self):
        """ Get the total expenses, ordered by year. """
        #TODO: extra flag in database, in seperate table?
        #prd_expenses = [
        #        'account.start',
        #        'account.tx',
        #        'invest.invest',
        #        'invest.changestocks',
        #        'invest.buystocks']
        #strprd_expenses = ''
        #for prd in prd_expenses:
        #    str_list = [
        #            strprd_expenses,
        #            'and t1.product <>',
        #            "'" + prd + "'"]
        #    prd_expensestr = ' '.join(str_list)
        #str_list = [
        #        'select extract(year from t1.date), sum(t1.amount) from',
        #        self.tblfinance,
        #        't1 where t1.flag = 0 and',
        #        strprd_expensess,
        #        'group by extract(year from t1.date);']
        values = []
        return values

    def get_passive(self):
        """ Get the total passive income, ordered by year. """
        #str_list = [
        #        'select sum(t1.amount) from',
        #        self.finance,
        #        "t1 where t1.product = 'invest.dividend'",
        #        "or t1.product = 'invest.refund';"]
        values = []
        return values

    def calculate_sw(self, sname):
        """ Calculate the safe withdrawal value. """
        #str_list = [
        #        'select t1.description, t2.description from',
        #        self.tblstockname,
        #        't1 join',
        #        self.tblmarket,
        #        't2 on t1.mid = t2.mid where t1.name =',
        #        "'" + str(sname) + "';"]
        values = []
        return values

    def file_import_lines(self, fields_db):
            """ Convert general financial information. """
            #TODO: put this in the inherited class
            try:
                session = self.Session()
                try:
                    now = datetime.now()
                    date_create = now.strftime("%Y-%m-%d %H:%M:%S")
                    date_modify = now.strftime("%Y-%m-%d %H:%M:%S")
                    
                    print("GENERAL")
                    print("_______")
                    print("Preparing statements...")
                    statements = []
                    records = 0
                    for fields in fields_db:
                        oid = self.oid_from_object(fields['object'], date_create, date_modify)
                        aid = self.aid_from_account(fields['account'], date_create, date_modify)
                        pid = self.pid_from_product(fields['product'], date_create, date_modify)
                                                
                        obj = session.query(T_FINANCE).filter_by(date=fields['date'], aid=aid, pid=pid, oid=oid, amount=Decimal(fields['amount']), flag=int(fields['flag']), comment=fields['comment']).first() is not None
                        if not obj: 
                            records = records + 1
                            statements.append(T_FINANCE(fields['date'], aid, pid, oid, Decimal(fields['amount']), int(fields['flag']), fields['comment'], 1, date_create, date_modify))
                    #for s in statements:
                    #    print('test: ', s)

                    print("Executing statements all at once...")
                    session.add_all(statements)
                finally:
                    session.commit()
                    session = None
                    print("{0} records added.".format(str(records)))
                    print("Done.")
            except Exception as ex:
                print("Error in file_import_lines: ", ex)
   
    def file_import_stocks(self, fields_db, fields_comment):
            """ Import stocks from comment information. """
            #TODO: put this in the inherited class
            try:
                session = self.Session()
                try:
                    now = datetime.now()
                    date_create = now.strftime("%Y-%m-%d %H:%M:%S")
                    date_modify = now.strftime("%Y-%m-%d %H:%M:%S")
                    
                    print("STOCKS")
                    print("______")
                    print("Preparing statements...")
                    statements = []
                    records = 0
                    i = 0
                    for fields in fields_db:
                        oid = self.oid_from_object(fields['object'], date_create, date_modify)
                        aid = self.aid_from_account(fields['account'], date_create, date_modify)
                        pid = self.pid_from_product(fields['product'], date_create, date_modify)
                        # Get id from T_FINANCE (to import in T_STOCK)
                        for instance in session.query(T_FINANCE).filter_by(date=fields['date'], aid=aid, pid=pid, oid=oid, amount=Decimal(fields['amount']), flag=int(fields['flag']), comment=fields['comment']):
                            id = instance.id

                        # Get snid from T_STOCK_NAME if it exists (a new entry will be made in T_STOCK_NAME if it doesn't)
                        if fields_comment[i] != {}:
                            mid = self.mid_from_market(fields_comment[i]['market'], date_create, date_modify)
                            snid = self.snid_from_stockname(fields_comment[i]['name'], mid, date_create, date_modify)

                            # Add new entry if it doesn't already exist
                            obj = session.query(T_STOCK).filter_by(id=id, snid=snid, action=fields_comment[i]['action'], price=Decimal(fields_comment[i]['price']), quantity=int(fields_comment[i]['quantity'])).first() is not None
                            if not obj: 
                                records = records + 1
                                statements.append(T_STOCK(id, snid, fields_comment[i]['action'], Decimal(fields_comment[i]['price']), int(fields_comment[i]['quantity']), 0, date_create, date_modify))
                        #fields_db and fields_comment are the same size, so we use an integer in the fields_db loop as an index
                        #to get the corresponding fields_comment value
                        i = i + 1
                    #for s in statements:
                    #    print('test: ', s)

                    print("Executing statements all at once...")
                    session.add_all(statements)
                finally:
                    session.commit()
                    session = None
                    print("{0} records added.".format(str(records)))
                    print("Done.")
            except Exception as ex:
                print("Error in file_import_stocks: ", ex)

    def export_lines(self, all=False):
            """ Returns the t_finance lines from the database. """
            #TODO: Retrieve the object name 
            results = []
            try:
                session = self.Session()
                try:
                    records = 0
                    if all:
                        for instance in session.query(T_FINANCE):
                            records = records + 1
                            outline = self.export_line(instance)
                            results.append(':'.join(outline))
                    else:
                        for instance in session.query(T_FINANCE).filter_by(active=1):
                            records = records + 1
                            outline = self.export_line(instance)
                            results.append(':'.join(outline))
                finally:
                    session.rollback()
                    session = None
                    print("{0} records retrieved.".format(str(records)))

            except Exception as ex:
                print("Error in export_lines: ", ex)
            finally:
                return results

    def export_line(self, line):
        """ Assemble an export line. """
        exportline = []
        date = datetime.strftime(line.date, '%Y-%m-%d')
        exportline.append(str(date))
        exportline.append(self.accountname_from_aid(line.account))
        exportline.append(self.productname_from_pid(line.product))
        exportline.append(self.objectname_from_oid(line.oid))
        exportline.append(str(line.amount))
        exportline.append(str(line.flag))
        exportline.append(line.comment)
        return exportline

    def oid_from_object(self, object_, date_create, date_modify):
        """ Get the oid from an object. """
        result = -1
        session = self.Session()
        try:
            # Get object id, based on object name
            # but first check if the object already exists
            # in T_OBJECT. If not, add it to the t_object table.
            obj = session.query(T_OBJECT).filter_by(name=object_).first() is not None
            if not obj: 
                session.add(T_OBJECT(object_, date_create, date_modify))
                session.commit()
                for instance in session.query(func.max(T_OBJECT.oid).label('oid')):
                    result = instance.oid
            else:
                for instance in session.query(T_OBJECT).filter_by(name=object_):
                    result = str(instance.oid)
        except Exception as ex:
            print("Error retrieving oid: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def aid_from_account(self, account, date_create, date_modify):
        """ Get the aid from an account. """
        result = -1
        session = self.Session()
        try:
            # Get account id, based on account name
            # but first check if the account already exists
            # in T_ACCOUNT. If not, add it to the t_account table.
            obj = session.query(T_ACCOUNT).filter_by(name=account).first() is not None
            if not obj: 
                session.add(T_ACCOUNT(account, date_create, date_modify))
                session.commit()
                for instance in session.query(func.max(T_ACCOUNT.aid).label('aid')):
                    result = instance.aid
            else:
                for instance in session.query(T_ACCOUNT).filter_by(name=account):
                    result = str(instance.aid)
        except Exception as ex:
            print("Error retrieving aid: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def pid_from_product(self, product, date_create, date_modify):
        """ Get the pid from a product. """
        result = -1
        session = self.Session()
        try:
            # Get pid, based on product name
            # but first check if the product already exists
            # in T_PRODUCT. If not, add it to the t_product table.
            # if product ends with .rx: flg_income = 1, else 0
            if(product[-3:] == '.rx'):
                flg_income = 1
            elif(product[-3:] == '.tx'):
                flg_income = 0
            else:
                raise Exception("Wrong product in input-file: {0}".format(product))
            obj = session.query(T_PRODUCT).filter_by(name=product).first() is not None
            if not obj: 
                session.add(T_PRODUCT(product, flg_income, date_create, date_modify))
                session.commit()
                for instance in session.query(func.max(T_PRODUCT.pid).label('pid')):
                    result = instance.pid
            else:
                for instance in session.query(T_PRODUCT).filter_by(name=product):
                    result = str(instance.pid)
        except Exception as ex:
            print("Error retrieving pid: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def snid_from_stockname(self, stockname, mid, date_create, date_modify):
        """ Get the snid from T_STOCK_NAME. """
        result = -1
        session = self.Session()
        try:
            # Get snid, based on stockname
            # but first check if the account already exists
            # in T_ACCOUNT. If not, add it to the t_account table.
            obj = session.query(T_STOCK_NAME).filter_by(name=stockname, mid=mid).first() is not None
            if not obj: 
                session.add(T_STOCK_NAME(stockname, mid, '', date_create, date_modify))
                session.commit()
                for instance in session.query(func.max(T_STOCK_NAME.snid).label('snid')):
                    result = instance.snid
            else:
                for instance in session.query(T_STOCK_NAME).filter_by(name=stockname, mid=mid):
                    result = str(instance.snid)
        except Exception as ex:
            print("Error retrieving snid: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def mid_from_market(self, code, date_create, date_modify):
        """ Get the mid from T_MARKET. """
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
                session.add(T_MARKET(code, 'TBD', '??', date_create, date_modify))
                session.commit()
                for instance in session.query(func.max(T_MARKET.mid).label('mid')):
                    result = instance.mid
            else:
                for instance in session.query(T_MARKET).filter_by(code=code):
                    result = str(instance.mid)
        except Exception as ex:
            print("Error retrieving mid: ", ex)
        finally:
            session.rollback()
            session = None
        return result


    def objectname_from_oid(self, oid):
        """ Get the objectname for a given oid from the T_OBJECT table. """
        result = ''
        try:
            session = self.Session()
            for instance in session.query(T_OBJECT).filter_by(oid=oid):
                result = instance.name
        except Exception as ex:
            print("Error retrieving objectname from oid: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def accountname_from_aid(self, aid):
        """ Get the accountname for a given aid from the T_ACCOUNT table. """
        result = ''
        try:
            session = self.Session()
            for instance in session.query(T_ACCOUNT).filter_by(aid=aid):
                result = instance.name
        except Exception as ex:
            print("Error retrieving accountname from aid: ", ex)
        finally:
            session.rollback()
            session = None
        return result

    def productname_from_pid(self, pid):
        """ Get the productname for a given pid from the T_PRODUCT table. """
        result = ''
        try:
            session = self.Session()
            for instance in session.query(T_PRODUCT).filter_by(pid=pid):
                result = instance.name
        except Exception as ex:
            print("Error retrieving productname from pid: ", ex)
        finally:
            session.rollback()
            session = None
        return result
