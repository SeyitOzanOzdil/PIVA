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

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 147, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.checkBox_2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(100, 50, 71, 18))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))

        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 78, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(100, 80, 81, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))   
             
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(20, 50, 71, 18))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(190, 80, 91, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(180, 50, 91, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 261, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.checkBox_3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 130, 71, 18))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))

        self.checkBox_4 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(100, 130, 71, 18))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))

        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(190, 130, 91, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.checkBox.setChecked(True)
        self.checkBox_4.setChecked(True)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)

        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("clicked()"), self.CheckStates)
        QtCore.QObject.connect(self.checkBox_2, QtCore.SIGNAL("clicked()"), self.CheckStates2)

        QtCore.QObject.connect(self.checkBox_3, QtCore.SIGNAL("clicked()"), self.CheckStates3)
        QtCore.QObject.connect(self.checkBox_4, QtCore.SIGNAL("clicked()"), self.CheckStates4)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dataset Ac", None))
        self.groupBox.setTitle(_translate("Dialog", "Dataset Okuma Parametreleri", None))
        self.label.setText(_translate("Dialog", "Ozellik(Feature) isimleri var mi?", None))
        self.checkBox_2.setText(_translate("Dialog", "Yok", None))
        self.label_2.setText(_translate("Dialog", "Ayirici karakter :", None))
        self.checkBox.setText(_translate("Dialog", "Var", None))
        self.label_3.setText(_translate("Dialog", "(Default: 1 bosluk)", None))
        self.label_4.setText(_translate("Dialog", "(Default: Var)", None))
        self.label_5.setText(_translate("Dialog", "Eksik ya da silinmis verilere sahip ornekler silinsin mi?", None))
        self.checkBox_3.setText(_translate("Dialog", "Evet", None))
        self.checkBox_4.setText(_translate("Dialog", "Hayir", None))
        self.label_6.setText(_translate("Dialog", "(Default: Hayir)", None))

    def GetValues(self):
        
        #Default Values
        hasFeatureLine = True
        seperator = " "
        deleteBadData = False

        if ((not self.checkBox.isChecked()) and self.checkBox_2.isChecked()):
            hasFeatureLine = False

        if self.lineEdit.text() is not None:
            seperator = self.lineEdit.text()

        if self.checkBox_3.isChecked() and ( not self.checkBox_4.isChecked()):
            deleteBadData = True

        return hasFeatureLine, seperator, deleteBadData

    def CheckStates(self):

        if self.checkBox.isChecked():

            self.checkBox_2.setChecked(False)

    def CheckStates2(self):

        if self.checkBox_2.isChecked():

            self.checkBox.setChecked(False)

    def CheckStates3(self):

        if self.checkBox_3.isChecked():

            self.checkBox_4.setChecked(False)

    def CheckStates4(self):

        if self.checkBox_4.isChecked():

            self.checkBox_3.setChecked(False)

