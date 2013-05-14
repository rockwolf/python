#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.
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

    def csv_export(self):
        """ Export all data to csv-files. """
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
                    # write column names on first row
                    i = 0
                    if i == 0:
                        outcsv.writerow([column.name for column
                            in dba.loaded_objects[viewname].c])
                    i = i + 1
                    # write records
                    for record in records:
                        outcsv.writerow([ getattr(record, column.name) for
                            column in dba.loaded_objects[viewname].c ])
                    print("Writing", len(records), "records for", tablename, "to file", exportpath, "...")
                exportfile.close()
                #Note: no need to close the csv, because it's just a parser
                #that uses exportfile as an underlying file. Closing exportfile
                #is all you need to do.
                print("Done.")
            finally:
                dba = None
        except Exception as ex:
            print("Error in csv_export: ", ex)

    def ledger_export(self):
        """ Export all data to ledger-cli dat files. """
        try:
            print('Not implemented yet...')
        except Exception as ex:
            print("Error in ledger_export: ", ex)
