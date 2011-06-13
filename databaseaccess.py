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
#import psycopg2 as dbapi2
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import mapper
from mappings import *

class DatabaseAccess():
    """ Connecting to the database. """ 

    def __init__(self, config):
        """ Initialize object. """
        self.config = config

        print("Test1")
        db = create_engine('postgresql://' + self.config.dbuser + ':' + self.config.dbpass + '@' + self.config.dbhost + '/' + self.config.dbname)
        print("Test2")
        metadata = BoundMetaData(db)

        self.tblfinance = Table('T_FINANCE', metadata, autoload=True)
        self.tblstock = Table('T_STOCK', metadata, autoload=True)
        self.tblstockcurrent = Table('T_STOCK_CURRENT', metadata, autoload=True)
        self.tblmarket = Table('T_MARKET', metadata, autoload=True)
        self.tblstockname = Table('T_STOCK_NAME', metadata, autoload=True)
        self.tblproduct = Table('T_PRODUCT', metadata, autoload=True)
        self.tblmargin = Table('T_MARGIN', metadata, autoload=True)
        self.tblmargintype = Table('T_MARGIN_TYPE', metadata, autoload=True)

        self.tables = { 
                'finance': 'T_FINANCE',
                'stock': 'T_STOCK',
                'stockcurrent': 'T_STOCK_CURRENT',
                'market': 'T_MARKET',
                'stockname': 'T_STOCK_NAME',
                'product': 'T_PRODUCT',
                'margin': 'T_MARGIN',
                'margintype': 'T_MARGIN_TYPE'
                }

        self.sqlpath = 'sql'
        self.sqldrop = [ 'drop_tables.sql' ]
        self.sqlcreate = [ 'create_tables.sql' ]
        self.sqlinit = [ 'init_tables.sql' ]
        self.msgHandler = __import__('messagehandler')
    
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

    def file_import_line(self, fields_db):
            """ Convert general financial information. """
            #TODO: put this in the inherited class
            try:
                print("Test: file_import_line")
                #TODO: Create session in sqlalchemy and do the update that way.
                #db = dbapi2.connect(host=self.get_dbhost(),database=self.get_dbname(), user=self.get_dbuser(), password=self.get_dbpass())
                #cur = db.cursor()
                try:
                    exit(1)
                    now = datetime.now()
                    date_create = now.strftime("%Y-%m-%d %H:%M:%S")
                    date_modify = now.strftime("%Y-%m-%d %H:%M:%S")

                    #cur = db.cursor()
                    #cur.execute("insert into " + self.tblfinance + "(date, account, product, amount, flag, comment, date_create, date_modify) values('" + fields_db['date'] + "','" + fields_db['acc'] + "','" + fields_db['prod'] + "','" + fields_db['amount'] + "','" + fields_db['flag'] + "','" + fields_db['comment'] + "','" + date_create + "','" + date_modify + "');")
                finally:
                    #db.commit()
                    session.save()
                    session.flush()
                    #cur.close()
                    #db.close()
                    session = None
                #self.Progress() #Progress report should not be here, but at the highest level
            #except dbapi2.DatabaseError, e:
            except:
                print("Error: procedures: %s" % str(e))
                exit(1)
