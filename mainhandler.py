#!/usr/env/python
"""
Author: Andy Nagels
Date: 2010-08-24
Lisa: Pyqt gui for clipf, with extra functionality.

Copyright (C) 2010 Andy Nagels

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
from os.path import isfile
from subprocess import call

class Controller():
    """ Contains the bussiness logic of the application. """
    
    def __init__(self):
        """ Construct basic QApplication, add widgets and start exec_loop """
        # initialise special vars
        # TODO: Write this better and put 
        # fbackup and fcurrent in the config file
        self.fbackup = "/home/rockwolf/.config/clipf/db/op.bak"
        self.fcurrent = "/home/rockwolf/.config/clipf/db/op"
        # initialise the command buffer
        self.cmdbuffer = []

    # Methods
    ## General
    def write_commands(self):
        """ """
        #TODO: working with session etc. Use this for the export.
        # Safety first: take backup
        self.backup()
        self.pipe_commands()
        self.clear_commands()

    def backup(self):
        """ Make a backup of the output file for clipf. """
        # remove old backup
        if isfile(self.fbackup):
            try:
                os.remove(self.fbackup)
                print(self.fbackup + ' removed.')
            except IOError as strerror:
                print("Error: {0}".format(strerror))
        # copy current to .bak
        if isfile(self.fcurrent) and not isfile(self.fbackup):
            try:
                shutil.copy(self.fcurrent, self.fbackup)
                print(self.fbackup + ' created.')
            except:
                print('Error: application fucked up while creating backup.')
        else:
            print('Error: backup file already exists.')

    def pipe_commands(self):
        """ Pipe the commands in the buffer to clipf. """
        # write to current
        if isfile(self.fcurrent):
            try:
                for cmd in self.cmdbuffer:                
                    pipe1 = Popen(
                        ['echo',
                        'set acc ' + self.gui.cmb_account.currentText(),
                        '\n' + str(cmd)],
                        stdout=PIPE)
                    Popen(
                        ['clipf'],
                        stdin=pipe1.stdout)
            except Exception as strerror:
                print("Error: {0}.".format(strerror))

    def initgui(self):
        """ Initialise fields """
        # Dates
        self.gui.dt_date.setDate(QtCore.QDate.currentDate())
        self.gui.dt_datematch.setDate(QtCore.QDate.currentDate())
        # Info labels
        self.gui.lbl_infofinance.clear()
        self.gui.lbl_infofinance.setText('>> ' + self.fcurrent)
        self.gui.lbl_infodetails.clear()
        # fill all combo boxes
        self.fillcombos()
        self.gui.cmb_account.setCurrentIndex(1)

    def fillcombos(self):
        """ fill in the combo boxes with values. """
        dba = DatabaseAccess()
        # Products
        for prod in dba.get_products():
            self.gui.cmb_product.addItem(prod)
        # Accounts
        for acc in dba.get_accounts():
            self.gui.cmb_account.addItem(acc)
        # Choice
        self.gui.cmb_choice.addItem('A')
        self.gui.cmb_choice.addItem('B')
        # Market codes
        for mcd in dba.get_markets():
            self.gui.cmb_marketcode.addItem(mcd)
        # Stock names
        self.fillcmb_stockname()
        dba = None

    ## Stocks
    def fillcmb_stockname(self):
        """ fill cmb function """
        dba = DatabaseAccess()
        self.gui.cmb_stockname.clear()
        for name in dba.get_stocknames(self.gui.cmb_marketcode.currentText()):
            self.gui.cmb_stockname.addItem(name)
        dba = None
       
    def update_info_details(self):
        """ Update infolabel details. """
        dba = DatabaseAccess()
        prod = self.gui.cmb_product.currentText()
        stock = self.gui.cmb_stockname.currentText()
        if(
            prod == 'invest.buystocks' or
            prod == 'invest.sellstocks'
        ) and stock != '':
            info = dba.get_stockinfo(stock)
            self.gui.lbl_infodetails.setText('[' + info[1] + '] : ' + info[0])
        dba = None

    def add_command(self):
        """ Create the command to send to clipf and add it to the buffer. """
        # parse comment?
        prod = self.gui.cmb_product.currentText() 
        if(
            prod == 'invest.buystocks' or
            prod == 'invest.sellstocks'):
            str_list = [
                self.gui.cmb_marketcode.currentText(),
                '.',
                self.gui.cmb_stockname.currentText(),
                ',', 
                self.gui.spnQuantity.textFromValue(
                    self.gui.spnQuantity.value()),
                ',',
                self.gui.spnPrice.textFromValue(self.gui.spnPrice.value())]
            comment = ''.join(str_list) 
            if prod == 'invest.changestocks':
                comment = comment + ',' + self.gui.txt_comment.text()
        else:
            comment = self.gui.txt_comment.text() 
        
        str_list = [
            'op add -d ',
            str(self.gui.dt_date.date().toString(QtCore.Qt.ISODate)),
            str(self.gui.cmb_product.currentText()),
            ' ',
            str(self.gui.spn_amount.textFromValue(self.gui.spn_amount.value())),
            ' "' + str(comment) + '"']
        cmd = ''.join(str_list)
        self.cmdbuffer.append(cmd)
        self.gui.txt_summary.append(cmd)
        self.clear_fields()
   
    def clear_commands(self):
        """ Clear the command buffer and the summary panel. """
        self.cmdbuffer = [] 
        self.gui.txt_summary.clear()

    def clear_fields(self):
        """ Clear the main input fields. """
        self.gui.txt_comment.clear()
        self.gui.spn_amount.setValue(0)

    def layout(self):
        """ Everything about the layout off the application. """
        print('layout not implemented yet...')
        # Theming?

    def file_import(self):
        """ Import data from text file. """
        print('import... dummy')

    def file_export(self):
        """ Export data to text file. """
        print('export... dummy')

    def install(self):
        """ Setup the database through an external script. """
        try:
            call(["sh", "install.sh"])
        except:
            print('Error: could not load install.sh script.')

    def uninstall(self):
        """ Remove all from database through an external script. """
        try:
            call(["sh", "uninstall.sh"])
        except:
            print('Error: could not load uninstall.sh script.')
