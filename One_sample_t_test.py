# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from scipy import stats

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
    def setupUi(self, Form, dataset):
        Form.setObjectName(_fromUtf8("Form"))
        self.setFixedSize(400, 300)
        self.dataset = dataset
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 291, 141))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radio_noteq = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radio_noteq.setChecked(True)
        self.radio_noteq.setObjectName(_fromUtf8("radio_noteq"))
        self.buttonGroup = QtGui.QButtonGroup(Form)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.radio_noteq)
        self.verticalLayout.addWidget(self.radio_noteq)
        self.radio_less = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radio_less.setObjectName(_fromUtf8("radio_less"))
        self.buttonGroup.addButton(self.radio_less)
        self.verticalLayout.addWidget(self.radio_less)
        self.radio_greater = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radio_greater.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_greater.sizePolicy().hasHeightForWidth())
        self.radio_greater.setSizePolicy(sizePolicy)
        self.radio_greater.setObjectName(_fromUtf8("radio_greater"))
        self.buttonGroup.addButton(self.radio_greater)
        self.verticalLayout.addWidget(self.radio_greater)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.h0_edit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.h0_edit.setObjectName(_fromUtf8("h0_edit"))
        self.horizontalLayout.addWidget(self.h0_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.con_edit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.con_edit.setObjectName(_fromUtf8("con_edit"))
        self.horizontalLayout_2.addWidget(self.con_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItems(dataset.numericFeatures)
        self.currentVar = dataset.numericFeatures[0]
        self.connect(self.comboBox, QtCore.SIGNAL('currentIndexChanged(QString)'), self.changeMethod)
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.reset = QtGui.QPushButton(self.gridLayoutWidget)
        self.reset.setObjectName(_fromUtf8("reset"))
        self.reset.clicked.connect(self.resetle)
        self.horizontalLayout_5.addWidget(self.reset)
        self.ok = QtGui.QPushButton(self.gridLayoutWidget)
        self.ok.clicked.connect(self.accept)
        self.ok.setObjectName(_fromUtf8("ok"))
        self.horizontalLayout_5.addWidget(self.ok)
        self.help = QtGui.QPushButton(self.gridLayoutWidget)
        self.help.setObjectName(_fromUtf8("help"))
        self.horizontalLayout_5.addWidget(self.help)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def accept(self):
        h0 = float(self.h0_edit.text())
        con = float(self.con_edit.text())
        one_sample_data = self.dataset.GetNumericValues(self.currentVar)[0]
        self.t_score, self.pvalue = stats.ttest_1samp(one_sample_data, h0)

        if self.radio_noteq.isChecked():
            pass
        elif self.radio_greater.isChecked():
            self.pvalue /= 2
        elif self.radio_less.isChecked():
            self.pvalue /= 2

    def resetle(self):
        self.h0_edit.setText('')
        self.con_edit.setText('')
        self.radio_noteq.setChecked(True)
        self.comboBox.setCurrentIndex(0)

    def changeMethod(self, var):
        self.currentVar = var


    def retranslateUi(self, Form):
        self.radio_noteq.setText(_translate("Form", "Ha != mu0", None))
        self.radio_less.setText(_translate("Form", "Ha < mu0", None))
        self.radio_greater.setText(_translate("Form", "Ha > mu0", None))
        self.label_2.setText(_translate("Form", "   H0 mu =        ", None))
        self.label.setText(_translate("Form", "Güven aralığı = ", None))
        self.reset.setText(_translate("Form", "Reset", None))
        self.ok.setText(_translate("Form", "Tamam", None))
        self.help.setText(_translate("Form", "Yardım", None))