# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

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
        self.appropriate = appropriate
        self.others = others
        self.dataset = dataset

        self.setFixedSize(300, 200)
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 246, 83))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.help = QtGui.QPushButton(self.gridLayoutWidget)
        self.help.setObjectName(_fromUtf8("help"))
        self.horizontalLayout.addWidget(self.help)

        self.ok = QtGui.QPushButton(self.gridLayoutWidget)
        self.ok.setObjectName(_fromUtf8("ok"))
        self.horizontalLayout.addWidget(self.ok)
        self.ok.clicked.connect(self.accept)

        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))

        self.group_combo = QtGui.QComboBox(self.gridLayoutWidget)
        groups = appropriate.keys()
        self.group_combo.addItems(groups)
        self.connect(self.group_combo, QtCore.SIGNAL('currentIndexChanged(QString)'), self.changeGroup)
        self.currentGroup = groups[0]
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_combo.sizePolicy().hasHeightForWidth())
        self.group_combo.setSizePolicy(sizePolicy)
        self.group_combo.setObjectName(_fromUtf8("group_combo"))
        self.horizontalLayout_3.addWidget(self.group_combo)

        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        self.feature_combo = QtGui.QComboBox(self.gridLayoutWidget)
        self.feature_combo.addItems(others)
        self.connect(self.feature_combo, QtCore.SIGNAL('currentIndexChanged(QString)'), self.changeMethod)
        self.currentVar = others[0]
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feature_combo.sizePolicy().hasHeightForWidth())
        self.feature_combo.setSizePolicy(sizePolicy)
        self.feature_combo.setObjectName(_fromUtf8("feature_combo"))
        self.horizontalLayout_2.addWidget(self.feature_combo)

        """
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.con_edit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.con_edit.setObjectName(_fromUtf8("con_edit"))
        self.con_edit.setText("0.05")
        self.horizontalLayout_3.addWidget(self.con_edit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1)
        """

        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def accept(self):
        data = []
        x_bars = []
        samples = self.appropriate[self.currentGroup]
        for i in range(len(samples)):
            data.append([])

        group_values, counts = self.dataset.GetNumericValues(self.currentVar)

        for i in range(1, len(group_values)+1):
            tmp = self.dataset.GetValue(self.currentGroup, i)
            index = samples.index(float(tmp))
            data[index].append(group_values[i-1])

        N = np.concatenate(data).size
        xbar_grand = np.concatenate(data).mean()
        for i in data:
            x_bars.append(sum(i)/len(i))

        ssb_groups = []
        for i in range(len(data)):
            ssb_groups.append(len(data[i])*np.square(x_bars[i]-xbar_grand))
        self.SSB = sum(ssb_groups)

        ssw_gorups = []
        for i in range(len(data)):
            tmp = 0
            for j in data[i]:
                tmp += np.square(j-x_bars[i])

            ssw_gorups.append(tmp)
        self.SSW = sum(ssw_gorups)

        #the degrees of freedom
        k = len(samples)        # Number of sample groups
        self.dfB = k - 1  # Degrees of freedom between groups
        self.dfW = N - k  # Degrees of freedom within groups
        # Calculate the Mean squared difference
        self.MSB = self.SSB /self. dfB
        self.MSW = self.SSW / self.dfW
        # Calculate the F-statistic
        self.F = self.MSB / self.MSW
        self.F_critical = stats.distributions.f.ppf(1 - 0.05, self.dfB, self.dfW)

        # chart için hesaplanan değerler
        self.x_plot = np.linspace(0, 5, 250)
        self.y_plot = stats.distributions.f.pdf(self.x_plot, self.dfB, self.dfW)

        self.x_fcrit = np.linspace(self.F_critical, 5, 250)
        self.y_fcrit = stats.distributions.f.pdf(self.x_fcrit, self.dfB, self.dfW)


    def changeGroup(self, var):
        self.currentGroup = var

    def changeMethod(self, var):
        self.currentVar = var

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_3.setText(_translate("Form", "Gruplar", None))
        self.help.setText(_translate("Form", "Yardım", None))
        self.ok.setText(_translate("Form", "Tamam", None))
        self.label_2.setText(_translate("Form", "Test Değişkenleri", None))
        #self.label.setText(_translate("Form", "Güven aralığı  ", None))


