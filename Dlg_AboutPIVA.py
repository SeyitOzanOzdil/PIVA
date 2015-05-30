# -*- coding: utf-8 -*-

import sys
import os

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

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(324, 214)
        Dialog.setMaximumSize(QtCore.QSize(324, 214))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pic = QtGui.QLabel(Dialog)
        self.pic.setPixmap(QtGui.QPixmap("resources/amb.png"))
        self.gridLayout.addWidget(self.pic, 0,0,1,1)
        self.txt = QtGui.QLabel(Dialog)
        self.txt.setText("2014-All Rights Reserved "
                         u"\n\nVersion 2.0.0\n\nSeyit Ozan ÖZDİL \nYunus YILDIRIM"
                         "\n\n" + "*-*-*-*-*-*-*-*-*-*-*-*"
                         u"\n\nVersion 1.0.0\n\nDilara OZIRMAK \nSerdar GOKCEN \n")
        self.gridLayout.addWidget(self.txt, 1,0,1,1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "HAKKINDA", None))
