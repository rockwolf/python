# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewpyqt.ui'
#
# Created: Fri May  3 18:35:57 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1198, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem, 0, 7, 1, 1)
        self.lbl_check = QtGui.QLabel(self.centralwidget)
        self.lbl_check.setFrameShape(QtGui.QFrame.Panel)
        self.lbl_check.setFrameShadow(QtGui.QFrame.Raised)
        self.lbl_check.setObjectName(_fromUtf8("lbl_check"))
        self.gridLayout_10.addWidget(self.lbl_check, 0, 5, 1, 1)
        self.cmb_account = QtGui.QComboBox(self.centralwidget)
        self.cmb_account.setInputMethodHints(QtCore.Qt.ImhLowercaseOnly)
        self.cmb_account.setEditable(True)
        self.cmb_account.setObjectName(_fromUtf8("cmb_account"))
        self.gridLayout_10.addWidget(self.cmb_account, 0, 3, 1, 1)
        self.lbl_infofinance = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Envy Code R"))
        self.lbl_infofinance.setFont(font)
        self.lbl_infofinance.setObjectName(_fromUtf8("lbl_infofinance"))
        self.gridLayout_10.addWidget(self.lbl_infofinance, 0, 8, 1, 1)
        self.lbl_account = QtGui.QLabel(self.centralwidget)
        self.lbl_account.setObjectName(_fromUtf8("lbl_account"))
        self.gridLayout_10.addWidget(self.lbl_account, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem1, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_10)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.btn_reset = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Envy Code R"))
        self.btn_reset.setFont(font)
        self.btn_reset.setObjectName(_fromUtf8("btn_reset"))
        self.gridLayout_6.addWidget(self.btn_reset, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 2, 1, 1)
        self.btn_exit = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Envy Code R"))
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.gridLayout_6.addWidget(self.btn_exit, 0, 3, 1, 1)
        self.btn_update = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Envy Code R"))
        self.btn_update.setFont(font)
        self.btn_update.setObjectName(_fromUtf8("btn_update"))
        self.gridLayout_6.addWidget(self.btn_update, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_6)
        self.vl_table = QtGui.QVBoxLayout()
        self.vl_table.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.vl_table.setObjectName(_fromUtf8("vl_table"))
        self.verticalLayout.addLayout(self.vl_table)
        self.verticalLayout.setStretch(3, 1)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_update, self.btn_reset)
        MainWindow.setTabOrder(self.btn_reset, self.btn_exit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lbl_check.setText(_translate("MainWindow", "TextLabel", None))
        self.lbl_infofinance.setText(_translate("MainWindow", "TextLabel", None))
        self.lbl_account.setText(_translate("MainWindow", "Account", None))
        self.btn_reset.setText(_translate("MainWindow", "&Reset", None))
        self.btn_exit.setText(_translate("MainWindow", "&Quit", None))
        self.btn_update.setText(_translate("MainWindow", "&Update", None))

