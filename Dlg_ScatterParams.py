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

class Ui_ScatterParams(object):
    def setupUi(self, ScatterParams):
        ScatterParams.setObjectName(_fromUtf8("ScatterParams"))
        ScatterParams.resize(429, 117)

        self.gridLayout = QtGui.QGridLayout(ScatterParams)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.comboBox = QtGui.QComboBox(ScatterParams)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label = QtGui.QLabel(ScatterParams)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label2 = QtGui.QLabel(ScatterParams)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 1,0,1,1)

        self.comboBox2 = QtGui.QComboBox(ScatterParams)
        self.comboBox2.setObjectName("comboBox2")
        self.gridLayout.addWidget(self.comboBox2, 1,1,1,1)

        self.pushButton = QtGui.QPushButton(ScatterParams)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        self.retranslateUi(ScatterParams)
        QtCore.QMetaObject.connectSlotsByName(ScatterParams)

    def retranslateUi(self, ScatterParams):
        ScatterParams.setWindowTitle(_translate("ScatterParams", "Dialog", None))
        self.label.setText(_translate("ScatterParams", "1.Ozellik:", None))
        self.pushButton.setText(_translate("ScatterParams", "GOSTER", None))
        self.label2.setText(_translate("ScatterParams", "2.Ozellik:", None))
