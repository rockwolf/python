# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewpyqt_dialog_emma.ui'
#
# Created: Sat Sep 28 17:43:12 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_DialogEmma(object):
    def setupUi(self, DialogEmma):
        DialogEmma.setObjectName(_fromUtf8("DialogEmma"))
        DialogEmma.resize(1196, 565)
        self.verticalLayout = QtGui.QVBoxLayout(DialogEmma)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.txt_general = QtGui.QTextEdit(DialogEmma)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.txt_general.setFont(font)
        self.txt_general.setFrameShadow(QtGui.QFrame.Raised)
        self.txt_general.setReadOnly(True)
        self.txt_general.setObjectName(_fromUtf8("txt_general"))
        self.gridLayout.addWidget(self.txt_general, 1, 0, 1, 1)
        self.lbl_general = QtGui.QLabel(DialogEmma)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_general.setFont(font)
        self.lbl_general.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_general.setObjectName(_fromUtf8("lbl_general"))
        self.gridLayout.addWidget(self.lbl_general, 0, 0, 1, 1)
        self.txt_sell = QtGui.QTextEdit(DialogEmma)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.txt_sell.setFont(font)
        self.txt_sell.setFrameShadow(QtGui.QFrame.Raised)
        self.txt_sell.setReadOnly(True)
        self.txt_sell.setObjectName(_fromUtf8("txt_sell"))
        self.gridLayout.addWidget(self.txt_sell, 5, 0, 1, 1)
        self.txt_buy = QtGui.QTextEdit(DialogEmma)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.txt_buy.setFont(font)
        self.txt_buy.setFrameShadow(QtGui.QFrame.Raised)
        self.txt_buy.setReadOnly(True)
        self.txt_buy.setObjectName(_fromUtf8("txt_buy"))
        self.gridLayout.addWidget(self.txt_buy, 3, 0, 1, 1)
        self.lbl_buy = QtGui.QLabel(DialogEmma)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_buy.setFont(font)
        self.lbl_buy.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_buy.setObjectName(_fromUtf8("lbl_buy"))
        self.gridLayout.addWidget(self.lbl_buy, 2, 0, 1, 1)
        self.lbl_sell = QtGui.QLabel(DialogEmma)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_sell.setFont(font)
        self.lbl_sell.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sell.setObjectName(_fromUtf8("lbl_sell"))
        self.gridLayout.addWidget(self.lbl_sell, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(DialogEmma)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogEmma)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogEmma.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogEmma.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), DialogEmma.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogEmma)

    def retranslateUi(self, DialogEmma):
        DialogEmma.setWindowTitle(_translate("DialogEmma", "Dialog", None))
        self.lbl_general.setText(_translate("DialogEmma", "General", None))
        self.lbl_buy.setText(_translate("DialogEmma", "Buy", None))
        self.lbl_sell.setText(_translate("DialogEmma", "Sell", None))

