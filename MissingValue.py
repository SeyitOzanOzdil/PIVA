# -*- coding: utf-8 -*-

import Errors
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

        self.yontem = ""
        Form.setObjectName(_fromUtf8("Dialog"))
        Form.resize(305, 163)
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 269, 47))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton_2 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout.addWidget(self.radioButton)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 271, 61))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.fak)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def fak(self):
        if self.radioButton.isChecked():
            self.yontem = "0 (Sıfır) ile Doldur"
            self.close()
        elif self.radioButton_2.isChecked():
            self.yontem = self.radioButton_2.text()
            self.close()
        else:
            Errors.ShowWarningMsgBox(self,u"Hiç bir seçeneği işaretlemediniz!")


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Kayıp Değer", None))
        self.radioButton_2.setText(_translate("Form", "Tahmin et", None))
        self.radioButton.setText(_translate("Form", u"0 (Sıfır) ile Doldur", None))
        self.label.setText(_translate("Form", "Verisetinde eksik satırlar bulunmaktadır! \n"
"Lütfen düzeltme yöntemini seçiniz.", None))
        self.pushButton.setText(_translate("Form", "Düzelt", None))

