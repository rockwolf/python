#! /usr/local/bin/python
"""
This file is part of Clipf2db.

Clipf2db is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Clipf2db is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Clipf2db. If not, see <http://www.gnu.org/licenses/>.
					
"""
import ConfigParser, psycopg2 as dbapi2
from datetime import datetime

class DatabaseAccess():
    """ Connecting to the database. """ 

    def __init__(self):
        """ Initialise the database class. """ 
        self.myconf = 'config/lisa.rc'
        self.dbhost = ''
        self.dbname = ''
        self.dbuser = ''
        self.dbpass = ''
        self.config()
        self.tblfinance = 'T_FINANCE'
        self.tblstocks = 'T_STOCKS'
        self.tblcurstocks = 'T_CURSTOCKS'
        self.tblbets = 'T_BETS'
        self.tblbetresults = 'T_BETRESULTS'
        self.tblcurbets = 'T_CURBETS'
        self.tblteams = 'T_TEAMS'
        self.tblmcodes = 'T_MCODES'
        self.tblstocknames = 'T_STOCKNAMES'
        self.tblproducts = 'T_PRODUCTS'
        self.tblsafetymargins = 'T_SAFETYMARGINS'
        self.tables = [
                self.tblteams,
                self.tblmcodes,
                self.tblstocknames,
                self.tblproducts,
                self.tblsafetymargins]

        self.sqlpath = 'sql/'
        self.sqldrop = '01_drop_tables.sql'
        self.sqlcreate = [
                '01_create_T_TEAMS.sql',
                '02_create_T_MCODES.sql',
                '03_create_T_STOCKNAMES.sql',
                '04_create_T_PRODUCTS.sql',
                '05_create_T_SAFETYMARGINS.sql']
        self.sqlinit = [
                '01_init_T_TEAMS.sql',
                '02_init_T_MCODES.sql',
                '03_init_T_STOCKNAMES.sql',
                '04_init_T_PRODUCTS.sql',
                '05_init_T_SAFETYMARGINS.sql']
        self.msgHandler = __import__('messagehandler')

    def config(self):
        """ Retrieve config file values """
        config = ConfigParser.RawConfigParser()
        config.read(self.myconf)
        
        self.dbhost = config.get('database', 'host')[1:-1]
        self.dbname = config.get('database', 'name')[1:-1]
        self.dbuser = config.get('database', 'user')[1:-1]
        self.dbpass = config.get('database', 'password')[1:-1]

    def install(self):
        """ install the db. """
        msgObj = self.msgHandler.MessageHandler()
        print('Setting up the database...')  
        self.create_tables(); 
        msgObj.print_action('Created table', self.tables)
        print('Fill in known values...')
        self.init_tables()
        msgObj.print_action('Added known values to table', self.tables)
        msgObj = None
    
    def create_tables(self):
        """ The actual creation of the tables. """
        db = dbapi2.connect(
                host=self.dbhost,
                database=self.dbname,
                user=self.dbuser,
                password=self.dbpass)
        cur = db.cursor()
        try:
            try:
                for script in self.sqlcreate:
                    sqlfile = "%s/%s" % (str(self.sqlpath),str(script))
                    procedures = open(sqlfile,'r').read()
                    cur.execute(procedures)
                    db.commit()
            finally:
                cur.close()
                db.close()
        except dbapi2.DatabaseError, e:
            print("Error in create_tables: procedures: ",str(e))
            exit(1)

    def init_tables(self): 
        """ Fill tables with initial values. """
        #TODO: refactor so it becomes a script to exec a list of sql files. Can be used by create_tables too.
        now = datetime.now()
        db = dbapi2.connect(
                host=self.dbhost,
                database=self.dbname,
                user=self.dbuser,
                password=self.dbpass)
        cur = db.cursor()
        try:
            try:
                for script in self.sqlinit:
                    sqlfile = "%s/%s" % (str(self.sqlpath),str(script))
                    procedures = open(sqlfile,'r').read()
                    cur.execute(procedures)
                    db.commit()
            finally:
                cur.close()
                db.close()
        except dbapi2.DatabaseError, e:
            print("Error in init_tables: procedures: ",str(e))
            exit(1)
        # Crossover
        #TODO: get years and corresponding values and return them, add them here.
        # Make dba.get_expenses and get_passive and calculate_sw
        #for year in yearpassiveswexpenses:
        #    cur.execute("""insert into """ + self.tblsafetymargins + """(description, value, date_created, date_modified) values('""" + margin + """','""" + str(margins[margin]) + """','""" +  str(now) + """','""" + str(now) + """');""")
        #db.commit()
 
    def uninstall(self):
        """ uninstall the tables + data from the db. """
        msgObj = self.msgHandler.MessageHandler()
        answer = msgObj.confirmation('uninstall all tables from the database')
        if answer == 0:
            self.drop_tables()
            msgObj = self.msgHandler.MessageHandler()
            msgObj.print_action('uninstalld table', self.tables)
        msgObj = None
       
    def get_values(self, qry):
        """ Global wrapper for retrieving values. """
        db = dbapi2.connect(
                host=self.dbhost,
                database=self.dbname,
                user=self.dbuser,
                password=self.dbpass)
        cur = db.cursor()
        cur.execute (qry)
        rows = cur.fetchall()
        values = []
        for row in rows:
            i = 0
            for col in row:
                values.append(row[i])
                i = i+1
        db.commit()
        cur.close()
        db.close()
        return values
 
    def get_teams(self, otn):
        """ Get a list of all teams

            The given team name is left out, so it can be used to fill
            combos without being able to select 2 identical teams.

        """
        #if otn != '' and otn != None:
        #    # Is it necessary to get new values? (Is A in B? and vice versa)
        #    if self.get_values("""select name from """ + self.tblteams + """ where active = 1 and name ='""" + str(otn) + """' order by name;""") == []:
        #        return None
        #    else:
        #        return self.get_values("""select name from """ + self.tblteams + """ where active = 1 and name <>'""" + str(otn) + """' order by name;""")
        #else:
            # It's a fill action at startup, just get everything
        str_list = [
                'select name from',
                self.tblteams,
                'where active = 1 order by name;']
        return self.get_values(' '.join(str_list))

    def get_products_from_finance(self):
        """ Get the products from the finance table. """
        str_list = [
                'select distinct prod from',
                self.tblfinance,
                'order by prod;']
        return self.get_values(' '.join(str_list))

    def get_products(self):
        """ Get the products. """
        str_list = [
                'select prod from',
                self.tblproducts,
                'order by prod;']
        return self.get_values(' '.join(str_list))

    def get_accounts(self):
        """ Get the accounts. """
        str_list = [
                'select distinct acc from',
                self.tblfinance,
                'order by acc;']
        return self.get_values(' '.join(str_list))
 
    def get_mcodes(self):
        """ Get the market codes. """
        str_list = [
                'select distinct mcode from',
                self.tblmcodes,
                'order by mcode;']
        return self.get_values(' '.join(str_list))
 
    def get_stocknames(self, mcode):
        """ Get the stock names. """
        str_list = [
                'select t1.name from',
                self.tblstocknames,
                't1 join',
                self.tblmcodes,
                't2 on t1.mid = t2.mid where t2.mcode =',
                "'" + str(mcode) + "'",
                'order by t1.name;']
        return self.get_values(' '.join(str_list))

    def get_stockinfo(self, sname):
        """ Get extra stock info. """
        str_list = [
                'select t1.description, t2.description from',
                self.tblstocknames,
                't1 join',
                self.tblmcodes,
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
                'invest.buystocks',
                'bet.place']
        strprd_expenses = ''
        for prd in prd_expenses:
            str_list = [
                    strprd_expenses,
                    'and t1.prod <>',
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
                "t1 where t1.prod = 'invest.dividend'",
                "or t1.prod = 'invest.refund';"]
        return self.get_values(' '.join(str_list))

    def calculate_sw(self, sname):
        """ Calculate the safe withdrawal value. """
        str_list = [
                'select t1.description, t2.description from',
                self.tblstocknames,
                't1 join',
                self.tblmcodes,
                't2 on t1.mid = t2.mid where t1.name =',
                "'" + str(sname) + "';"]
        return self.get_values(' '.join(str_list))
       
    def drop_tables(self):
        """ The actual removal of the tables. """
        db = dbapi2.connect(
                host=self.dbhost,
                database=self.dbname,
                user=self.dbuser,
                password=self.dbpass)
        cur = db.cursor()
        try:
            try:
                sqlfile = "%s/%s" % (str(self.sqlpath),str(self.sqldrop))
                procedures = open(sqlfile,'r').read()
                cur.execute(procedures)
            finally:
                db.commit()
                cur.close()
                db.close()
        except dbapi2.DatabaseError, e:
            print('Error in drop tables: procedures: {0}',str(e))
            exit(1)
