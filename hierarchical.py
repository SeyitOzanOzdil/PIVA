__author__ = 'Seyit'
# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
class Hierarchical():
    def setupUi(self, Dialog, dataset):
        self.dataset = dataset
        self.data_dict = []
        self.features = []
        self.fList = []
        self.fname = 0
        self.currentMethod = 'single'
        self.currentDistance = 'euclidean'
        hier_layout = QGridLayout()
        distanceMethods = ['euclidean', 'minkowski', 'manhattan']
        self.distLabel = QLabel('uzaklik metodu')
        self.distMethod = QComboBox()
        self.distMethod.addItems(distanceMethods)
        self.distLabel.setBuddy(self.distMethod)
        hierMethod = ['single', 'complete', 'average', 'weighted', 'centroid']
        self.hmLabel = QLabel('yontem')
        self.hMethod = QComboBox()
        self.hMethod.addItems(hierMethod)
        self.hmLabel.setBuddy(self.hMethod)
        self.warn1 = QLabel("Ozellik seciniz!")
        self.warn1.setStyleSheet("QLabel { color : red; font-size : 12px }")
        self.warn1.hide()
        self.report = QCheckBox('Raporu Kaydet')
        self.report.stateChanged.connect(self.isRepChecked)
        self.doc = QPushButton('Dosya..')
        self.doc.hide()
        self.doc.clicked.connect(self.dosyaYolu)
        hier_layout.addWidget(self.hmLabel, 1, 0)
        hier_layout.addWidget(self.hMethod, 1, 1)
        hier_layout.addWidget(self.distLabel, 2, 0)
        hier_layout.addWidget(self.distMethod, 2, 1)
        hier_layout.addWidget(self.report, 3, 0)
        hier_layout.addWidget(self.doc, 3, 1)
        hier_layout.addWidget(self.ozellikler(self.create_cb_c, 'Kumeleme'), 4, 0)
        hier_layout.addWidget(self.warn1, 4, 1)
        hier_layout.addLayout(self.butonlar(), 5, 1)
        self.connect(self.hMethod, SIGNAL('currentIndexChanged(QString)'), self.changeMethod)
        self.connect(self.distMethod, SIGNAL('currentIndexChanged(QString)'), self.changeDistance)

        self.setLayout(hier_layout)
        self.setFixedSize(300, 300+(5*len(self.dataset.numericFeatures)))

    def dosyaYolu(self):
        self.fname = QFileDialog.getSaveFileName(self)

    def isRepChecked(self, state):
        if state == Qt.Checked:
            self.doc.show()
        elif state == Qt.Unchecked:
            self.doc.hide()

    def accept(self):
        source = self.sender()
        if str(source.text()) == 'Tamam':
            call = True
            if len(self.fList) == 0:
                self.warn1.show()
                call = False
            else:
                self.value_f = []
                for i in self.fList:
                    self.value_f.append(str(i.text()))
                call = True

            if call:
                self.run()
        else:
            print 'Yardim'

    def changeMethod(self, method):
        self.currentMethod = str(method)

    def changeDistance(self, method):

        if str(method) == 'manhattan':
            method = 'cityblock'

        self.currentDistance = method

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

    def cChecked(self, state):
        source = self.sender()
        if state == Qt.Checked:
            self.fList.append(source)
        elif state == Qt.Unchecked:
            self.fList.remove(source)

    def run(self):
        plt.close()
        noe = 0
        nesne_kumesi = []
        for i in self.dataset.numericFeatures:
            if i in self.value_f:
                values, counts = self.dataset.GetNumericValues(i)
                noe = len(values)
                self.data_dict.append(values)
                self.features.append(i)

        for i in range(noe):
            nesne_kumesi.append([])

        for i in range(len(self.data_dict)):
            for j in range(noe):
                nesne_kumesi[j].append(self.data_dict[i][j])

        dist_mat = squareform(pdist(nesne_kumesi))
        linka = linkage(dist_mat, self.currentMethod)
        dendrogram(linka)
        plt.xlabel('Veriler')
        plt.ylabel('Mesafe')
        f = 0
        if self.fname:
            txt = str(self.fname)
            f = open(txt, 'w')
        clusternum = noe
        while(clusternum > 0):
            clustdict = {i: [i] for i in xrange(len(linka)+1)}
            for i in xrange(len(linka)-clusternum+1):
                clust1 = int(linka[i][0])
                clust2 = int(linka[i][1])
                clustdict[max(clustdict)+1] = clustdict[clust1] + clustdict[clust2]
                del clustdict[clust1], clustdict[clust2]
            if f:
                f.write('\n'+'%d Kumede birlesim'%(clusternum)+'\n')
                f.write(str(clustdict))
                f.write('\n')
            clusternum -= 1
        plt.show()