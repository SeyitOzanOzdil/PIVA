#-*- coding: utf-8 -*-
__author__ = 'Seyit'
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class DBS(object):
    def setupUi(self, Dialog, dataset):
        self.count = 0
        self.dataset = dataset
        self.features = []
        self.data_dict = []
        self.cList = []
        self.fList = []
        self.stepCheck = False
        self.adim = -1

        Dbs_layout = QGridLayout()
        self.eps = QLabel(u'Epsilon değerini girin')
        self.get_eps = QLineEdit()
        self.eps.setBuddy(self.get_eps)
        self.minpts = QLabel(u'En az komşu sayısını giriniz')
        self.get_minpts = QLineEdit()
        self.minpts.setBuddy(self.get_minpts)
        self.report = QCheckBox('Raporu Kaydet')
        self.report.stateChanged.connect(self.isRepChecked)
        self.doc = QPushButton('Dosya..')
        self.doc.hide()
        self.doc.clicked.connect(self.dosyaYolu)
        self.step_plot = QCheckBox('Adim adim cizim')
        self.step_plot.stateChanged.connect(self.pChecked)
        self.warn = QLabel(u"2 veya 3 tane özelllik seciniz!")
        self.warn.setStyleSheet("QLabel { color : red; font-size : 13px }")
        self.warn.hide()
        self.warn1 = QLabel(u"Özellik seciniz!")
        self.warn1.setStyleSheet("QLabel { color : red; font-size : 12px }")
        self.warn1.hide()
        Dbs_layout.addWidget(self.eps, 0, 0)
        Dbs_layout.addWidget(self.get_eps, 0, 1)
        Dbs_layout.addWidget(self.minpts, 1, 0)
        Dbs_layout.addWidget(self.get_minpts, 1, 1)
        Dbs_layout.addWidget(self.report, 2, 0)
        Dbs_layout.addWidget(self.doc, 2, 1)
        #Dbs_layout.addWidget(self.step_plot, 3, 0)
        #Dbs_layout.addLayout(self.step(), 3, 1)
        Dbs_layout.addWidget(self.ozellikler(self.create_cb_c, u'Kümeleme'), 4, 0)
        Dbs_layout.addWidget(self.ozellikler(self.create_cb, u'Çizim'), 4, 1)
        Dbs_layout.addWidget(self.warn1, 5, 0)
        Dbs_layout.addWidget(self.warn, 5, 1)
        Dbs_layout.addLayout(self.butonlar(), 6, 1)

        self.setLayout(Dbs_layout)
        self.setWindowTitle("DBSCAN")
        self.setFixedSize(380, 350+(2*len(self.dataset.numericFeatures)))

    def dosyaYolu(self):
        self.fname = QFileDialog.getSaveFileName(self)

    '''def step(self):
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
        return hbox'''

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
        groupBox = QGroupBox(amac+u' icin özellik seçiniz')
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

    def create_cb_c(self, feature):
        cb = QCheckBox(feature)
        cb.stateChanged.connect(self.cChecked)
        return cb

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


    def accept(self):
        source = self.sender()
        if str(source.text()) == 'Tamam':
            self.warn.hide()
            self.warn1.hide()
            epsilon = self.get_eps.text()
            minpts = self.get_minpts.text()
            if epsilon == '' or minpts == '':
                QMessageBox.warning(self, 'Uyari', 'Eksik bilgi girdiniz!', QMessageBox.Cancel, QMessageBox.NoButton, QMessageBox.NoButton)
            else:
                epsilon = int(epsilon)
                minpts = int(minpts)
                call1 = True
                call2 = True
                call3 = True
                if len(self.cList) < 2:
                    self.warn.show()
                    call1 = False
                else:
                    self.value = []
                    for i in self.cList:
                        self.value.append(str(i.text()))
                    call1 = True
                if len(self.fList) == 0:
                    self.warn1.show()
                    call2 = False
                else:
                    self.value_f = []
                    for i in self.fList:
                        self.value_f.append(str(i.text()))
                    call1 = True

                if call1 and call2:
                    if self.stepCheck:
                        self.nextButton.show()
                        self.backButton.show()
                    self.run(epsilon, minpts)


    def run(self, eps, min_points):
        clusters = [[]]
        visited = []
        noise = []
        self.plot_memory = []
        self.noise_memory = []
        nesne_kumesi = []
        self.features = []
        self.kumelenecek = []
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

        for i in range(len(nesne_kumesi)):
            if not nesne_kumesi[i] in visited:
                visited.append(nesne_kumesi[i])
                core = nesne_kumesi[i]
                neighbor = self.regionQuerry(core, eps, nesne_kumesi, visited)
                if len(neighbor) >= min_points:
                    c = self.expandCluster(neighbor, eps, min_points, visited, nesne_kumesi, clusters)
                    clusters.append(c)
                    self.plot_memory.append([])
                    self.plot_memory[-1].append(clusters[:])
                else:
                    noise.append(nesne_kumesi[i])
                    self.noise_memory.append([0])
                    self.noise_memory[-1][0] = noise[:]
        clusters.pop(0)

        if self.report.checkState() == Qt.Checked:
            txt = str(self.fname)
            f = open(txt, 'w')
            f.write('\t')
            f.write('   '.join(self.dataset.numericFeatures))
            f.write('\n')
            for i in range(len(clusters)):
                for j in clusters[i]:
                    for k in range(len(j)):
                        f.write(str(i+1)+"."+"\t" + ' ' + str(j[k]))
                    f.write('\n')

            for i in range(len(noise)):
                f.write(u'gurultu')
                for j in noise[i]:
                    f.write('\t' + ' ' + str(j))
                f.write('\n')
            f.close()


        if self.stepCheck:
            indis = []
            for i in range(len(self.features)):
                if self.features[i] in self.value:
                    indis.append(i)
            if len(indis) == 2:
                self.fig = plt.figure()
                self.ax = self.fig.add_subplot(111)
            else:
                self.fig1 = plt.figure()
                self.ax1 = self.fig.add_subplot(111, projection='3d')
            plt.ion()
            plt.show()
        else:
            self.scatter(clusters, noise)


    def expandCluster(self, neighbor, eps, MinPts, visited, data, clusters):
        cluster = []
        for i in neighbor:
            if not i in visited:
                visited.append(i)
                neighbor2 = self.regionQuerry(i, eps, data, visited)
                if len(neighbor2) >= MinPts:
                    neighbor.extend(neighbor2)
            for j in clusters:
                if not i in j and (not i in cluster):
                    cluster.append(i)
        return cluster

    def regionQuerry(self, core, eps, data, visited):
        neighbor = [core]
        for j in range(len(data)):
            dist = 0
            for i in range(len(self.kumelenecek)):
                dist += abs(core[self.kumelenecek[i]] - data[j][self.kumelenecek[i]])

            if dist <= eps:
                if not data[j] in visited:
                    neighbor.append(data[j])
        return neighbor

    def scatter(self, clusters, noise):
        plt.close()
        colors = ['b', 'r', 'y', 'g', 'm', 'k', 'c', 'silver', 'indigo', 'darkblue', 'orange', 'maroon', 'darkslategray']
        indis = []
        for i in range(len(self.features)):
            if self.features[i] in self.value:
                indis.append(i)

        if len(indis) == 2:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            for i in range(len(clusters)):
                for j in range(len(clusters[i])-1):
                    ax.scatter(clusters[i][j][indis[0]], clusters[i][j][indis[1]], c=colors[i])
                ax.scatter(clusters[i][j+1][indis[0]], clusters[i][j+1][indis[1]], c=colors[i], label=u'%d. Küme'%(i+1))
            for i in range(len(noise)-1):
                ax.scatter(noise[i][indis[0]], noise[i][indis[1]], c='c')
            ax.scatter(noise[-1][indis[0]], noise[-1][indis[1]], c='c', label=u'Gürültü')
            plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
            ax.set_xlabel(self.value[0])
            ax.set_ylabel(self.value[1])

        elif len(indis) == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            for i in range(len(clusters)):
                for j in range(len(clusters[i])):
                    ax.scatter(clusters[i][j][indis[0]], clusters[i][j][indis[1]], clusters[i][j][indis[2]], c=colors[i])
            ax.set_xlabel(self.value[0])
            ax.set_ylabel(self.value[1])
            ax.set_zlabel(self.value[2])
        else:
            pass

        plt.show()

    '''def adim_adim(self):
        colors = ['b', 'r', 'y', 'g', 'silver', 'indigo', 'darkblue', 'orange', 'maroon', 'darkslategray']
        indis = []
        source = self.sender()
        for i in range(len(self.features)):
            if self.features[i] in self.value:
                indis.append(i)

        if len(indis) == 2:
            self.ax.clear()
            clusters = self.plot_memory[-1][0]
            clusters.pop(0)
            if str(source.text()) == 'ileri':
                if self.adim < len(self.plot_memory)-1:
                    self.adim += 1
                    clusters = self.plot_memory[self.adim][0]
                    clusters.pop(0)
            else:
                if self.adim > 0:
                    self.adim -= 1
                    clusters = self.plot_memory[self.adim][0]
                    clusters.pop(0)
                elif self.adim < 0:
                    self.adim += 1
                    clusters = self.plot_memory[self.adim][0]
                    clusters.pop(0)

            for i in range(len(clusters)):
                for j in range(len(clusters[i])):
                    self.ax.scatter(clusters[i][j][indis[0]], clusters[i][j][indis[1]], c=colors[i])
            self.ax.set_xlabel(self.value[0])
            self.ax.set_ylabel(self.value[1])
            self.ax.scatter(1, 1, c='r', s=100)
            self.ax.scatter(2, 2, c='r', s=100)
            self.ax.scatter(2, 2, c='r', s=100)
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
            for i in range(len(clusters)):
                for j in range(len(clusters[i])):
                    self.ax.scatter(clusters[i][j][indis[0]], clusters[i][j][indis[1]], clusters[i][j][indis[2]], c=colors[i])
            self.ax.set_xlabel(self.value[0])
            self.ax.set_ylabel(self.value[1])
            self.ax.set_zlabel(self.value[2])
'''