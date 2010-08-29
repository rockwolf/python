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

    def get_tblfinance(self):
        """ tblfinance """
        return self._tblfinance

    def set_tblfinance(self, version):
        """ set tblfinance """
        self._tblfinance = version

    tblfinance = property(get_tblfinance, set_tblfinance)

    def get_tblstocks(self):
        """ tblstocks """
        return self._tblstocks

    def set_tblstocks(self, version):
        """ set tblstocks """
        self._tblstocks = version

    tblstocks = property(get_tblstocks, set_tblstocks)

    def get_tblcurstocks(self):
        """ tblcurstocks """
        return self._tblcurstocks

    def set_tblcurstocks(self, version):
        """ set tblcurstocks """
        self._tblcurstocks = version

    tblcurstocks = property(get_tblcurstocks, set_tblcurstocks)

    def get_tblbets(self):
        """ tblbets """
        return self._tblbets

    def set_tblbets(self, version):
        """ set tblbets """
        self._tblbets = version

    tblbets = property(get_tblbets, set_tblbets)

    def get_tblbetresults(self):
        """ tblbetresults """
        return self._tblbetresults

    def set_tblbetresults(self, version):
        """ set tblbetresults """
        self._tblbetresults = version

    tblbetresults = property(get_tblbetresults, set_tblbetresults)

    def get_tblcurbets(self):
        """ tblcurbets """
        return self._tblcurbets

    def set_tblcurbets(self, version):
        """ set tblcurbets """
        self._tblcurbets = version

    tblcurbets = property(get_tblcurbets, set_tblcurbets)

    def get_tblteams(self):
        """ tblteams """
        return self._tblteams

    def set_tblteams(self, version):
        """ set tblteams """
        self._tblteams = version

    tblteams = property(get_tblteams, set_tblteams)

    def get_tblmcodes(self):
        """ tblmcodes """
        return self._tblmcodes

    def set_tblmcodes(self, version):
        """ set tblmcodes """
        self._tblmcodes = version

    tblmcodes = property(get_tblmcodes, set_tblmcodes)

    def __init__(self):
       """ Initialise the database class. """ 
       self.set_myconf(self.ConfFile())
       self.Config()
       self.msgHandler = __import__('messagehandler')

    def ConfFile(self):
        """ Get config file path from XDG_CONFIG_DIR. """
        # TODO: get from env var
        #return '~/.config/clipf2db/clipf2db.rc'
        return 'config/lisagui/lisagui.rc'

    def Config(self):
        """ Retrieve config file values """
        config = ConfigParser.RawConfigParser()
        config.read(self.get_myconf())
        
        dbhost = config.get('database', 'host')[1:-1]
        dbname = config.get('database', 'name')[1:-1]
        dbuser = config.get('database', 'user')[1:-1]
        dbpass = config.get('database', 'password')[1:-1]
        tblfinance = config.get('data', 'tablefinance')[1:-1]
        tblstocks = config.get('data', 'tablestocks')[1:-1]
        tblcurstocks = config.get('data', 'tablecurstocks')[1:-1]
        tblbets = config.get('data', 'tablebets')[1:-1]
        tblbetresults = config.get('data', 'tablebetresults')[1:-1]
        tblcurbets = config.get('data', 'tablecurbets')[1:-1]
        tblteams = config.get('data', 'tableteams')[1:-1]
        tblmcodes = config.get('data', 'tablemcodes')[1:-1]
        self.set_dbhost(dbhost)        
        self.set_dbname(dbname)        
        self.set_dbuser(dbuser)        
        self.set_dbpass(dbpass)        
        self.set_tblfinance(tblfinance)        
        self.set_tblstocks(tblstocks)        
        self.set_tblcurstocks(tblcurstocks)        
        self.set_tblbets(tblbets)        
        self.set_tblbetresults(tblbetresults)        
        self.set_tblcurbets(tblcurbets)        
        self.set_tblteams(tblteams)        
        self.set_tblmcodes(tblmcodes)        

    def Setup(self):
        """ Setup the db. """
        msgObj = self.msgHandler.MessageHandler()
        print "Setting up the database..."  
        self.SetupTables(); 
        tables = [self.get_tblteams(), self.get_tblmcodes()]
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
        cur.execute ("""CREATE TABLE """ + self.get_tblteams() + """(tid serial not null, name varchar(30) not null, division varchar(30), active int not null default 1, date_created timestamp, date_modified timestamp, constraint pk_tid primary key(tid));""")
        db.commit()
        cur.execute ("""CREATE TABLE """ + self.get_tblmcodes() + """(mid serial not null, mcode varchar(3) not null, description varchar(30), date_created timestamp, date_modified timestamp, constraint pk_mid primary key(mid));""")
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
            cur.execute("""insert into teams(name, division, date_created, date_modified) values('""" + team + """','""" + teams[team] + """','""" +  str(now) + """','""" + str(now) + """');""")
        db.commit()
        mcds = {'ebr':'Brussels',
            'aex':'Amsterdam'}
        for mcd in mcds:
            cur.execute("""insert into mcodes(mcode, description, date_created, date_modified) values('""" + mcd + """','""" + mcds[mcd] + """','""" +  str(now) + """','""" + str(now) + """');""")
        db.commit()
        cur.close()
        db.close()
        
    def Remove(self):
        """ Remove the tables + data from the db. """
        msgObj = self.msgHandler.MessageHandler()
        answer = msgObj.Confirmation('remove all tables from the database')
        if answer == 0:
            self.RemoveTables()
            msgObj = self.msgHandler.MessageHandler()
            tables = [self.get_tblteams(), self.get_tblmcodes()]
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
            values.append(row[0])
        db.commit()
        cur.close()
        db.close()
        return values
 
    def GetTeams(self):
        """ Get the teams. """
        return self.GetValues("""select name from """ + self.get_tblteams() + """ where active = 1 order by name;""")

    def GetProducts(self):
        """ Get the products. """
        return self.GetValues("""select distinct prod from """ + self.get_tblfinance() + """ order by prod;""")

    def GetAccounts(self):
        """ Get the accounts. """
        return self.GetValues("""select distinct acc from """ + self.get_tblfinance() + """ order by acc;""")
 
    def GetMcodes(self):
        """ Get the market codes. """
        return self.GetValues("""select distinct mcode from """ + self.get_tblmcodes() + """ order by mcode;""")
        
    def RemoveTables(self):
        """ The actual removal of the tables. """
        db = dbapi2.connect(host=self.get_dbhost(),database=self.get_dbname(), user=self.get_dbuser(), password=self.get_dbpass())
        cur = db.cursor()
        cur.execute ("""drop table """ + self.get_tblteams() + """;drop table """ + self.get_tblmcodes() + """;""")
        db.commit()
        cur.close()
        db.close()
