import peach as p
import numpy as np
import random
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Fuzzy():
    def setupUi(self, Dialog, dataset):
        self.count = 0
        self.dataset = dataset
        self.cList = []
        Fuzzy_layout = QGridLayout()
        self.m = QLabel('m degerini giriniz:')
        self.get_m = QLineEdit()
        self.m.setBuddy(self.get_m)
        self.noc = QLabel("Kume sayisi")
        self.get_noc = QLineEdit()
        self.noc.setBuddy(self.get_noc)
        self.report = QCheckBox('Raporu Kaydet')
        self.report.stateChanged.connect(self.isRepChecked)
        self.doc = QPushButton('Dosya..')
        self.doc.hide()
        self.doc.clicked.connect(self.dosyaYolu)
        self.warn1 = QLabel("2 Ozellik seciniz!")
        self.warn1.setStyleSheet("QLabel { color : red; font-size : 12px }")
        self.warn1.hide()
        Fuzzy_layout.addWidget(self.m, 0, 0)
        Fuzzy_layout.addWidget(self.get_m, 0, 1)
        Fuzzy_layout.addWidget(self.noc, 1, 0)
        Fuzzy_layout.addWidget(self.get_noc, 1, 1)
        Fuzzy_layout.addWidget(self.report, 2, 0)
        Fuzzy_layout.addWidget(self.doc, 2, 1)
        Fuzzy_layout.addWidget(self.ozellikler(self.create_cb, 'Kumeleme'), 3, 0)
        Fuzzy_layout.addWidget(self.warn1, 3, 1)
        Fuzzy_layout.addLayout(self.butonlar(), 4, 1)
        self.setLayout(Fuzzy_layout)
        self.setWindowTitle("Fuzzy C Means")
        self.setFixedSize(380, 350+(2*len(self.dataset.numericFeatures)))

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


    def create_cb(self, feature):
        cb = QCheckBox(feature)
        cb.stateChanged.connect(self.isChecked)
        return cb

    def isChecked(self, state):
        source = self.sender()
        if state == Qt.Checked and self.count < 2:
            self.count += 1
            self.cList.append(source)
        elif state == Qt.Unchecked:
            self.count -= 1
            self.cList.remove(source)
        elif state == Qt.Checked and self.count == 2:
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
            self.warn1.hide()
            noc = self.get_noc.text()
            m = self.get_m.text()
            if noc == '' or m == '':
                QMessageBox.warning(self, 'Uyari', 'Eksik bilgi girdiniz!', QMessageBox.Cancel, QMessageBox.NoButton, QMessageBox.NoButton)

            else:
                noc = int(noc)
                m = float(m)
                self.value = []
                call = True
                call2 = True
                for i in self.cList:
                    self.value.append(str(i.text()))

                if len(self.cList) < 2:
                    self.warn1.show()
                    call = False
                else:
                    self.value = []
                    for i in self.cList:
                        self.value.append(str(i.text()))
                    call = True

                if self.report.checkState() == Qt.Checked and str(self.doc.text()) == 'Dosya adi giriniz.':
                    QMessageBox.warning(self, 'uyari', 'Uygun bir dosya adi giriniz', QMessageBox.Cancel, QMessageBox.NoButton, QMessageBox.NoButton)
                    call2 = False
                else:
                    call2 = True

                if call and call2:
                    self.init(noc, m)

    def init(self, noc, m=1.25):
        self.data_dict = []
        self.features = []
        nesne_kumesi = []
        noe = 0
        for i in self.dataset.numericFeatures:
            if i in self.value:
                values, counts = self.dataset.GetNumericValues(i)
                noe = len(values)

                self.data_dict.append(values)
                self.features.append(i)

        for i in range(noe):
            nesne_kumesi.append([])

        for i in range(len(self.data_dict)):
            for j in range(noe):
                nesne_kumesi[j].append(self.data_dict[i][j])

        mu = []
        for i in range(len(nesne_kumesi)):
            mu.append([])
            toplam = 0
            y = random.uniform(0.1, 0.3)
            for j in range(noc):
                if j == noc - 1:
                    mu[i].append(abs(1-toplam))
                else:
                    toplam += y
                    mu[i].append(y)
                    y = random.uniform(0.1, 1-toplam)

        clusters = []
        for i in range(noc):
            clusters.append([])

        mu = np.array(mu)
        fcm = p.FuzzyCMeans(nesne_kumesi, mu, m)
        membership = fcm.membership()
        centers = fcm.centers()
        for i in range(len(membership)):
            cs = 0
            for j in range(len(membership[i])):
                if membership[i][j] > cs:
                    cs = membership[i][j]
                    cluster = j

            clusters[cluster].append(nesne_kumesi[i])

        if self.report.checkState() == Qt.Checked:
            txt = str(self.fname)
            f = open(txt, 'w')

            for i in range(noc):
                if i == 0:
                    f.write('\t         ')
                    f.write(('Kume %d' %(i+1)))
                else:
                    f.write('  ')
                    f.write(('Kume %d' %(i+1)))
            f.write('\n')

            for i in range(len(nesne_kumesi)):
                f.write(str(nesne_kumesi[i]))
                for j in range(noc):
                    f.write('    %.4f' % (membership[i][j]))
                f.write('\n')
            f.close()

        self.scatter(clusters, centers, noc)

    def scatter(self, clusters, centers, noc):
        plt.close()
        colors = ['b', 'r', 'y', 'g', 'm', 'k', 'c', 'silver', 'indigo', 'darkblue', 'orange', 'maroon', 'darkslategray']
        indis = []
        for i in range(len(self.features)):
            if self.features[i] in self.value:
                indis.append(i)

        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i in range(noc):
            for j in range(len(clusters[i])):
                ax.scatter(clusters[i][j][indis[0]], clusters[i][j][indis[1]], c=colors[i])
            ax.scatter(centers[i][indis[0]], centers[i][indis[1]], s=100, c=colors[i], marker='*', label='%d. Kume'%(i+1))
        ax.set_xlabel(self.value[0])
        ax.set_ylabel(self.value[1])
        plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
        plt.show()