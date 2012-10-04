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

class Statement():
    """ A class to contain statements to be executed within the orm session. """

    def __init__(self, table_name):
        """ Init """
        try:
            self.statements = []
            self.table_name = table_name
        except Exception as ex:
            print("Error in initialisation of Statements: ", ex)
 
    def add(self, recordid, tablerow_object):
        """ Add a statement with recordid and tablerow object. """
        try:
            # Add a statement
            # with recordid
            self.statements.append([recordid, tablerow_object])
            # tablerow object (statement)
            #self.statements[recordid-1].append(tablerow_object)
        except Exception as ex:
            print("Error adding statement for", self.table_name, ": ", ex)
   
    def remove(self, index=-1):
        """ Remove statement added on specified index """
        try:
            self.statements.pop(index)
        except Exception as ex:
            print("Error removing statement from the list: ", ex)
    
    def execute(self, session):
        """ Execute list of statements for given session """
        try:
            # First collect the statements, without the recordid.
            tablerow_objects = []
            for line in self.statements:
                tablerow_objects.append(line[1])
            # Now add the tablerows to the database, all at once.
            session.add_all(self.statements)
        except Exception as ex:
            print("Error executing statements: ", ex)

    def print_statements(self):
        """ Method that actually prints the statement info and text on the screen. """
        print('Statements for', self.table_name)
        print('_______________' + '_'*len(self.table_name), '\n')
        for s in (self.statements):
            print(s)
