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
from mdlimport import FileImport
from mdlexport import FileExport
from mdlstock import Stock
from PyQt4 import QtCore, QtGui
from databaseaccess import DatabaseAccess
from tablemodel import TableModel
import shutil
import os
from decimal import *

class Controller():
    """ Contains the bussiness logic of the application. """
    
    def __init__(self, gui, config):
        """ Construct basic QApplication, add widgets and start exec_loop """
        # initialise special vars
        self.gui = gui #QtGui.QDialog 
        self.config = config #object
        # initialise the command buffer
        self.inputbuffer = []
        # Decimal precision
        getcontext().prec = 4

    # Methods
    ## General
    def write_commands(self):
        """ """
        try:
            fields_db = []
            for field in self.inputbuffer:
                product = field[2]
                if(product[-3:] == '.rx'):
                    flg_income = 1
                elif(product[-3:] == '.tx'):
                    flg_income = 0
                fields_db.append({
                    'date':field[0],
                    'account':field[1], #Note: Get AID from T_ACCOUNT for final insert
                    'product':field[2], #Note: Get PID from T_PRODUCT for final insert
                    'object':field[3], #Note: Get OID from T_OBJECT for final insert
                    'amount':field[4],
                    'flag':flg_income,
                    'comment':field[5],
                    'stock':field[6],
                    'market':field[7],
                    'shares':field[8],
                    'price':field[9],
                    'commission':field[10],
                    'tax':field[11]
                })
            # import finance info from inputbuffer
            dba = DatabaseAccess(self.config)
            dba.file_import_lines(fields_db)
            dba = None
            # import stock info from inputbuffer
            fields_stock = []
            stock = Stock(self.config)
            for field in fields_db:
                fields_stock.append(stock.parse_stocks(field))
            stock.process_stocks(fields_db, fields_stock)
            stock = None
            #TODO: process_trades
            self.clear_inputbuffer()
        except Exception as ex:
            print("Error in write_commands: ", ex)

    def backup(self):
        """ Make a backup of the output file for clipf. """
        # remove old backup
        if isfile(self.config.backupfile):
            try:
                os.remove(self.config.backupfile)
                print(self.config.backupfile + ' removed.')
            #except IOError as strerror:
            except Exception as ex:
                print("Error: ", ex)
        # copy current to .bak
        if isfile(self.config.exportfile) and not isfile(self.config.backupfile):
            try:
                shutil.copy(self.config.exportfile, self.config.backupfile)
                print(self.config.backupfile + ' created.')
            except Exception as ex:
                print('Error: application fucked up while creating backup: ', ex)
        else:
            print('Error: backup file already exists.')

    def pipe_commands(self):
        """ Pipe the commands in the buffer to clipf. """
        #TODO: no longer piping of commands. It's all done in a session, so add values to a session array or something.
        # write to current
        if isfile(self.config.exportfile):
            try:
                for cmd in self.inputbuffer:                
                    pipe1 = Popen(
                        ['echo',
                        'set acc ' + self.gui.cmb_account.currentText(),
                        '\n' + str(cmd)],
                        stdout=PIPE)
                    Popen(
                        ['clipf'],
                        stdin=pipe1.stdout)
            #except Exception as strerror:
            except:
                print("Error: {0}.".format(strerror))
    ## Init of gui
    def fillcombos(self):
        """ fill in the combo boxes with values. """
        #TODO: fix databaseaccess first
        dba = DatabaseAccess(self.config)
        # Products
        for prod in dba.get_products():
            self.gui.cmb_product.addItem(prod)
        # Accounts
        for acc in dba.get_accounts():
            self.gui.cmb_account.addItem(acc)
        # Object
        for obj in dba.get_objects():
            self.gui.cmb_object.addItem(obj)
        # Market codes
        for mcd in dba.get_markets():
            self.gui.cmb_marketcode.addItem(mcd)
        # Stock names
        self.fillcmb_stockname()
        self.filltxt_marketdescription()
        self.filltxt_stockdescription()
        dba = None
        # Init tbl_summary
        self.init_tbl_summary()

    ## Clear
    def clear_inputbuffer(self):
        """ Clear the command buffer and the summary panel. """
        self.inputbuffer = [] 
        self.table.clearContents()
        self.table.tablecontent = []

    def clear_fields(self):
        """ Clear the main input fields. """
        self.gui.txt_comment.clear()
        self.gui.spn_amount.setValue(0)

    def add_inputline(self):
        """ Command that adds an input finance line into a temporary buffer. """
        if(self.gui.cmb_object.currentText() == 'buystocks' or \
                self.gui.cmb_object.currentText() == 'sellstocks'):
            market = str(self.gui.cmb_marketcode.currentText())
            stock = str(self.gui.cmb_stockname.currentText())
        else:
            market = ''
            stock = ''
        str_list = [
            str(self.gui.dt_date.date().toString(QtCore.Qt.ISODate)),
            str(self.gui.cmb_account.currentText()),
            str(self.gui.cmb_product.currentText()),
            str(self.gui.cmb_object.currentText()),
            str(self.gui.spn_amount.textFromValue(self.gui.spn_amount.value())),
            str(self.gui.txt_comment.text()),
            stock,
            market,
            str(self.gui.spn_quantity.textFromValue(
                self.gui.spn_quantity.value())),
            str(self.gui.spn_price.textFromValue(self.gui.spn_price.value())),
            str(self.gui.spn_commission.textFromValue(self.gui.spn_commission.value())),
            str(Decimal(self.gui.spn_tax.textFromValue(self.gui.spn_tax.value()))/100),
            str(self.gui.spn_risk.textFromValue(self.gui.spn_risk.value())),
            ]
        #self.inputbuffer.append(str_list)
        self.add_tbl_summary(str_list)
        self.clear_fields()

    def update_info_details(self):
        """ Update infolabel details. """
        dba = DatabaseAccess(self.config)
        prod = self.gui.cmb_product.currentText()
        stock = self.gui.cmb_stockname.currentText()
        #TODO: make entire program dependent on pids, so there are no longer
        #hardcoded strings.
        if(
            prod == 'invest.tx' or
            prod == 'trade.tx' or
            prod == 'invest.rx' or
            prod == 'trade.rx'
        ) and stock != '':
            info = dba.get_stockinfo(stock)
            self.gui.lbl_infodetails.setText(info[1] + '(' + ''.join(info[2].split()) +'): ' + info[0])
        else:
            self.gui.lbl_infodetails.setText('')
        dba = None

    def fillcmb_stockname(self):
        """ fill cmb function """
        dba = DatabaseAccess(self.config)
        self.gui.cmb_stockname.clear()
        for name in dba.get_stocknames(self.gui.cmb_marketcode.currentText()):
            self.gui.cmb_stockname.addItem(name)
        dba = None
    
    def filltxt_marketdescription(self):
        """ fill market description """
        dba = DatabaseAccess(self.config)
        self.gui.txt_marketdescription.clear()
        self.gui.txt_marketdescription.setText( \
                dba.get_marketdescription( \
                self.gui.cmb_marketcode.currentText()))
        dba = None

    def filltxt_stockdescription(self):
        """ fill stock description """
        dba = DatabaseAccess(self.config)
        self.gui.txt_stockdescription.clear()
        self.gui.txt_stockdescription.setText( \
                dba.get_stockdescription( \
                self.gui.cmb_stockname.currentText()))
        dba = None

    def file_import(self):
        """ Import data from text file. """
        fi = FileImport(self.config)
        fi.file_import()
        fi = None

    def file_export(self):
        """ Export data to text file. """
        fe = FileExport(self.config)
        # Safety first: take backup
        self.backup()
        fe.file_export()
        fe = None

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

    def init_tbl_summary(self):
        """ Initialize tbl_summary. """
        # set the table header
        # TODO: set header values in mdlconstants and use the constants
        header = ['date', 'account', 'product', 'object', 'amount', 'comment', 'stock', 'market', 'quantity', 'price', 'commission', 'tax', 'risk']
        data = self.inputbuffer
        self.table = TableModel(header, data, len(data), len(header))
        # takeAt(0) removes the default empty table that's there and addWidget
        # adds a newly created one.
        self.gui.vl_table.takeAt(0)
        self.gui.vl_table.addWidget(self.table)

    def add_tbl_summary(self, row):
        """ Add or remove a row from the table view """
        self.table.add_row(row)
