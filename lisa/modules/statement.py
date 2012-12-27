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
            self.statements_insert = []
            self.statements_update = []
            self.statements_delete = []
            self.table_name = table_name
        except Exception as ex:
            print("Error in initialisation of Statements: ", ex)

    def get_value_list(self, insupdel=0):
        """
            Returns value_list of the statements.
        """
        #NOTE: statement = [record, {...}]
        result = []
        if insupdel == 0:
            statements = self.statements_insert
        elif insupdel == 1:
            statements = self.statements_update
        elif insupdel == 2:
            statements = self.statements_delete
        for statement in statements:    
            result.append([key for key, val in statement[1].items()])
        return result
 
    def add(self, recordid, tablerow_object, insupdel=0):
        """ Add a statement with recordid and tablerow object. """
        try:
            # Add a statement
            # with recordid
            if insupdel == 0:
                self.statements_insert.append([recordid, tablerow_object])
            elif insupdel == 1:
            	self.statements_update.append([recordid, tablerow_object])
            elif insupdel == 2:
                self.statements_delete.append([recordid, tablerow_object])
        except Exception as ex:
            print("Error adding statement for", self.table_name, ": ", ex)
   
    def remove(self, index=-1, insupdel=0):
        """ Remove statement added on specified index """
        try:
            if insupdel == 0:
                self.statements_insert.pop(index)
            elif insupdel == 1:
            	self.statements_update.pop(index)
            elif insupdel == 2:
            	self.statements_delete.pop(index)
        except Exception as ex:
            print("Error removing statement from the list: ", ex)

    def print_statements(self):
        """ 
            Method that prints the statement info and text
            on the screen (logic).
        """
        self.print_statements_when_needed(self.statements_insert,
            'Insert statements for')
        self.print_statements_when_needed(self.statements_update,
            'Update statements for')
        self.print_statements_when_needed(self.statements_delete,
            'Delete statements for')

    def print_statements_when_needed(self, statements, message):
        """ 
            Method that prints the statement info and text
            on the screen (logic).
        """
        if statements != []:
            print(message, self.table_name)
            print('_'*len(message) + '_'*len(self.table_name), '\n')
            for s in statements:
                print(s)

    def get_statement_list(self, insupdel=0):
        """
            Returns a list of statements from the statement object,
            without the recordid.
        """
        #NOTE: statement = [record, {...}]
        result = []
        try:
            if insupdel == 0:
            	statements = self.statements_insert
            elif insupdel == 1:
            	statements = self.statements_update
            elif insupdel == 2:
            	statements = self.statements_delete
            if statements is not None:
                for statement in statements:
                    result.append(statement[1])
        except Exception as ex:
            print("Error retrieving statement list: ", ex)
        return result
