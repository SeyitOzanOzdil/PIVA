# -*- coding: utf-8 -*-
from PyQt4 import QtGui

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import Statistical
import Errors

class Ui_SummariesParams(object):
    def setupUi(self, Dialog, dataset):
        self.listEleman = []
        self.listStatistic = []
        self.result = ""
        self.dataset = dataset
        self.data = self.dataset.numericFeatures

        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(("gridLayout"))

        self.gridLayout.addWidget(self.ozellikler(self.create_cb_eleman, u'Sütun'), 0, 0)
        self.gridLayout.addWidget(self.ozellikler(self.create_cb_istatistik, u'İstatistiksel Hesaplama'), 0, 1)

        self.pushButton = QtGui.QPushButton("Hesapla")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton)

        self.setLayout(self.gridLayout)

    def ozellikler(self, fonk, amac):
        groupBox = QGroupBox(amac+' Seciniz')
        groupBox.setFlat(True)
        vbox = QVBoxLayout()
        if amac.find(u"Sütun") == -1:
            self.data = ["Mean", "Median", "Ortalama", "Standard Deviation", "Variance", "Co-Variance", "Correlation"]

        for i in self.data:
            cb = fonk(i)
            vbox.addWidget(cb)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)
        return groupBox

    def create_cb_eleman(self, feature):
        cb = QCheckBox(feature)
        cb.stateChanged.connect(self.checkedEleman)
        return cb

    def create_cb_istatistik(self, feature):
        cb = QCheckBox(feature)
        cb.stateChanged.connect(self.checkedStatistic)
        return cb

    def checkedStatistic(self, state):
        source = self.sender()
        if state == Qt.Checked:
            self.listStatistic.append(str(source.text()))
        elif state == Qt.Unchecked:
            self.listStatistic.remove(str(source.text()))

    def checkedEleman(self, state):
        source = self.sender()
        if state == Qt.Checked:
            self.listEleman.append(str(source.text()))
        elif state == Qt.Unchecked:
            self.listEleman.remove(str(source.text()))

    def istatistikHesapla(self):
        self.result = ""
        if len(self.listEleman) > 0:
            for column in self.listEleman:
                values = list()
                for i in self.dataset.dataSetDic[column]:
                    values.append(i.value)
                self.result += column + "\n"
                self.result += "      Minimum : " + str(Statistical.minimum(values)) + "\n"
                self.result += "      Maximum : " + str(Statistical.maximum(values)) + "\n"
                for stat in self.listStatistic:
                    if str(stat) == 'Mean':
                        self.result += "      Mean : " + str(Statistical.mean(values)) + "\n"
                    if str(stat) == 'Median':
                      self.result += "      Median : " + str(Statistical.median(values)) + "\n"
                    if str(stat) == 'Ortalama':
                      self.result += "      Ortalama : " + str(Statistical.average(values)) + "\n"
                    if str(stat) == 'Standard Deviation':
                      self.result += "      Standard Deviation : " + str(Statistical.standardDeviation(values)) + "\n"
                    if str(stat) == 'Variance':
                        self.result += "      Variance : " + str(Statistical.variance(values)) + "\n"
                self.result += "\n"

            if ('Co-Variance' in self.listStatistic or 'Correlation' in self.listStatistic):
                if len(self.listEleman) == 2:
                    list1 = list()
                    list2 = list()
                    for i in self.dataset.dataSetDic[self.listEleman[0]]:
                        list1.append(i.value)
                    for i in self.dataset.dataSetDic[self.listEleman[1]]:
                        list2.append(i.value)
                    if 'Co-Variance' in self.listStatistic:
                        self.result += " Co-Variance : " + str(Statistical.coVariance(list1, list2)) + "\n"
                    if 'Correlation' in self.listStatistic:
                        self.result += " Correlation  : " + str(Statistical.correlation(list1, list2)) + "\n"
                else:
                    Errors.ShowWarningMsgBox(self, u"Seçili istatistik işlemleri için iki eleman seçilmelidir!")

        else:
            Errors.ShowWarningMsgBox(self, u"Lütfen Bir Eleman Seçiniz!")

        return self.result