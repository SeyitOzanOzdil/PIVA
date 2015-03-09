# -*- coding: utf-8 -*-
import numpy as np
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class SVD():
    def setupUi(self, Dialog, dataset):
        self.count = 0
        self.dataset = dataset
        self.cList = [0]*len(dataset.numericFeatures)
        SVD_layout = QGridLayout()
        self.esik_degeri = QLabel("Esik Seviyesi")
        self.get_esik_degeri = QLineEdit()
        self.esik_degeri.setBuddy(self.get_esik_degeri)
        self.report = QCheckBox('Raporu Kaydet')
        self.report.stateChanged.connect(self.isRepChecked)
        self.doc = QPushButton('Dosya..')
        self.doc.hide()
        self.doc.clicked.connect(self.dosyaYolu)
        self.warn = QLabel("2 veya daha fazla veri seciniz!")
        self.warn.setStyleSheet("QLabel { color : red; font-size : 12px }")
        self.warn.hide()

        SVD_layout.addWidget(self.esik_degeri, 1, 0)
        SVD_layout.addWidget(self.get_esik_degeri, 1, 1)
        SVD_layout.addWidget(self.report, 2, 0)
        SVD_layout.addWidget(self.doc, 2, 1)
        SVD_layout.addWidget(self.ozellikler(self.create_cb, 'Boyut indirgeme'), 3, 0)
        SVD_layout.addWidget(self.warn, 3, 1)
        SVD_layout.addLayout(self.butonlar(), 4, 1)

        self.setLayout(SVD_layout)
        self.setFixedSize(350, 300)

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
            self.warn.hide()
            esik_degeri = float(self.get_esik_degeri.text())
            self.value = []
            self.call = True
            self.call1 = True
            for i in self.cList:
                if i != 0:
                    self.value.append(str(i.text()))

            if len(self.value) < 2:
                self.warn.show()
                self.call = False
            else:
                self.call = True

            if self.report.checkState() == Qt.Checked and str(self.fname) == '':
                QMessageBox.warning(self, 'uyari', 'Uygun bir dosya adi giriniz', QMessageBox.Cancel, QMessageBox.NoButton, QMessageBox.NoButton)
                self.call1 = False
            else:
                self.call1 = True

            if self.call and self.call1:
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

        nesne_kumesi=np.zeros((len(self.data_dict), noe))
        for i in range(len(self.data_dict)):
            for j in range(noe):
                nesne_kumesi[i][j] = self.data_dict[i][j]
                
        nesne_kumesi=nesne_kumesi.T
        U=np.dot(nesne_kumesi,nesne_kumesi.T)
        V=np.dot(nesne_kumesi.T,nesne_kumesi)
        eigValueU,eigVectorU=np.linalg.eig(U)
        eigValueV,eigVectorV=np.linalg.eig(V)
        U, s, V  = np.linalg.svd(nesne_kumesi, full_matrices=False)  
        self.Uo, self.So, self.Vo = np.linalg.svd(nesne_kumesi, full_matrices=False)
        self.npdot =  np.dot(np.dot(U, np.diag(s)), V)
        yerDizisiV=[]
        for i in range(len(eigValueV)):
            yerDizisiV.append(i)    
           

        for i in range(len(eigValueV)):
            yer=i
            for j in range(i+1,len(eigValueV)):
                if eigValueV[j] > eigValueV[yer]:
                    yer = j

            tmp = eigValueV[i]
            eigValueV[i] = eigValueV[yer]
            eigValueV[yer] = tmp
            tmp = yerDizisiV[i]
            yerDizisiV[i] = yerDizisiV[yer]
            yerDizisiV[yer] = tmp
    
        toplam=0
        for i in range(len(s)):
            toplam += s[i]
            
        i=0
        gecici=0
        self.s = []
        while(esik_degeri >= gecici/toplam  and i < len(s)):
            gecici += s[i]
            self.s.append(s[i])
            i = i+1

        self.secilenOzellikSayisi=i

        self.yer = []
        for i in range(self.secilenOzellikSayisi):
            self.yer.append(i)

        if self.report.checkState() == Qt.Checked:
            txt = str(self.fname)
            f = open(txt, 'w')
            f.write('U: ' + str(U) + '\n')
            f.write('\ns: ' + str(s) + '\n')
            f.write('\nV: ' + str(V) + '\n')
            f.write('\nilk matrisin bir daha elde edilmesi:\n' + str(self.npdot) + '\n')
            f.write('\nSecilen ozellik sayisi: ' + str(self.secilenOzellikSayisi) + '\n')
            for i in range(self.secilenOzellikSayisi):
                f.write(str(self.value[self.yer[i]]) + ' tekil degeri: ' + str(self.s[i]))
            f.close()