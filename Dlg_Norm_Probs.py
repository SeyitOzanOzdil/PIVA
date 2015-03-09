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

class Norm_Probs_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(354, 224)

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


        self.normVars = QtGui.QLineEdit(Dialog)
        self.normVars.setObjectName(_fromUtf8("normVars"))
        self.gridLayout.addWidget(self.normVars, 0,1,1,1)

        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1,0,1,1)

        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2,0,1,1)

        self.normMean = QtGui.QLineEdit(Dialog)
        self.normMean.setObjectName(_fromUtf8("normMean"))
        self.gridLayout.addWidget(self.normMean, 1,1,1,1)

        self.normStd = QtGui.QLineEdit(Dialog)
        self.normStd.setObjectName(_fromUtf8("normStd"))
        self.gridLayout.addWidget(self.normStd, 2,1,1,1)

        self.normLowerT = QtGui.QRadioButton(Dialog)
        self.normLowerT.setObjectName(_fromUtf8("normLowerT"))
        self.gridLayout.addWidget(self.normLowerT, 3,0,1,1)

        self.normUpperT = QtGui.QRadioButton(Dialog)
        self.normUpperT.setObjectName(_fromUtf8("normUpperT"))
        self.gridLayout.addWidget(self.normUpperT, 4,0,1,1)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Değişken Değerleri:", None))
        self.label_2.setText(_translate("Dialog", "Ortalama:", None))
        self.label_3.setText(_translate("Dialog", "Standart Sapma:", None))
        self.normLowerT.setText(_translate("Dialog", "Alt Sınır", None))
        self.normUpperT.setText(_translate("Dialog", "Üst Sınır", None))

    def GetValues(self):
        mean = [0]  #default value
        std = [1]   #default value
        lower = True

        if self.normVars.text() != "":
            str = self.normVars.text()
            inputArr = General_Func.convertUserStringToInput(str)
        else:
            return None, "Degerler girilmelidir.", False, False
        if self.normMean.text() != "":
            mean = General_Func.convertUserStringToInput(self.normMean.text())

        if self.normStd.text() != "":
            std = General_Func.convertUserStringToInput(self.normStd.text())

        if len(mean)>1 or len(std)>1 :
            return None, "Tek bir Ortalama ve Standart Sapma degeri girilebilir.", False, False

        else:
            if self.normUpperT.isChecked():
                lower = False;

        return inputArr, mean[0], std[0], lower

    def SetDefault(self):

        self.normMean.setText("0")
        self.normStd.setText("1")
        self.normLowerT.setChecked(True)