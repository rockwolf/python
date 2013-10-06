#!/usr/bin/env python
"""
    Tutorial from youtube.
"""

from PyQt4 import QtGui, QtCore, uic
import sys

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanLooks")

    # DATA
    data = ["one", "two", "three", "four", "five"]

    # LISTWIDGET
    #listWidget = QtGui.QListWidget()
    #listWidget.show()
    #listWidget.addItems(data)

    #count = listWidget.count()
    #for i in range(count):
    #    item = listWidget.item(i)
    #    item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
   
    ## COMBOBOX
    #comboBox = QtGui.QComboBox()
    #comboBox.show()
    #comboBox.addItems(data)

    # LISTVIEW
    model = QtGui.QStringListModel(data)

    listView = QtGui.QListView()
    listView.show()
    listView.setModel(model)
    
    listView2 = QtGui.QListView()
    listView2.show()
    listView2.setModel(model)
    
    # COMBOBOX
    combobox = QtGui.QComboBox()
    combobox.setModel(model)
    combobox.show()

    sys.exit(app.exec_())
