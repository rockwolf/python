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
from sqlalchemy.orm import mapper
from mappings import *
from sqlalchemy.orm import sessionmaker
from decimal import Decimal

class DatabaseAccess():
    """ Connecting to the database. """ 

    def __init__(self, config):
        """ Initialize object. """
        try:
            self.config = config

            #print('postgresql://' + self.config.dbuser + ':' + self.config.dbpass + '@' + self.config.dbhost + '/' + self.config.dbname)
            self.db = create_engine('postgresql://' + self.config.dbuser + ':' + self.config.dbpass + '@' + self.config.dbhost + '/' + self.config.dbname, echo=False)
            self.Session = sessionmaker(bind=self.db) 
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
                    'object': 't_object'
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
        
    def config(self):
        """ Retrieve config file values """
        config = ConfigParser.RawConfigParser()
        config.read(self.myconf)
        
        self.dbhost = config.get('database', 'host')[1:-1]
        self.dbname = config.get('database', 'name')[1:-1]
        self.dbuser = config.get('database', 'user')[1:-1]
        self.dbpass = config.get('database', 'password')[1:-1]

    def get_values(self, qry):
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
        return values
 
    def get_products_from_finance(self):
        """ Get the products from the finance table. """
        str_list = [
                'select distinct product from',
                self.tblfinance,
                'order by prod;']
        return self.get_values(' '.join(str_list))

    def get_products(self):
        """ Get the products. """
        str_list = [
                'select product from',
                self.tblproduct,
                'order by product;']
        return self.get_values(' '.join(str_list))

    def get_accounts(self):
        """ Get the accounts. """
        str_list = [
                'select distinct acc from',
                self.tblfinance,
                'order by acc;']
        return self.get_values(' '.join(str_list))
 
    def get_markets(self):
        """ Get the market codes. """
        str_list = [
                'select distinct code from',
                self.tblmarket,
                'order by code;']
        return self.get_values(' '.join(str_list))
 
    def get_stocknames(self, code):
        """ Get the stock names. """
        str_list = [
                'select t1.name from',
                self.tblstockname,
                't1 join',
                self.tblmarket,
                't2 on t1.mid = t2.mid where t2.code =',
                "'" + str(code) + "'",
                'order by t1.name;']
        return self.get_values(' '.join(str_list))

    def get_stockinfo(self, sname):
        """ Get extra stock info. """
        str_list = [
                'select t1.description, t2.description from',
                self.tblstockname,
                't1 join',
                self.tblmarket,
                't2 on t1.mid = t2.mid where t1.name =',
                "'" + str(sname) + "';"]
        return self.get_values(' '.join(str_list))
        
    def get_expenses(self):
        """ Get the total expenses, ordered by year. """
        #TODO: extra flag in database, in seperate table?
        prd_expenses = [
                'account.start',
                'account.tx',
                'invest.invest',
                'invest.changestocks',
                'invest.buystocks']
        strprd_expenses = ''
        for prd in prd_expenses:
            str_list = [
                    strprd_expenses,
                    'and t1.product <>',
                    "'" + prd + "'"]
            prd_expensestr = ' '.join(str_list)
        str_list = [
                'select extract(year from t1.date), sum(t1.amount) from',
                self.tblfinance,
                't1 where t1.flag = 0 and',
                strprd_expensess,
                'group by extract(year from t1.date);']
        return self.get_values()

    def get_passive(self):
        """ Get the total passive income, ordered by year. """
        str_list = [
                'select sum(t1.amount) from',
                self.finance,
                "t1 where t1.product = 'invest.dividend'",
                "or t1.product = 'invest.refund';"]
        return self.get_values(' '.join(str_list))

    def calculate_sw(self, sname):
        """ Calculate the safe withdrawal value. """
        str_list = [
                'select t1.description, t2.description from',
                self.tblstockname,
                't1 join',
                self.tblmarket,
                't2 on t1.mid = t2.mid where t1.name =',
                "'" + str(sname) + "';"]
        return self.get_values(' '.join(str_list))

    def file_import_lines(self, fields_db):
            """ Convert general financial information. """
            #TODO: put this in the inherited class
            try:
                session = self.Session()
                try:
                    now = datetime.now()
                    date_create = now.strftime("%Y-%m-%d %H:%M:%S")
                    date_modify = now.strftime("%Y-%m-%d %H:%M:%S")
                    
                    print("Preparing statements...")
                    statements = []
                    for fields in fields_db:
                        # Get object id, based on object name
                        oid = -1
                        # TODO: check if objectname exists, if not, add a new one first!
                        for instance in session.query(T_OBJECT).filter_by(name=fields['object']): 
                            oid=instance.oid
                        statements.append(T_FINANCE(fields['date'], fields['account'], fields['product'], oid, Decimal(fields['amount']), int(fields['flag']), fields['comment'], date_create, date_modify))
                    #for s in statements:
                    #    print('test: ', s)

                    #TODO: get OID from T_OBJECT and use that for the insert, in stead of fields_db['object']
                    session.add_all(statements)
                finally:
                    session.commit()
                    session = None
            except Exception as ex:
                print("Error in file_import_lines: ", ex)
