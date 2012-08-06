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
import shutil
import os
from decimal import Decimal, getcontext
from PyQt4 import QtCore

from modules.fileimport import FileImport
from modules.fileexport import FileExport
from stock import Stock
from database.databaseaccess import DatabaseAccess

class Controller():
    """ Contains the bussiness logic of the application. """
    
    def __init__(self, gui, config):
        """ Construct basic QApplication, add widgets and start exec_loop """
        # initialise special vars
        self.gui = gui #QtGui.QDialog 
        self.config = config #object
        # Decimal precision
        getcontext().prec = 4

    # Methods
    ## General
    def write_commands(self):
        """ """
        try:
            fields_db = []
            for field in self.table.tablecontent:
                category = field[2]
                if(category[-3:] == '.rx'):
                    flg_income = 1
                elif(category[-3:] == '.tx'):
                    flg_income = 0
                fields_db.append({
                    'date':field[0],
                    'account':field[1], #Note: Get AID from T_ACCOUNT for final insert
                    'category':field[2], #Note: Get CID from T_CATEGORY for final insert
                    'subcategory':field[3], #Note: Get SCID from T_SUBCATEGORY for final insert
                    'amount':field[4],
                    'flag':flg_income,
                    'comment':field[5],
                    'stock':field[6],
                    'market':field[7],
                    'shares':field[8],
                    'price':field[9],
                    'commission':field[10],
                    'tax':field[11],
                    'risk':field[12]
                })
            # import finance info from table data
            dba = DatabaseAccess(self.config)
            dba.file_import_lines(fields_db)
            dba = None
            # import stock info from table data
            fields_stock = []
            stock = Stock(self.config)
            for field in fields_db:
                fields_stock.append(stock.parse_stocks(field))
            stock.process_stocks(fields_db, fields_stock)
            stock = None
            #TODO: process_trades
            self.table.clear()
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

    ## Init of gui
    def fillcombos(self):
        """ fill in the combo boxes with values. """
        #TODO: fix databaseaccess first
        dba = DatabaseAccess(self.config)
        # Products
        for prod in dba.get_categories():
            self.gui.cmb_category.addItem(prod)
        # Accounts
        for acc in dba.get_accounts():
            self.gui.cmb_account.addItem(acc)
        # Object
        for obj in dba.get_subcategories():
            self.gui.cmb_subcategory.addItem(obj)
        # Market codes
        for mcd in dba.get_markets():
            self.gui.cmb_marketcode.addItem(mcd)
        # Stock names
        self.fillcmb_stockname()
        self.filltxt_marketdescription()
        self.filltxt_stockdescription()
        dba = None

    ## Clear
    def clear_inputbuffer(self, table):
        """ Clear the command buffer and the summary panel. """
        table.clear()

    def clear_fields(self):
        """ Clear the main input fields. """
        self.gui.txt_comment.clear()
        self.gui.spn_amount.setValue(0)

    def add_inputline(self, table):
        """ Command that adds an input finance line into a temporary buffer. """
        #TODO: self....cerrentText() and all this crap is PyQt specific.
        #This should be moved to the view (guihandler).
        # create a self.gui.get_subcategory etc.
        if(self.gui.cmb_subcategory.currentText() == 'buy' or \
                self.gui.cmb_subcategory.currentText() == 'sell'):
            market = str(self.gui.cmb_marketcode.currentText())
            stock = str(self.gui.cmb_stockname.currentText())
        else:
            market = ''
            stock = ''
        str_list = [
            str(self.gui.dt_date.date().toString(QtCore.Qt.ISODate)),
            str(self.gui.cmb_account.currentText()),
            str(self.gui.cmb_category.currentText()),
            str(self.gui.cmb_subcategory.currentText()),
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
        self.add_tbl_summary(table, str_list)
        self.clear_fields()

    def update_info_details(self):
        """ Update infolabel details. """
        dba = DatabaseAccess(self.config)
        prod = self.gui.cmb_category.currentText()
        stock = self.gui.cmb_stockname.currentText()
        #TODO: make entire program dependent on cids, so there are no longer
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
            call(["sh", "setup/install.sh"])
        except:
            print('Error: could not load install.sh script.')

    def uninstall(self):
        """ Remove all from database through an external script. """
        try:
            call(["sh", "setup/uninstall.sh"])
        except:
            print('Error: could not load uninstall.sh script.')

    def add_tbl_summary(self, table, row):
        """ Add or remove a row from the table view """
        table.add_row(row)
