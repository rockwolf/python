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
from subprocess import call

class Setup():
    """ Setup methods. """

    def __init__(self):
        """ Initialise, nothing to see here... """ 
        pass

    def install(self):
        """ Setup the database through an external script. """
        try:
            call(["sh", "setup/install.sh"])
        except:
            print('Error: could not load install.sh script.')

    def uninstall(self):
        """ Remove all from database through an external script. """
        try:
            call(["sh", "setup/uninstall.sh"])
        except:
            print('Error: could not load uninstall.sh script.')

    def clear_tables(self):
        """ This function can be used to empty the database tables. """
        try:
            call(["sh", "setup/clear_tables.sh"])
        except:
            print('Error: could not load clear_tables.sh script.')

    def drop_constraints(self):
        """ This function can be used to drop all table constraints. """
        try:
            call(["sh", "setup/drop_constraints.sh"])
        except:
            print('Error: could not load drop_constraints.sh script.')

    def add_constraints(self):
        """ This function can be used to create all table constraints. """
        try:
            call(["sh", "setup/add_constraints.sh"])
        except:
            print('Error: could not load add_constraints.sh script.')
