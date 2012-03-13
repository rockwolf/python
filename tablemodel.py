#/usr/env/python
from PyQt4.QtGui import QTableWidget, QTableWidgetItem
from PyQt4 import QtCore, QtGui

class TableModel(QTableWidget): 
    """ Model for a table. """

    def __init__(self, header, data, *args):
        """ Initialize the table. """
        QTableWidget.__init__(self, *args)
        self.header = header 
        self.tablecontent = data
        self.setHorizontalHeaderLabels(header)
        self.initialize_data(data)
       
    def display_data(self):
        """ Display the data as a 2D list and format + display it in the table """
        nrows = len(self.tablecontent)
        ncols = len(self.tablecontent[0])
        self.setRowCount(nrows)
        self.setColumnCount(ncols)
        self.setHorizontalHeaderLabels(self.header)
        rows = self.tablecontent
        print(rows)
        for row in range(len(rows)):
            cols = self.list_to_qtablewidgetitems(rows[row])
            for col in range(len(cols)):
                print(cols[col])
                self.setItem(row, col, cols[col])
            self.setRowHeight(row, 18)

            # set col width first time through
            if row == 0:
                self.resizeColumnsToContents()
                #self.setColumnWidth(4,250)

        # format col width
        self.resizeColumnsToContents()
        #self.setColumnWidth(4,250)

    def initialize_data(self, data):
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

    def list_to_qtablewidgetitems(self, list):
        """ transforms a list in a collection of QTableWidgetItems """
        table_items = []
        for i in range(len(list)):
            table_item = QTableWidgetItem(list[i])
            table_items.append(table_item)
            return table_items

    def add_row(self, data):
        """ insert new row """
        for item in data:
            newitem = QTableWidgetItem(item)
            self.setItem(len(self.tablecontent)+1, len(data), newitem)

    def delete_row(self, data):
        """ delete the last row """
        self.delete_row(data, len(data))

    def delete_row(self, data, index):
        """ delete a row """
        print('TBD')
