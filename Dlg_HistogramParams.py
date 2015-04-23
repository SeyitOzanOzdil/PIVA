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

class Ui_HistogramParams(object):
    def setupUi(self, HistogramParams):
        HistogramParams.setObjectName(_fromUtf8("HistogramParams"))
        HistogramParams.resize(429, 117)

        self.gridLayout = QtGui.QGridLayout(HistogramParams)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.comboBox = QtGui.QComboBox(HistogramParams)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label = QtGui.QLabel(HistogramParams)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QtGui.QLabel(HistogramParams)
        self.label_2.setObjectName("label2")
        self.gridLayout.addWidget(self.label_2, 1,0,1,1)

        self.lineEdit = QtGui.QLineEdit(HistogramParams)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1,1,1,1)

        self.pushButton = QtGui.QPushButton(HistogramParams)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        self.retranslateUi(HistogramParams)
        QtCore.QMetaObject.connectSlotsByName(HistogramParams)

    def retranslateUi(self, HistogramParams):
        HistogramParams.setWindowTitle(_translate("HistogramParams", "Dialog", None))
        self.label.setText(_translate("HistogramParams", u" Özellik:", None))
        self.pushButton.setText(_translate("HistogramParams", u"GÖSTER", None))
        self.label_2.setText(_translate("HistogramParams", u"Bin Sayısı:", None))


    def GetChoosenFeature(self):

        choosen = self.comboBox.currentText()

        return choosen

    def SetComboBox(self, features):

        self.comboBox.addItems(features)

    def ClearComboBox(self):
        
        self.comboBox.clear() 

    def GetBinCount(self):

        binCount = self.lineEdit.text()

        return int(binCount)