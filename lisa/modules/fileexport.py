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
import os
import csv

from database.databaseaccess import DatabaseAccess
from modules_generic.function import current_date

class FileExport():
    """ Class with methods to export to a textfile. """
    
    def __init__(self, config):
        """ Initialize """
        self.config = config

    def file_export(self):
        """ Export all data to text-files. """
        try:
            #TODO: write to csv like this:
            #records = session.Query(MyModel).all()
            #[ outcsv.writerow(curr.field_one, curr.field_two)  for curr in records ]
            ## or maybe use outcsv.writerows(records)
            #outfile.close()
            
            dba = DatabaseAccess(self.config)
            try:
                #Prepare export dir
                exportdir = self.config.exportdir
                if not os.path.isdir(exportdir):
                    os.makedirs(exportdir)
                #Create subdir to store the txt-files in
                subdir = os.path.join(exportdir, 'export_' + current_date('%Y-%m-%d_%H%M%S'))
                if not os.path.isdir(subdir):
                    os.makedirs(subdir)
                print("Retrieving table records from database...")
                #Export all tables that are loaded by the ORM
                #But views where created per table to have more control:
                #to limit the export, only the views need to be updated.
                viewnames = []
                for tablename in dba.tables:
                    viewnames.append(tablename.upper().replace('T_', 'V_'))
                for viewname in viewnames:
                    # use the viewname for this function,
                    # the tablename to create the file
                    tablename = viewname.replace('V_', 'T_')
                    exportpath = os.path.join(subdir, tablename)
                    exportfile = open(exportpath, 'w')
                    outcsv = csv.writer(exportfile)
                    records = dba.export_records(dba.loaded_objects[viewname])
                    for record in records:
                        #outcsv.writerow(record.field_one, record.field_two)
                        #outcsv.writerow([ getattr(record, column.name) for
                        #    column in dba.loaded_objects[viewname].__mapper__.columns ])
                        for col in dba.loaded_objects[viewname].c:
                            print(col)
                    #[ outcsv.writerow(curr.field_one, curr.field_two)  for curr in records ]
                    print("Writing data for", tablename, "to file", exportpath, "...")
                    #for line in lines:
                    #    exportfile.write(line + '\n')
                exportfile.close()
                outcsv.close()
                print("Done.")
            finally:
                dba = None
        except Exception as ex:
            print("Error in file_export: ", ex)
