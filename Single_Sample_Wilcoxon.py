# -*- coding: utf-8 -*-

import numpy as np
from scipy.stats import wilcoxon

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

class Ui_Dialog(object):
    def setupUi(self, Dialog, dataset):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setFixedSize(450, 310)

        self.dataset = dataset

        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 230, 271, 61))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.btnTemizle = QtGui.QPushButton(self.layoutWidget)
        self.btnTemizle.setObjectName(_fromUtf8("btnTemizle"))
        self.btnTemizle.clicked.connect(self.resetle)
        self.horizontalLayout_4.addWidget(self.btnTemizle)
        self.btnTamam = QtGui.QPushButton(self.layoutWidget)
        self.btnTamam.setObjectName(_fromUtf8("btnTamam"))
        self.btnTamam.clicked.connect(self.rankHesapla)
        self.horizontalLayout_4.addWidget(self.btnTamam)
        self.btnYardim = QtGui.QPushButton(self.layoutWidget)
        self.btnYardim.setObjectName(_fromUtf8("btnYardim"))
        self.horizontalLayout_4.addWidget(self.btnYardim)
        self.layoutWidget_4 = QtGui.QWidget(Dialog)
        self.layoutWidget_4.setGeometry(QtCore.QRect(30, 200, 381, 41))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.h0_edit = QtGui.QLineEdit(self.layoutWidget_4)
        self.h0_edit.setObjectName(_fromUtf8("h0_edit"))
        self.horizontalLayout.addWidget(self.h0_edit)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 90, 105, 111))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_Hipotez = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_Hipotez.setObjectName(_fromUtf8("groupBox_Hipotez"))
        self.radio_greater = QtGui.QRadioButton(self.groupBox_Hipotez)
        self.radio_greater.setEnabled(True)
        self.radio_greater.setGeometry(QtCore.QRect(10, 60, 100, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_greater.sizePolicy().hasHeightForWidth())
        self.radio_greater.setSizePolicy(sizePolicy)
        self.radio_greater.setObjectName(_fromUtf8("radio_greater"))
        self.radio_noteq = QtGui.QRadioButton(self.groupBox_Hipotez)
        self.radio_noteq.setGeometry(QtCore.QRect(10, 20, 100, 16))
        self.radio_noteq.setChecked(True)
        self.radio_noteq.setObjectName(_fromUtf8("radio_noteq"))
        self.radio_less = QtGui.QRadioButton(self.groupBox_Hipotez)
        self.radio_less.setGeometry(QtCore.QRect(10, 40, 100, 16))
        self.radio_less.setObjectName(_fromUtf8("radio_less"))
        self.verticalLayout.addWidget(self.groupBox_Hipotez)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 90, 271, 111))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_TestType = QtGui.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_TestType.setObjectName(_fromUtf8("groupBox_TestType"))
        self.radioExact = QtGui.QRadioButton(self.groupBox_TestType)
        self.radioExact.setGeometry(QtCore.QRect(10, 40, 256, 17))
        self.radioExact.setObjectName(_fromUtf8("radioExact"))
        self.radioDefault = QtGui.QRadioButton(self.groupBox_TestType)
        self.radioDefault.setGeometry(QtCore.QRect(10, 20, 256, 17))
        self.radioDefault.setChecked(True)
        self.radioDefault.setObjectName(_fromUtf8("radioDefault"))
        self.radioNormalCorrection = QtGui.QRadioButton(self.groupBox_TestType)
        self.radioNormalCorrection.setGeometry(QtCore.QRect(10, 80, 256, 17))
        self.radioNormalCorrection.setObjectName(_fromUtf8("radioNormalCorrection"))
        self.radioNormal = QtGui.QRadioButton(self.groupBox_TestType)
        self.radioNormal.setGeometry(QtCore.QRect(10, 60, 256, 17))
        self.radioNormal.setObjectName(_fromUtf8("radioNormal"))
        self.verticalLayout_2.addWidget(self.groupBox_TestType)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 381, 91))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_6 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.comboBox = QtGui.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItems(self.dataset.numericFeatures)
        self.currentVar = self.dataset.numericFeatures[0]
        self.connect(self.comboBox, QtCore.SIGNAL('currentIndexChanged(QString)'), self.changeMethod)
        self.horizontalLayout_3.addWidget(self.comboBox)
        spacerItem = QtGui.QSpacerItem(100, 67, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def resetle(self):
        self.h0_edit.setText('0.0')
        self.radio_noteq.setChecked(True)
        self.radioDefault.setChecked(True)
        self.comboBox.setCurrentIndex(0)

    def changeMethod(self, var):
        self.currentVar = var

    def rankHesapla(self):
        self.z_statistic, self.p_value = wilcoxon(np.array(self.dataset.GetNumericValues(self.currentVar)[0])
                                                  - float(self.h0_edit.text()))


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Form", None))
        self.btnTemizle.setText(_translate("Dialog", "Temizle", None))
        self.btnTamam.setText(_translate("Dialog", "Tamam", None))
        self.btnYardim.setText(_translate("Dialog", "Yardım", None))
        self.label_2.setText(_translate("Dialog", "   Null Hipotez: mu      ", None))
        self.h0_edit.setText(_translate("Dialog", "0.0", None))
        self.groupBox_Hipotez.setTitle(_translate("Dialog", "Alternatif Hipotez", None))
        self.radio_greater.setText(_translate("Dialog", "mu > 0", None))
        self.radio_noteq.setText(_translate("Dialog", "İki taraflı", None))
        self.radio_less.setText(_translate("Dialog", "mu < 0", None))
        self.groupBox_TestType.setTitle(_translate("Dialog", "Test Tipi", None))
        self.radioExact.setText(_translate("Dialog", "Exact", None))
        self.radioDefault.setText(_translate("Dialog", "Default", None))
        self.radioNormalCorrection.setText(_translate("Dialog", "Normal Approximation with continuity correction", None))
        self.radioNormal.setText(_translate("Dialog", "Normal Approximation", None))
        self.label_6.setText(_translate("Dialog", "Grup Seçiniz", None))

