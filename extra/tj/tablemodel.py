#/usr/env/python
from PyQt4.QtGui import QTableWidget, QTableWidgetItem
from PyQt4 import QtCore, QtGui

class TableModel(QTableWidget): 
    """ Model for a table. """

    def __init__(self, header, data, *args):
        """ Initialize the table. """
        QTableWidget.__init__(self, *args)
        self.header = header 
        self.setHorizontalHeaderLabels(header)
        self.setmydata(data)
        
    def setmydata(self, data):
        """ set data for the table. """
        n = 0
        m = 0
        for key in data:
            m = 0
            for item in data[data.index(key)]:
                newitem = QTableWidgetItem(item)
                self.setItem(n, m, newitem)
                m += 1
            n+=1
