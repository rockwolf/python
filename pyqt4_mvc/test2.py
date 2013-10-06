#!/usr/bin/env python

from PyQt4 import QtCore, QtGui, uic
import sys

class PaletteTableModel(QtCore.QAbstractTableModel):
    """
        Subclass all abstract models. This is for the TableModel.
    """
    def __init__(self, colors = [[]], headers = [], parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.__colors = colors
        self.__headers = headers
   
    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section < len(self.__headers):
                    return self.__headers[section]
                else:
                    return "TEMP"
            else:
                return "Color {}".format(section)

    def rowCount(self, parent):
        return len(self.__colors)

    def columnCount(self, parent):
        return len(self.__colors[0])

    def data(self, index, role):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            return self.__colors[row][column].name()
        if role == QtCore.Qt.ToolTipRole:
            row = index.row()
            column = index.column()
            return "Hex code: " + self.__colors[row][column].name()
        if role == QtCore.Qt.DecorationRole:
                row = index.row()
                column = index.column()
                value = self.__colors[row][column]
                pixmap = QtGui.QPixmap(26, 26)
                pixmap.fill(value)
                icon = QtGui.QIcon(pixmap)
                return icon
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.__colors[row][column]
            return value.name()
   
    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role = QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            color = QtGui.QColor(value)
            if color.isValid():
                self.__colors[row][column] = color
                self.dataChanged.emit(index, index)
                return True
        return False
    
    def insertRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginInsertRows(QtCore.QModelIndex(), position, position + rows - 1)
        for i in range(rows):
            defaultValues = [QtGui.QColor("#000000") for i in range(self.columnCount(None))]
            self.__colors.insert(position, defaultValues)
        self.endInsertRows()
        return True

    def insertColumns(self, position, columns, parent = QtCore.QModelIndex()):
        self.beginInsertColumns(QtCore.QModelIndex(), position, position + columns - 1)
        row_count = len(self.__colors)
        for i in range(columns):
            for j in range(row_count):
                self.__colors[j].insert(position, QtGui.QColor("#000000"))
        self.endInsertColumns()
        return True
    def removeRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginRemoveRows(QtCore.QModelIndex(), position, position + rows - 1)
        for i in range(rows):
            value = self.__colors[position]
            self.__colors.remove(value)
        self.endRemoveRows()


class PaletteListModel(QtCore.QAbstractListModel):
    """
        Subclass all abstract models. This is for the ListModel.
    """
    def __init__(self, colors = [], parent = None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.__colors = colors

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return "Palette"
            else:
                return "Color {}".format(section)

    def rowCount(self, parent):
        return len(self.__colors)

    def data(self, index, role):
        if role == QtCore.Qt.EditRole:
            return self.__colors[index.row()].name()
        if role == QtCore.Qt.ToolTipRole:
            return "Hex code: " + self.__colors[index.row()].name()
        if role == QtCore.Qt.DecorationRole:
                row = index.row()
                value = self.__colors[row]
                pixmap = QtGui.QPixmap(26, 26)
                pixmap.fill(value)
                icon = QtGui.QIcon(pixmap)
                return icon
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value = self.__colors[row]
            return value.name()

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role = QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            color = QtGui.QColor(value)
            if color.isValid():
                self.__colors[row] = color
                self.dataChanged.emit(index, index)
                return True
        return False

    def insertRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginInsertRows(QtCore.QModelIndex(), position, position + rows - 1)
        for i in range(rows):
            self.__colors.insert(position, QtGui.QColor("#000000"))
        self.endInsertRows()
        return True

    def removeRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginRemoveRows(QtCore.QModelIndex(), position, position + rows - 1)
        for i in range(rows):
            value = self.__colors[position]
            self.__colors.remove(value)
        self.endRemoveRows()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanLooks")

    # VIEWS
    listView = QtGui.QListView()
    listView.show()
   
    # commented out, because it doesn't work with the tableViewModel
    #treeView = QtGui.QTreeView()
    #treeView.show()

    comboBox = QtGui.QComboBox()
    comboBox.show()

    tableView = QtGui.QTableView()
    tableView.show()


    # COLORS
    red = QtGui.QColor(255, 0, 0)
    green = QtGui.QColor(0, 255, 0)
    blue = QtGui.QColor(0, 0, 255)
    
    # TABLE DATA
    rowcount = 4
    columncount = 6
    headers = ["Pallet0", "Colors", "Brushes", "Omg", "Technical", "Artist"]
    tableData0 = [[QtGui.QColor("#00ffff") for i in range(columncount)] for j in range(rowcount)] 
    # MODEL
    #model = PaletteListModel([red, green, blue])
    model = PaletteTableModel(tableData0, headers)

    listView.setModel(model)
    #treeView.setModel(model)
    comboBox.setModel(model)
    tableView.setModel(model)


    # TEST INSERT/REMOVE
    model.insertRows(2, 5)
    model.insertColumns(2, 5)
    #model.removeRows(2, 5)
    # RUN
    sys.exit(app.exec_())
