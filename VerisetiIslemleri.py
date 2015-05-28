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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setFixedSize(384, 156)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 0, 271, 161))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnSatirEkle = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnSatirEkle.setObjectName(_fromUtf8("btnSatirEkle"))
        self.horizontalLayout_2.addWidget(self.btnSatirEkle)
        self.btnSatirSil = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnSatirSil.setObjectName(_fromUtf8("btnSatirSil"))
        self.horizontalLayout_2.addWidget(self.btnSatirSil)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnSutunEkle = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnSutunEkle.setObjectName(_fromUtf8("btnSutunEkle"))
        self.horizontalLayout.addWidget(self.btnSutunEkle)
        self.btnSutunSil = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnSutunSil.setObjectName(_fromUtf8("btnSutunSil"))
        self.horizontalLayout.addWidget(self.btnSutunSil)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Veriseti İşlemleri", None))
        self.btnSatirEkle.setText(_translate("Form", "Satır Ekle", None))
        self.btnSatirSil.setText(_translate("Form", "Satır Sil", None))
        self.btnSutunEkle.setText(_translate("Form", "Sütun Ekle", None))
        self.btnSutunSil.setText(_translate("Form", "Sütun Sil", None))

