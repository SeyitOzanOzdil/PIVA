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
        Dialog.resize(327, 206)

        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonApply = QtGui.QPushButton("Uygula")
        self.buttonBox.addButton(self.buttonApply, QtGui.QDialogButtonBox.ActionRole)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4,0,1,1)

        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0,0,1,1)

        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1,0,1,1)

        self.probs = QtGui.QLineEdit(Dialog)
        self.probs.setObjectName(_fromUtf8("probs"))
        self.gridLayout.addWidget(self.probs, 0,1,1,1)

        self.df = QtGui.QLineEdit(Dialog)
        self.df.setObjectName(_fromUtf8("df"))
        self.gridLayout.addWidget(self.df, 1,1,1,1)

        self.lowerT = QtGui.QRadioButton(Dialog)
        self.lowerT.setObjectName(_fromUtf8("lowerT"))
        self.lowerT.setChecked(True)
        self.gridLayout.addWidget(self.lowerT, 2,0,1,1)

        self.upperT = QtGui.QRadioButton(Dialog)
        self.upperT.setObjectName(_fromUtf8("upperT"))
        self.gridLayout.addWidget(self.upperT, 3,0,1,1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Olasılıklar:", None))
        self.label_2.setText(_translate("Dialog", "Serbestlik Derecesi:", None))
        self.lowerT.setText(_translate("Dialog", "Alt Sınır", None))
        self.upperT.setText(_translate("Dialog", "Üst Sınır", None))

    def GetValues(self):
        lower = True

        if self.probs.text() != "" and self.df.text() != "":
            
            probsArr = General_Func.convertUserStringToInput(self.probs.text())
            dfArr = General_Func.convertUserStringToInput(self.df.text())

            if len(dfArr)>1:    #tek bir degrees of freedom  degeri olabilir, bu yuzden ikincisi varsa False dondur
                return None, "Tek bir serbestlik derecesi girilebilir.", False
            else:
                if self.upperT.isChecked():
                    lower = False

                return probsArr, dfArr[0], lower
        else:
            return None, "Degerleri girmeniz gerekmektedir.", False   #todo: bos array de donucek

