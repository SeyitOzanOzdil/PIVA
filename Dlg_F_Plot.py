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
        Dialog.resize(289, 217)

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

        self.dfn = QtGui.QLineEdit(Dialog)
        self.dfn.setObjectName(_fromUtf8("dfn"))
        self.gridLayout.addWidget(self.dfn, 0,1,1,1)

        self.dfd = QtGui.QLineEdit(Dialog)
        self.dfd.setObjectName(_fromUtf8("dfd"))
        self.gridLayout.addWidget(self.dfd, 1,1,1,1)

        self.plotDensity = QtGui.QRadioButton(Dialog)
        self.plotDensity.setObjectName(_fromUtf8("plotDensity"))
        self.plotDensity.setChecked(True)
        self.gridLayout.addWidget(self.plotDensity, 2,0,1,1)

        self.plotDist = QtGui.QRadioButton(Dialog)
        self.plotDist.setObjectName(_fromUtf8("plotDist"))
        self.gridLayout.addWidget(self.plotDist, 3,0,1,1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Pay Serbestlik Derecesi:", None))
        self.label_2.setText(_translate("Dialog", "Payda Serbestlik Derecesi:", None))
        self.plotDensity.setText(_translate("Dialog", "Yoğunluk Fonksiyonu Grafiğini Çiz", None))
        self.plotDist.setText(_translate("Dialog", "Dağılım Fonksiyonu Grafiğini Çiz", None))

    def GetValues(self):
        density = True

        if self.dfn.text() != "" and self.dfd.text() != "":
            
            dfnArr = General_Func.convertUserStringToInput(self.dfn.text())
            dfdArr = General_Func.convertUserStringToInput(self.dfd.text())

            if len(dfnArr)>1 or len(dfdArr)>1:
                return None, "Tek bir serbestlik dereceleri birer sayı olmalıdır.", False
            else: 
                if self.plotDist.isChecked():
                    density = False
                return dfnArr[0], dfdArr[0], density

        else:
            return None, "Degerleri girmeniz gerekmektedir.", False
