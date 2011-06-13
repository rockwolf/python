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
            
            print(self.config.importfile + ' -> ' + self.config.dbhost + '/' + self.config.dbname + ': ')
            
            i = 0
            print('[{0}{1}]'.format('  0','%') , end = "")
            for line in lines:
                fields = line.split(':')
                fields_db = {
                    'date':fields[0],
                    'account':fields[1],
                    'product':fields[2],
                    'object':fields[3], #Note: Get OID from T_OBJECT for final insert
                    'amount':fields[4],
                    'flag':fields[5],
                    'comment':fields[6].replace('\'','\\\'')
                }
                self.process_line(fields_db)
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

            print('')
        except Exception as ex:
            print('')
            print("Error while processing {0}:".format(self.config.importfile), ex)
        finally:
            source.close()
                
    def process_line(self, fields_db):
        """ Processing lines of the input file. """
        self.process_line_db(fields_db)
        #self.parse_comment(fields_db)
        #cmnt = self.commentfields
        #if cmnt != {}:
        #    # we have comment fields
        #    if 'market' in cmnt:
        #        # They are stocks
        #        self.process_line_db_stock(self.commentfields) #stocks_current will also be in this function

    def process_line_db(self, fields_db):
        """ Convert general financial information. """
        dba = DatabaseAccess(self.config)
        dba.file_import_line(fields_db)
        dba = None
        
    def parse_comment(self, fields_db):
        """ Convert financial entries that abuse the comment field for more functionality. """
        fields_comment = []
        fields_comment_db = {}
        
        if fields_db['object'] == 'buystocks' or fields_db['object'] == 'sellstocks':
            # stocks
            name = ''
            market = ''
            action = ''
            price = '0'
            quantity = '0'
            fields_comment = fields_db['comment'].split(',')
            name = str(fields_comment[0]).split('.')[1]
            market = fields_comment[0].split('.')[0]
            quantity = fields_comment[1]
            price = fields_comment[2]
            action = fields_db['object'][:-6] #buy/sell/change
            #print 'test: action =' + action
            fields_comment_db = {
                'name': name,
                'market': mcode,
                'action': action,
                'price': price,
                'quantity': quantity,
            }
        self.commentfields = fields_comment_db
        
    def file_import_line_stock(self, fields_comment_db):
        """" Convert general stock information. """
        #TODO: put this in the inherited dbaccess
        try:
            #db = dbapi2.connect(host=self.get_dbhost(),database=self.get_dbname(), user=self.get_dbuser(), password=self.get_dbpass())
            #cur = db.cursor()
            try:
                print("Test: file_import_line_stock")
                exit(1)
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
            self.Progress()
        #except dbapi2.DatabaseError, e:
        except:
            print("Error: procedures: %s" % str(e))
            exit(1)
