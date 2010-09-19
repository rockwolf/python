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
import sys, getopt, time, shutil, os
from PyQt4 import QtCore, QtGui
from lisagui import Ui_frmMain
from datetime import datetime
from databaseaccess import DatabaseAccess
from os.path import *
from subprocess import *

class lisa(QtGui.QDialog, Ui_frmMain):

    def __init__(self, parent=None):
        """ Construct basic QApplication, add widgets and start exec_loop """
        # initialize gui
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_frmMain()
        self.ui.setupUi(self) 
        self.ConnectSlots(self.ui)
        self.InitGui()
        self.Layout()
        # initialise the command buffer
        self.cmdbuffer = []

    def ConnectSlots(self, parent):
        """ Connect methods to the signals the gui emits """
        self.ui.btnExit.connect(self.ui.btnExit, QtCore.SIGNAL("clicked()"), self.BtnExit_Clicked)
        self.ui.cmbProduct.connect(self.ui.cmbProduct, QtCore.SIGNAL("currentIndexChanged(QString)"), self.CmbProduct_Changed)
        self.ui.cmbProduct.connect(self.ui.tabDetails, QtCore.SIGNAL("currentChanged(int)"), self.TabDetails_Changed)
        self.ui.cmbProduct.connect(self.ui.btnAdd, QtCore.SIGNAL("clicked()"), self.BtnAdd_Clicked)
        self.ui.cmbProduct.connect(self.ui.cmbMarketCode, QtCore.SIGNAL("currentIndexChanged(QString)"), self.CmbMarketCode_Changed)
        self.ui.cmbProduct.connect(self.ui.cmbStockName, QtCore.SIGNAL("currentIndexChanged(QString)"), self.CmbStockName_Changed)
        self.ui.cmbTeamA.connect(self.ui.cmbTeamA, QtCore.SIGNAL("currentIndexChanged(QString)"), self.CmbTeamA_Changed)
        self.ui.cmbTeamA2.connect(self.ui.cmbTeamA2, QtCore.SIGNAL("currentIndexChanged(QString)"), self.CmbTeamA2_Changed)
        self.ui.cmbTeamB.connect(self.ui.cmbTeamB, QtCore.SIGNAL("currentIndexChanged(QString)"), self.CmbTeamB_Changed)
        self.ui.cmbTeamB2.connect(self.ui.cmbTeamB2, QtCore.SIGNAL("currentIndexChanged(QString)"), self.CmbTeamB2_Changed)
        self.ui.btnExit.connect(self.ui.btnExecute, QtCore.SIGNAL("clicked()"), self.BtnExecute_Clicked)

    def BtnExecute_Clicked(self):
        """ Pipe commands to clipf. """
        # Safety first: take backup
        self.Backup()
        self.WriteCmds()
        
    def BtnExit_Clicked(self):
        """ Exit """
        sys.exit(0)

    def Backup(self):
        """ Make a backup of the output file for clipf. """
        #TODO: Write this better and put fbackup and fcurrent in the config file
        fbackup = "/home/rockwolf/.config/clipf/db/op.bak"
        fcurrent = "/home/rockwolf/.config/clipf/db/op"
        # remove old backup
        if isfile(fbackup):
            try:
                os.remove(fbackup)
                print fbackup + ' removed.'
            except IOError as (errno, strerror):
                print "Error {0}: {1}".format(errno,strerror)
        # copy current to .bak
        if isfile(fcurrent) and not isfile(fbackup):
            try:
                shutil.copy(fcurrent, fbackup)
                print fbackup + ' created.'
            except:
                print 'Error: application fucked up while creating backup.'
        else:
            print 'Error: backup file already exists.'

    def WriteCmds(self):
        """ Pipe the commands in the buffer to clipf. """
        #TODO: Write this better and put fbackup and fcurrent in the config file
        fbackup = "/home/rockwolf/.config/clipf/db/op.bak"
        fcurrent = "/home/rockwolf/.config/clipf/db/op"
        # write to current
        if isfile(fcurrent):
            try:
                for cmd in self.cmdbuffer:                
                    p1 = Popen(['echo', str(cmd)], stdout=PIPE)
                    p2 = Popen(['clipf'], stdin=p1.stdout)
                    #Popen(['/bin/echo','test'])
            except Exception as strerror:
                print "Error: {0}.".format(strerror)

    def CmbProduct_Changed(self, selstr):
        """ When the account combo selection changes. """
        self.ui.txtComment.setEnabled(True)
        if selstr == 'bet.place':
            self.ui.tabDetails.currentTabName = self.ui.tabDetails.setCurrentIndex(2)
        elif selstr == 'bet.cashin':
            self.ui.tabDetails.currentTabName = self.ui.tabDetails.setCurrentIndex(3)
        elif selstr == 'invest.buystocks' or selstr == 'invest.sellstocks' or selstr == 'invest.changestocks':
            self.ui.tabDetails.currentTabName = self.ui.tabDetails.setCurrentIndex(1)
            self.UpdateInfoDetails()
            if selstr != 'invest.changestocks':
                self.ui.txtComment.setEnabled(False)
        else:
            self.ui.tabDetails.currentTabName = self.ui.tabDetails.setCurrentIndex(0)

    def TabDetails_Changed(self, index):
        """ What to do if you change a tab. """
        self.CmbProduct_Changed(self.ui.cmbProduct.currentText())

    def InitGui(self):
        """ Initialise fields """
        # Dates
        self.ui.dtDate.setDate(QtCore.QDate.currentDate())
        self.ui.dtDateMatch.setDate(QtCore.QDate.currentDate())
        # Info labels
        self.ui.lblInfoFinance.clear()
        self.ui.lblInfoDetails.clear()
        # Fill all combo boxes
        self.FillCombos()

    def FillCombos(self):
        """ Fill in the combo boxes with values. """
        # Teams
        self.FillCmbTeamA()
        self.FillCmbTeamB()
        self.FillCmbTeamA2()
        self.FillCmbTeamB2()
        dba = DatabaseAccess()
        # Products
        for prod in dba.GetProducts():
            self.ui.cmbProduct.addItem(prod)
        # Accounts
        for acc in dba.GetAccounts():
            self.ui.cmbAccount.addItem(acc)
        # Choice
        self.ui.cmbChoice.addItem('A')
        self.ui.cmbChoice.addItem('B')
        # Market codes
        for mcd in dba.GetMcodes():
            self.ui.cmbMarketCode.addItem(mcd)
        # Stock names
        self.FillCmbStockName()
        dba = None

    def FillCmbStockName(self):
        """ Fill cmb function """
        dba = DatabaseAccess()
        self.ui.cmbStockName.clear()
        for name in dba.GetStockNames(self.ui.cmbMarketCode.currentText()):
            self.ui.cmbStockName.addItem(name)
        dba = None
       
    def CmbMarketCode_Changed(self, selstr):
        """ When the marketcode combo selection changes. """
        self.FillCmbStockName()
    
    def CmbStockName_Changed(self, selstr):
        """ When the stock name selection changes. """    
        self.UpdateInfoDetails()        
        
    def CmbTeamA_Changed(self, selstr):
        """ When the team name selection changes for bet.place. """    

    def FillCmbTeamA(self):
        """ Put values in the cmb. """ 
        dba = DatabaseAccess()
        selstr = ''
        teams = dba.GetTeams(selstr)
        if teams != None:
            self.ui.cmbTeamA.clear()
            for team in teams:
                self.ui.cmbTeamA.addItem(team)
        dba = None
        
    def CmbTeamB_Changed(self, selstr):
        """ When the team name selection changes for bet.cashin. """    
    
    def FillCmbTeamB(self):
        """ Put values in the cmb. """ 
        dba = DatabaseAccess()
        selstr = ''
        teams = dba.GetTeams(selstr)
        if teams != None:
            self.ui.cmbTeamB.clear()
            for team in teams:
                self.ui.cmbTeamB.addItem(team) 
        dba = None 

    def CmbTeamA2_Changed(self, selstr):
        """ When the team name selection changes for bet.place. """    
   
    def FillCmbTeamA2(self):     
        """ Put values in the cmb. """ 
        dba = DatabaseAccess()
        selstr = ''
        teams = dba.GetTeams(selstr)
        if teams != None:
            self.ui.cmbTeamA2.clear()
            for team in teams:
                self.ui.cmbTeamA2.addItem(team)
        dba = None
        
    def CmbTeamB2_Changed(self, selstr):
        """ When the team name selection changes for bet.cashin. """    

    def FillCmbTeamB2(self):
        """ Put values in the cmb. """ 
        dba = DatabaseAccess()
        selstr = ''
        teams = dba.GetTeams(selstr)
        if teams != None:
            self.ui.cmbTeamB2.clear()
            for team in teams:
                self.ui.cmbTeamB2.addItem(team)
        dba = None
        
    def UpdateInfoDetails(self):
        """ Update infolabel details. """
        dba = DatabaseAccess()
        prod = self.ui.cmbProduct.currentText()
        stock = self.ui.cmbStockName.currentText()
        if (prod == 'invest.buystocks' or prod == 'invest.sellstocks' or prod == 'invest.changestocks') and stock != '':
            info = dba.GetStockInfo(stock)
            self.ui.lblInfoDetails.setText('[' + info[1] + '] : ' + info[0])
        dba = None

    def BtnAdd_Clicked(self):
        """ Create the command to send to clipf and add it to the buffer. """
        # parse comment?
        prod = self.ui.cmbProduct.currentText() 
        if prod == 'bet.place':
            comment = self.ui.cmbTeamA.currentText() + ',' + self.ui.cmbTeamB.currentText() + ',' + self.ui.cmbChoice.currentText() + ',' + self.ui.dtDateMatch.dateTime().toString("yyyy-MM-dd HH:mm")
        elif prod == 'bet.cashin':
            comment = self.ui.cmbTeamA2.currentText() + ',' + self.ui.cmbTeamB2.currentText() + ',' + self.ui.spnScoreA.textFromValue(self.ui.spnScoreA.value()) + '-' + self.ui.spnScoreB.textFromValue(self.ui.spnScoreB.value())
        elif prod == 'invest.buystocks' or prod == 'invest.sellstocks' or prod == 'invest.changestocks':
            comment = self.ui.cmbMarketCode.currentText() + '.' + self.ui.cmbStockName.currentText() + ',' + self.ui.spnQuantity.textFromValue(self.ui.spnQuantity.value()) + ',' + self.ui.spnPrice.textFromValue(self.ui.spnPrice.value())
            if prod == 'invest.changestocks':
                comment = comment + ',' + self.ui.txtComment.text()
        else:
            comment = self.ui.txtComment.text() 
        cmd = 'op add -d ' + self.ui.dtDate.date().toString(QtCore.Qt.ISODate) + ' ' +  self.ui.cmbProduct.currentText() + ' ' + self.ui.spnAmount.textFromValue(self.ui.spnAmount.value()) + ' "' + comment + '"'
        self.cmdbuffer.append(cmd)
        print self.cmdbuffer
        self.ui.txtSummary.append(cmd)
    
    def Layout(self):
        """ Everything about the layout off the application. """
        print 'Layout not implemented yet...'
        # Theming?

class MainWrapper():
    """ Parsed options get there functionality here, it's seperate from the gui part of the app. """ 

    def get_pprog(self):
        """ pprog """
        return self._pprog

    def set_pprog(self, name):
        """ set pprog """
        self._pprog = name

    pprog = property(get_pprog, set_pprog)

    def get_pversion(self):
        """ pversion """
        return self._pversion

    def set_pversion(self, version):
        """ set pversion """
        self._pversion = version

    pversion = property(get_pversion, set_pversion)
     
    def get_prelease(self):
        """ prelease """
        return self._prelease

    def set_prelease(self, release):
        """ set prelease """
        self._prelease = release

    prelease = property(get_prelease, set_prelease)
     
    def get_pdate(self):
        """ pdate """
        return self._pdate

    def set_pdate(self, date):
        """ set pdate """
        self._pdate = date

    pdate = property(get_pdate, set_pdate)
    
    def get_exitstate(self):
        """ Run or exit program? """
        return self._exitstate

    def set_exitstate(self, state):
        """ Set run-/exitstate """
        self._exitstate = state

    exitstate = property(get_exitstate, set_exitstate)

    def __init__(self, parent=None):
        """ Construct basic QApplication, add widgets and start exec_loop. """
        # general properties of the app
        self.set_pprog('lisa.py')
        self.set_pversion('0.01a')
        self.set_prelease('Wow, the exit button works!')
        self.set_pdate('2010-08-28')     
        self.set_exitstate(0)   
        self.msgHandler = __import__('messagehandler')
    
    def Usage(self):
        """ Print usage info and exit """
        print '''{0} : Less Interaction Saves Arbeit
Options: 
 -h : displays this help message
 --setup : creates tables that help make the app more userfriendly
 --remove : deletes all relevant tables in the database, all data will be destroyed...
 --version : displays version
 --python : displays Python version
All arguments are optional.'''.format(self.get_pprog())

    def Run(self):
        """ This is the main driver for the program. """
        if self.get_exitstate() == 1:
            sys.exit(0)
        # Run the gui app
        app = QtGui.QApplication(sys.argv)
        myapp = lisa()
        myapp.show()
        sys.exit(app.exec_())

    def Setup(self):
        """ Set up the database. """
        dba = DatabaseAccess()
        dba.Setup()
        dba = None

    def Remove(self):
        """ Set up the database. """
        dba = DatabaseAccess()
        dba.Remove()
        dba = None

def Main():
    """ Main driver, startup and cli options parsing. """
    # Gonna switch this to optparse later
    try:
        options, xarguments = getopt.getopt(sys.argv[1:], 'h', ['setup', 'remove', 'version', 'python'])
    except getopt.error,err:
        print 'Error: ' + str(err)
        sys.exit(1)

    cl = MainWrapper()

    for opt in options[:]:
        if opt[0] == '-h':
            cl.Usage()
            cl.set_exitstate(1) # don't run the program after the optionparsing
    for opt in options[:]:
        if opt[0] == '--setup':
            cl.Setup()
            cl.set_exitstate(1)
            break
    for opt in options[:]:
        if opt[0] == '--remove':
            cl.Remove()
            cl.set_exitstate(1)
            break
    for opt in options[:]:
        if opt[0] == '--version':
            print cl.get_pprog() + ' version '+ cl.get_pversion() + ' (' + cl.get_pdate() + '), \'' + cl.get_prelease() + '\' release.'
            cl.set_exitstate(1)
            break
    for opt in options[:]:
        if opt[0] == '--python':
            print 'Python '+sys.version
            cl.set_exitstate(1)
            break

    cl.Run() #run the main method for the program

if __name__ == "__main__":
    Main()
