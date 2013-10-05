# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/viewpyqt_dialog_parameters.ui'
#
# Created: Sat Oct  5 08:14:16 2013
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

class Ui_DialogParameters(object):
    def setupUi(self, DialogParameters):
        DialogParameters.setObjectName(_fromUtf8("DialogParameters"))
        DialogParameters.resize(858, 758)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        DialogParameters.setFont(font)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DialogParameters)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.vl_parameters = QtGui.QVBoxLayout()
        self.vl_parameters.setObjectName(_fromUtf8("vl_parameters"))
        self.verticalLayout_2.addLayout(self.vl_parameters)
        self.buttonBox = QtGui.QDialogButtonBox(DialogParameters)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(DialogParameters)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogParameters.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogParameters.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogParameters)

    def retranslateUi(self, DialogParameters):
        DialogParameters.setWindowTitle(_translate("DialogParameters", "DialogParameters", None))

