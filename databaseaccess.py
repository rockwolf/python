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
        tables = [self.tblteams, self.tblmcodes, self.tblstocknames, self.tblproducts, self.tblsafetymargins]
        msgObj.PrintAction('Created table', tables)
        print "Fill in known values..."
        self.FillTables()
        msgObj.PrintAction('Added known values to table', tables)
        msgObj = None
    
    def SetupTables(self):
        """ The actual creation of the tables. """
        db = dbapi2.connect(host=self.get_dbhost(),database=self.get_dbname(), user=self.get_dbuser(), password=self.get_dbpass())
        cur = db.cursor()
        #TODO: add if(exists) stuff
        cur.execute ("""CREATE TABLE """ + self.tblteams + """(tid serial not null, name varchar(30) not null, division varchar(30), active int not null default 1, date_created timestamp, date_modified timestamp, constraint pk_tid primary key(tid));""")
        db.commit()
        cur.execute ("""CREATE TABLE """ + self.tblmcodes + """(mid serial not null, mcode varchar(3) not null, description varchar(30), date_created timestamp, date_modified timestamp, constraint pk_mid primary key(mid));""")
        db.commit()
        cur.execute ("""CREATE TABLE """ + self.tblstocknames + """(snid serial not null, name varchar(5) not null, mid int not null, description varchar(30), date_created timestamp, date_modified timestamp, constraint pk_snid primary key(snid), constraint fk_mid foreign key(mid) references """ + self.tblmcodes + """(mid));""")
        db.commit()
        cur.execute ("""CREATE TABLE """ + self.tblproducts + """(pid serial not null, prod varchar(30) not null, date_created timestamp, date_modified timestamp, constraint pk_pid primary key(pid));""")
        db.commit()
        #cur.execute ("""CREATE TABLE """ + self.tblcrossover + """(year varchar(4) not null, passive decimal(18,4) not null default 0.0, sw decimal(18,4) not null default 0.0, expenses decimal(18,4) not null default 0.0, comment varchar(256), date_created timestamp, date_modified timestamp, constraint pk_yid primary key(year));""")
        db.commit()
        cur.execute ("""CREATE TABLE """ + self.tblsafetymargins + """(smid serial not null, description varchar(100) not null, value decimal(18,4) not null default 0.0, date_created timestamp, date_modified timestamp, constraint pk_smid primary key(smid));""")
        db.commit()
        cur.close()
        db.close()

    def FillTables(self): 
        """ Fill in values we already know. """
        now = datetime.now()
        db = dbapi2.connect(host=self.get_dbhost(),database=self.get_dbname(), user=self.get_dbuser(), password=self.get_dbpass())
        cur = db.cursor()
        #TODO: add if exists check
        # NHL only
        teams = {'New Jersey Devils':'Atlantic',
                'New York Islanders':'Atlantic',
                'Philadelphia Flyers':'Atlantic',
                'Pittsburgh Penguins':'Atlantic',
                'Boston Bruins':'Northeast', 
                'Buffalo Sabres':'Northeast',
                'Montreal Canadiens':'Northeast',
                'Ottawa Senators':'Northeast',
                'Toronto Maple Leafs':'Northeast',
                'Atlanta Thrashers':'Southeast',
                'Carolina Hurricanes':'Southeast',
                'Florida Panthers':'Southeast',
                'Tampa Bay Lightning':'Southeast',
                'Washington Capitals':'Southeast',
                'Chicago Blackhawks':'Central',
                'Columbus Blue Jackets':'Central',
                'Detroit Red Wings':'Central',
                'Nashville Predators':'Central',
                'St. Louis Blues':'Central',
                'Calgary Flames':'Northwest',
                'Colorado Avalanche':'Northwest',
                'Edmonton Oilers':'Northwest',
                'Minnesota Wild':'Northwest',
                'Vancouver Canucks':'Northwest',
                'Anaheim Ducks':'Pacific',
                'Dallas Stars':'Pacific',
                'Los Angeles Kings':'Pacific',
                'Phoenix Coyotes':'Pacific',
                'San Jose Sharks':'Pacific'}
        for team in teams:
            cur.execute("""insert into """ + self.tblteams + """(name, division, date_created, date_modified) values('""" + team + """','""" + teams[team] + """','""" +  str(now) + """','""" + str(now) + """');""")
        db.commit()
        mcds = {'ams':'Amsterdam',
            'ebr':'Brussels'}
        for mcd in mcds:
            cur.execute("""insert into """ + self.tblmcodes + """(mcode, description, date_created, date_modified) values('""" + mcd + """','""" + mcds[mcd] + """','""" +  str(now) + """','""" + str(now) + """');""")
        db.commit()
        stocks = {'rhji' : ['RHJI International S.A.','2'],
            'nests' : ['Nestle','2'],
            'devg' : ['Devgen','2'],
            'enin' : ['4 Energy Invest','2'],
            'adhof' : ['Koninklijke AHOLD N.V.','1'],
            'dexb' : ['Dexia','2'],
            'crxl' : ['Crucell N.V.','1'],
            'drak' : ['Draka Holding N.V.','1'],
            'theb' : ['Thenergo N.V.','2'],
            'eurn' : ['Euronav','2'],
            'tnet' : ['Telenet','2'],
            'exm': ['Exmar','2']}
        for stock in stocks:
            cur.execute("""insert into """ + self.tblstocknames + """(name, mid, description, date_created, date_modified) values('""" + stock + """','""" + stocks[stock][1] + """','""" + stocks[stock][0] + """','""" +  str(now) + """','""" + str(now) + """');""")
        db.commit()
        # Products
        for prod in self.GetProductsFromFinance():
            cur.execute("""insert into """ + self.tblproducts + """(prod, date_created, date_modified) values('""" + prod + """','""" +  str(now) + """','""" + str(now) + """');""")
        db.commit()
        # Margins
        margins = {
            'Financial reserve' : 5000,
            'Financial reserve after crossover' : 160000,
            'Safety margin passive income' : 5000,
            'Safe withdrawal rate' : 0.03,
            'Bargain reserve' : 100000
        }
        for margin in margins:
            cur.execute("""insert into """ + self.tblsafetymargins + """(description, value, date_created, date_modified) values('""" + margin + """','""" + str(margins[margin]) + """','""" +  str(now) + """','""" + str(now) + """');""")
        db.commit()
        # Crossover
        #TODO: get years and corresponding values and return them, add them here.
        # Make dba.GetExpenses and GetPassive and CalculateSW
        #for year in yearpassiveswexpenses:
        #    cur.execute("""insert into """ + self.tblsafetymargins + """(description, value, date_created, date_modified) values('""" + margin + """','""" + str(margins[margin]) + """','""" +  str(now) + """','""" + str(now) + """');""")
        #db.commit()
        cur.close()
        db.close()
 
    def Remove(self):
        """ Remove the tables + data from the db. """
        msgObj = self.msgHandler.MessageHandler()
        answer = msgObj.Confirmation('remove all tables from the database')
        if answer == 0:
            self.RemoveTables()
            msgObj = self.msgHandler.MessageHandler()
            tables = [self.tblteams, self.tblmcodes, self.tblstocknames, self.tblproducts, self.tblsafetymargins]
            msgObj.PrintAction('Removed table', tables)
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
        cur.execute ("""drop table """ + self.tblteams + """;drop table """ + self.tblstocknames + """;drop table """ + self.tblmcodes + """;drop table """ + self.tblproducts + """;drop table """ + self.tblsafetymargins + """;""")
        db.commit()
        cur.close()
        db.close()
