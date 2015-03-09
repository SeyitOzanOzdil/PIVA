# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import General_Func

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
        Dialog.resize(359, 224)

        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonApply = QtGui.QPushButton("Uygula")
        self.buttonBox.addButton(self.buttonApply, QtGui.QDialogButtonBox.ActionRole)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5,0,1,1)

        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0,0,1,1)

        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1,0,1,1)

        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2,0,1,1)

        self.vals = QtGui.QLineEdit(Dialog)
        self.vals.setObjectName(_fromUtf8("vals"))
        self.gridLayout.addWidget( self.vals, 0,1,1,1)

        self.dfn = QtGui.QLineEdit(Dialog)
        self.dfn.setObjectName(_fromUtf8("dfn"))
        self.gridLayout.addWidget(self.dfn, 1,1,1,1)

        self.dfd = QtGui.QLineEdit(Dialog)
        self.dfd.setObjectName(_fromUtf8("dfd"))
        self.gridLayout.addWidget(self.dfd, 2,1,1,1)

        self.lowerT = QtGui.QRadioButton(Dialog)
        self.lowerT.setObjectName(_fromUtf8("lowerT"))
        self.lowerT.setChecked(True)
        self.gridLayout.addWidget(self.lowerT,3,0,1,1)

        self.upperT = QtGui.QRadioButton(Dialog)
        self.upperT.setObjectName(_fromUtf8("upperT"))
        self.gridLayout.addWidget(self.upperT,4,0,1,1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Değişken Değerleri:", None))
        self.label_2.setText(_translate("Dialog", "Pay Serbestlik Derecesi:", None))
        self.label_3.setText(_translate("Dialog", "Payda Serbestlik Derecesi:", None))
        self.lowerT.setText(_translate("Dialog", "Alt Sınır", None))
        self.upperT.setText(_translate("Dialog", "Üst Sınır", None))

    def GetValues(self):
        lower = True

        if self.vals.text() != "" and self.dfn.text() != "" and self.dfd.text() != "":
            valsArr = General_Func.convertUserStringToInput(self.vals.text())
            dfnArr = General_Func.convertUserStringToInput(self.dfn.text())
            dfdArr = General_Func.convertUserStringToInput(self.dfd.text())

            if len(dfnArr)>1 or len(dfdArr)>1:
                return None, "Serbestlik dereceleri birer sayi olmalidir.", False, False
            else: 
                if self.upperT.isChecked():
                    lower = False
                return valsArr, dfnArr[0], dfdArr[0], lower


        else: 
            return None, "Degerleri girmeniz gerekmektedir.", False, False

