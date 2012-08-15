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
from database.databaseaccess import DatabaseAccess
from modules_generic.function import current_date
import os

class FileExport():
    """ Class with methods to export to a textfile. """
    
    def __init__(self, config):
        """ Initialize """
        self.config = config

    def file_export(self):
        """ Export all data to text-files. """
        try:
            dba = DatabaseAccess(self.config)
            try:
                #Prepare export dir
                exportdir = self.config.exportdir
                if not os.path.isdir(exportdir):
                    os.makedirs(exportdir)
                #Create subdir to store the txt-files in
                subdir = os.path.join(exportdir, 'export_' + current_date())
                if not os.path.isdir(subdir):
                    os.makedirs(subdir)
                print("Retrieving table records from database...")
                #Process all tables that are loaded by the ORM
                #But views where created per table to have more control:
                #to limit the export, only the views need to be updated.
                viewnames = []
                for name in dba.tables:
                    viewnames.append(name.upper().replace('T_', 'V_'))
                for name in viewnames:
                    exportfile = open(os.path.join(subdir, name), 'w')
                    lines = dba.export_lines(name)
                    print("Writing data for", name, "to file", exportfile, "...")
                    for line in lines:
                        exportfile.write(line + '\n')
            finally:
                print("Done.")
                file.close()
                dba = None
        except Exception as ex:
            print("Error in file_export: ", ex)
