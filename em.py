# -*- coding: utf-8 -*-

import itertools
import numpy as np
from scipy import linalg
import pylab as pl
import matplotlib as mpl
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from sklearn import mixture
  
class EM(object):
    def setupUi(self, Dialog, dataset):
        self.count = 0
        self.cList = []
        self.dataset = dataset

        Em_layout = QGridLayout()
        self.noc1 = QLabel(u'Küme sayisi')
        self.get_noc1 = QLineEdit()
        self.noc1.setBuddy(self.get_noc1)
        self.maxIter = QLabel('Maksimum iterasyon sayisi')
        self.get_maxIter = QLineEdit()
        self.maxIter.setBuddy(self.get_maxIter)
        self.report = QCheckBox('Raporu Kaydet')
        self.report.stateChanged.connect(self.isRepChecked)
        self.doc = QPushButton('Dosya..')
        self.doc.hide()
        self.doc.clicked.connect(self.dosyaYolu)
        self.warn1 = QLabel(u"Özellik seçiniz!")
        self.warn1.setStyleSheet("QLabel { color : red; font-size : 12px }")
        self.warn1.hide()

        Em_layout.addWidget(self.noc1, 0, 0)
        Em_layout.addWidget(self.get_noc1, 0, 1)
        Em_layout.addWidget(self.maxIter, 1, 0)
        Em_layout.addWidget(self.get_maxIter, 1, 1)
        Em_layout.addWidget(self.report, 2, 0)
        Em_layout.addWidget(self.doc, 2, 1)
        Em_layout.addWidget(self.ozellikler(self.create_cb, u'Kümeleme'), 3, 0)
        Em_layout.addWidget(self.warn1, 3, 1)
        Em_layout.addLayout(self.butonlar(), 4, 1)

        self.setLayout(Em_layout)
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
        groupBox = QGroupBox(amac+u' için özellik seçiniz')
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

    def isRepChecked(self, state):
        if state == Qt.Checked:
            self.doc.show()
        elif state == Qt.Unchecked:
            self.doc.hide()

    def isChecked(self, state):
        source = self.sender()
        if state == Qt.Checked:
            self.cList.append(source)
        elif state == Qt.Unchecked:
            self.cList.remove(source)

    def accept(self):
        source = self.sender()
        if str(source.text()) == 'Tamam':
            self.warn1.hide()
            noc = self.get_noc1.text()
            self.iter = self.get_maxIter.text()
            if noc == '' or self.iter == '':
                QMessageBox.warning(self, 'Uyari', 'Eksik bilgi girdiniz!', QMessageBox.Cancel, QMessageBox.NoButton, QMessageBox.NoButton)
            else:
                noc = int(noc)
                self.iter = int(self.iter)

                self.call = True
                self.call2 = True
                if len(self.cList) < 2:
                    self.warn1.show()
                    self.call = False
                else:
                    self.value = []
                    for i in self.cList:
                        self.value.append(str(i.text()))
                    self.call = True

                if self.report.checkState() == Qt.Checked and str(self.fname) == '':
                    QMessageBox.warning(self, 'uyari', 'Uygun bir dosya adi giriniz', QMessageBox.Cancel, QMessageBox.NoButton, QMessageBox.NoButton)
                    self.call2 = False

                else:
                    self.call2 = True

                if self.call and self.call2:
                    self.init(noc)
        else:
            print 'Yardım'

    def init(self, noc):
        self.data_dict = []
        self.features = []
        nesne_kumesi = []
        noe = 0
        kumelenecek = []
        for i in self.dataset.numericFeatures:
            if i in self.value:
                kumelenecek.append(self.dataset.numericFeatures.index(i))
                values, counts = self.dataset.GetNumericValues(i)
                noe = len(values)

                self.data_dict.append(values)
                self.features.append(i)

        for i in range(noe):
            nesne_kumesi.append([])

        for i in range(len(self.data_dict)):
            for j in range(noe):
                nesne_kumesi[j].append(self.data_dict[i][j])

        X = np.array(nesne_kumesi)

        # Fit a mixture of gaussians with EM using n components
        gmm = mixture.GMM(n_components=noc, covariance_type='full', n_iter=self.iter)
        gmm.fit(X)

        color_iter = itertools.cycle(['b', 'r', 'y', 'g', 'silver', 'deeppink', 'indigo', 'darkblue', 'orange', 'maroon', 'darkslategray'])
        f = 0
        if self.report.checkState() == Qt.Checked:
            txt = str(self.fname)
            f = open(txt, 'w')
            for i in range(len(self.value)):
                f.write(u'Kumelemede kullanilan ozellik: ' + str(self.value[i]) + u', indisi: ' + str(kumelenecek[i]))
                f.write('\n')
        for i, (clf, title) in enumerate([(gmm, 'GMM')]):
            splot = pl.subplot(111)
            Y_ = clf.predict(X)
            for i, (mean, covar, color) in enumerate(zip(
                    clf.means_, clf._get_covars(), color_iter)):
                v, w = linalg.eigh(covar)
                u = w[0] / linalg.norm(w[0])

                if not np.any(Y_ == i):
                    continue
                pl.scatter(X[Y_ == i, 0], X[Y_ == i, 1], color=color)
                if f:
                    x = X[Y_ == i, 0]
                    y = X[Y_ == i, 1]
                    f.write('%d. kumenin elemanlari:\n'%(i+1))
                    f.write('x koordinatlari: ' + str(x) + '\n')
                    f.write('y koordinatlari: ' + str(y) + '\n')
                # Plot an ellipse to show the Gaussian component
                angle = np.arctan(u[1] / u[0])
                angle = 180 * angle / np.pi  # convert to degrees
                ell = mpl.patches.Ellipse(mean, v[0], v[1], 180 + angle, color=color)
                ell.set_clip_box(splot.bbox)
                ell.set_alpha(0.5)
                splot.add_artist(ell)
        pl.show()