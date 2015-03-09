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

class Ui_PieChartParams(object):
    def setupUi(self, PieChartParams):
        PieChartParams.setObjectName(_fromUtf8("PieChartParams"))
        PieChartParams.resize(429, 117)
        self.gridLayout = QtGui.QGridLayout(PieChartParams)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox = QtGui.QComboBox(PieChartParams)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label = QtGui.QLabel(PieChartParams)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(PieChartParams)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.retranslateUi(PieChartParams)
        QtCore.QMetaObject.connectSlotsByName(PieChartParams)

    def retranslateUi(self, PieChartParams):
        PieChartParams.setWindowTitle(_translate("PieChartParams", "Dialog", None))
        self.label.setText(_translate("PieChartParams", " Ozellik:", None))
        self.pushButton.setText(_translate("PieChartParams", "GOSTER", None))


    def GetChoosenFeature(self):

        choosen = self.comboBox.currentText()

        return choosen
    def SetComboBox(self, features):

        self.comboBox.addItems(features)

    def ClearComboBox(self):
        
        self.comboBox.clear() 