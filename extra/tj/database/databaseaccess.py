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
from decimal import Decimal
from datetime import datetime

from mappings import *

#TODO: compare this one with the lisa databaseaccess.py and put the same code in a global databaseaccess
# and inherit from that one.
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
            self.tblobject = Table('t_object', self.metadata, autoload=True)
            self.tblaccount = Table('t_account', self.metadata, autoload=True)
            self.tbltradingjournal = Table('t_tradingjournal', self.metadata, autoload=True)
            
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
                    'account': 't_account',
                    'tradingjournal': 't_trading_journal'
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
        mapper(T_TRADING_JOURNAL, self.tbltradingjournal)
        
    def config(self):
        """ Retrieve config file values """
        config = ConfigParser.RawConfigParser()
        config.read(self.myconf)
        
        self.dbhost = config.get('database', 'host')[1:-1]
        self.dbname = config.get('database', 'name')[1:-1]
        self.dbuser = config.get('database', 'user')[1:-1]
        self.dbpass = config.get('database', 'password')[1:-1]
 
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

    def oid_from_object(self, object_, date_created, date_modified):
        """ Get the oid from an object. """
        result = -1
        session = self.Session()
        try:
            # Get object id, based on object name
            # but first check if the object already exists
            # in T_OBJECT. If not, add it to the t_object table.
            obj = session.query(T_OBJECT).filter_by(name=object_).first() is not None
            if not obj: 
                session.add(T_OBJECT(object_, date_created, date_modified))
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

    def aid_from_account(self, account, date_created, date_modified):
        """ Get the aid from an account. """
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

    def pid_from_product(self, product, date_created, date_modified):
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
                session.add(T_PRODUCT(product, flg_income, date_created, date_modified))
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

    def snid_from_stockname(self, stockname, mid, date_created, date_modified):
        """ Get the snid from T_STOCK_NAME. """
        result = -1
        session = self.Session()
        try:
            # Get snid, based on stockname
            # but first check if the account already exists
            # in T_ACCOUNT. If not, add it to the t_account table.
            obj = session.query(T_STOCK_NAME).filter_by(name=stockname, mid=mid).first() is not None
            if not obj: 
                session.add(T_STOCK_NAME(stockname, mid, '', date_created, date_modified))
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

    def mid_from_market(self, code, date_created, date_modified):
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
                session.add(T_MARKET(code, 'TBD', '??', date_created, date_modified))
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
