#/usr/bin/env python
from PyQt4 import QtCore, QtGui, uic
import sys

class TableModelLisa(QtCore.QAbstractTableModel): 
    """ Table model for lisa """

    def __init__(self, data = [[]], headers = [], parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.__data = data 
        self.__headers = headers
   
    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section < len(self.__headers):
                    return self.__headers[section]
                else:
                    return "TEMP"
            else:
                return "{}".format(section)

    def rowCount(self, parent):
        return len(self.__data)

    def columnCount(self, parent):
        return len(self.__data[0])

    def data(self, index, role):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            return self.__data[row][column].name()
        if role == QtCore.Qt.ToolTipRole:
            row = index.row()
            column = index.column()
            return "data: " + self.__data[row][column].name()
        #if role == QtCore.Qt.DecorationRole:
        #        row = index.row()
        #        column = index.column()
        #        value = self.__data[row][column]
        #        pixmap = QtGui.QPixmap(26, 26)
        #        pixmap.fill(value)
        #        icon = QtGui.QIcon(pixmap)
        #        return icon
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.__data[row][column]
            return value.name()
   
    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role = QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            if value.isValid():
                self.__data[row][column] = value
                self.dataChanged.emit(index, index)
                return True
        return False
    
    def insertRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginInsertRows(QtCore.QModelIndex(), position, position + rows - 1)
        for i in range(rows):
            defaultValues = ["" for i in range(self.columnCount(None))]
            self.__data.insert(position, defaultValues)
        self.endInsertRows()
        return True

    def insertColumns(self, position, columns, values = [], parent = QtCore.QModelIndex()):
        self.beginInsertColumns(QtCore.QModelIndex(), position, position + columns - 1)
        row_count = len(self.__data)
        for i in range(columns):
            for j in range(row_count):
                self.__data[j].insert(position, values[j])
        self.endInsertColumns()
        return True

    def removeRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginRemoveRows(QtCore.QModelIndex(), position, position + rows - 1)
        for i in range(rows):
            value = self.__data[position]
            self.__data.remove(value)
        self.endRemoveRows()
