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

from database.mappings import *

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
            
            self.tblfinance = Table('t_finance', self.metadata, autoload=True)
            self.tblstock = Table('t_stock', self.metadata, autoload=True)
            self.tblstockcurrent = Table('t_stock_current', self.metadata, autoload=True)
            self.tblmarket = Table('t_market', self.metadata, autoload=True)
            self.tblstockname = Table('t_stock_name', self.metadata, autoload=True)
            self.tblcategory = Table('t_category', self.metadata, autoload=True)
            self.tblmargin = Table('t_margin', self.metadata, autoload=True)
            self.tblmargintype = Table('t_margin_type', self.metadata, autoload=True)
            self.tblsubcategory = Table('t_sub_category', self.metadata, autoload=True)
            self.tblaccount = Table('t_account', self.metadata, autoload=True)
            
            self.map_tables()
            
            self.tables = { 
                'finance': 't_finance',
                'stock': 't_stock',
                'stockcurrent': 't_stock_current',
                'market': 't_market',
                'stockname': 't_stock_name',
                'category': 't_category',
                'margin': 't_margin',
                'margintype': 't_margin_type',
                'subcategory': 't_sub_category',
                'account': 't_account'
            }

            self.sqlpath = 'sql'
            self.sqldrop = [ 'drop_tables.sql' ]
            self.sqlcreate = [ 'create_tables.sql' ]
            self.sqlinit = [ 'init_tables.sql' ]
            self.msgHandler = __import__('messagehandler')

            self.statementFinance = StatementFinance()
            self.statementStock = StatementStock()
        except Exception as ex:
            print("Error in initialisation of DatabaseAccess: ", ex)
    
    def map_tables(self):
        """ Create mappers for the tables on the db and the table classes. """
        mapper(T_FINANCE, self.tblfinance)
        mapper(T_STOCK, self.tblstock)
        mapper(T_STOCK_CURRENT, self.tblstockcurrent)
        mapper(T_MARKET, self.tblmarket)
        mapper(T_STOCK_NAME, self.tblstockname)
        mapper(T_PRODUCT, self.tblcategory)
        mapper(T_MARGIN, self.tblmargin)
        mapper(T_MARGIN_TYPE, self.tblmargintype)
        mapper(T_SUB_CATEGORY, self.tblsubcategory)
        mapper(T_ACCOUNT, self.tblaccount)
        
    def config(self):
        """ Retrieve config file values """
        config = ConfigParser.RawConfigParser()
        config.read(self.myconf)
        
        self.dbhost = config.get('database', 'host')[1:-1]
        self.dbname = config.get('database', 'name')[1:-1]
        self.dbuser = config.get('database', 'user')[1:-1]
        self.dbpass = config.get('database', 'password')[1:-1]
 
    def get_categorys(self):
        """ Get the categorys. """
        values = []
        try:
            session = self.Session()
            query = session.query(T_PRODUCT)
            for instance in query: 
                values.append(instance.name)
        except Exception as ex:
            print("Error in get_categorys: ", ex)
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
            query = session.query(T_SUB_CATEGORY)
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
            query = session.query(T_STOCK_NAME).join \
            (
                T_MARKET, 
                T_STOCK_NAME.mid == T_MARKET.mid
            ).filter \
            (
                T_MARKET.code == code
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
                T_STOCK_NAME.mid == T_MARKET.mid
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
        
    def file_import_lines(self, fields_db):
        """ Convert general financial information. """
        #TODO: put this in the inherited class
        try:
            session = self.Session()
            try:
                now = datetime.now()
                date_created = now.strftime("%Y-%m-%d %H:%M:%S")
                date_modified = now.strftime("%Y-%m-%d %H:%M:%S")
                
                print("GENERAL")
                print("_______")
                print("Preparing statements...")
                self.statementFinance = StatementFinance()
                records = 0
                for fields in fields_db:
                    scid = self.scid_from_subcategory(fields['subcat'], date_created, date_modified)
                    aid = self.aid_from_account(fields['account'], date_created, date_modified)
                    cid = self.cid_from_category(fields['category'], date_created, date_modified)
                                            
                    obj = session.query(T_FINANCE).filter_by(
                              date=fields['date'],
                              aid=aid,
                              cid=cid,
                              scid=scid,
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
                                aid,
                                cid,
                                scid,
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
                        
                    #else:
                    #    # UPDATE EXISTING
                    #    #TODO: fix - SessionMaker has no attribute save - error
                    #    obj.date = fields['date']
                    #    obj.aid = aid
                    #    obj.cid = cid
                    #    obj.scid = scid
                    #    obj.amount = Decimal(fields['amount'])
                    #    obj.comment = fields['comment']
                    #    obj.stock = fields['stock']
                    #    obj.market = fields['market']
                    #    obj.shares = int(fields['shares'])
                    #    obj.price = Decimal(fields['price'])
                    #    obj.tax = Decimal(fields['tax'])
                    #    obj.commission = Decimal(fields['commission'])
                    #    obj.active = 1
                    #    obj.date_modified = date_modified
                    #    obj.risk = Decimal(fields['risk'])
                    #    session.save(obj)
                    #    session.flush()
                        
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
                now = datetime.now()
                date_created = now.strftime("%Y-%m-%d %H:%M:%S")
                date_modified = now.strftime("%Y-%m-%d %H:%M:%S")
                
                print("STOCKS")
                print("______")
                print("Preparing statements...")
                self.statementStock = StatementStock()
                records = 0
                i = 0
                for fields in fields_db:
                    if (not fields['stock'] == '') :
                        scid = self.scid_from_subcategory(fields['subcat'], date_created, date_modified)
                        aid = self.aid_from_account(fields['account'], date_created, date_modified)
                        cid = self.cid_from_category(fields['category'], date_created, date_modified)
                        # Get id from T_FINANCE (to import in T_STOCK)
                        for instance in session.query(T_FINANCE).filter_by(
                            date=fields['date'],
                            aid=aid,
                            cid=cid,
                            scid=scid,
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
                            id = instance.id

                        if fields_stock[i] != {}:
                            # Add new entry if it doesn't already exist
                            if self.update_stock(fields_stock, session, i,
                                    id, i):
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

    def update_finance(self, fields_db, session, i, id, recordid):
        """ Add a new finance entry or update an existing one. """

    def update_stock(self, fields_stock, session, i, id, recordid):
        """ Add a new stock entry or update an existing one. """
        try:
            now = datetime.now()
            date_created = now.strftime("%Y-%m-%d %H:%M:%S")
            date_modified = now.strftime("%Y-%m-%d %H:%M:%S")

            # Get snid from T_STOCK_NAME if it exists (a new entry will be made in T_STOCK_NAME if it doesn't)
            #TODO: add descriptions to mid_from_market and to snid_from_stockname)
            mid = self.mid_from_market(fields_stock[i]['market'], date_created, date_modified)
            snid = self.snid_from_stockname(fields_stock[i]['name'], mid, date_created, date_modified)
            vartax = Decimal(fields_stock[i]['tax'])
            varcommission = Decimal(fields_stock[i]['commission'])

            obj = session.query(T_STOCK).filter_by(
                      id=id,
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
                        id,
                        snid,
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
            #else:
            #    # Update existing
            #    #TODO:WTF should I put here? I add statements to the class and
            #    #execute them all at once?
            #    #Perhaps use 2 lists: one with new values and one with
            #    #values to update?
            #    #Note: Why update this? Just assume we only add new stuff,
            #    #which is the case anyway.
            #    #We do however, need to be able to update the lists in the
            #    #Statement class, for when we made a mistake.
        except Exception as ex:
           print("Error in update_stock: ", ex)
        return False;

    def export_lines(self, all=False):
        """ Returns the t_finance lines from the database. """
        #TODO: create an export line. Perhaps gather everything in a view
        #and export that? That might make this a whole lot easier!
        results = []
        try:
            session = self.Session()
            try:
                records = 0
                if all:
                    query = session.query(T_FINANCE)
                else:
                    query = session.query(T_FINANCE).filter_by(active=1)
                for instance in query:
                    records = records + 1
                    outline = self.export_line(instance)
                    results.append(':'.join(outline))
            except Exception as ex:
                print("Error in export_lines: ", ex)
            finally:
                session.rollback()
                session = None
                print("{0} records retrieved.".format(str(records)))

        except Exception as ex:
            print("Error in session of export_lines: ", ex)
        finally:
            return results

    def export_line(self, line):
        """ Assemble an export line. """
        exportline = []
        date = datetime.strftime(line.date, '%Y-%m-%d')
        exportline.append(str(date))
        exportline.append(self.accountname_from_aid(line.aid))
        exportline.append(self.category_from_cid(line.cid))
        exportline.append(self.subcategory_from_scid(line.scid))
        exportline.append(str(line.amount))
        exportline.append(str(line.market))
        exportline.append(str(line.stock))
        exportline.append(str(line.shares))
        exportline.append(str(line.price))
        exportline.append(str(line.tax))
        exportline.append(str(line.commission))
        exportline.append(str(line.comment))
        exportline.append(str(line.risk))
        return exportline

    def remove_line(self, rownumber):
        """ Removes a line from the table. """
        #TODO: when trade.tx, tr... etc. (= stock), remove from both
        #classes.
        #TODO: make the Statement-classes accessible from this function?

    def scid_from_subcategory(self, subcat, date_created, date_modified):
        """ Get the scid from a subcategory. """
        result = -1
        session = self.Session()
        try:
            # Get scid, based on subcat name
            # but first check if the subcat already exists
            # in T_SUB_CATEGORY. If not, add it to the t_sub_categorytable.
            obj = session.query(T_SUB_CATEGORY).filter_by(name=subcat).first() is not None
            if not obj: 
                session.add(T_SUB_CATEGORY(subcat, date_created, date_modified))
                session.commit()
                for instance in session.query(func.max(T_SUB_CATEGORY.scid).label('scid')):
                    result = instance.scid
            else:
                for instance in session.query(T_SUB_CATEGORY).filter_by(name=subcat):
                    result = str(instance.scid)
        except Exception as ex:
            print("Error retrieving scid: ", ex)
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

    def cid_from_category(self, category, date_created, date_modified):
        """ Get the cid from a category. """
        result = -1
        session = self.Session()
        try:
            # Get cid, based on category name
            # but first check if the category already exists
            # in T_PRODUCT. If not, add it to the t_category table.
            # if category ends with .rx: flg_income = 1, else 0
            if(category[-3:] == '.rx'):
                flg_income = 1
            elif(category[-3:] == '.tx'):
                flg_income = 0
            else:
                raise Exception("Wrong category in input-file: {0}".format(category))
            obj = session.query(T_PRODUCT).filter_by(name=category).first() is not None
            if not obj: 
                session.add(T_PRODUCT(category, flg_income, date_created, date_modified))
                session.commit()
                for instance in session.query(func.max(T_PRODUCT.cid).label('cid')):
                    result = instance.cid
            else:
                for instance in session.query(T_PRODUCT).filter_by(name=category):
                    result = str(instance.cid)
        except Exception as ex:
            print("Error retrieving cid: ", ex)
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

    def subcategory_from_scid(self, scid):
        """ Get the subcategory for a given scid from the T_SUB_CATEGORY table. """
        result = ''
        try:
            session = self.Session()
            for instance in session.query(T_SUB_CATEGORY).filter_by(scid=scid):
                result = instance.name
        except Exception as ex:
            print("Error retrieving subcategory from scid: ", ex)
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

    def category_from_cid(self, cid):
        """ Get the category for a given cid from the T_PRODUCT table. """
        result = ''
        try:
            session = self.Session()
            for instance in session.query(T_PRODUCT).filter_by(cid=cid):
                result = instance.name
        except Exception as ex:
            print("Error retrieving category from cid: ", ex)
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
