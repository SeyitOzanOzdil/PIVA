# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 19:26:48 2014

@author: Mustafa
"""

import numpy as np
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class PCA():
    def setupUi(self, Dialog, dataset):
        self.count = 0
        self.dataset = dataset
        self.cList = [0]*len(dataset.numericFeatures)
        PCA_layout = QGridLayout()
        self.esik_degeri = QLabel("Esik Seviyesi")
        self.get_esik_degeri = QLineEdit()
        self.esik_degeri.setBuddy(self.get_esik_degeri)
        self.report = QCheckBox('Raporu Kaydet')
        self.report.stateChanged.connect(self.isRepChecked)
        self.doc = QPushButton('Dosya..')
        self.doc.hide()
        self.doc.clicked.connect(self.dosyaYolu)
        self.warn = QLabel("2 veya daha fazla veri seciniz!")
        self.warn.setStyleSheet("QLabel { color : red; font-size : 13px }")
        self.warn.hide()

        PCA_layout.addWidget(self.esik_degeri, 1, 0)
        PCA_layout.addWidget(self.get_esik_degeri, 1, 1)
        PCA_layout.addWidget(self.report, 2, 0)
        PCA_layout.addWidget(self.doc, 2, 1)
        PCA_layout.addWidget(self.ozellikler(self.create_cb, 'Boyut indirgeme'), 3, 0)
        PCA_layout.addLayout(self.butonlar(), 4, 1)

        self.setLayout(PCA_layout)
        self.setFixedSize(350, 300+(2*len(self.dataset.numericFeatures)))

    def butonlar(self):
        hbox = QHBoxLayout()
        self.OkButton = QPushButton("Tamam")
        self.OkButton.clicked.connect(self.accept)
        self.helpButton = QPushButton("Yardim")
        self.helpButton.clicked.connect(self.accept)
        hbox.addWidget(self.OkButton)
        hbox.addWidget(self.helpButton)
        hbox.addStretch(1)
        return hbox

    def ozellikler(self, fonk, amac):
        groupBox = QGroupBox(amac+' icin ozellik seciniz')
        groupBox.setFlat(True)
        vbox = QVBoxLayout()
        for i in self.dataset.numericFeatures:
            cb = fonk(i)
            vbox.addWidget(cb)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)
        return groupBox

    def create_cb(self, feature):
        cb = QCheckBox(feature)
        cb.stateChanged.connect(self.isChecked)
        return cb

    def isChecked(self, state):
        source = self.sender()
        if state == Qt.Checked:
            indis = self.dataset.numericFeatures.index(str(source.text()))
            self.cList[indis] = source
        elif state == Qt.Unchecked:
            indis = self.dataset.numericFeatures.index(str(source.text()))
            self.cList[indis] = 0

    def isRepChecked(self, state):
        if state == Qt.Checked:
            self.doc.show()
        elif state == Qt.Unchecked:
            self.doc.hide()

    def dosyaYolu(self):
        self.fname = QFileDialog.getSaveFileName(self)

    def accept(self):
        source = self.sender()
        if str(source.text()) == 'Tamam':
            esik_degeri = float(self.get_esik_degeri.text())
            self.value = []
            self.call = True
            for i in self.cList:
                if i != 0:
                    self.value.append(str(i.text()))

            if len(self.cList) < 2:
                self.warn.show()
                self.call = False
            else:
                self.call = True

            if self.report.checkState() == Qt.Checked and str(self.fname) == '':
                QMessageBox.warning(self, 'uyari', 'Uygun bir dosya adi giriniz', QMessageBox.Cancel, QMessageBox.NoButton, QMessageBox.NoButton)
                self.call = False
            else:
                self.call = True

            if self.call:
                self.init(esik_degeri)


    def init(self, esik_degeri):
        self.data_dict = []
        self.features = []
        noe = 0
        for i in self.dataset.numericFeatures:
            if i in self.value:
                values, counts = self.dataset.GetNumericValues(i)
                noe = len(values)
                self.data_dict.append(values)
                self.features.append(i)

        nesne_kumesi = np.zeros((len(self.data_dict), noe))
        for i in range(len(self.data_dict)):
            for j in range(noe):
                nesne_kumesi[i][j] = self.data_dict[i][j]

        nesne_kumesi = nesne_kumesi.T
        means = np.mean(nesne_kumesi, axis=0)
        nesne_kumesi = nesne_kumesi - means
        nesne_kumesi = nesne_kumesi.T
        self.covMatris = np.cov(nesne_kumesi)
        eigValue, eigVector=np.linalg.eig(self.covMatris)
        self.eigValue1 ,self.eigVector1 = np.linalg.eig(self.covMatris)

        yerDizisi=[]
        
        for i in range(len(eigValue)):
            yerDizisi.append(i)

        for i in range(len(eigValue)):
            yer = i
            for j in range(i+1, len(eigValue)):
                if eigValue[j] > eigValue[yer]:
                    yer = j

            tmp = eigValue[i]
            eigValue[i] = eigValue[yer]
            eigValue[yer] = tmp
            tmp = yerDizisi[i]
            yerDizisi[i] = yerDizisi[yer]
            yerDizisi[yer] = tmp

        toplam=0
        for i in range(len(eigValue)):
            toplam += eigValue[i]

        i=0
        gecici=0
        while(esik_degeri >= gecici/toplam  and i < len(eigValue)):
            gecici += eigValue[i]
            print eigValue[i]
            i = i+1

        print "Secilen ozellik sayisi:",i
        self.secilenOzellikSayisi=i

        self.yer = []
        for i in range(self.secilenOzellikSayisi):
            self.yer.append(yerDizisi[i])
            print "Yeri:",yerDizisi[i]
        
        feature_vector=np.zeros((len(self.data_dict), self.secilenOzellikSayisi), dtype=float)
        
        for i in range(len(self.data_dict)):
            for j in range(self.secilenOzellikSayisi):
                feature_vector[i][j]=eigVector[i][yerDizisi[j]]

        son_veri = np.dot(nesne_kumesi.T, feature_vector)
        self.eigVector2 = eigVector
        self.fv = feature_vector
        self.last = son_veri

        if self.report.checkState() == Qt.Checked:
            txt = str(self.fname)
            f = open(txt, 'w')
            f.write('Kovaryans matrisi: \n' + str(self.covMatris))
            f.write('\nEigenvalue(ozdeger) \n')
            for i in range(len(self.eigValue1)):
                f.write(str(self.value[i]) + ": " + str(self.eigValue1[i]))

            f.write('\nSecilen ozellik sayisi: ' + str(self.secilenOzellikSayisi) + '\n')
            for i in range(self.secilenOzellikSayisi):
                f.write("Secilen ozellik: " + str(self.value[self.yer[i]]))

            f.write('\nSon veri: \n' + str(son_veri))
            f.close()