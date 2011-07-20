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
from time import sleep
import sys
from databaseaccess import DatabaseAccess

class FileImport():
    """ Class with methods to import files. """

    def __init__(self, config):
        """ Initializes """
        self.config = config

    def file_import(self):
        """ Parse textfile and insert data in db. """
        try:
            source = open(self.config.importfile)
            lines = source.readlines()
            fields = {}
            fields_db = []
            
            print(self.config.importfile + ' -> ' + self.config.dbhost + '/' + self.config.dbname + ': ')
            
            i = 0
            print('[{0}{1}]'.format('  0','%') , end = "")
            for line in lines:
                try:
                    fields = line.strip().split(':')
                    fields_db.append({
                        'date':fields[0],
                        'account':fields[1], #Note: Get AID from T_ACCOUNT for final insert
                        'product':fields[2], #Note: Get PID from T_PRODUCT for final insert
                        'object':fields[3], #Note: Get OID from T_OBJECT for final insert
                        'amount':fields[4],
                        'flag':fields[5],
                        'comment':fields[6]
                        #.replace('\'','\\\'')
                    })
                    i = i + 1
                    percent = int(i/len(lines)*100)
                    percentlen = len(str(percent))-1

                    #[  1%]
                    #[123%]
                    #123456
                    print(6*'\b', end = "")

                    print('[{0}{1}]'.format((3-percentlen-1)*' ' + str(percent),'%') , end = "")
                    sleep(0.001)
                    sys.stdout.flush()
                except Exception as ex:
                    print("Error in for loop: ", ex)
                    break
            print('')
            self.process_lines(fields_db)
            self.process_comments(fields_db)
        except Exception as ex:
            print('')
            print("Error while processing {0}:".format(self.config.importfile), ex)
        finally:
            source.close()
            exit(1)
                
    def process_comments(self, fields_db):
        """ Processing lines of the input file. """
        # stocks
        fields_comment_stocks = []
        for field in fields_db:
            fields_comment_stocks.append(self.parse_comment_stocks(field))
        try:
            cmnt = fields_comment_stocks
            if cmnt != {}:
                self.process_stocks(fields_db, fields_comment_stocks)
        except Exception as ex:
            print("Error in process_comments: ", ex)

    def process_lines(self, fields_db):
        """ Convert general financial information. """
        dba = DatabaseAccess(self.config)
        dba.file_import_lines(fields_db)
        dba = None
 
    def process_stocks(self, fields_db, commentfields):
        """ Import stock information. """
        dba = DatabaseAccess(self.config)
        dba.file_import_stocks(fields_db, commentfields)
        dba = None
        
        
    def parse_comment_stocks(self, fields):
        """ Convert financial entries that abuse the comment field for stock functionality. """
        fields_comment = []
        fields_comment_db = {}
        
        try:
            if fields['object'] == 'buystocks' or fields['object'] == 'sellstocks':
                # stocks
                name = ''
                market = ''
                action = ''
                price = '0'
                quantity = '0'
                fields_comment = fields['comment'].split(',')
                name = str(fields_comment[0]).split('.')[1]
                market = fields_comment[0].split('.')[0]
                quantity = fields_comment[1]
                price = fields_comment[2]
                action = fields['object'] #buystocks/sellstocks
                #print 'test: action =' + action
                fields_comment_db = {
                    'name': name,
                    'market': market,
                    'action': action,
                    'price': price,
                    'quantity': quantity,
                }
            else:
                fields_comment_db = {}
        except Exception as ex:
            print("Error in parse_comment: ", ex)
        finally:
            return fields_comment_db
        
    def file_import_line_stock(self, fields_comment_db):
        """" Convert general stock information. """
        #TODO: put this in the inherited dbaccess
        try:
            #db = dbapi2.connect(host=self.get_dbhost(),database=self.get_dbname(), user=self.get_dbuser(), password=self.get_dbpass())
            #cur = db.cursor()
            try:
                now = datetime.now()
                date_create = now.strftime("%Y-%m-%d %H:%M:%S")
                date_modify = now.strftime("%Y-%m-%d %H:%M:%S")
                
                cur = db.cursor()
                cur.execute("select  max(id) from " + self.tblfinance + ";")
                id = cur.fetchone()[0]
                #TODO: insert in T_STOCK_NAME too
                #TODO: check if already exists in T_STOCK_NAME (if not exists?)
                #insert into t_stock_name(name, mid) select 'test2',2 where not exists(select name from t_stock_name where name = 'test2' and mid= 2);

                cur.execute("insert into " + self.tblstocks + \
                        "(id, snid, mcode, action, price, qty, date_create, date_modify) values(" + \
                        str(id) + ", select snid from " + self.tblstockname + " where name ='" + fields_comment_db['name'] + \
                        "', '" + fields_comment_db['mcode'] + "', '" + fields_comment_db['action'] + "', " + \
                        fields_comment_db['price'] + ", " + fields_comment_db['qty'] + ", '" + date_create + "', '" + date_modify + "');")
            finally:
                    db.commit()
                    cur.close()
                    db.close()
        #except dbapi2.DatabaseError, e:
        except:
            print("Error: procedures: %s" % str(e))
            exit(1)
