# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tj.ui'
#
# Created: Sun Mar 11 18:04:33 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1440, 900)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1441, 891))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_update = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_update.setObjectName(_fromUtf8("btn_update"))
        self.horizontalLayout.addWidget(self.btn_update)
        self.cmb_view = QtGui.QComboBox(self.verticalLayoutWidget)
        self.cmb_view.setMinimumSize(QtCore.QSize(200, 0))
        self.cmb_view.setObjectName(_fromUtf8("cmb_view"))
        self.horizontalLayout.addWidget(self.cmb_view)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_exit = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.horizontalLayout.addWidget(self.btn_exit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tblJournal = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.tblJournal.setStyleSheet(_fromUtf8("background: transparent;\n"
"color: inherit;"))
        self.tblJournal.setFrameShape(QtGui.QFrame.NoFrame)
        self.tblJournal.setFrameShadow(QtGui.QFrame.Plain)
        self.tblJournal.setAlternatingRowColors(True)
        self.tblJournal.setObjectName(_fromUtf8("tblJournal"))
        self.tblJournal.setColumnCount(0)
        self.tblJournal.setRowCount(0)
        self.verticalLayout.addWidget(self.tblJournal)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_update.setText(QtGui.QApplication.translate("Dialog", "&Update", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_exit.setText(QtGui.QApplication.translate("Dialog", "&Quit", None, QtGui.QApplication.UnicodeUTF8))

