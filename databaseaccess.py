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

    def get_myconf(self):
        """ myconf """
        return self._myconf

    def set_myconf(self, release):
        """ set myconf """
        self._myconf = release

    myconf = property(get_myconf, set_myconf)
 
    def get_dbhost(self):
        """ dbhost """
        return self._dbhost

    def set_dbhost(self, version):
        """ set dbhost """
        self._dbhost = version

    dbhost = property(get_dbhost, set_dbhost)

    def get_dbname(self):
        """ dbname """
        return self._dbname

    def set_dbname(self, version):
        """ set dbname """
        self._dbname = version

    dbname = property(get_dbname, set_dbname)

    def get_dbuser(self):
        """ dbuser """
        return self._dbuser

    def set_dbuser(self, version):
        """ set dbuser """
        self._dbuser = version

    dbuser = property(get_dbuser, set_dbuser)

    def get_dbpass(self):
        """ dbpass """
        return self._dbpass
    
    def set_dbpass(self, version):
        """ set dbpass """
        self._dbpass = version

    dbpass = property(get_dbpass, set_dbpass)

    def __init__(self):
        """ Initialise the database class. """ 
        self.set_myconf(self.ConfFile())
        self.Config()
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
        self.tables = [self.tblteams, self.tblmcodes, self.tblstocknames, self.tblproducts, self.tblsafetymargins]

        self.sqlpath = 'sql/'
        self.sqldrop = '01_drop_tables.sql'
        self.sqlcreate = ['01_create_T_TEAMS.sql', '02_create_T_MCODES.sql', '03_create_T_STOCKNAMES.sql', '04_create_T_PRODUCTS.sql', '05_create_T_SAFETYMARGINS.sql']
        self.sqlinit = ['01_init_T_TEAMS.sql', '02_init_T_MCODES.sql', '03_init_T_STOCKNAMES.sql', '04_init_T_PRODUCTS.sql', '05_init_T_SAFETYMARGINS.sql']
        self.msgHandler = __import__('messagehandler')

    def ConfFile(self):
        """ Get config file path from XDG_CONFIG_DIR. """
        # TODO: get from env var
        #return '~/.config/clipf2db/clipf2db.rc'
        return 'config/lisa.rc'

    def Config(self):
        """ Retrieve config file values """
        config = ConfigParser.RawConfigParser()
        config.read(self.get_myconf())
        
        dbhost = config.get('database', 'host')[1:-1]
        dbname = config.get('database', 'name')[1:-1]
        dbuser = config.get('database', 'user')[1:-1]
        dbpass = config.get('database', 'password')[1:-1]
        self.set_dbhost(dbhost)        
        self.set_dbname(dbname)        
        self.set_dbuser(dbuser)        
        self.set_dbpass(dbpass)        

    def Setup(self):
        """ Setup the db. """
        msgObj = self.msgHandler.MessageHandler()
        print "Setting up the database..."  
        self.SetupTables(); 
        msgObj.PrintAction('Created table', self.tables)
        print "Fill in known values..."
        self.FillTables()
        msgObj.PrintAction('Added known values to table', self.tables)
        msgObj = None
    
    def SetupTables(self):
        """ The actual creation of the tables. """
        db = dbapi2.connect(host=self.get_dbhost(),database=self.get_dbname(), user=self.get_dbuser(), password=self.get_dbpass())
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
            print "Error: procedures: %s" % str(e)
            exit(1)

    def FillTables(self): 
        """ Fill in values we already know. """
        #TODO: refactor so it becomes a script to exec a list of sql files. Can be used by setupTables too.
        now = datetime.now()
        db = dbapi2.connect(host=self.get_dbhost(),database=self.get_dbname(), user=self.get_dbuser(), password=self.get_dbpass())
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
            print "Error: procedures: %s" % str(e)
            exit(1)
        # Crossover
        #TODO: get years and corresponding values and return them, add them here.
        # Make dba.GetExpenses and GetPassive and CalculateSW
        #for year in yearpassiveswexpenses:
        #    cur.execute("""insert into """ + self.tblsafetymargins + """(description, value, date_created, date_modified) values('""" + margin + """','""" + str(margins[margin]) + """','""" +  str(now) + """','""" + str(now) + """');""")
        #db.commit()
 
    def Remove(self):
        """ Remove the tables + data from the db. """
        msgObj = self.msgHandler.MessageHandler()
        answer = msgObj.Confirmation('remove all tables from the database')
        if answer == 0:
            self.RemoveTables()
            msgObj = self.msgHandler.MessageHandler()
            msgObj.PrintAction('Removed table', self.tables)
        msgObj = None
       
    def GetValues(self, qry):
        """ Global wrapper for retrieving values. """
        db = dbapi2.connect(host=self.get_dbhost(),database=self.get_dbname(), user=self.get_dbuser(), password=self.get_dbpass())
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
 
    def GetTeams(self, otn):
        """ Get the teams, but leave out the other team name. This way, teams are always different. """
        #if otn != '' and otn != None:
        #    # Is it necessary to get new values? (Is A in B? and vice versa)
        #    if self.GetValues("""select name from """ + self.tblteams + """ where active = 1 and name ='""" + str(otn) + """' order by name;""") == []:
        #        return None
        #    else:
        #        return self.GetValues("""select name from """ + self.tblteams + """ where active = 1 and name <>'""" + str(otn) + """' order by name;""")
        #else:
            # It's a fill action at startup, just get everything
        return self.GetValues("""select name from """ + self.tblteams + """ where active = 1 order by name;""");

    def GetProductsFromFinance(self):
        """ Get the products from the finance table. """
        return self.GetValues("""select distinct prod from """ + self.tblfinance + """ order by prod;""")

    def GetProducts(self):
        """ Get the products. """
        return self.GetValues("""select prod from """ + self.tblproducts + """ order by prod;""")

    def GetAccounts(self):
        """ Get the accounts. """
        return self.GetValues("""select distinct acc from """ + self.tblfinance + """ order by acc;""")
 
    def GetMcodes(self):
        """ Get the market codes. """
        return self.GetValues("""select distinct mcode from """ + self.tblmcodes + """ order by mcode;""")
 
    def GetStockNames(self, mcode):
        """ Get the stock names. """
        return self.GetValues("""select t1.name from """ + self.tblstocknames + """ t1 join """ + self.tblmcodes + """ t2 on t1.mid = t2.mid where t2.mcode = '""" + str(mcode) + """' order by t1.name;""")

    def GetStockInfo(self, sname):
        """ Get extra stock info. """
        return self.GetValues("""select t1.description, t2.description from """ + self.tblstocknames + """ t1 join """ + self.tblmcodes + """ t2 on t1.mid = t2.mid where t1.name = '""" + str(sname) + """';""")
        
    def GetExpenses():
        """ Get the total expenses, ordered by year. """
        #TODO: extra flag in database, in seperate table?
        exprds = ['account.start', 'account.tx', 'invest.invest', 'invest.changestocks', 'invest.buystocks', 'bet.place']
        strexprd = ""
        for prd in exprds:
            exprdstr = strexprd + " and t1.prod <> '" + prd + "'"
        return self.GetValues("""select extract(year from t1.date), sum(t1.amount) from """ + self.tblfinance + """ t1 where t1.flag = 0 and """ + strexprds + """ group by extract(year from t1.date);""")

    def GetPassive():
        """ Get the total passive income, ordered by year. """
        return self.GetValues("""select sum(t1.amount) from """ + self.finance + """ t1 where t1.prod = 'invest.dividend' or t1.prod = 'invest.refund';""")

    def CalculateSW():
        """ Calculate the safe withdrawal value. """
        return self.GetValues("""select t1.description, t2.description from """ + self.tblstocknames + """ t1 join """ + self.tblmcodes + """ t2 on t1.mid = t2.mid where t1.name = '""" + str(sname) + """';""")
       
    def RemoveTables(self):
        """ The actual removal of the tables. """
        db = dbapi2.connect(host=self.get_dbhost(),database=self.get_dbname(), user=self.get_dbuser(), password=self.get_dbpass())
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
            print "Error: procedures: %s" % str(e)
            exit(1)
