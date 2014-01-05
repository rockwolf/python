#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.					
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
            print 'Error: could not load install.sh script.'

    def uninstall(self):
        """ Remove all from database through an external script. """
        try:
            call(["sh", "setup/uninstall.sh"])
        except:
            print 'Error: could not load uninstall.sh script.'

    def clear_tables(self):
        """ This function can be used to empty the database tables. """
        try:
            call(["sh", "setup/clear_tables.sh"])
        except:
            print 'Error: could not load clear_tables.sh script.'

    def drop_constraints(self):
        """ This function can be used to drop all table constraints. """
        try:
            call(["sh", "setup/drop_constraints.sh"])
        except:
            print 'Error: could not load drop_constraints.sh script.'

    def add_constraints(self):
        """ This function can be used to create all table constraints. """
        try:
            call(["sh", "setup/add_constraints.sh"])
        except:
            print 'Error: could not load add_constraints.sh script.'
