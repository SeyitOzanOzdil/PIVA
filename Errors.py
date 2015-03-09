
from PyQt4 import QtCore, QtGui


def ShowInfoMsgBox(self, infoMsg):

    QtGui.QMessageBox.information(self, "Information", infoMsg, QtGui.QMessageBox.Ok)

def ShowWarningMsgBox(self, warnMsg):

    QtGui.QMessageBox.warning(self, "Warning", warnMsg, QtGui.QMessageBox.Ok)


