#!/usr/env/python
from PyQt4 import QtCore, QtGui
import viewtest
import viewpyqt_dialog_emma

class DialogEmma(QtGui.QDialog):
    def __init__(self, parent=None):
        super(DialogEmma, self).__init__(parent)
        self.ui = viewpyqt_dialog_emma.Ui_DialogEmma()
        self.ui.setupUi(self)
        # use new style signals
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def accept(self):
        super(DialogEmma, self).accept()  # call the accept method of QDialog. 
                                           # super is needed 
                                           # since we just override the accept method

def show_dialog():
    dlg = DialogEmma()
    dlg.exec_()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = viewtest.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_test.clicked.connect(show_dialog)
    MainWindow.show()
    sys.exit(app.exec_())

