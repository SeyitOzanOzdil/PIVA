# -*- coding: utf-8 -*-
import random
import math

import matplotlib.pyplot as plt
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Kmeans(object):
    def setupUi(self, Dialog, dataset):
        self.count = 0
        self.cList = []
        self.fList = []
        self.dataset = dataset
        self.stepCheck = False

        Kmns_layout = QGridLayout()
        self.noc1 = QLabel(u'Küme sayisi')
        self.get_noc1 = QLineEdit()
        self.noc1.setBuddy(self.get_noc1)
        self.maxIter = QLabel('Maksimum iterasyon sayisi')
        self.get_maxIter = QLineEdit()
        self.maxIter.setBuddy(self.get_maxIter)
        self.combo = QLabel('Mesafe fonksiyonu')
        self.currentMet = "Manhattan"
        self.aliste = QComboBox()
        self.methods = ["Manhattan", "Euclidean"]
        self.aliste.addItems(self.methods)
        self.combo.setBuddy(self.aliste)
        self.connect(self.aliste, SIGNAL('currentIndexChanged(QString)'), self.changeMethod)
        self.report = QCheckBox('Raporu Kaydet')
        self.report.stateChanged.connect(self.isRepChecked)
        self.doc = QPushButton('Dosya..')
        self.doc.hide()
        self.doc.clicked.connect(self.dosyaYolu)
        self.warn = QLabel(u"2 veya daha fazla özellik seçiniz!")
        self.warn.setStyleSheet("QLabel { color : red; font-size : 12px }")
        self.warn.hide()
        self.warn1 = QLabel(u"Özellik seçiniz!")
        self.warn1.setStyleSheet("QLabel { color : red; font-size : 12px }")
        self.warn1.hide()
        self.step_plot = QCheckBox(u'Adım adım çizim')
        self.step_plot.stateChanged.connect(self.pChecked)

        Kmns_layout.addWidget(self.noc1, 0, 0)
        Kmns_layout.addWidget(self.get_noc1, 0, 1)
        Kmns_layout.addWidget(self.maxIter, 1, 0)
        Kmns_layout.addWidget(self.get_maxIter, 1, 1)
        Kmns_layout.addWidget(self.combo, 2, 0)
        Kmns_layout.addWidget(self.aliste, 2, 1)
        Kmns_layout.addWidget(self.report, 4, 0)
        Kmns_layout.addWidget(self.doc, 4, 1)
        Kmns_layout.addWidget(self.step_plot, 5, 0)
        Kmns_layout.addLayout(self.step(), 5, 1)
        Kmns_layout.addWidget(self.ozellikler(self.create_cb_c, u'Kümeleme'), 6, 0)
        Kmns_layout.addWidget(self.ozellikler(self.create_cb, u'Çizim'), 6, 1)
        Kmns_layout.addWidget(self.warn1, 7, 0)
        Kmns_layout.addWidget(self.warn, 7, 1)
        Kmns_layout.addLayout(self.butonlar(), 8, 1)

        self.setLayout(Kmns_layout)
        self.setWindowTitle("K-Means")
        self.setFixedSize(380, 350+(2*len(self.dataset.numericFeatures)))

    def dosyaYolu(self):
        self.fname = QFileDialog.getSaveFileName(self)

    def step(self):
        hbox = QHBoxLayout()
        self.nextButton = QPushButton("ileri")
        self.nextButton.clicked.connect(self.adim_adim)
        self.backButton = QPushButton("geri")
        self.backButton.clicked.connect(self.adim_adim)
        self.nextButton.hide()
        self.backButton.hide()
        hbox.addWidget(self.nextButton)
        hbox.addWidget(self.backButton)
        hbox.addStretch(1)
        return hbox

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

    def create_cb_c(self, feature):
        cb = QCheckBox(feature)
        cb.stateChanged.connect(self.cChecked)
        return cb

    def create_cb(self, feature):
        cb = QCheckBox(feature)
        cb.stateChanged.connect(self.isChecked)
        return cb

    def isRepChecked(self, state):
        if state == Qt.Checked:
            self.doc.show()
        elif state == Qt.Unchecked:
            self.doc.hide()

    def pChecked(self, state):
        if state == Qt.Checked:
            self.stepCheck = True
        elif state == Qt.Unchecked:
            self.stepCheck = False

    def isChecked(self, state):
        source = self.sender()
        if state == Qt.Checked and self.count < 3:
            self.count += 1
            self.cList.append(source)
        elif state == Qt.Unchecked:
            self.count -= 1
            self.cList.remove(source)
        elif state == Qt.Checked and self.count == 3:
            self.cList.append(source)
            source.setCheckState(Qt.Unchecked)
            self.count += 1

    def cChecked(self, state):
        source = self.sender()
        if state == Qt.Checked:
            self.fList.append(source)
        elif state == Qt.Unchecked:
            self.fList.remove(source)

    def changeMethod(self, method):
        self.currentMet = method

    def accept(self):
        source = self.sender()
        if str(source.text()) == 'Tamam':
            self.warn.hide()
            self.warn1.hide()

            noc = self.get_noc1.text()
            self.iter = self.get_maxIter.text()
            if noc == '' or self.iter == '':
                QMessageBox.warning(self, 'Uyari', 'Eksik bilgi girdiniz!', QMessageBox.Cancel, QMessageBox.NoButton, QMessageBox.NoButton)
            else:
                noc = int(noc)
                self.iter = int(self.iter)
                self.call = True
                self.call1 = True
                self.call2 = True
                if len(self.cList) < 2:
                    self.warn.show()
                    self.call = False
                else:
                    self.value = []
                    for i in self.cList:
                        self.value.append(str(i.text()))
                    self.call = True

                if len(self.fList) == 0:
                    self.warn1.show()
                    self.call1 = False

                else:
                    self.value_f = []
                    for i in self.fList:
                        self.value_f.append(str(i.text()))
                    self.call1 = True

                if self.report.checkState() == Qt.Checked and str(self.fname) == '':
                    QMessageBox.warning(self, 'uyari', 'Uygun bir dosya adi giriniz', QMessageBox.Cancel, QMessageBox.NoButton, QMessageBox.NoButton)
                    self.call2 = False

                else:
                    self.call2 = True

                if self.call and self.call1 and self.call2:
                    if self.stepCheck:
                        self.nextButton.show()
                        self.backButton.show()
                    self.init(noc)
        else:
            self.helpGui()

    def init(self, noc):
        self.adim = -1
        self.data_dict = []
        self.features = []
        nesne_kumesi = []
        noe = 0
        maxV = 0
        minV = 0
        self.kumelenecek = []
        for i in self.dataset.numericFeatures:
            if i in self.value_f:
                self.kumelenecek.append(self.dataset.numericFeatures.index(i))
            values, counts = self.dataset.GetNumericValues(i)
            noe = len(values)

            if max(values) > maxV:
                maxV = max(values)
            if min(values) < minV:
                minV = min(values)

            self.data_dict.append(values)
            self.features.append(i)

        for i in range(noe):
            nesne_kumesi.append([])

        for i in range(len(self.data_dict)):
            for j in range(noe):
                nesne_kumesi[j].append(self.data_dict[i][j])

        again = True

        clusters = []

        for k in range(noc):
            clusters.append([])

        while again:
            for k in range(len(clusters)):
                clusters[k] = []
            centers = []
            self.setCenter(noc, nesne_kumesi, centers)
            again = False
            old_centers = centers[:]

            for i in range(len(nesne_kumesi)):
                dist = 999999999
                for j in range(noc):
                    distp = 0
                    for k in range(len(self.kumelenecek)):                #range(len(nesne_kumesi[i])): #################
                        if self.currentMet == 'Manhattan':
                            distp += abs(centers[j][self.kumelenecek[k]] - nesne_kumesi[i][self.kumelenecek[k]])
                        elif self.currentMet == 'Euclidean':
                            distp += math.sqrt((centers[j][self.kumelenecek[k]] - nesne_kumesi[i][self.kumelenecek[k]])**2)
                    if distp < dist:
                        dist = distp
                        indis = j
                clusters[indis].append(nesne_kumesi[i])

            for j in clusters:
                if len(j) == 0:
                    again = True

        self.clustered(nesne_kumesi, noc, centers, old_centers, clusters)

    def setCenter(self, noc, data, centers):
        for i in range(noc):
            tmp = data[random.randint(0, len(data)-1)]
            while tmp in centers:
                tmp = data[random.randint(0, len(data)-1)]
            centers.append(tmp)
        return centers

    def clustered(self, nesne_kumesi, noc, centers, old_centers, clusters):
        self.plot_memory = []
        again = True
        self.iterasyon = 0
        while again and self.maxIter:
            self.iterasyon += 1
            for i in range(len(nesne_kumesi)):
                dist = 999999999
                for j in range(noc):
                    distc = 0
                    for k in range(len(self.kumelenecek)):                #range(len(nesne_kumesi[i])): #################
                        if self.currentMet == 'Manhattan':
                            distc += abs(centers[j][self.kumelenecek[k]] - nesne_kumesi[i][self.kumelenecek[k]])
                        elif self.currentMet == 'Euclidean':
                            distc += math.sqrt((centers[j][self.kumelenecek[k]] - nesne_kumesi[i][self.kumelenecek[k]])**2)
                    if distc < dist:
                        dist = distc
                        indis = j
                clusters[indis].append(nesne_kumesi[i])

            self.plot_memory.append([0, 0])
            self.plot_memory[-1][0] = clusters[:]
            self.plot_memory[-1][1] = centers[:]
            centers = []
            for i in range(noc):
                sum = []
                for j in range(len(nesne_kumesi[0])):
                    sum.append(0)

                count = 0
                for j in range(len(clusters[i])):
                    for k in range(len(nesne_kumesi[0])):
                        sum[k] += clusters[i][j][k]
                    count += 1
                for j in range(len(sum)):
                    sum[j] /= count

                centers.append(sum)


            if old_centers == centers:
                again = False

            else:
                self.iter -= 1
                if self.iter == 0:
                    pass
                else:
                    old_centers = []
                    for k in range(len(centers)):
                        old_centers.append(centers[k])
                        clusters[k] = []

        if self.report.checkState() == Qt.Checked:
            txt = str(self.fname)
            f = open(txt, 'w')
            f.write('\t')
            f.write('   '.join(self.dataset.numericFeatures))
            f.write('\n')
            for i in range(noc):
                for j in clusters[i]:
                    for k in range(len(j)):
                        f.write(str(i+1)+"."+"\t" + ' ' + str(j[k]))
                    f.write('\n')

            f.close()

        self.kume_eleman = []
        for i in range(len(clusters)):
            self.kume_eleman.append(len(clusters[i]))

        if self.stepCheck:
            indis = []
            for i in range(len(self.features)):
                if self.features[i] in self.value:
                    indis.append(i)
            if len(indis) == 2:
                self.fig = plt.figure()
                self.ax = self.fig.add_subplot(111)
            else:
                self.fig = plt.figure()
                self.ax = self.fig.add_subplot(111, projection='3d')
            plt.ion()
            plt.show()
        else:
            self.scatter(noc)


    def scatter(self, noc):
        colors = ['b', 'r', 'y', 'g', 'silver', 'deeppink', 'indigo', 'darkblue', 'orange', 'maroon', 'darkslategray']
        indis = []
        for i in range(len(self.features)):
            if self.features[i] in self.value:
                indis.append(i)

        if len(indis) == 2:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            plt.ion()
            plt.show()
            for z in range(len(self.plot_memory)):
                ax.clear()
                clusters = self.plot_memory[z][0]
                centers = self.plot_memory[z][1]
                for i in range(noc):
                    for j in range(len(clusters[i])):
                        ax.scatter(clusters[i][j][indis[0]], clusters[i][j][indis[1]], c=colors[i])
                    ax.scatter(centers[i][indis[0]], centers[i][indis[1]], s=80, c=colors[i], marker='*', label='%d. Kume'%(i+1))
                ax.set_xlabel(self.value[0])
                ax.set_ylabel(self.value[1])
                plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
                plt.pause(0.5)
        elif len(indis) == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            plt.ion()
            plt.show()
            for z in range(len(self.plot_memory)):
                ax.clear()
                clusters = self.plot_memory[z][0]
                centers = self.plot_memory[z][1]

                for i in range(noc):
                    for j in range(len(clusters[i])):
                        ax.scatter(clusters[i][j][indis[0]], clusters[i][j][indis[1]], clusters[i][j][indis[2]], c=colors[i])
                    ax.scatter(centers[i][indis[0]], centers[i][indis[1]], centers[i][indis[2]], s=80, c=colors[i], marker='*', label='%d. Kume'%(i+1))
                ax.set_xlabel(self.value[0])
                ax.set_ylabel(self.value[1])
                ax.set_zlabel(self.value[2])
                plt.legend(loc='upper left', numpoints=1, ncol=3, fontsize=8, bbox_to_anchor=(0, 0))
                plt.pause(0.5)

        else:
            pass


    def adim_adim(self):
        colors = ['b', 'r', 'y', 'g', 'silver', 'deeppink', 'indigo', 'darkblue', 'orange', 'maroon', 'darkslategray']
        indis = []
        source = self.sender()
        for i in range(len(self.features)):
            if self.features[i] in self.value:
                indis.append(i)

        if len(indis) == 2:
            self.ax.clear()
            if str(source.text()) == 'ileri':
                if self.adim < len(self.plot_memory)-1:
                    self.adim += 1
            else:
                if self.adim > 0:
                    self.adim -= 1
                elif self.adim < 0:
                    self.adim += 1

            clusters = self.plot_memory[self.adim][0]
            centers = self.plot_memory[self.adim][1]
            for i in range(len(clusters)):
                for j in range(len(clusters[i])):
                    self.ax.scatter(clusters[i][j][indis[0]], clusters[i][j][indis[1]], c=colors[i])
                self.ax.scatter(centers[i][indis[0]], centers[i][indis[1]], s=100, c=colors[i], marker='*', label='%d. Kume'%(i+1))
            self.ax.set_xlabel(self.value[0])
            self.ax.set_ylabel(self.value[1])
            plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)

        elif len(indis) == 3:
            self.ax.clear()
            if str(source.text()) == 'ileri':
                if self.adim < len(self.plot_memory)-1:
                    self.adim += 1
            else:
                if self.adim > 0:
                    self.adim -= 1
                elif self.adim < 0:
                    self.adim += 1

            clusters = self.plot_memory[self.adim][0]
            centers = self.plot_memory[self.adim][1]
            for i in range(len(clusters)):
                for j in range(len(clusters[i])):
                    self.ax.scatter(clusters[i][j][indis[0]], clusters[i][j][indis[1]], clusters[i][j][indis[2]], c=colors[i])
                self.ax.scatter(centers[i][indis[0]], centers[i][indis[1]], centers[i][indis[2]], s=100, c=colors[i], marker='*', label='%d. Kume'%(i+1))
            self.ax.set_xlabel(self.value[0])
            self.ax.set_ylabel(self.value[1])
            self.ax.set_zlabel(self.value[2])
            plt.legend(loc='upper left', numpoints=1, ncol=3, fontsize=8, bbox_to_anchor=(0, 0))
