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
        Dialog.resize(317, 187)

        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonApply = QtGui.QPushButton("Uygula")
        self.buttonBox.addButton(self.buttonApply, QtGui.QDialogButtonBox.ActionRole)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3,0,1,1)

        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0,0,1,1)

        self.plotDensity = QtGui.QRadioButton(Dialog)
        self.plotDensity.setObjectName(_fromUtf8("plotDensity"))
        self.plotDensity.setChecked(True)
        self.gridLayout.addWidget(self.plotDensity, 1,0,1,1 )

        self.plotDist = QtGui.QRadioButton(Dialog)
        self.plotDist.setObjectName(_fromUtf8("plotDist"))
        self.gridLayout.addWidget(self.plotDist, 2,0,1,1)

        self.df = QtGui.QLineEdit(Dialog)
        self.df.setObjectName(_fromUtf8("df"))
        self.gridLayout.addWidget(self.df, 0,1,1,1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Serbestlik Derecesi:", None))
        self.plotDensity.setText(_translate("Dialog", "Yoğunluk Fonksiyonu Grafiğini Çizdir", None))
        self.plotDist.setText(_translate("Dialog", "Dağılım Fonksiyonu Grafiğini Çizdir", None))

    def GetValues(self):
        density = True

        if self.df.text() != "":
            dfArr = General_Func.convertUserStringToInput(self.df.text())

            if len(dfArr)>1:    #tek bir degrees of freedom  degeri olabilir, bu yuzden ikincisi varsa False dondur
                return None, "Tek bir serbestlik derecesi girilebilir."
            else:
                if self.plotDist.isChecked():
                    density = False

                return dfArr[0], density

        else:
            return None, "Serbestlik derecesi girilmelidir."

    


