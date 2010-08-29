"""
This file is part of Clipf2db.

Clipf2db is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Clipf2db is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Clipf2db. If not, see <http://www.gnu.org/licenses/>.
"""
class MessageHandler:
    """ A general class to handle messages """

    def __init__(self):
        """ Init of MessageHandler class """
    
    def Confirmation(self, strAct):
        """ Show confirmation dialog """
        answer = raw_input('Are you sure you want to %s? [y|n] ' % strAct).strip().lower()
        if answer != 'y':
            print 'Aborted.'
            return -1
        elif answer == 'y':
            return 0

    def PrintAction(self, strAct, lstStr):
        """ Print message about strAction for each item in the lstObj list """
        for s in lstStr:
            print '{0} {1}.'.format(strAct, s)

class ErrorHandler(MessageHandler):
    """ A class to handle error messages, it inherits from MessageHandler """

    def __init__(self):
        """ Init of ErrorHandler class """
        print 'ErrorHandling loaded...'
