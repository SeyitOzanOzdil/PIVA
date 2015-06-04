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
    def setupUi(self, Form, dataset, featrures):
        Form.setObjectName(_fromUtf8("Form"))
        self.setFixedSize(340, 270)
        self.dataset = dataset
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 20, 326, 211))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
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
        self.radio_greater.setObjectName(_fromUtf8("radio_greater"))
        self.buttonGroup.addButton(self.radio_greater)
        self.verticalLayout.addWidget(self.radio_greater)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.group_combo = QtGui.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_combo.sizePolicy().hasHeightForWidth())
        self.group_combo.setSizePolicy(sizePolicy)
        self.group_combo.addItems(featrures)
        self.connect(self.group_combo, QtCore.SIGNAL('currentIndexChanged(QString)'), self.changeGroup)
        self.currentGroup = featrures[0]
        self.group_combo.setObjectName(_fromUtf8("group_combo"))
        self.horizontalLayout_7.addWidget(self.group_combo)
        spacerItem = QtGui.QSpacerItem(100, 67, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.feature_combo = QtGui.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feature_combo.sizePolicy().hasHeightForWidth())
        self.feature_combo.setSizePolicy(sizePolicy)
        self.feature_combo.addItems(featrures)
        self.connect(self.feature_combo, QtCore.SIGNAL('currentIndexChanged(QString)'), self.changeFeature)
        self.currentVar = featrures[0]
        self.feature_combo.setObjectName(_fromUtf8("feature_combo"))
        self.horizontalLayout_6.addWidget(self.feature_combo)
        spacerItem1 = QtGui.QSpacerItem(100, 67, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.reset = QtGui.QPushButton(self.gridLayoutWidget)
        self.reset.setObjectName(_fromUtf8("reset"))
        self.reset.clicked.connect(self.resetle)
        self.horizontalLayout_5.addWidget(self.reset)
        self.ok = QtGui.QPushButton(self.gridLayoutWidget)
        self.ok.setObjectName(_fromUtf8("ok"))
        self.ok.clicked.connect(self.accept)
        self.horizontalLayout_5.addWidget(self.ok)
        self.help = QtGui.QPushButton(self.gridLayoutWidget)
        self.help.setObjectName(_fromUtf8("help"))
        self.horizontalLayout_5.addWidget(self.help)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.con_edit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.con_edit.setObjectName(_fromUtf8("con_edit"))
        self.con_edit.setText("0.05")
        self.horizontalLayout_2.addWidget(self.con_edit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def resetle(self):
        self.con_edit.setText('')
        self.radio_noteq.setChecked(True)
        self.group_combo.setCurrentIndex(0)
        self.feature_combo.setCurrentIndex(0)

    def changeGroup(self, var):
        self.currentGroup = var

    def changeFeature(self, var):
        self.currentVar = var

    def accept(self):
        self.no_exeption = False
        self.con = float(self.con_edit.text())
        first_sample, counts = self.dataset.GetNumericValues(self.currentGroup)
        second_sample, counts2 = self.dataset.GetNumericValues(self.currentVar)
        if first_sample == second_sample:
            self.no_exeption = True
            QtGui.QMessageBox.warning(self, u'Uyarı', u'Test için farklı örneklemleri seçiniz!', QtGui.QMessageBox.Cancel,
                                QtGui.QMessageBox.NoButton, QtGui.QMessageBox.NoButton)

        else:
            self.t_score, self.pvalue = stats.ttest_rel(first_sample, second_sample)
            if len(first_sample) < len(second_sample):
                self.df = len(first_sample)-1
            else:
                self.df = len(second_sample)-1

            mean1 = sum(first_sample)/len(first_sample)
            mean2 = sum(second_sample)/len(second_sample)
            self.means = [mean1, mean2]

            if self.radio_noteq.isChecked():
                pass
            elif self.radio_greater.isChecked():
                self.pvalue /= 2
            elif self.radio_less.isChecked():
                self.pvalue /= 2

            self.P_obs = stats.t.ppf(1-self.con, self.df)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Bağımlı İki Grup t Testi", None))
        self.radio_noteq.setText(_translate("Form", "İki taraflı", None))
        self.radio_less.setText(_translate("Form", "Fark < 0", None))
        self.radio_greater.setText(_translate("Form", "Fark > 0", None))
        self.label_4.setText(_translate("Form", "Birinci Değişken", None))
        self.label_3.setText(_translate("Form", "İkinci Değişken", None))
        self.reset.setText(_translate("Form", "Temizle", None))
        self.ok.setText(_translate("Form", "Tamam", None))
        self.help.setText(_translate("Form", "Yardım", None))
        self.label.setText(_translate("Form", "Güven aralığı  ", None))

