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

class FileExport():
    """ Class with methods to export to a textfile. """
    
    def __init__(self, config):
        """ Initialize """
        self.config = config

    def file_export(self):
        """ Export financial data to text-file. """
        try:
            dba = DatabaseAccess(self.config)
            try:
                print("Retrieving lines from database...")
                lines = dba.export_lines()
                print("Writing data to file...")
                file = open(self.config.exportfile, 'w')
                for line in lines:
                    file.write(line + '\n')
            finally:
                print("Done.")
                file.close()
                dba = None
        except Exception as ex:
            print("Error in file_export: ", ex)
