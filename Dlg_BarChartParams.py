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

class Ui_BarChartParams(object):
    def setupUi(self, BarChartParams):
        BarChartParams.setObjectName(_fromUtf8("BarChartParams"))
        BarChartParams.resize(429, 134)
        self.gridLayout = QtGui.QGridLayout(BarChartParams)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox = QtGui.QComboBox(BarChartParams)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.label = QtGui.QLabel(BarChartParams)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(BarChartParams)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)
        self.label_2 = QtGui.QLabel(BarChartParams)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(BarChartParams)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(BarChartParams)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(BarChartParams)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)

        self.retranslateUi(BarChartParams)
        QtCore.QMetaObject.connectSlotsByName(BarChartParams)

    def retranslateUi(self, BarChartParams):
        BarChartParams.setWindowTitle(_translate("BarChartParams", "Dialog", None))
        self.label.setText(_translate("BarChartParams", " Ozellik:", None))
        self.pushButton.setText(_translate("BarChartParams", "GOSTER", None))
        self.label_2.setText(_translate("BarChartParams", "Standart Sapma:", None))
        self.label_3.setText(_translate("BarChartParams", "Bar Kalinligi (Width):", None))

    def GetChoosenFeature(self):

        choosen = self.comboBox.currentText()

        return choosen

    def SetComboBox(self, features):

        self.comboBox.addItems(features)

    def ClearComboBox(self):
        
        self.comboBox.clear()