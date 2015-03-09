# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import *
from math import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Node:

    def __init__(self, FV_size=10, Y=0, X=0):
        self.FV_size=FV_size
        self.FV = [0.0]*FV_size # Feature Vector
        self.X=X # X location
        self.Y=Y # Y location
        
        for i in range(FV_size):
            self.FV[i]=random() # Assign a random number from 0 to 1

class SOM:
    #Let radius=False if you want to autocalculate the radis

    def setupUi(self, Dialog, dataset):
        self.dataset = dataset
        self.cList = []
        self.fList = []
        self.count = 0
        Som_layout = QGridLayout()
        self.heightL = QLabel(u'Yüksekliği giriniz')
        self.get_height = QLineEdit()
        self.heightL.setBuddy(self.get_height)
        self.widthL = QLabel(u'Genişliği giriniz')
        self.get_width = QLineEdit()
        self.widthL.setBuddy(self.get_width)
        self.learning_rateL = QLabel(u'Öğrenme oranı giriniz')
        self.get_learning_rate = QLineEdit()
        self.learning_rateL.setBuddy(self.get_learning_rate)
        self.maxIterL = QLabel(u'Maksimum iterasyon sayisi')
        self.get_maxIter = QLineEdit()
        self.maxIterL.setBuddy(self.get_maxIter)
        self.warn = QLabel(u"2 veya daha fazla özellik seçiniz!")
        self.warn.setStyleSheet("QLabel { color : red; font-size : 12px }")
        self.warn.hide()
        self.warn1 = QLabel(u"Özellik seçiniz!")
        self.warn1.setStyleSheet("QLabel { color : red; font-size : 12px }")
        self.warn1.hide()

        self.report = QCheckBox('Raporu Kaydet')
        self.report.stateChanged.connect(self.isRepChecked)
        self.doc = QPushButton('Dosya..')
        self.doc.hide()
        self.doc.clicked.connect(self.dosyaYolu)

        Som_layout.addWidget(self.heightL, 0, 0)
        Som_layout.addWidget(self.get_height, 0, 1)
        Som_layout.addWidget(self.widthL, 1, 0)
        Som_layout.addWidget(self.get_width, 1, 1)
        Som_layout.addWidget(self.learning_rateL, 2, 0)
        Som_layout.addWidget(self.get_learning_rate, 2, 1)
        Som_layout.addWidget(self.maxIterL, 3, 0)
        Som_layout.addWidget(self.get_maxIter, 3, 1)
        Som_layout.addWidget(self.report, 4, 0)
        Som_layout.addWidget(self.doc, 4, 1)
        Som_layout.addWidget(self.ozellikler(self.create_cb_c, 'Kumeleme'), 5, 0)
        Som_layout.addWidget(self.ozellikler(self.create_cb, 'Cizim'), 5, 1)
        Som_layout.addWidget(self.warn1, 6, 0)
        Som_layout.addWidget(self.warn, 6, 1)
        Som_layout.addLayout(self.butonlar(), 7, 1)

        self.setLayout(Som_layout)
        self.setWindowTitle("SOM")
        self.setFixedSize(310, 300+(5*len(self.dataset.numericFeatures)))

    def dosyaYolu(self):
        self.fname = QFileDialog.getSaveFileName(self)

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

    def pChecked(self, state):
        if state == Qt.Checked:
            self.stepCheck = True
        elif state == Qt.Unchecked:
            self.stepCheck = False

    def cChecked(self, state):
        source = self.sender()
        if state == Qt.Checked:
            self.fList.append(source)
        elif state == Qt.Unchecked:
            self.fList.remove(source)

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

    def isRepChecked(self, state):
        if state == Qt.Checked:
            self.doc.show()
        elif state == Qt.Unchecked:
            self.doc.hide()

    def accept(self):
        source = self.sender()
        if str(source.text()) == 'Tamam':
            self.warn.hide()
            self.warn1.hide()
            height = self.get_height.text()
            width = self.get_width.text()
            self.maxIter = self.get_maxIter.text()
            self.learning_rate = self.get_learning_rate.text()
            if height == '' and width == '' and self.maxIter == '' and self.learning_rate == '':
                QMessageBox.warning(self, 'Uyari', 'Eksik bilgi girdiniz!', QMessageBox.Cancel, QMessageBox.NoButton, QMessageBox.NoButton)
            else:
                height = int(height)
                width = int(width)
                self.maxIter = int(self.maxIter)
                self.learning_rate = float(self.learning_rate)
                self.total = width*height
                self.radius = (height + width)/2.0
                self.data_dict = []
                self.features = []
                nesne_kumesi = []
                self.nodes = [0]*(self.total)
                noe = 0
                self.kumelenecek = []
                call = True
                call1 = True
                call2 = True

                if len(self.cList) < 2:
                    self.warn.show()
                    call = False
                else:
                    self.value = []
                    for i in self.cList:
                        self.value.append(str(i.text()))
                    call = True

                if len(self.fList) == 0:
                    self.warn1.show()
                    call1 = False

                else:
                    self.value_f = []
                    for i in self.fList:
                        self.value_f.append(str(i.text()))
                    call1 = True

                if self.report.checkState() == Qt.Checked and str(self.fname) == '':
                    QMessageBox.warning(self, 'uyari', 'Uygun bir dosya adi giriniz', QMessageBox.Cancel, QMessageBox.NoButton, QMessageBox.NoButton)
                    call2 = False

                else:
                    call2 = True

                if call1 and call2 and call:
                    for i in self.dataset.numericFeatures:
                        if i in self.value_f:
                            self.kumelenecek.append(self.dataset.numericFeatures.index(i))
                        values, counts = self.dataset.GetNumericValues(i)
                        noe = len(values)
                        self.data_dict.append(values)
                        self.features.append(i)

                    for i in range(noe):
                        nesne_kumesi.append([])

                    for i in range(len(self.data_dict)):
                        for j in range(noe):
                            nesne_kumesi[j].append(self.data_dict[i][j])

                    noeFV = len(nesne_kumesi[0])

                    for i in range(height):
                        for j in range(width):
                            self.nodes[(i)*(width)+j] = Node(noeFV, i, j)

                    self.FV_size = noeFV
                    self.train(self.maxIter, nesne_kumesi)
        else:
            pass
    def train(self, iterations, train_vector):
        if log(self.radius) == 0:
            self.radius = 1.25
        time_constant = iterations/log(self.radius)

        for i in range(1, iterations+1):
            radius_decaying = self.radius*exp(-1.0*i/time_constant)
            learning_rate_decaying = self.learning_rate*exp(-1.0*i/time_constant)

            j = randint(0, len(train_vector)-1)
            input_FV = train_vector[j]
            best = self.best_match(input_FV)
            stack = []
            for k in range(self.total):
                dist = self.distance(self.nodes[best], self.nodes[k])
                if dist < radius_decaying:
                    temp_FV = [0.0]*self.FV_size
                    influence = exp((-1.0*(dist**2))/(2*radius_decaying*i))
                    for l in range(self.FV_size):
                        #Learning
                        temp_FV[l] = self.nodes[k].FV[l]+(influence*learning_rate_decaying*(input_FV[l] - self.nodes[k].FV[l]))

                    #Push the unit onto stack to update in next interval
                    stack[0:0] = [[[k], temp_FV]]

                for l in range(len(stack)):                    
                    self.nodes[stack[l][0][0]].FV[:] = stack[l][1][:]

        clusters = []
        for i in range(self.total):
            clusters.append([self.nodes[i].FV])

        for i in train_vector:
            min = 9999999
            for j in range(len(self.nodes)):
                fark = 0
                for k in (self.kumelenecek):
                    fark += (i[k] - self.nodes[j].FV[k])**2
                fark = sqrt(fark)
                if fark < min:
                    min = fark
                    indis = j
            clusters[indis].append(i)

            if len(i) == 0:
                clusters.remove(i)

        if self.report.checkState() == Qt.Checked:
            txt = str(self.fname)
            f = open(txt, 'w')
            for i in range(len(self.value_f)):
                f.write(u'Kumelemede kullanilan ozellik: ' + str(self.value_f[i]) + u', indisi: ' + str(self.kumelenecek[i]))
                f.write('\n')
            for i in range(len(clusters)):
                f.write(u'\n %d. Kume'%(i+1))
                for j in range(len(clusters[i])):
                    if j == 0:
                        f.write(u'\nDugum: ' + str(clusters[i][j]))
                    else:
                        f.write('eleman: ' + str(clusters[i][j]))
                    f.write('\n')
            f.close()

        fig = plt.figure()
        ax = fig.add_subplot(111)
        colors = ['b', 'r', 'y', 'g', 'm', 'k', 'c', 'silver', 'indigo', 'darkblue', 'orange', 'maroon', 'darkslategray']
        indis = []
        for i in range(len(self.features)):
            if self.features[i] in self.value:
                indis.append(i)

        for i in range(self.total-1):
            ax.scatter(self.nodes[i].FV[0], self.nodes[i].FV[1], c='b', marker='*', s=100)
        ax.scatter(self.nodes[-1].FV[0], self.nodes[-1].FV[1], c='b', marker='*', s=100, label=u'düğüm')

        for i in range(len(train_vector)-1):
            ax.scatter(train_vector[i][0], train_vector[i][1],  c='r')
        ax.scatter(train_vector[-1][0], train_vector[-1][1],  c='r', label="veri")

        if len(indis) == 2:
            fig1 = plt.figure()
            ax1 = fig1.add_subplot(111)
            for i in range(len(clusters)):
                for j in range(1, len(clusters[i])):
                    ax1.scatter(clusters[i][j][indis[0]], clusters[i][j][indis[1]],  c=colors[i])
                ax1.scatter(clusters[i][0][indis[0]], clusters[i][0][indis[1]], s=80, c=colors[i], marker='*', label=u'%d. Küme'%(i+1))

            plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
            ax1.set_xlabel(self.value[0])
            ax1.set_ylabel(self.value[1])
        elif len(indis) == 3:
            fig1 = plt.figure()
            ax1 = fig1.add_subplot(111, projection='3d')
            for i in range(len(clusters)):
                for j in range(1, len(clusters[i])):
                    ax1.scatter(clusters[i][j][indis[0]], clusters[i][j][indis[1]], clusters[i][j][indis[2]], c=colors[i])
                ax1.scatter(clusters[i][0][indis[0]], clusters[i][0][indis[1]], clusters[i][j][indis[2]], s=80, c=colors[i], marker='*', label=u'%d. Küme'%(i+1))

            plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
            ax1.set_xlabel(self.value[0])
            ax1.set_ylabel(self.value[1])
            ax1.set_zlabel(self.value[2])

        plt.show()

    #Returns best matching unit's index
    def best_match(self, target_FV):
        min = 9999999
        for j in range(len(self.nodes)):
            fark = 0
            for k in (self.kumelenecek):
                fark += (target_FV[k] - self.nodes[j].FV[k])**2
            fark = sqrt(fark)
            if fark < min:
                min = fark
                indis = j
        return indis


    def distance(self, node1, node2):
        return sqrt((node1.X-node2.X)**2+(node1.Y-node2.Y)**2)



