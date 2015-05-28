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
            self.data = ["Ortalama (Mean)", "Medyan (Median)", "Standard Sapma", "Varyans (Variance)",
                         u"Ceyrek (Quantiles)", u"Ko-Varyans (Co-Variance)", u"Iliski (Correlation)"]

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
        if str(cb.text()).find("Mean") != -1:
            cb.setChecked(True)
        if str(cb.text()).find("Median") != -1:
            cb.setChecked(True)
        if str(cb.text()).find("Standard Sapma") != -1:
            cb.setChecked(True)

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
        self.result = "           Min   Max   "
        if "Ortalama (Mean)" in self.listStatistic:
            self.result += "  Ort    "
        if "Medyan (Median)" in self.listStatistic:
            self.result += "     Medyan   "
        if "Standard Sapma" in self.listStatistic:
            self.result += "Std    "
        if "Varyans (Variance)" in self.listStatistic:
            self.result += "   Var    "
        if "Ceyrek (Quantiles)" in self.listStatistic:
            self.result += "   %25    "
            self.result += "  %50    "
            self.result += "  %75    "
            self.result += " IQR    "

        self.result += "\n"
        if len(self.listEleman) > 0:
            for column in self.listEleman:
                values = list()
                for i in self.dataset.dataSetDic[column]:
                    values.append(i.value)
                self.result += column + "\n"
                self.result += "         " + str(Statistical.minimum(values))
                self.result += "   " + str(Statistical.maximum(values))

                for stat in self.listStatistic:
                    if str(stat).find('Quantiles') != -1 :
                        self.result += "    "+ str(Statistical.quantiles(values,25)) +\
                                       "     "+ str(Statistical.quantiles(values,50)) +\
                                       "     "+ str(Statistical.quantiles(values,75)) +\
                                       "     "+ str(Statistical.quantiles(values,75)-Statistical.quantiles(values,25))

                    if str(stat).find('Mean') != -1:
                        self.result += "    %.3f" %(Statistical.mean(values))
                    if str(stat).find('Median') != -1:
                      self.result += "    %.3f" %(Statistical.median(values))
                    if str(stat).find('Standard Sapma') != -1:
                      self.result += "   %.3f" %(Statistical.standardDeviation(values))
                    if str(stat).find('(Variance)') != -1:
                        self.result += "    %.3f" %(Statistical.variance(values))

                self.result += "\n"

            if ('Ko-Varyans (Co-Variance)' in self.listStatistic or 'Iliski (Correlation)' in self.listStatistic):
                if len(self.listEleman) == 2:
                    list1 = list()
                    list2 = list()
                    for i in self.dataset.dataSetDic[self.listEleman[0]]:
                        list1.append(i.value)
                    for i in self.dataset.dataSetDic[self.listEleman[1]]:
                        list2.append(i.value)
                    if 'Ko-Varyans (Co-Variance)' in self.listStatistic:
                        self.result += "\n Ko-Varyans : %.3f\n" %(Statistical.coVariance(list1, list2))
                    if 'Iliski (Correlation)' in self.listStatistic:
                        self.result += "\n Iliski (Correlation)  : %.3f\n" %(Statistical.correlation(list1, list2))
                else:
                    Errors.ShowWarningMsgBox(self, u"Seçili istatistik işlemleri için iki eleman seçilmelidir!")

        else:
            Errors.ShowWarningMsgBox(self, u"Lütfen Bir Eleman Seçiniz!")

        return self.result
