#! /usr/local/bin/python
"""
Author: Andy Nagels
Date: 2010-03-11
Ih2rem: Add NHL schedule data, from a team, to your remind calendar.

Copyright (C) 2010 Andy Nagels

This file is part of Ih2rem.

Ih2rem is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Ih2rem is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Ih2rem. If not, see <http://www.gnu.org/licenses/>.
					
"""

import sys, getopt, time, os, vobject
from subprocess import call
from string import strip
from datetime import datetime
from datetime import timedelta
from pytz import timezone


class Ih2rem:
 
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
    
    def get_inputdir(self):
        """ inputdir """
        return self._inputdir
    
    def set_inputdir(self, version):
        """ set inputdir """
        self._inputdir = version
    
    inputdir = property(get_inputdir, set_inputdir)

    def get_outputfile(self):
        """ outputfile """
        return self._outputfile
    
    def set_outputfile(self, version):
        """ set outputfile """
        self._outputfile = version
    
    outputfile = property(get_outputfile, set_outputfile)

    def get_tzlocal(self):
        """ tzlocal """
        return self._tzlocal
    
    def set_tzlocal(self, version):
        """ set tzlocal """
        self._tzlocal = version
    
    tzlocal = property(get_tzlocal, set_tzlocal)
    
    def __init__(self):
        """ Init of main class """
        self.set_pprog('ih2rem.py')
        self.set_pversion('0.01a')
        self.set_prelease('Icecave')
        self.set_pdate('2010-03-11')
        self.set_exitstate(0)
        self.set_inputdir('./')
        self.set_outputfile('/home/rockwolf/.reminders_nhl')
        self.set_tzlocal(timezone('Europe/Brussels'))
   
    def fUsage(self):
	    """ Print usage info and exit """
	    print self.get_pprog() + ''' : Application that will create remind code for an NHL team schedule, so the match dates and hours can be displayed in your calendar.
	Options: 
	    -h : displays this help message
	    -i <path/to/input.csv | path/to/input.ics> : import this csv|ical schedule (downloadable from the NHL websites)
	    -o <path/to/reminders-file> : export to this reminders file (default in ~/.reminders_nhl)
	    -t <integer> : add this timezone delay to the time value in the csv (default 5, so 5 hours get added)
	    --version : displays version
	    --python : displays Python version'''

    def fRun(self):
        """ This is the main driver for the program. """
        # Main method to call, goes here
        sys.path.append(self.get_inputdir())
        for subdir, dirs, files in os.walk(self.get_inputdir()):
            for file in files:
                if (file[-4:] == ".csv"):
                    self.fProcess_csv(file)
                elif (file[-4:] == ".ics"):
                    self.fProcess_ics(file)
        sys.exit(0)
            
    def fProcess_csv(self, file):
        """ Read a csv file and append it to the reminders file. """
        # csv file from http://www.mysportscal.com
        try:
            src = open(self.get_inputdir() + '/' + file)
            dst = open(self.get_outputfile(),"a")
            try:
                lines = src.readlines()
                fields = {}
                firstline = 0
                now = self.get_tzlocal().localize(datetime.now())
                #print now.strftime("%Y-%m-%d %H:%M:%S") + ": running main thread ..."
                tzinput=timezone("US/Central")
                
                for line in lines:
                    print 'L>>', line
                    fields = line.split(',')
                    #REM Feb 16 2009 AT 9:15 +30 DURATION 2:15 MSG Match x is now.

                    if firstline == 0:
                        firstline = 1
                    else:
                        output = {
                            'subject' : fields[2],
                            'start' : fields[0] + ' ' + fields[8],
                            'end' : fields[1] + ' ' + fields[12]
                        }
                        
                        start = tzinput.localize(datetime.strptime(output['start'], "%m/%d/%Y %I:%M %p")).astimezone(self.get_tzlocal())
                        #if start >= now:
                        end = tzinput.localize(datetime.strptime(output['end'], "%m/%d/%Y %I:%M %p")).astimezone(self.get_tzlocal())
                        #print 'test: ' + output['subject']
                        #print 'test_start: ' + str(start.isoformat())
                        #print 'test_end: ' + str(end.isoformat())
                        # REM + day(datetime) + AT + time(start) + +30 DURATION + time(end)-time(start) + MSG + subject
                        duration = datetime.strptime(str(end-start), "%H:%M:%S").time().strftime("%H:%M")
                        outstr = 'REM ' + str(start.strftime('%b %d %Y')) + ' AT ' + str(start.time().strftime('%H:%M')) + ' +30 DURATION ' + str(duration) + ' MSG ' + output['subject'] + '\n'
                        #print outstr
                        dst.write(outstr)
            finally:
                src.close()
		dst.close()
        except IOError as (errno, strerror):
            print "Error {0}: {1} at {2}.".format(errno, strerror, self.get_inputdir() + '/' + file) 

    def fProcess_ics(self, file):
        """ Read an ics (ical) file and append it to the reminders file. """
        try:
            src = open(self.get_inputdir() + '/' + file)
            dst = open(self.get_outputfile(),"a")
            try:
                tzinput = timezone('Etc/UTC') # ics files from http://www.mysportscal.com
                datefmt = '%b %d %Y'
                timefmt = '%H:%M'
                remfmt = 'REM %s AT %s +30 DURATION %s MSG %s'

                cal = vobject.readOne(src)

                for event in cal.vevent_list:
                    text = event.summary.value

                    dtstart = event.dtstart.value.astimezone(tzinput).astimezone(self.get_tzlocal())
                    dtend = event.dtend.value.astimezone(tzinput).astimezone(self.get_tzlocal())
                    duration = str(dtend - dtstart)[:-3]

                    now = self.get_tzlocal().localize(datetime.now())
                    #if dtstart >= now:
                    print >>dst, remfmt % (
                        dtstart.strftime(datefmt),
                        dtstart.strftime(timefmt),
                        duration, text
                    )
            finally:
                src.close()
        except IOError as (errno, strerror):
            print "Error {0}: {1} input:{2} output:{3}.".format(errno, strerror, self.get_inputdir() + '/' + file, self.get_outputfile()) 
 
def fMain():
    """ Main driver, startup and cli options parsing. """
    # Gonna switch this to optparse later
    try:
        options, xarguments = getopt.getopt(sys.argv[1:], 'hi:o:', ['version', 'python'])
    except getopt.error,err:
        print 'Error: ' + str(err)
        sys.exit(1)

    cl = Ih2rem()

    for opt in options[:]:
        if opt[0] == '-h':
            cl.fUsage()
            cl.set_exitstate(1) # don't run the program after the optionparsing
    for opt in options[:]:
        if opt[0] == '-i':
            cl.set_inputdir(opt[1].strip().replace('/',''))
            break
    for opt in options[:]:
        if opt[0] == '-o':
    	    cl.set_outputfile(opt[1].strip())
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

    if(cl.get_exitstate() == 1):
        sys.exit(0)
    else:
        cl.fRun() #run the main method for the program

if __name__ == "__main__":
    fMain()
