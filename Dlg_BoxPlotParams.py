# -*- coding: utf-8 -*-

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

class Ui_BoxPlot(object):
        
    eklenenler = list()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(428, 126)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_Ekle = QtGui.QPushButton(Dialog)
        self.pushButton_Ekle.setObjectName(_fromUtf8("pushButton_Ekle"))
        self.gridLayout_2.addWidget(self.pushButton_Ekle, 2, 0, 1, 1)
        self.pushButton_hepsiniEkle = QtGui.QPushButton(Dialog)
        self.pushButton_hepsiniEkle.setObjectName(_fromUtf8("pushButton_hepsiniEkle"))
        self.gridLayout_2.addWidget(self.pushButton_hepsiniEkle, 3, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_Goster = QtGui.QPushButton(Dialog)
        self.pushButton_Goster.setObjectName(_fromUtf8("pushButton_Goster"))
        self.gridLayout.addWidget(self.pushButton_Goster, 1, 0, 1, 1)
        self.pushButton_Temizle = QtGui.QPushButton(Dialog)
        self.pushButton_Temizle.setObjectName(_fromUtf8("pushButton_Temizle"))
        self.gridLayout.addWidget(self.pushButton_Temizle, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton_Ekle.setText(_translate("Dialog", "EKLE", None))
        self.pushButton_hepsiniEkle.setText(_translate("Dialog", "HEPSINI EKLE", None))
        self.label.setText(_translate("Dialog", "Ozellikler:", None))
        self.pushButton_Goster.setText(_translate("Dialog", "GOSTER", None))
        self.pushButton_Temizle.setText(_translate("Dialog", "TEMIZLE", None))

    def GetChoosenFeature(self):

        choosen = self.comboBox.currentText()
        
        return choosen

    def SetComboBox(self, features):

        self.comboBox.addItems(features)

    def ClearComboBox(self):
        
        self.comboBox.clear()

    def ClearTextEdit(self):

        self.textEdit.clear()
