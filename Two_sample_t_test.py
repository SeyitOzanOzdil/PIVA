# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from scipy.stats import ttest_ind

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
    def setupUi(self, Form, dataset, appropriate, others):
        Form.setObjectName(_fromUtf8("Form"))
        self.dataset = dataset
        self.appropriate = appropriate
        self.others = others
        self.setFixedSize(400, 300)
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 301, 171))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
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
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
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
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.variances = QtGui.QCheckBox(self.gridLayoutWidget)
        self.variances.setObjectName(_fromUtf8("variances"))
        self.variances.setChecked(True)
        self.equal_variances = True
        self.variances.stateChanged.connect(self.isChecked)
        self.horizontalLayout.addWidget(self.variances)
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
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))

        self.group_combo = QtGui.QComboBox(self.gridLayoutWidget)
        self.group_combo.setObjectName(_fromUtf8("group_combo"))
        groups = appropriate.keys()
        self.group_combo.addItems(groups)
        self.connect(self.group_combo, QtCore.SIGNAL('currentIndexChanged(QString)'), self.changeGroup)
        self.currentGroup = groups[0]
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_combo.sizePolicy().hasHeightForWidth())
        self.group_combo.setSizePolicy(sizePolicy)
        self.horizontalLayout_7.addWidget(self.group_combo)

        spacerItem = QtGui.QSpacerItem(100, 67, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))

        self.feature_combo = QtGui.QComboBox(self.gridLayoutWidget)
        self.feature_combo.setObjectName(_fromUtf8("feature_combo"))
        self.feature_combo.addItems(others)
        self.connect(self.feature_combo, QtCore.SIGNAL('currentIndexChanged(QString)'), self.changeMethod)
        self.currentVar = others[0]
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feature_combo.sizePolicy().hasHeightForWidth())
        self.feature_combo.setSizePolicy(sizePolicy)
        self.horizontalLayout_6.addWidget(self.feature_combo)

        spacerItem1 = QtGui.QSpacerItem(100, 67, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def isChecked(self, state):
        source = self.sender()
        if state == QtCore.Qt.Checked:
            self.equal_variances = True
        elif state == QtCore.Qt.Unchecked:
            self.equal_variances = False

    def resetle(self):
        self.variances.setChecked(True)
        self.con_edit.setText('')
        self.radio_noteq.setChecked(True)
        self.group_combo.setCurrentIndex(0)
        self.feature_combo.setCurrentIndex(0)

    def changeGroup(self, var):
        self.currentGroup = var

    def changeMethod(self, var):
        self.currentVar = var

    def accept(self):
        con = float(self.con_edit.text())
        first_data = []
        second_data = []
        samples = self.appropriate[self.currentGroup]

        group_values, counts = self.dataset.GetNumericValues(self.currentVar)

        for i in range(len(group_values)):
            if self.dataset.GetValue(self.currentGroup, i) == samples[0]:
                element = group_values[i]
                first_data.append(element)
            elif self.dataset.GetValue(self.currentGroup, i) == samples[1]:
                element = group_values[i]
                second_data.append(element)

        self.t_score, self.pvalue = ttest_ind(first_data, second_data, equal_var=self.equal_variances)
        mean1 = sum(first_data)/len(first_data)
        mean2 = sum(second_data)/len(second_data)
        self.means = {samples[0]:mean1, samples[1]:mean2}

        if self.radio_noteq.isChecked():
            pass
        elif self.radio_greater.isChecked():
            self.pvalue /= 2
        elif self.radio_less.isChecked():
            self.pvalue /= 2

    def retranslateUi(self, Form):
        self.reset.setText(_translate("Form", "Reset", None))
        self.ok.setText(_translate("Form", "Tamam", None))
        self.help.setText(_translate("Form", "Yardım", None))
        self.radio_noteq.setText(_translate("Form", "İki Taraflı", None))
        self.radio_less.setText(_translate("Form", "Fark < 0", None))
        self.radio_greater.setText(_translate("Form", "Fark > 0", None))
        self.label_2.setText(_translate("Form", "   Varyanslar eşit         ", None))
        self.label.setText(_translate("Form", "    Güven aralığı  ", None))
        self.label_4.setText(_translate("Form", "Grup Seçiniz", None))
        self.label_3.setText(_translate("Form", "Özellik Seçiniz", None))












'''import numpy as np
from scipy.stats import ttest_ind
from scipy.special import stdtr

np.random.seed(1)

# Create sample data.
a = np.random.randn(40)
b = 4*np.random.randn(50)

# Use scipy.stats.ttest_ind.
t, p = ttest_ind(a, b, equal_var=False)
print "ttest_ind: t = %g  p = %g" % (t, p)

# The following is basically the same as the implementation in
# scipy.stats.ttest_ind.

# Compute the descriptive statistics of a and b.
abar = a.mean()
avar = a.var(ddof=1)
na = a.size
adof = na - 1

bbar = b.mean()
bvar = b.var(ddof=1)
nb = b.size
bdof = nb - 1

# Compute Welch's t-test using the descriptive statistics.
tf = (abar - bbar) / np.sqrt(avar/na + bvar/nb)
dof = (avar/na + bvar/nb)**2 / (avar**2/(na**2*adof) + bvar**2/(nb**2*bdof))
pf = 2*stdtr(dof, -np.abs(tf))

print "formula:   t = %g  p = %g" % (tf, pf)'''