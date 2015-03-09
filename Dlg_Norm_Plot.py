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

class Norm_Plot_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(331, 215)

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

        self.normPlotMean = QtGui.QLineEdit(Dialog)
        self.normPlotMean.setObjectName(_fromUtf8("normPlotMean"))
        self.gridLayout.addWidget(self.normPlotMean, 0,1,1,1)

        self.normPlotStd = QtGui.QLineEdit(Dialog)
        self.normPlotStd.setObjectName(_fromUtf8("normPlotStd"))
        self.gridLayout.addWidget(self.normPlotStd, 1,1,1,1)

        self.normPlotDensity = QtGui.QRadioButton(Dialog)
        self.normPlotDensity.setObjectName(_fromUtf8("normPlotDensity"))
        self.gridLayout.addWidget(self.normPlotDensity, 2,0,1,1)

        self.normPlotDist = QtGui.QRadioButton(Dialog)
        self.normPlotDist.setObjectName(_fromUtf8("normPlotDist"))
        self.gridLayout.addWidget(self.normPlotDist, 3,0,1,1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Ortalama:", None))
        self.label_2.setText(_translate("Dialog", "Standart Sapma:", None))
        self.normPlotDensity.setText(_translate("Dialog", "Yoğunluk Fonksiyonu Grafiği Çizdir", None))
        self.normPlotDist.setText(_translate("Dialog", "Dağılım Fonksiyonu Grafiğini Çizdir", None))

    def GetValues(self):
        mean = [0]   #default value
        std = [1]    #default value
        density = True  #default value

        if self.normPlotMean.text() != "":
            mean = General_Func.convertUserStringToInput(self.normPlotMean.text())

        if self.normPlotStd.text() != "":
            std = General_Func.convertUserStringToInput(self.normPlotStd.text())

        if len(mean)>1 or len(std)>1 :
            return None, "Tek bir Ortalama ve Standart Sapma degeri girilebilir.", False

        else:
            if self.normPlotDist.isChecked():
                density = False

        return mean[0], std[0], density

    def SetDefault(self):

        self.normPlotMean.setText("0")
        self.normPlotStd.setText("1")
        self.normPlotDensity.setChecked(True)
