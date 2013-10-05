# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/viewpyqt.ui'
#
# Created: Sat Oct  5 10:25:22 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1198, 600)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(_fromUtf8("#MainWindow\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_check\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_infofinance\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_date\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_account\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_amount\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_marketcode\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_commodity_name\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_quantity\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_price\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_commission\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_tax\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_comment\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_currency_from\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_currency_to\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_exchange_rate\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_expiration\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_pool\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#chk_manual_commission\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_risk\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#lbl_infodetails\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#chk_long\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#btn_emma\n"
"{\n"
"    background: #b58900;\n"
"    color: #fdf6e3;\n"
"}\n"
"#btn_gnucash\n"
"{\n"
"    background: #b58900;\n"
"    color: #fdf6e3;\n"
"}\n"
"#btn_parameters\n"
"{\n"
"    background: #b58900;\n"
"    color: #fdf6e3;\n"
"}\n"
"#btn_add\n"
"{\n"
"    background: #586e75;\n"
"    color: #fdf6e3;\n"
"}\n"
"#btn_update\n"
"{\n"
"    background: #586e75;\n"
"    color: #fdf6e3;\n"
"}\n"
"#btn_remove\n"
"{\n"
"    background: #586e75;\n"
"    color: #fdf6e3;\n"
"}\n"
"#btn_removelast\n"
"{\n"
"    background: #586e75;\n"
"    color: #fdf6e3;\n"
"}\n"
"#btn_clear\n"
"{\n"
"    background: #586e75;\n"
"    color: #fdf6e3;\n"
"}\n"
"#btn_execute\n"
"{\n"
"    background: #cb4b16;\n"
"    color: #fdf6e3;\n"
"}\n"
"#btn_exit\n"
"{\n"
"    background: #ffffd7;\n"
"    color: #626262;\n"
"}\n"
"#cmb_account_to\n"
"{\n"
"    background: #ffffff;\n"
"    color: #626262;\n"
"}\n"
"#btn_account_from\n"
"{\n"
"    background: #ffffdd;\n"
"    color: #626262;\n"
"}\n"
"*\n"
"{\n"
"    color: #626262;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.centralwidget.setFont(font)
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
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_check.setFont(font)
        self.lbl_check.setFrameShape(QtGui.QFrame.Panel)
        self.lbl_check.setFrameShadow(QtGui.QFrame.Raised)
        self.lbl_check.setObjectName(_fromUtf8("lbl_check"))
        self.gridLayout_10.addWidget(self.lbl_check, 0, 5, 1, 1)
        self.lbl_infofinance = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_infofinance.setFont(font)
        self.lbl_infofinance.setObjectName(_fromUtf8("lbl_infofinance"))
        self.gridLayout_10.addWidget(self.lbl_infofinance, 0, 8, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem1, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_10)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.spn_amount = QtGui.QDoubleSpinBox(self.centralwidget)
        self.spn_amount.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.spn_amount.setFont(font)
        self.spn_amount.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.spn_amount.setDecimals(6)
        self.spn_amount.setMaximum(999999.999999)
        self.spn_amount.setProperty("value", 0.0)
        self.spn_amount.setObjectName(_fromUtf8("spn_amount"))
        self.gridLayout.addWidget(self.spn_amount, 1, 2, 1, 1)
        self.spn_price = QtGui.QDoubleSpinBox(self.centralwidget)
        self.spn_price.setMinimumSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.spn_price.setFont(font)
        self.spn_price.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.spn_price.setDecimals(6)
        self.spn_price.setMaximum(999999.999999)
        self.spn_price.setObjectName(_fromUtf8("spn_price"))
        self.gridLayout.addWidget(self.spn_price, 1, 8, 1, 1)
        self.lbl_date = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_date.setFont(font)
        self.lbl_date.setObjectName(_fromUtf8("lbl_date"))
        self.gridLayout.addWidget(self.lbl_date, 0, 0, 1, 1)
        self.lbl_marketcode = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_marketcode.setFont(font)
        self.lbl_marketcode.setObjectName(_fromUtf8("lbl_marketcode"))
        self.gridLayout.addWidget(self.lbl_marketcode, 0, 5, 1, 1)
        self.lbl_commodity_name = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_commodity_name.setFont(font)
        self.lbl_commodity_name.setObjectName(_fromUtf8("lbl_commodity_name"))
        self.gridLayout.addWidget(self.lbl_commodity_name, 0, 6, 1, 1)
        self.lbl_quantity = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_quantity.setFont(font)
        self.lbl_quantity.setObjectName(_fromUtf8("lbl_quantity"))
        self.gridLayout.addWidget(self.lbl_quantity, 0, 7, 1, 1)
        self.lbl_price = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_price.setFont(font)
        self.lbl_price.setObjectName(_fromUtf8("lbl_price"))
        self.gridLayout.addWidget(self.lbl_price, 0, 8, 1, 1)
        self.lbl_commission = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_commission.setFont(font)
        self.lbl_commission.setObjectName(_fromUtf8("lbl_commission"))
        self.gridLayout.addWidget(self.lbl_commission, 0, 9, 1, 1)
        self.lbl_tax = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_tax.setFont(font)
        self.lbl_tax.setObjectName(_fromUtf8("lbl_tax"))
        self.gridLayout.addWidget(self.lbl_tax, 0, 10, 1, 1)
        self.spn_pool = QtGui.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.spn_pool.setFont(font)
        self.spn_pool.setDecimals(6)
        self.spn_pool.setMaximum(999999.999999)
        self.spn_pool.setObjectName(_fromUtf8("spn_pool"))
        self.gridLayout.addWidget(self.spn_pool, 5, 8, 1, 1)
        self.lbl_pool = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_pool.setFont(font)
        self.lbl_pool.setObjectName(_fromUtf8("lbl_pool"))
        self.gridLayout.addWidget(self.lbl_pool, 4, 8, 1, 1)
        self.dt_date = QtGui.QDateEdit(self.centralwidget)
        self.dt_date.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.dt_date.setFont(font)
        self.dt_date.setDate(QtCore.QDate(1900, 1, 1))
        self.dt_date.setCalendarPopup(True)
        self.dt_date.setObjectName(_fromUtf8("dt_date"))
        self.gridLayout.addWidget(self.dt_date, 1, 0, 1, 1)
        self.cmb_market_code = QtGui.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.cmb_market_code.setFont(font)
        self.cmb_market_code.setInputMethodHints(QtCore.Qt.ImhLowercaseOnly)
        self.cmb_market_code.setEditable(False)
        self.cmb_market_code.setObjectName(_fromUtf8("cmb_market_code"))
        self.gridLayout.addWidget(self.cmb_market_code, 1, 5, 1, 1)
        self.cmb_commodity_name = QtGui.QComboBox(self.centralwidget)
        self.cmb_commodity_name.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.cmb_commodity_name.setFont(font)
        self.cmb_commodity_name.setInputMethodHints(QtCore.Qt.ImhLowercaseOnly)
        self.cmb_commodity_name.setEditable(False)
        self.cmb_commodity_name.setObjectName(_fromUtf8("cmb_commodity_name"))
        self.gridLayout.addWidget(self.cmb_commodity_name, 1, 6, 1, 1)
        self.spn_quantity = QtGui.QSpinBox(self.centralwidget)
        self.spn_quantity.setMinimumSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.spn_quantity.setFont(font)
        self.spn_quantity.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.spn_quantity.setMaximum(999999)
        self.spn_quantity.setObjectName(_fromUtf8("spn_quantity"))
        self.gridLayout.addWidget(self.spn_quantity, 1, 7, 1, 1)
        self.spn_commission = QtGui.QDoubleSpinBox(self.centralwidget)
        self.spn_commission.setMinimumSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.spn_commission.setFont(font)
        self.spn_commission.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.spn_commission.setDecimals(6)
        self.spn_commission.setMaximum(999999.999999)
        self.spn_commission.setObjectName(_fromUtf8("spn_commission"))
        self.gridLayout.addWidget(self.spn_commission, 1, 9, 1, 1)
        self.spn_tax = QtGui.QDoubleSpinBox(self.centralwidget)
        self.spn_tax.setMinimumSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.spn_tax.setFont(font)
        self.spn_tax.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.spn_tax.setDecimals(6)
        self.spn_tax.setMaximum(999999.999999)
        self.spn_tax.setObjectName(_fromUtf8("spn_tax"))
        self.gridLayout.addWidget(self.spn_tax, 1, 10, 1, 1)
        self.txt_market_description = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.txt_market_description.setFont(font)
        self.txt_market_description.setReadOnly(True)
        self.txt_market_description.setObjectName(_fromUtf8("txt_market_description"))
        self.gridLayout.addWidget(self.txt_market_description, 3, 5, 1, 1)
        self.txt_commodity_description = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.txt_commodity_description.setFont(font)
        self.txt_commodity_description.setReadOnly(True)
        self.txt_commodity_description.setObjectName(_fromUtf8("txt_commodity_description"))
        self.gridLayout.addWidget(self.txt_commodity_description, 3, 6, 1, 1)
        self.cmb_account_from = QtGui.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.cmb_account_from.setFont(font)
        self.cmb_account_from.setInputMethodHints(QtCore.Qt.ImhPreferLowercase)
        self.cmb_account_from.setEditable(True)
        self.cmb_account_from.setObjectName(_fromUtf8("cmb_account_from"))
        self.gridLayout.addWidget(self.cmb_account_from, 1, 1, 1, 1)
        self.lbl_amount = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_amount.setFont(font)
        self.lbl_amount.setObjectName(_fromUtf8("lbl_amount"))
        self.gridLayout.addWidget(self.lbl_amount, 0, 2, 1, 1)
        self.lbl_account = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_account.setFont(font)
        self.lbl_account.setObjectName(_fromUtf8("lbl_account"))
        self.gridLayout.addWidget(self.lbl_account, 0, 1, 1, 1)
        self.lbl_currency_from = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_currency_from.setFont(font)
        self.lbl_currency_from.setObjectName(_fromUtf8("lbl_currency_from"))
        self.gridLayout.addWidget(self.lbl_currency_from, 4, 2, 1, 1)
        self.cmb_currency_from = QtGui.QComboBox(self.centralwidget)
        self.cmb_currency_from.setMinimumSize(QtCore.QSize(90, 0))
        self.cmb_currency_from.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.cmb_currency_from.setFont(font)
        self.cmb_currency_from.setObjectName(_fromUtf8("cmb_currency_from"))
        self.gridLayout.addWidget(self.cmb_currency_from, 5, 2, 1, 1)
        self.spn_risk = QtGui.QDoubleSpinBox(self.centralwidget)
        self.spn_risk.setMinimumSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.spn_risk.setFont(font)
        self.spn_risk.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.spn_risk.setDecimals(6)
        self.spn_risk.setMaximum(999999.999999)
        self.spn_risk.setObjectName(_fromUtf8("spn_risk"))
        self.gridLayout.addWidget(self.spn_risk, 5, 9, 1, 1)
        self.lbl_risk = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_risk.setFont(font)
        self.lbl_risk.setObjectName(_fromUtf8("lbl_risk"))
        self.gridLayout.addWidget(self.lbl_risk, 4, 9, 1, 1)
        self.lbl_expiration = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_expiration.setFont(font)
        self.lbl_expiration.setFrameShape(QtGui.QFrame.NoFrame)
        self.lbl_expiration.setObjectName(_fromUtf8("lbl_expiration"))
        self.gridLayout.addWidget(self.lbl_expiration, 4, 7, 1, 1)
        self.dt_expiration = QtGui.QDateEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.dt_expiration.setFont(font)
        self.dt_expiration.setDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dt_expiration.setDate(QtCore.QDate(1900, 1, 1))
        self.dt_expiration.setCalendarPopup(True)
        self.dt_expiration.setObjectName(_fromUtf8("dt_expiration"))
        self.gridLayout.addWidget(self.dt_expiration, 5, 7, 1, 1)
        self.lbl_exchange_rate = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_exchange_rate.setFont(font)
        self.lbl_exchange_rate.setObjectName(_fromUtf8("lbl_exchange_rate"))
        self.gridLayout.addWidget(self.lbl_exchange_rate, 4, 6, 1, 1)
        self.spn_exchange_rate = QtGui.QDoubleSpinBox(self.centralwidget)
        self.spn_exchange_rate.setMinimumSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.spn_exchange_rate.setFont(font)
        self.spn_exchange_rate.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.spn_exchange_rate.setDecimals(6)
        self.spn_exchange_rate.setMaximum(999999.999999)
        self.spn_exchange_rate.setObjectName(_fromUtf8("spn_exchange_rate"))
        self.gridLayout.addWidget(self.spn_exchange_rate, 5, 6, 1, 1)
        self.lbl_currency_to = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_currency_to.setFont(font)
        self.lbl_currency_to.setObjectName(_fromUtf8("lbl_currency_to"))
        self.gridLayout.addWidget(self.lbl_currency_to, 4, 5, 1, 1)
        self.cmb_currency_to = QtGui.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.cmb_currency_to.setFont(font)
        self.cmb_currency_to.setObjectName(_fromUtf8("cmb_currency_to"))
        self.gridLayout.addWidget(self.cmb_currency_to, 5, 5, 1, 1)
        self.txt_comment = QtGui.QLineEdit(self.centralwidget)
        self.txt_comment.setEnabled(True)
        self.txt_comment.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.txt_comment.setFont(font)
        self.txt_comment.setObjectName(_fromUtf8("txt_comment"))
        self.gridLayout.addWidget(self.txt_comment, 5, 1, 1, 1)
        self.lbl_comment = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_comment.setFont(font)
        self.lbl_comment.setObjectName(_fromUtf8("lbl_comment"))
        self.gridLayout.addWidget(self.lbl_comment, 4, 1, 1, 1)
        self.cmb_account_to = QtGui.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.cmb_account_to.setFont(font)
        self.cmb_account_to.setInputMethodHints(QtCore.Qt.ImhLowercaseOnly)
        self.cmb_account_to.setEditable(True)
        self.cmb_account_to.setObjectName(_fromUtf8("cmb_account_to"))
        self.gridLayout.addWidget(self.cmb_account_to, 3, 1, 1, 1)
        self.chk_manual_commission = QtGui.QCheckBox(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(98, 98, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 98, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 98, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 98, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 98, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 98, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 98, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 98, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 98, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.chk_manual_commission.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.chk_manual_commission.setFont(font)
        self.chk_manual_commission.setChecked(False)
        self.chk_manual_commission.setObjectName(_fromUtf8("chk_manual_commission"))
        self.gridLayout.addWidget(self.chk_manual_commission, 3, 8, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.btn_clear = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName(_fromUtf8("btn_clear"))
        self.gridLayout_6.addWidget(self.btn_clear, 1, 7, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 1, 12, 1, 1)
        self.btn_exit = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.gridLayout_6.addWidget(self.btn_exit, 1, 15, 1, 1)
        self.btn_add = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.gridLayout_6.addWidget(self.btn_add, 1, 3, 1, 1)
        self.btn_execute = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.btn_execute.setFont(font)
        self.btn_execute.setObjectName(_fromUtf8("btn_execute"))
        self.gridLayout_6.addWidget(self.btn_execute, 1, 10, 1, 1)
        self.lbl_infodetails = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.lbl_infodetails.setFont(font)
        self.lbl_infodetails.setObjectName(_fromUtf8("lbl_infodetails"))
        self.gridLayout_6.addWidget(self.lbl_infodetails, 1, 13, 1, 1)
        self.btn_update = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.btn_update.setFont(font)
        self.btn_update.setObjectName(_fromUtf8("btn_update"))
        self.gridLayout_6.addWidget(self.btn_update, 1, 4, 1, 1)
        self.btn_remove = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.btn_remove.setFont(font)
        self.btn_remove.setObjectName(_fromUtf8("btn_remove"))
        self.gridLayout_6.addWidget(self.btn_remove, 1, 5, 1, 1)
        self.btn_removelast = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.btn_removelast.setFont(font)
        self.btn_removelast.setObjectName(_fromUtf8("btn_removelast"))
        self.gridLayout_6.addWidget(self.btn_removelast, 1, 6, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 1, 14, 1, 1)
        self.btn_emma = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.btn_emma.setFont(font)
        self.btn_emma.setObjectName(_fromUtf8("btn_emma"))
        self.gridLayout_6.addWidget(self.btn_emma, 1, 0, 1, 1)
        self.btn_gnucash = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.btn_gnucash.setFont(font)
        self.btn_gnucash.setObjectName(_fromUtf8("btn_gnucash"))
        self.gridLayout_6.addWidget(self.btn_gnucash, 1, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 1, 9, 1, 1)
        self.btn_parameters = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Inconsolata"))
        font.setPointSize(14)
        self.btn_parameters.setFont(font)
        self.btn_parameters.setObjectName(_fromUtf8("btn_parameters"))
        self.gridLayout_6.addWidget(self.btn_parameters, 1, 2, 1, 1)
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
        MainWindow.setTabOrder(self.dt_date, self.cmb_market_code)
        MainWindow.setTabOrder(self.cmb_market_code, self.cmb_commodity_name)
        MainWindow.setTabOrder(self.cmb_commodity_name, self.spn_quantity)
        MainWindow.setTabOrder(self.spn_quantity, self.spn_price)
        MainWindow.setTabOrder(self.spn_price, self.spn_commission)
        MainWindow.setTabOrder(self.spn_commission, self.spn_tax)
        MainWindow.setTabOrder(self.spn_tax, self.txt_market_description)
        MainWindow.setTabOrder(self.txt_market_description, self.txt_commodity_description)
        MainWindow.setTabOrder(self.txt_commodity_description, self.btn_add)
        MainWindow.setTabOrder(self.btn_add, self.btn_update)
        MainWindow.setTabOrder(self.btn_update, self.btn_remove)
        MainWindow.setTabOrder(self.btn_remove, self.btn_removelast)
        MainWindow.setTabOrder(self.btn_removelast, self.btn_clear)
        MainWindow.setTabOrder(self.btn_clear, self.btn_execute)
        MainWindow.setTabOrder(self.btn_execute, self.btn_exit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lbl_check.setText(_translate("MainWindow", "TextLabel", None))
        self.lbl_infofinance.setText(_translate("MainWindow", "TextLabel", None))
        self.lbl_date.setText(_translate("MainWindow", "Date", None))
        self.lbl_marketcode.setText(_translate("MainWindow", "Market", None))
        self.lbl_commodity_name.setText(_translate("MainWindow", "Commodity", None))
        self.lbl_quantity.setText(_translate("MainWindow", "Quantity", None))
        self.lbl_price.setText(_translate("MainWindow", "Price", None))
        self.lbl_commission.setText(_translate("MainWindow", "Commission", None))
        self.lbl_tax.setText(_translate("MainWindow", "Tax（％）", None))
        self.lbl_pool.setText(_translate("MainWindow", "Pool", None))
        self.dt_date.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd", None))
        self.lbl_amount.setText(_translate("MainWindow", "Amount", None))
        self.lbl_account.setText(_translate("MainWindow", "Account", None))
        self.lbl_currency_from.setText(_translate("MainWindow", "Currency from", None))
        self.lbl_risk.setText(_translate("MainWindow", "Risk (%)", None))
        self.lbl_expiration.setText(_translate("MainWindow", "Expires on", None))
        self.dt_expiration.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd", None))
        self.lbl_exchange_rate.setText(_translate("MainWindow", "Exchange rate", None))
        self.lbl_currency_to.setText(_translate("MainWindow", "Currency to", None))
        self.lbl_comment.setText(_translate("MainWindow", "Comment", None))
        self.chk_manual_commission.setText(_translate("MainWindow", "Automatic", None))
        self.btn_clear.setText(_translate("MainWindow", "&Clear", None))
        self.btn_exit.setText(_translate("MainWindow", "&Quit", None))
        self.btn_add.setText(_translate("MainWindow", "&Add", None))
        self.btn_execute.setText(_translate("MainWindow", "E&xecute", None))
        self.lbl_infodetails.setText(_translate("MainWindow", "TextLabel", None))
        self.btn_update.setText(_translate("MainWindow", "&Update", None))
        self.btn_remove.setText(_translate("MainWindow", "&Remove", None))
        self.btn_removelast.setText(_translate("MainWindow", "Remove &last", None))
        self.btn_emma.setText(_translate("MainWindow", "&Emma", None))
        self.btn_gnucash.setText(_translate("MainWindow", "&Gnucash", None))
        self.btn_parameters.setText(_translate("MainWindow", "&Parameters", None))

