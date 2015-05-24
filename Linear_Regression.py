# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from scipy import stats
import ChartCreator

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
    def setupUi(self, Dialog, dataset):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(316, 257)

        self.dataset = dataset
        self.result = ""

        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(45, 190, 221, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.btnTamam = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnTamam.setObjectName(_fromUtf8("btnTamam"))
        self.horizontalLayout.addWidget(self.btnTamam)
        self.btnIptal = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnIptal.setObjectName(_fromUtf8("btnIptal"))
        self.horizontalLayout.addWidget(self.btnIptal)
        self.btnIptal.clicked.connect(self.temizle)

        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 295, 175))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.listResponse = QtGui.QListWidget(self.gridLayoutWidget)
        self.listResponse.setObjectName(_fromUtf8("listResponse"))
        self.gridLayout.addWidget(self.listResponse, 1, 0, 1, 1)

        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.listExplanatory = QtGui.QListWidget(self.gridLayoutWidget)
        self.listExplanatory.setObjectName(_fromUtf8("listExplanatory"))
        self.gridLayout.addWidget(self.listExplanatory, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def temizle(self):
        self.listResponse.clearSelection()
        self.listExplanatory.clearSelection()

    def addITem(self, features):
        self.listResponse.addItems(features)
        self.listExplanatory.addItems(features)

    def getChoosenItemOnResponse(self):
        return str(self.listResponse.currentItem().text())

    def getChoosenItemOnExplanatory(self):
        return str(self.listExplanatory.currentItem().text())
        """
        x=[]
        for i in list(self.listExplanatory.selectedItems()):
            x.append(str(i.text()))
        return x
        """

    def regressionHesapla(self):
        resp = self.getChoosenItemOnResponse()
        exp = self.getChoosenItemOnExplanatory()

        slope, intercept, r_value, p_value, std_err = stats.linregress(self.dataset.GetNumericValues(resp)[0],
                                                                       self.dataset.GetNumericValues(exp)[0])

        #self.line = slope*self.dataset.GetNumericValues(resp)[0] + intercept

        self.result = "Response Değişkeni      :  %s \nExplanatory Değişkeni  :  %s\n\n" % (resp, exp)
        self.result += "     Intercept     :  %.4f\n" %(intercept)
        self.result += "     Slope           :  %.4f\n"  %(slope)
        self.result += "     R-squared   :  %.4f\n"  %(r_value**2)
        self.result += "     P-value       :  %.4f\n"  %(p_value)
        self.result += "     Std. Error   :  %.4f\n"  %(std_err)

        return self.result

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Linear Regression", None))
        self.btnTamam.setText(_translate("Dialog", "Tamam", None))
        self.btnIptal.setText(_translate("Dialog", "Temizle", None))
        self.label.setText(_translate("Dialog", "Response Variable\n", None))
        self.label_2.setText(_translate("Dialog", "Explanatory Variables\n", None))

