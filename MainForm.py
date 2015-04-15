# -*- coding: utf-8 -*-

import sys
import os
import datetime
import time
import shutil
from PyQt4.QtGui import QTableWidgetItem
from py_expression_eval import Parser

from PyQt4 import QtCore, QtGui
from tables import indexes

import Parsero
import FileOperations
import TableOperations
import Errors
import ChartCreator
import Utils
import General_Func
import Distributions

import Dlg_PieChartParams
import Dlg_BarChartParams
import Dlg_BoxPlotParams
import Dlg_ScatterParams
import Dlg_HistogramParams

import Dlg_Norm_Quan
import Dlg_Norm_Probs
import Dlg_Norm_Plot
import Dlg_T_Chi_Quan
import Dlg_T_Chi_Probs
import Dlg_T_Chi_Plot
import Dlg_F_Quan
import Dlg_F_Probs
import Dlg_F_Plot
import Dlg_AboutPIVA

import webbrowser

import k_means
import k_medoids
import fuzzy_c_mean
import hierarchical
import dbscan
import Som
import em
import pca
import svd

import New_Column
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(820, 600)
        MainWindow.setWindowIcon(QtGui.QIcon("resources/p.jpg"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))

        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        #dockWidget_DataSet
        self.dockWidget_DataSet = QtGui.QDockWidget("Veri Seti")
        self.dockWidget_DataSet.setObjectName("dockWidget_DataSet")
        self.dockWidget_DataSet.setMinimumSize(QtCore.QSize(466, 125))
        #self.dockWidget_DataSet.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        #self.dockWidget_DataSet.setReadOnly(True)

        self.gridLayout.addWidget(self.dockWidget_DataSet, 1, 0, 1, 1)

        #TextEdit_Down
        self.textEdit_Down = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_Down.setObjectName(_fromUtf8("textEdit_Down"))
        self.textEdit_Down.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.textEdit_Down.setReadOnly(True)

        self.label2 = QtGui.QLabel(self.centralwidget)
        self.label2.setObjectName("label2")

        self.gridLayout.addWidget(self.label2, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.textEdit_Down, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        #DockWidget_Params
        self.dockWidget_Params = QtGui.QDockWidget("Parametreler")
        self.dockWidget_Params.setMinimumSize(QtCore.QSize(466, 125))
        self.dockWidget_Params.setObjectName(_fromUtf8("dockWidget_Params"))
        self.dockWidgetContents_10 = QtGui.QWidget()
        self.dockWidgetContents_10.setObjectName(_fromUtf8("dockWidgetContents_10"))
        self.gridLayout_Params = QtGui.QGridLayout(self.dockWidgetContents_10)
        self.gridLayout_Params.setObjectName(_fromUtf8("gridLayout_Params"))
        self.dockWidget_Params.setWidget(self.dockWidgetContents_10)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_Params)

        #DockWidget_LogScreen
        self.dockWidget_LogScreen = QtGui.QDockWidget("Log Ekrani")
        self.dockWidget_LogScreen.setMaximumSize(QtCore.QSize(524287, 130))
        self.dockWidget_LogScreen.setObjectName(_fromUtf8("dockWidget_LogScreen"))
        self.dockWidgetContents_11 = QtGui.QWidget()
        self.dockWidgetContents_11.setObjectName(_fromUtf8("dockWidgetContents_11"))
        self.gridLayout_5 = QtGui.QGridLayout(self.dockWidgetContents_11)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))

        self.textEdit_LogScreen = QtGui.QTextEdit(self.dockWidgetContents_11)
        self.textEdit_LogScreen.setObjectName(_fromUtf8("textEdit_LogScreen"))
        self.textEdit_LogScreen.setReadOnly(True)
        p = QtGui.QPalette()
        p.setColor(QtGui.QPalette.Base, QtGui.QColor(0,0,0))
        self.textEdit_LogScreen.setPalette(p)
        self.textEdit_LogScreen.setTextColor(QtGui.QColor(255,255,255))
        self.gridLayout_5.addWidget(self.textEdit_LogScreen, 0, 0, 1, 1)
        self.dockWidget_LogScreen.setWidget(self.dockWidgetContents_11)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_LogScreen)

        #DockWidget_Graphs
        self.dockWidget_Graphs = QtGui.QDockWidget("Grafikler")
        self.dockWidget_Graphs.setObjectName(_fromUtf8("dockWidget_Graphs"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_Graphs = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_Graphs.setObjectName(_fromUtf8("gridLayout_Graphs"))
        self.mplwidget = MatplotlibWidget(self.dockWidgetContents)
        self.mplwidget.setObjectName(_fromUtf8("mplwidget"))
        self.gridLayout_Graphs.addWidget(self.mplwidget, 0, 0, 1, 1)
        self.dockWidget_Graphs.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_Graphs)

        #--------------------------------------------------------------------

                #------------- STATUS BAR-----------------#
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

                #------------- TOOL BAR-----------------#
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.actionOpenFile_tb = QtGui.QAction(MainWindow)
        self.actionOpenFile_tb.setObjectName("actionOpenFile_tb")
        self.actionOpenFile_tb.setIcon(QtGui.QIcon("resources/open.png"))
        self.toolBar.addAction(self.actionOpenFile_tb)

        self.actionSave_tb = QtGui.QAction(MainWindow)
        self.actionSave_tb.setObjectName("actionSave_tb")
        self.actionSave_tb.setIcon(QtGui.QIcon("resources/save.png"))
        self.toolBar.addAction(self.actionSave_tb)

                #------------- MENU BAR-----------------#
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.menuDosya = QtGui.QMenu(self.menubar)
        self.menuDosya.setObjectName(_fromUtf8("menuDosya"))

        self.menuData = QtGui.QMenu(self.menubar)
        self.menuData.setObjectName(_fromUtf8("menuData"))

        self.menuTable = QtGui.QMenu(self.menubar)
        self.menuTable.setObjectName(_fromUtf8("menuTable"))
        self.menuTable.setEnabled(False);

        self.menuSiniflama = QtGui.QMenu(self.menubar)
        self.menuSiniflama.setObjectName(_fromUtf8("menuSiniflama"))

        self.menuKumeleme = QtGui.QMenu(self.menubar)
        self.menuKumeleme.setObjectName(_fromUtf8("menuKumeleme"))

        self.menuGrafikler = QtGui.QMenu(self.menubar)
        self.menuGrafikler.setObjectName(_fromUtf8("menuGrafikler"))

        self.menuYardim = QtGui.QMenu(self.menubar)
        self.menuYardim.setObjectName(_fromUtf8("menuYardim"))

        self.menuDagilimlar = QtGui.QMenu(self.menubar)
        self.menuDagilimlar.setObjectName(_fromUtf8("menuDagilimlar"))

        self.menuPreprocessing = QtGui.QMenu(self.menubar)
        self.menuPreprocessing.setObjectName(_fromUtf8("menuProcessing"))


        MainWindow.setMenuBar(self.menubar)

        # Menu Kumeleme Actions
        self.actionKMeans = QtGui.QAction(MainWindow)
        self.actionKMeans.setObjectName(_fromUtf8("actionKMeans"))

        self.actionKMedoids = QtGui.QAction(MainWindow)
        self.actionKMedoids.setObjectName(_fromUtf8("actionKMedoids"))

        self.actionFuzzyCMeans = QtGui.QAction(MainWindow)
        self.actionFuzzyCMeans.setObjectName(_fromUtf8("actionFuzzyCMeans"))

        self.actionHierarchy = QtGui.QAction(MainWindow)
        self.actionHierarchy.setObjectName(_fromUtf8("actionHierarchy"))

        self.actionEM = QtGui.QAction(MainWindow)
        self.actionEM.setObjectName(_fromUtf8("actionEM"))

        self.actionDBSCAN = QtGui.QAction(MainWindow)
        self.actionDBSCAN.setObjectName(_fromUtf8("actionDBSCAN"))

        self.actionSOM = QtGui.QAction(MainWindow)
        self.actionSOM.setObjectName(_fromUtf8("actionSOM"))

        self.menuKumeleme.addAction(self.actionKMeans)
        self.menuKumeleme.addAction(self.actionKMedoids)
        self.menuKumeleme.addAction(self.actionFuzzyCMeans)
        self.menuKumeleme.addAction(self.actionHierarchy)
        self.menuKumeleme.addAction(self.actionEM)
        self.menuKumeleme.addAction(self.actionDBSCAN)
        self.menuKumeleme.addAction(self.actionSOM)

        # Menu PreProcessing Actions
        self.actionPca = QtGui.QAction(MainWindow)
        self.actionPca.setObjectName(_fromUtf8("actionPca"))

        self.actionSvd = QtGui.QAction(MainWindow)
        self.actionSvd.setObjectName(_fromUtf8("actionSvd"))

        self.menuPreprocessing.addAction(self.actionPca)
        self.menuPreprocessing.addAction(self.actionSvd)

        # Menu Table Actions
        self.actionAddRow = QtGui.QAction(MainWindow)
        self.actionAddRow.setObjectName(_fromUtf8("actionAddRow"))

        self.actionDelRow = QtGui.QAction(MainWindow)
        self.actionDelRow.setObjectName(_fromUtf8("actionDelRow"))

        self.actionAddClm = QtGui.QAction(MainWindow)
        self.actionAddClm.setObjectName(_fromUtf8("actionAddClm"))

        self.actionDelClm = QtGui.QAction(MainWindow)
        self.actionDelClm.setObjectName(_fromUtf8("actionDelClm"))

        self.menuTable.addAction(self.actionAddRow)
        self.menuTable.addAction(self.actionDelRow)
        self.menuTable.addAction(self.actionAddClm)
        self.menuTable.addAction(self.actionDelClm)

        # Menu Grafikler Actions
        self.actionPie_Chart = QtGui.QAction(MainWindow)
        self.actionPie_Chart.setObjectName(_fromUtf8("actionPie_Chart"))

        self.actionBar_Chart = QtGui.QAction(MainWindow)
        self.actionBar_Chart.setObjectName(_fromUtf8("actionBar_Chart"))

        self.actionHistogram = QtGui.QAction(MainWindow)
        self.actionHistogram.setObjectName(_fromUtf8("actionHistogram"))

        self.actionBox_Plot = QtGui.QAction(MainWindow)
        self.actionBox_Plot.setObjectName(_fromUtf8("actionBox_Plot"))

        self.actionScatter = QtGui.QAction(MainWindow)
        self.actionScatter.setObjectName(_fromUtf8("actionScatter"))
        self.actionScatter.setText("Scatter")

        self.actionLine = QtGui.QAction(MainWindow)
        self.actionLine.setObjectName("actionLine")
        self.actionLine.setText("Line Chart")

        self.menuGrafikler.addAction(self.actionPie_Chart)
        self.menuGrafikler.addAction(self.actionBar_Chart)
        self.menuGrafikler.addAction(self.actionHistogram)
        self.menuGrafikler.addAction(self.actionBox_Plot)
        self.menuGrafikler.addAction(self.actionScatter)
        self.menuGrafikler.addAction(self.actionLine)

        # Menu Dosya Actions
        self.actionOpenFile = QtGui.QAction(MainWindow)
        self.actionOpenFile.setObjectName(_fromUtf8("actionOpenFile"))
        self.actionOpenFile.setStatusTip(_translate("MainWindow", "Dataset yüklemenizi sağlar", None))

        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))

        self.actionSaveAs = QtGui.QAction(MainWindow)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))

        self.actionSaveOutput = QtGui.QAction(MainWindow)
        self.actionSaveOutput.setObjectName(_fromUtf8("actionSaveOutput"))

        self.menuOpenRecentFiles = QtGui.QMenu(MainWindow)
        self.menuOpenRecentFiles.setObjectName(_fromUtf8("actionRecentFiles"))

        self.menuDosya.addAction(self.actionOpenFile)
        self.menuDosya.addAction(self.actionSave)
        self.menuDosya.addAction(self.actionSaveAs)
        self.menuDosya.addSeparator()
        self.menuDosya.addAction(self.actionSaveOutput)
        self.menuDosya.addSeparator()
        self.menuDosya.addMenu(self.menuOpenRecentFiles)

        # Adding All Actions to Menubar
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuTable.menuAction())
        self.menubar.addAction(self.menuSiniflama.menuAction())
        self.menubar.addAction(self.menuKumeleme.menuAction())
        self.menubar.addAction(self.menuPreprocessing.menuAction())
        self.menubar.addAction(self.menuGrafikler.menuAction())
        self.menubar.addAction(self.menuDagilimlar.menuAction())
        self.menubar.addAction(self.menuYardim.menuAction())

        # Menu Dagilimlar Actions
        self.submenuContinuousDist = QtGui.QMenu(MainWindow)
        self.submenuContinuousDist.setObjectName(_fromUtf8("actionContinuousDist"))

        self.submenuDescreteDist = QtGui.QMenu(MainWindow)
        self.submenuDescreteDist.setObjectName(_fromUtf8("actionDescreteDist"))

        # --menu dagilimlar - alt menuler
        self.submenuNormalDist = QtGui.QMenu(MainWindow)
        self.submenuNormalDist.setObjectName(_fromUtf8("actionNormalDist"))

        self.submenuTDist = QtGui.QMenu(MainWindow)
        self.submenuTDist.setObjectName(_fromUtf8("actionTDist"))

        self.submenuChiSquaredDist = QtGui.QMenu(MainWindow)
        self.submenuChiSquaredDist.setObjectName(_fromUtf8("actionChiSquaredDist"))
        
        self.submenuFDist = QtGui.QMenu(MainWindow)
        self.submenuFDist.setObjectName(_fromUtf8("submenuFDist"))
        # --/menu dagilimlar - alt menuler

        # --menu dagilimlar - alt menuler - alt menuleri
        self.actionNormalQuantiles = QtGui.QAction(MainWindow)
        self.actionNormalQuantiles.setObjectName(_fromUtf8("actionNormalQuan"))

        self.actionNormalProbabilities = QtGui.QAction(MainWindow)
        self.actionNormalProbabilities.setObjectName(_fromUtf8("actionNormalProb"))

        self.actionPlotNormalDist = QtGui.QAction(MainWindow)
        self.actionPlotNormalDist.setObjectName(_fromUtf8("actionPlotNormalDist"))


        self.actionTQuantiles = QtGui.QAction(MainWindow)
        self.actionTQuantiles.setObjectName(_fromUtf8("actionTQuan"))

        self.actionTProbabilities = QtGui.QAction(MainWindow)
        self.actionTProbabilities.setObjectName(_fromUtf8("actionTProb"))

        self.actionPlotTDist = QtGui.QAction(MainWindow)
        self.actionPlotTDist.setObjectName(_fromUtf8("actionPlotTDist"))


        self.actionChi2Quantiles = QtGui.QAction(MainWindow)
        self.actionChi2Quantiles.setObjectName(_fromUtf8("actionChi2Quan"))

        self.actionChi2Probabilities = QtGui.QAction(MainWindow)
        self.actionChi2Probabilities.setObjectName(_fromUtf8("actionChi2Prob"))

        self.actionPlotChi2Dist = QtGui.QAction(MainWindow)
        self.actionPlotChi2Dist.setObjectName(_fromUtf8("actionPlotChi2Dist"))


        self.actionFQuantiles = QtGui.QAction(MainWindow)
        self.actionFQuantiles.setObjectName(_fromUtf8("actionFQuan"))

        self.actionFProbabilities = QtGui.QAction(MainWindow)
        self.actionFProbabilities.setObjectName(_fromUtf8("actionFProb"))

        self.actionPlotFDist = QtGui.QAction(MainWindow)
        self.actionPlotFDist.setObjectName(_fromUtf8("actionPlotFDist"))


        self.menuDagilimlar.addMenu(self.submenuContinuousDist)
        self.menuDagilimlar.addMenu(self.submenuDescreteDist)


        self.submenuContinuousDist.addMenu(self.submenuNormalDist)
        self.submenuContinuousDist.addMenu(self.submenuTDist)
        self.submenuContinuousDist.addMenu(self.submenuChiSquaredDist)
        self.submenuContinuousDist.addMenu(self.submenuFDist)

        self.submenuNormalDist.addAction(self.actionNormalQuantiles)
        self.submenuNormalDist.addAction(self.actionNormalProbabilities)
        self.submenuNormalDist.addAction(self.actionPlotNormalDist)

        self.submenuTDist.addAction(self.actionTQuantiles)
        self.submenuTDist.addAction(self.actionTProbabilities)
        self.submenuTDist.addAction(self.actionPlotTDist)

        self.submenuChiSquaredDist.addAction(self.actionChi2Quantiles)
        self.submenuChiSquaredDist.addAction(self.actionChi2Probabilities)
        self.submenuChiSquaredDist.addAction(self.actionPlotChi2Dist)

        self.submenuFDist.addAction(self.actionFQuantiles)
        self.submenuFDist.addAction(self.actionFProbabilities)
        self.submenuFDist.addAction(self.actionPlotFDist)

        self.submenuFDist.addActions([self.actionFQuantiles,self.actionFProbabilities, self.actionPlotFDist])


        self.actionHakkinda = QtGui.QAction(MainWindow)
        self.actionHakkinda.setObjectName("actionHakkinda")
        self.menuYardim.addAction(self.actionHakkinda)

        self.actionOrnekVeri = QtGui.QAction(MainWindow)
        self.actionOrnekVeri.setObjectName("actionOrnekVeri")
        self.menuData.addAction(self.actionOrnekVeri)

        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuYardim.addAction(self.actionHelp)
        
        #---------------SIGNALS-----------------------------#

        self.connect(self.actionOpenFile, QtCore.SIGNAL("triggered()"), lambda path = None: self.OpenFile(path))
        self.connect(self.actionOpenFile_tb, QtCore.SIGNAL("triggered()"), lambda path = None: self.OpenFile(path))
        self.connect(self.actionSave, QtCore.SIGNAL("triggered()"), self.SaveFile)  
        self.connect(self.actionSave_tb, QtCore.SIGNAL("triggered()"), self.SaveFile)
        self.connect(self.actionSaveAs, QtCore.SIGNAL("triggered()"), self.SaveFileAs)
        
        self.connect(self.actionPie_Chart, QtCore.SIGNAL("triggered()"), self.CallPieChart)
        self.connect(self.actionBar_Chart, QtCore.SIGNAL("triggered()"), self.CallBarChart)
        self.connect(self.actionBox_Plot, QtCore.SIGNAL("triggered()"), self.CallBoxPlot)
        self.connect(self.actionHistogram, QtCore.SIGNAL("triggered()"), self.CallHistogram)
        self.connect(self.actionScatter, QtCore.SIGNAL("triggered()"), self.CallScatter)
        self.connect(self.actionLine, QtCore.SIGNAL("triggered()"), self.CallLineChart)

        #--------------CLUSTER -----------------------#

        self.connect(self.actionKMeans, QtCore.SIGNAL("triggered()"), self.CallKmeans)
        self.connect(self.actionKMedoids, QtCore.SIGNAL("triggered()"), self.CallKmedoids)
        self.connect(self.actionFuzzyCMeans, QtCore.SIGNAL("triggered()"), self.CallFuzzy)
        self.connect(self.actionHierarchy, QtCore.SIGNAL("triggered()"), self.CallHiearachy)
        self.connect(self.actionDBSCAN, QtCore.SIGNAL("triggered()"), self.CallDbscan)
        self.connect(self.actionSOM, QtCore.SIGNAL("triggered()"), self.CallSom)
        self.connect(self.actionEM, QtCore.SIGNAL("triggered()"), self.CallEm)

        #-------------END CLUSTER---------------------------#

        #--------------PreProcessing---------------------#
        self.connect(self.actionPca, QtCore.SIGNAL("triggered()"), self.CallPca)
        self.connect(self.actionSvd, QtCore.SIGNAL("triggered()"), self.CallSvd)
        #-------------END PreProcessing---------------------------#

        #-----------------Table----------------------------#
        self.connect(self.actionAddRow, QtCore.SIGNAL("triggered()"), self.Add_row)
        self.connect(self.actionDelRow, QtCore.SIGNAL("triggered()"), self.Delete_row)
        self.connect(self.actionAddClm, QtCore.SIGNAL("triggered()"), self.Add_clm)
        self.connect(self.actionDelClm, QtCore.SIGNAL("triggered()"), self.Del_clm)
        #-----------------End Table----------------------------#

        self.connect(self.actionNormalQuantiles, QtCore.SIGNAL("triggered()"), self.NormQuan)
        self.connect(self.actionNormalProbabilities, QtCore.SIGNAL("triggered()"), self.NormProbs)
        self.connect(self.actionPlotNormalDist, QtCore.SIGNAL("triggered()"), self.NormPlot)

        self.connect(self.actionTQuantiles, QtCore.SIGNAL("triggered()"), self.T_ChiQuan)
        self.connect(self.actionTProbabilities, QtCore.SIGNAL("triggered()"), self.T_ChiProbs)
        self.connect(self.actionPlotTDist, QtCore.SIGNAL("triggered()"), self.CallTDistributionPlot)

        self.connect(self.actionChi2Quantiles, QtCore.SIGNAL("triggered()"), self.T_ChiQuan)
        self.connect(self.actionChi2Probabilities, QtCore.SIGNAL("triggered()"), self.T_ChiProbs)
        self.connect(self.actionPlotChi2Dist, QtCore.SIGNAL("triggered()"), self.CallChi2DistributionPlot)

        self.connect(self.actionFQuantiles, QtCore.SIGNAL("triggered()"), self.F_Quan)
        self.connect(self.actionFProbabilities, QtCore.SIGNAL("triggered()"), self.F_Probs)
        self.connect(self.actionPlotFDist, QtCore.SIGNAL("triggered()"), self.F_Plot)  

        self.connect(self.actionHakkinda, QtCore.SIGNAL("triggered()"), self.CallAboutPiva)

        self.connect(self.actionOrnekVeri, QtCore.SIGNAL("triggered()"), self.CallOrnekVeri)

        self.connect(self.actionHelp, QtCore.SIGNAL("triggered()"), self.CallHelp)
        #--------------END OF SIGNALS-----------------------#

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.CheckRecentFiles()
        
        #---------------SLOTS-----------------------------#


    def OpenFile(self, path):
        self.path = path
        tmp = self.CreateDataSet()
        if tmp == 0:
            return 0

        self.menuTable.setEnabled(True)

        #datamizi olusturdugumuz tabloya aktarıp, layout'a yerlestirir
        self.table = TableOperations.CreateTable(self.centralwidget, self.myDataSet.featureCount,
                                                 self.myDataSet.lineCount, self.myDataSet.features)
        self.dockWidget_DataSet.setWidget(self.table)

        for row in range(0, self.myDataSet.featureCount):

            featureData = self.myDataSet.dataSetDic[self.myDataSet.features[row]]
            for column in range(0, self.myDataSet.lineCount):
                self.table.setItem(column, row, QtGui.QTableWidgetItem(str(featureData[column].value)))

        self.row_count = self.myDataSet.lineCount
        self.col_count = self.myDataSet.featureCount
        self.WriteLog("Veriseti tablo seklinde gorsellendi")

        self.AddRecentFile()
        self.ControlRecentFiles()

        self.CheckLayoutParams()
        self.CheckLayoutGraphs()

    def CreateDataSet(self):
        #Dosyamizi acarak, dataset nesnemizi olusturur
        self.myDataSet, self.fileInfo = FileOperations.OpenNewFile(self, self.path)

        if self.myDataSet == 0:
            return 0
        return 1

    def Add_row(self):
        self.row_count += 1
        self.table.setRowCount(self.row_count)
        for clm in range(0, self.col_count):
            self.table.setItem(self.row_count-1, clm, QtGui.QTableWidgetItem(str('')))

    def Delete_row(self):
        items = sorted(set(index.row() for index in
                      self.table.selectedIndexes()))
        items = items[::-1]

        if items:
            for item in items:
                self.table.removeRow(item)
        self.row_count -= len(items)
        self.table.setRowCount(self.row_count)

    def Add_clm(self):
        items = self.CallAddColumn()
        if items[0]:
            self.col_count += 1
            self.table.insertColumn(self.col_count-1)
            self.table.setHorizontalHeaderItem(self.col_count-1, QtGui.QTableWidgetItem(items[0]))
            if items[1]:
                try:
                    parser = Parser()
                    expr = parser.parse(str(items[1]))
                    variables = []
                    indexes = []
                    variables = expr.variables()
                    for i in range(len(variables)):
                        for j in range(self.col_count):
                            if variables[i] == self.table.horizontalHeaderItem(j).text():
                                indexes.append(j)
                                break
                    dict = {}
                    for satir in range(self.row_count):
                        for vari in range(len(variables)):
                            dict.update( {variables[vari]: self.table.item(satir,indexes[vari]).text()} )
                        self.table.setItem(satir, self.col_count-1, QtGui.QTableWidgetItem(str(Parsero.evaluate(str(items[1]), dict))))

                except Exception:
                    self.table.removeColumn(self.col_count)
                    self.col_count -= 1
                    self.table.setColumnCount(self.col_count)
                    Errors.ShowWarningMsgBox(self, u"Formül Hatalı!")
                    self.Add_clm() # formulun yanlis girilmesi durumunda tekrar sutun ekleme ekrani acilir
        else:
            Errors.ShowWarningMsgBox(self, u"Sütun ismi giriniz!")
            self.Add_clm() # formulun yanlis girilmesi durumunda tekrar sutun ekleme ekrani acilir

    def Del_clm(self):
        items = sorted(set(index.column() for index in
                      self.table.selectedIndexes()))
        items = items[::-1]
        if items:
            for item in items:
                self.table.removeColumn(item)
        self.col_count -= len(items)
        self.table.setColumnCount(self.col_count)

    def SaveFile(self):
        try:
            FileOperations.CreateAndWriteFile(self, self.table, self.path)
            self.CreateDataSet()
        except Exception:
            Errors.ShowWarningMsgBox(self, u"Kayıt Gerçekleşmedi")

    def SaveFileAs(self):
        try:
            FileOperations.CreateAndWriteFile(self, self.table, None)#self.myDataSet.lines
            self.CreateDataSet()
        except Exception:
            Errors.ShowWarningMsgBox(self, u"Dataset bulunmamaktadır")

    # Parametrelerin yer alacagi layout ta
    # herhangi bir widget in olup olmadigini 
    # kontrol eder.
    def CheckLayoutParams(self):

        if not self.gridLayout_Params.isEmpty():
                for i in reversed(range(self.gridLayout_Params.count())):
                    self.gridLayout_Params.itemAt(i).widget().deleteLater()
        self.CheckLayoutGraphs()

    # Mpl widgetlarin yer alacagi layout ta
    # herhangi bir widget in olup olmadigini 
    # kontrol eder.
    def CheckLayoutGraphs(self):

        if not self.gridLayout_Graphs.isEmpty():
            for i in reversed(range(self.gridLayout_Graphs.count())):
                self.gridLayout_Graphs.itemAt(i).widget().deleteLater()

    def SetDlgParamsTitle(self, title):

        self.dockWidget_Params.setWindowTitle(title)

    def CallTDistributionPlot(self):
        self.T_ChiPlot(True)

    def CallChi2DistributionPlot(self):
        self.T_ChiPlot(False)

    def CheckRecentFiles(self):

        if not os.path.isdir("RecentFiles"):
            os.makedirs("RecentFiles")
            self.recentFilesPath = 'RecentFiles'
            return

        self.recentFilesPath = 'RecentFiles'

        self.ControlRecentFiles()

    def AddRecentFile(self):

        path = self.recentFilesPath

        filesCount = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])

        if filesCount > 5:            
            oldestFile = self.FindOldestFile(path)
            os.remove(oldestFile)

        src =str(self.fileInfo.filePath())
        dst = str(path + "/" + str(self.fileInfo.fileName()))
        if src != dst:
            shutil.copy(src, dst)

    def FindOldestFile(self, rootfolder):
        return min(
            (os.path.join(dirname, filename)
            for dirname, dirnames, filenames in os.walk(rootfolder)
            for filename in filenames),
            key=lambda fn: os.stat(fn).st_mtime)

    def ControlRecentFiles(self):

        self.menuOpenRecentFiles.clear()
        files = os.listdir(self.recentFilesPath)

        for file in files:
            self.actionRecent = QtGui.QAction(MainWindow)
            self.actionRecent.setObjectName(file)
            self.menuOpenRecentFiles.addAction(self.actionRecent)
            self.actionRecent.setText(file)
            self.connect(self.actionRecent, QtCore.SIGNAL("triggered()"), lambda file1 = file: self.OpenRecentFile(file1))

    def OpenRecentFile(self, file):

        filePath = "RecentFiles/" + file

        self.OpenFile(filePath)

        self.WriteLog(file+" Dosyasi basariyla yuklendi")

    def CallAboutPiva(self):

        dlg = StartDlgAboutPiva()

        if dlg.exec_():

            a=0

    def CallOrnekVeri(self):

        fileInfo =QtCore.QFileInfo(QtGui.QFileDialog.getOpenFileName(
            self, "Open Directory",
            "OrnekVeri"))

        self.OpenFile(fileInfo.filePath())


    def CallHelp(self):

        new = 2
        url = "file:\\D:\PycharmProjects\proje\kume_yardım\dene.html"
        webbrowser.get().open(url, new=new)

    def CallKmeans(self):
        self.CheckLayoutParams()
        try:
            self.km = StartKmeans(self.myDataSet)
            self.gridLayout_Params.addWidget(self.km, 0, 0, 1, 1)
            self.km.OkButton.clicked.connect(self.kmeansout)
        except:
             Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")


    def kmeansout(self):
        self.clearOutput()
        kume_eleman = self.km.kume_eleman
        iterasyon = self.km.iterasyon

        self.WriteOutput('iterasyon sayısı : ' + str(iterasyon))
        for i in range(len(kume_eleman)):
            self.WriteOutput('\n %d. kümedeki eleman sayısı: '%(i+1) + str(kume_eleman[i]))

    def CallKmedoids(self):
        self.CheckLayoutParams()
        try:
            self.kmd = StartKmedoids(self.myDataSet)
            self.gridLayout_Params.addWidget(self.kmd, 0, 0, 1, 1)
            self.kmd.OkButton.clicked.connect(self.kmedoidsout)
        except:
            Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")

    def kmedoidsout(self):
        self.clearOutput()
        kume_eleman = self.kmd.kume_eleman
        iterasyon = self.kmd.iterasyon

        self.WriteOutput('iterasyon sayısı : ' + str(iterasyon))
        for i in range(len(kume_eleman)):
            self.WriteOutput('\n %d. kümedeki eleman sayısı: '%(i) + str(kume_eleman[i]))

    def CallFuzzy(self):
        self.CheckLayoutParams()
        try:
            fz = StartFuzzy(self.myDataSet)
            self.gridLayout_Params.addWidget(fz, 0, 0, 1, 1)

        except:
            Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")

    def CallHiearachy(self):
        self.CheckLayoutParams()
        try:
            hier = StartHiearachy(self.myDataSet)
            self.gridLayout_Params.addWidget(hier, 0, 0, 1, 1)

        except:
            Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")

    def CallDbscan(self):
        self.CheckLayoutParams()
        try:
            dbs = StartDbscan(self.myDataSet)
            self.gridLayout_Params.addWidget(dbs, 0, 0, 1, 1)

        except:
            Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")

    def CallSom(self):
        self.CheckLayoutParams()
        try:
            som = StartSom(self.myDataSet)
            self.gridLayout_Params.addWidget(som, 0, 0, 1, 1)

        except:
            Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")

    def CallEm(self):
        self.CheckLayoutParams()
        try:
            em = StartEm(self.myDataSet)
            self.gridLayout_Params.addWidget(em, 0, 0, 1, 1)

        except:
            Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")

    def CallPca(self):
        self.CheckLayoutParams()
        try:
            self.pca = StartPca(self.myDataSet)
            self.gridLayout_Params.addWidget(self.pca, 0, 0, 1, 1)
            self.pca.OkButton.clicked.connect(self.pcaOut)
        except:
            Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")

    def pcaOut(self):
        self.clearOutput()
        eigValue = self.pca.eigValue1
        eigCov = str(self.pca.covMatris)
        sonveri = str(self.pca.last)
        yer = self.pca.yer
        value= self.pca.value
        ozellik_sayisi = self.pca.secilenOzellikSayisi
        self.WriteOutput('Kovaryans matrisi: \n' + str(eigCov))
        self.WriteOutput('\nEigenvalue(özdeğer) \n')
        for i in range(len(eigValue)):
            out1 = str(value[i]) + ": " + str(eigValue[i])
            output = out1
            self.WriteOutput(output)

        self.WriteOutput('\nSeçilen özellik sayısı: ' + str(ozellik_sayisi) + '\n')
        for i in range(ozellik_sayisi):
            self.WriteOutput("Seçilen özellik: " + str(value[yer[i]]))

        self.WriteOutput('\nSon veri: \n' + str(sonveri))

    def CallSvd(self):
        self.CheckLayoutParams()
        try:
            self.svd = StartSvd(self.myDataSet)
            self.gridLayout_Params.addWidget(self.svd, 0, 0, 1, 1)
            self.svd.OkButton.clicked.connect(self.svdOut)
        except:
            Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")

    def svdOut(self):
        self.clearOutput()
        value = self.svd.value
        U = self.svd.Uo
        self.WriteOutput('U: ' + str(U) + '\n')
        s = self.svd.So
        self.WriteOutput('s: ' + str(s) + '\n')
        v = self.svd.Vo
        self.WriteOutput('V: ' + str(v) + '\n')
        npdot = self.svd.npdot
        self.WriteOutput('ilk matrisin bir daha elde edilmesi:\n' + str(npdot) + '\n')
        ozellik_sayisi = self.svd.secilenOzellikSayisi
        self.WriteOutput('Seçilen özellik sayısı: ' + str(ozellik_sayisi) + '\n')
        sList = self.svd.s
        yer = self.svd.yer
        for i in range(ozellik_sayisi):
            self.WriteOutput(str(value[yer[i]]) + ' tekil değeri: ' + str(sList[i]))

    def CallAddColumn(self):
        items = []
        dlg = StartDialogClm()
        if dlg.exec_():
            a = 0
        items.append(dlg.title)
        items.append(dlg.formul)
        return items



    ### PIE CHART ###

    # Pie chart icin parametre alacak dialog penceresini
    # olusturur ve yerlestirir. Sonra pie chart cizdirecek 
    # fonksiyonu cagirir.
    def CallPieChart(self):

        self.CheckLayoutParams()

        try:         
            self.dlg = StartDialogPieChart()

            if self.myDataSet.nonNumericFeatures > 0:
                self.dlg.ClearComboBox()
                self.dlg.SetComboBox(self.myDataSet.nonNumericFeatures)
            else:
                Errors.ShowInfoMsgBox(self, "Verisetinde uygun ozellik yer almamaktadır")

            self.gridLayout_Params.addWidget(self.dlg, 0, 0, 1, 1)
            self.SetDlgParamsTitle("Pie Chart Parametreleri")

            self.connect(self.dlg.pushButton, QtCore.SIGNAL("clicked()"), self.CreatePieChart)
    
        except:
            Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")

    # uygun parametreleri aldiktan sonra pie chart cizer 
    # ve layout a yerlestirir.
    def CreatePieChart(self):
        self.WriteLog("Pie Chart cizdiriliyor..")
        nonNumeric = str(self.dlg.comboBox.currentText())
        values, counts = self.myDataSet.GetNonNumericValues(nonNumeric)
        try:
            frame = ChartCreator.CreatePieChart(values, counts)
               
            self.CheckLayoutGraphs()   
                                           
            self.gridLayout_Graphs.addWidget(frame, 0,0,1,1)

            self.WriteLog("Pie Chart basarili bir sekilde cizdirildi")

        except: # Exception e:
            self.WriteLog("Pie Chart cizdirilemedi : ")
    
    ### BAR CHART ###
    def CallBarChart(self):

        self.CheckLayoutParams()

        try:         
            self.dlg = StartDialogBarChart()

            if self.myDataSet.nonNumericFeatures > 0:
                self.dlg.ClearComboBox()
                self.dlg.SetComboBox(self.myDataSet.nonNumericFeatures)
            else:
                Errors.ShowInfoMsgBox(self, "Verisetinde uygun ozellik yer almamaktadır")

            self.gridLayout_Params.addWidget(self.dlg, 0, 0, 1, 1)
            self.SetDlgParamsTitle("Bar Chart Parametreleri")

            self.connect(self.dlg.pushButton, QtCore.SIGNAL("clicked()"), self.CreateBarChart)

        except:
            Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")

    def CreateBarChart(self):

        self.WriteLog("Bar Chart cizdiriliyor..")

        nonNumeric = str(self.dlg.comboBox.currentText())
        values, counts = self.myDataSet.GetNonNumericValues(nonNumeric)

        width = 0.25
        stdDv = None

        try:
            self.main_frame = ChartCreator.CreateBarChart(counts, width, stdDv, values)
        
            self.CheckLayoutGraphs()

            self.gridLayout_Graphs.addWidget(self.main_frame, 0, 0, 1, 1)

            self.WriteLog("Bar Chart basarili bir sekilde cizdirildi")

        except Exception,e:
            self.WriteLog("Bar Chart cizdirilemedi : " + e.message)

    ### BOX PLOT ###
    def CallBoxPlot(self):

        self.CheckLayoutParams()

        try:         
            self.dlg = StartDialogBoxPlot()

            if self.myDataSet.numericFeatures > 0:
                self.dlg.ClearComboBox()
                self.dlg.SetComboBox(self.myDataSet.numericFeatures)
            else:
                Errors.ShowInfoMsgBox(self, "Verisetinde uygun ozellik yer almamaktadır")

            self.gridLayout_Params.addWidget(self.dlg, 0, 0, 1, 1)
            self.SetDlgParamsTitle("Box Plot Parametreleri")

            self.connect(self.dlg.pushButton_Goster, QtCore.SIGNAL("clicked()"), self.CreateBoxPlot)
            self.connect(self.dlg.pushButton_Ekle, QtCore.SIGNAL("clicked()"), self.ButtonEkleClicked)
            self.connect(self.dlg.pushButton_hepsiniEkle, QtCore.SIGNAL("clicked()"), self.ButtonHepEkleClicked)
            self.connect(self.dlg.pushButton_Temizle, QtCore.SIGNAL("clicked()"), self.ButtonTemizleClicked)

        except:
            Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")

    def ButtonEkleClicked(self):

        ozellik = self.dlg.GetChoosenFeature()

        if self.dlg.eklenenler.count(ozellik) > 0:
            Errors.ShowInfoMsgBox(self, "Sectiginiz ozellik zaten eklenmistir")
            return
        else:
            self.dlg.textEdit.append(ozellik)
            self.dlg.eklenenler.append(ozellik)
            self.WriteLog("Ozellik eklendi: " + ozellik)

    def ButtonHepEkleClicked(self):

        self.dlg.ClearTextEdit()

        for ozellik in self.myDataSet.numericFeatures:
            self.dlg.textEdit.append(ozellik)
            if self.dlg.eklenenler.count(ozellik) == 0:
                self.dlg.eklenenler.append(ozellik)

        self.WriteLog("Ozelliklerin tamami eklendi")
    def ButtonTemizleClicked(self):

        self.dlg.ClearTextEdit()
        
        for a in range(len(self.dlg.eklenenler)):
            self.dlg.eklenenler.remove(self.dlg.eklenenler[0])

        self.WriteLog("Eklenen ozellikler kaldirildi")

    def CreateBoxPlot(self):

        serie = list()
        for ozellik in self.dlg.eklenenler:
            values, counts = self.myDataSet.GetNumericValues(ozellik)
            serie.append(values)
        try:
            self.main_frame = ChartCreator.CreateBoxPlot(serie, self.dlg.eklenenler)

            self.CheckLayoutGraphs()

            self.gridLayout_Graphs.addWidget(self.main_frame, 0, 0, 1, 1)

            self.WriteLog("Box Plot basarili bir sekilde olusturuldu")
        except Exception, e:
            self.WriteLog("Box Plot olusturulamadi: " + e.message)

    ### HISTOGRAM ##
    def CallHistogram(self):

        self.CheckLayoutParams()

        try:         
            self.dlg = StartDialogHistogram()

            if self.myDataSet.numericFeatures > 0:
                self.dlg.ClearComboBox()
                self.dlg.SetComboBox(self.myDataSet.numericFeatures)
            else:
                Errors.ShowInfoMsgBox(self, "Verisetinde uygun ozellik yer almamaktadır")

            self.gridLayout_Params.addWidget(self.dlg, 0, 0, 1, 1)
            self.SetDlgParamsTitle("Histogram Parametreleri")

            self.connect(self.dlg.pushButton, QtCore.SIGNAL("clicked()"), self.CreateHistogram)

        except:
            Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")
        
    def CreateHistogram(self):
        
        self.WriteLog("Histogram cizdiriliyor..")

        numeric = str(self.dlg.comboBox.currentText())
        
        values = list()

        binCount = self.dlg.GetBinCount()

        for val in self.myDataSet.dataSetDic[numeric]:

            values.append(val.value)
        try:
            self.main_frame = ChartCreator.CreateHistogram(values, binCount)

            self.CheckLayoutGraphs()

            self.gridLayout_Graphs.addWidget(self.main_frame, 0, 0, 1, 1)

            self.WriteLog("Histogram basarili bir sekilde cizdirildi")
        except Exception, e:
            self.WriteLog("Histogram cizdirilemedi: " + e.message)

    ## SCATTER ##

    def CallScatter(self):

        self.CheckLayoutParams()

        try:         
            self.dlg = StartDialogScatter()

            if self.myDataSet.numericFeatures > 0:
                
                self.dlg.comboBox.addItems(self.myDataSet.numericFeatures)
                self.dlg.comboBox2.addItems(self.myDataSet.numericFeatures)
            else:
                Errors.ShowInfoMsgBox(self, "Verisetinde uygun ozellik yer almamaktadır")

            self.gridLayout_Params.addWidget(self.dlg, 0, 0, 1, 1)
            self.SetDlgParamsTitle("Scatter Chart Parametreleri")

            self.connect(self.dlg.pushButton, QtCore.SIGNAL("clicked()"), self.CreateScatter)

        except:
            Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")

    def CreateScatter(self):
        self.WriteLog("Scatter Chart cizdiriliyor..")
        numeric1 = str(self.dlg.comboBox.currentText())
        values1 = list()

        for val in self.myDataSet.dataSetDic[numeric1]:

            values1.append(val.value)

        numeric2 = str(self.dlg.comboBox2.currentText())
        values2 = list()

        for val in self.myDataSet.dataSetDic[numeric2]:

            values2.append(val.value)
        try:
            self.main_frame = ChartCreator.CreateScatter(values1, values2)

            self.CheckLayoutGraphs()

            self.gridLayout_Graphs.addWidget(self.main_frame, 0, 0, 1, 1)

            self.WriteLog("Scatter Chart basarili bir sekilde cizdirildi")
        except Exception,e:
            self.WriteLog("Scatter Chart cizdirilemedi: " + e.message)

    ## LINE CHART ##

    def CallLineChart(self):

        self.CheckLayoutParams()

        try:         
            self.dlg = StartDialogScatter()

            if self.myDataSet.numericFeatures > 0:
                
                self.dlg.comboBox.addItems(self.myDataSet.numericFeatures)
                self.dlg.comboBox2.addItems(self.myDataSet.numericFeatures)
            else:
                Errors.ShowInfoMsgBox(self, "Verisetinde uygun ozellik yer almamaktadır")

            self.gridLayout_Params.addWidget(self.dlg, 0, 0, 1, 1)
            self.SetDlgParamsTitle("Line Chart Parametreleri")

            self.connect(self.dlg.pushButton, QtCore.SIGNAL("clicked()"), self.CreateLineChart)

        except:
            Errors.ShowWarningMsgBox(self, "Lutfen veriseti yukleyiniz!")

    def CreateLineChart(self):

        self.WriteLog("Line Chart cizdiriliyor..")
        numeric1 = str(self.dlg.comboBox.currentText())
        values1 = list()

        for val in self.myDataSet.dataSetDic[numeric1]:

            values1.append(val.value)

        numeric2 = str(self.dlg.comboBox2.currentText())
        values2 = list()

        for val in self.myDataSet.dataSetDic[numeric2]:

            values2.append(val.value)
        try:
            self.main_frame = ChartCreator.CreateLinePlot(values1, values2)

            self.CheckLayoutGraphs()

            self.gridLayout_Graphs.addWidget(self.main_frame, 0, 0, 1, 1)
            self.WriteLog("Line Chart basarili bir sekilde cizdirildi")
        except Exception,e:
            self.WriteLog("Line Chart cizdirilemedi: "+ e.message)
        
    ### DAGILIMLAR ###
    def NormQuan(self):

        self.CheckLayoutParams()

        self.dlg = StartDlgNormQuan()

        self.dlg.SetDefault()

        self.gridLayout_Params.addWidget(self.dlg, 0,0,1,1)
        self.SetDlgParamsTitle("Normal Quantiles Parametreleri")

        self.connect(self.dlg.buttonApply, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CallNormQuan)

    def CallNormQuan(self):

            probs, mean, std, lower = self.dlg.GetValues()
            if probs != None:
                text, lower_yArray = Distributions.NormalQuantilesLowerTail(probs,mean,std)
                tail, yArrayStr = General_Func.getTailInfoAndCalculationRes(lower, lower_yArray)

                result = text + "  " + tail + "\n" + yArrayStr + "\n"
                self.WriteOutput(result)

            else:
                self.WriteLog(mean)
            

    def NormProbs(self):
        self.CheckLayoutParams()

        self.dlg = StartDlgNormProbs()

        self.dlg.SetDefault()

        self.gridLayout_Params.addWidget(self.dlg, 0,0,1,1)
        self.SetDlgParamsTitle("Normal Olasiliklar Parametreleri")

        self.connect(self.dlg.buttonApply, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CallNormProbs)

    def CallNormProbs(self):

            vals, mean, std, lower = self.dlg.GetValues()

            if vals != None:
                text, lower_yArray = Distributions.NormalProbabilitiesLowerTail(vals,mean,std)
                tail, yArrayStr = General_Func.getTailInfoAndCalculationRes(lower, lower_yArray)

                result = text + "  " + tail + "\n" + yArrayStr + "\n"
                self.WriteOutput(result)

            else:
                self.WriteLog(mean)
            

    def NormPlot(self):

        self.CheckLayoutParams()

        self.dlg = StartDlgNormPlot()

        self.dlg.SetDefault()

        self.gridLayout_Params.addWidget(self.dlg, 0,0,1,1)
        self.SetDlgParamsTitle("Normal Plot Parametreleri")

        self.connect(self.dlg.buttonApply, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CallNormPlot)

    def CallNormPlot(self):
        
            mean, std, density = self.dlg.GetValues()
            
            if mean != None:
                main_frame = None

                if density == True:
                    main_frame = Distributions.PlotNormalDistributionDensityFunction(mean,std)
                else:
                    main_frame = Distributions.PlotNormalDistributionDistributionFunction(mean,std)
                    
                self.CheckLayoutGraphs()

                self.gridLayout_Graphs.addWidget(main_frame, 0, 0, 1, 1)
            else:
                self.WriteLog(std)

    def T_ChiQuan(self):

        self.CheckLayoutParams()

        self.dlg = StartDlgTChiQuan()

        self.gridLayout_Params.addWidget(self.dlg, 0,0,1,1)
        self.SetDlgParamsTitle("T veya Chi-Square Quantiles Parametreleri")

        self.connect(self.dlg.buttonApply, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CallTChiQuan)

    def CallTChiQuan(self):

            probs, df, lower = self.dlg.GetValues()
            if probs != None:

                text, lower_yArray = Distributions.TQuantilesLowerTail(probs,df)
                tail, yArrayStr = General_Func.getTailInfoAndCalculationRes(lower, lower_yArray)

                result = text + "  " + tail + "\n" + yArrayStr + "\n"
                self.WriteOutput(result)

            else:
                self.WriteLog(df)

            
    def T_ChiProbs(self):

        self.CheckLayoutParams()

        self.dlg = StartDlgTChiProbs()

        self.gridLayout_Params.addWidget(self.dlg, 0,0,1,1)
        self.SetDlgParamsTitle("T veya Chi-Square Olasiliklar Parametreleri")

        self.connect(self.dlg.buttonApply, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CallTChiProbs)

    def CallTChiProbs(self):

            vals, df, lower = self.dlg.GetValues()
            if vals != None:
                text, lower_yArray = Distributions.TProbabilitiesLowerTail(vals, df)
                tail, yArrayStr = General_Func.getTailInfoAndCalculationRes(lower, lower_yArray)
                
                result = text + "  " + tail + "\n" + yArrayStr + "\n"
                self.WriteOutput(result)

            else: 
                self.WriteLog(df)
            

    def T_ChiPlot(self, isT):
        self.CheckLayoutParams()

        self.dlg = StartDlgTChiPlot()

        self.gridLayout_Params.addWidget(self.dlg, 0,0,1,1)
        self.SetDlgParamsTitle("T veya Chi-Square Plot Parametreleri")

        self.connect(self.dlg.buttonApply, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda tmp = isT: self.CallTChiPlot(tmp))
        
    def CallTChiPlot(self, isT):

            df, density = self.dlg.GetValues()

            if df != None:
                main_frame = None

                if isT == True:
                    if density == True:
                        main_frame = Distributions.PlotTDistributionDensityFunction(df)
                    else:
                        main_frame = Distributions.PlotTDistributionDistributionFunction(df) 
                else:
                    if density == True:
                        main_frame = Distributions.PlotChi2DistributionDensityFunction(df)
                    else: 
                        main_frame = Distributions.PlotChi2DistributionDistributionFunction(df)

                self.CheckLayoutGraphs()

                self.gridLayout_Graphs.addWidget(main_frame, 0, 0, 1, 1)
            else:
                self.WriteLog(density)
            

    def F_Quan(self):

        self.CheckLayoutParams()

        self.dlg = StartDlgFQuan()

        self.gridLayout_Params.addWidget(self.dlg, 0,0,1,1)

        self.SetDlgParamsTitle("F Quantiles Parametreleri")

        self.connect(self.dlg.buttonApply, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CallFQuan)

    def CallFQuan(self):

            probs, dfn, dfd, lower = self.dlg.GetValues()
            if probs != None:
                text, lower_yArray = Distributions.FQuantilesLowerTail(probs, dfn, dfd)
                tail, yArrayStr = General_Func.getTailInfoAndCalculationRes(lower, lower_yArray)

                result = text + "  " + tail + "\n" + yArrayStr + "\n"
                self.WriteOutput(result)
            else:
                self.WriteLog(dfn)
            

    def F_Probs(self):

        self.CheckLayoutParams()

        self.dlg = StartDlgFProbs()

        self.gridLayout_Params.addWidget(self.dlg, 0,0,1,1)
        self.SetDlgParamsTitle("F Olasiliklar Parametreleri")

        self.connect(self.dlg.buttonApply, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CallFProbs)

    def CallFProbs(self):

            vals, dfn, dfd, lower = self.dlg.GetValues()
            if vals != None:
                text, lower_yArray = Distributions.FProbabilitiesLowerTail(vals, dfn, dfd)
                tail, yArrayStr = General_Func.getTailInfoAndCalculationRes(lower, lower_yArray)

                result = text + "  " + tail + "\n" + yArrayStr + "\n"
                self.WriteOutput(result)

            else:
                self.WriteLog(dfn)

    def F_Plot(self):

        self.CheckLayoutParams()

        self.dlg = StartDlgFPlot()

        self.gridLayout_Params.addWidget(self.dlg, 0,0,1,1)
        self.SetDlgParamsTitle("F Plot Parametreleri")

        self.connect(self.dlg.buttonApply, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CallFPlot)

    def CallFPlot(self):
        
        dfn, dfd, density = self.dlg.GetValues()
            
        if dfn != None:
            main_frame = None

            if density == True:
                    main_frame = Distributions.PlotFDistributionDensityFunction(dfn, dfd) 
            else:
                    main_frame = Distributions.PlotFDistributionDistributionFunction(dfn, dfd)

            self.CheckLayoutGraphs()

            self.gridLayout_Graphs.addWidget(main_frame, 0, 0, 1, 1)

        else:
            self.WriteLog(dfd)


        #---------------END OF SLOTS----------------------#

    ### PRINT OUT METHODLARI ###
    def WriteLog(self, log):

        currentTime = time.strftime("%H:%M:%S")
        
        self.textEdit_LogScreen.append(currentTime + "   " + (_fromUtf8(str(log))))

    def WriteOutput(self, output):

        self.textEdit_Down.append(_fromUtf8(output))

    def clearOutput(self):
        self.textEdit_Down.clear()


    ### TRANSLATE ###
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PİVA", None))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya", None))
        self.menuData.setTitle(_translate("MainWindow", "Veri Seti", None))
        self.menuSiniflama.setTitle(_translate("MainWindow", "Sınıflama", None))
        self.menuKumeleme.setTitle(_translate("MainWindow", "Kümeleme", None))
        self.menuPreprocessing.setTitle(_translate("MainWindow", "Ön işleme", None))
        self.menuTable.setTitle(_translate("MainWindow", "Tablo", None))
        self.menuGrafikler.setTitle(_translate("MainWindow", "Grafikler", None))
        self.menuYardim.setTitle(_translate("MainWindow", "Yardım", None))
        self.menuDagilimlar.setTitle(_translate("MainWindow", "Dağılımlar", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionPie_Chart.setText(_translate("MainWindow", "Pie Chart", None))
        self.actionBar_Chart.setText(_translate("MainWindow", "Bar Chart", None))
        self.actionHistogram.setText(_translate("MainWindow", "Histogram", None))
        self.actionBox_Plot.setText(_translate("MainWindow", "Box Plot", None))
        self.actionOpenFile.setText(_translate("MainWindow", "Aç", None))
        self.actionSave.setText(_translate("MainWindow", "Kaydet", None))
        self.actionSaveAs.setText(_translate("MainWindow", "Farklı Kaydet", None))
        self.actionSaveOutput.setText(_translate("MainWindow", "Çıktı Kaydet", None))
        self.menuOpenRecentFiles.setTitle(_translate("MainWindow", "Önceki Verisetleri", None))
        self.label2.setText(_translate("MainWindow", "Çıktı: ", None))

        self.submenuContinuousDist.setTitle(_translate("MainWindow", "Devamlı Dağılımlar", None))
        self.submenuDescreteDist.setTitle(_translate("MainWindow", "Ayrık Dağılımlar", None))
        self.submenuNormalDist.setTitle(_translate("MainWindow", "Normal Dağılım", None))
        self.submenuTDist.setTitle(_translate("MainWindow", "T Dağılımı", None))
        self.submenuChiSquaredDist.setTitle(_translate("MainWindow", "Chi-Squared Dağılımı", None))
        self.submenuFDist.setTitle(_translate("MainWindow", "F Dağılımı", None))

        self.actionNormalQuantiles.setText(_translate("MainWindow", "Normal Quantile'lar", None))
        self.actionNormalProbabilities.setText(_translate("MainWindow", "Normal Olasılıklar", None))
        self.actionPlotNormalDist.setText(_translate("MainWindow", "Normal Dağılım Grafiği", None))

        self.actionTQuantiles.setText(_translate("MainWindow", "T Quantile'lar", None))
        self.actionTProbabilities.setText(_translate("MainWindow", "T Olasılıklar", None))
        self.actionPlotTDist.setText(_translate("MainWindow", "T Dağılım Grafiği", None))

        self.actionChi2Quantiles.setText(_translate("MainWindow", "Chi Squared Quantile'lar", None))
        self.actionChi2Probabilities.setText(_translate("MainWindow", "Chi Squared Olasılıklar", None))
        self.actionPlotChi2Dist.setText(_translate("MainWindow", "Chi Squared Dağılım Grafiği", None))

        self.actionFQuantiles.setText(_translate("MainWindow", "F Quantile'lar", None))
        self.actionFProbabilities.setText(_translate("MainWindow", "F Olasılıklar", None))
        self.actionPlotFDist.setText(_translate("MainWindow", "F Dağılım Grafiği", None))

        self.actionKMeans.setText(_translate("MainWindow", "K-Means", None))
        self.actionKMedoids.setText(_translate("MainWindow", "K-Medoids", None))
        self.actionFuzzyCMeans.setText(_translate("MainWindow", "Fuzzy C-Means", None))
        self.actionHierarchy.setText(_translate("MainWindow", "Hiyerarşik", None))
        self.actionEM.setText(_translate("MainWindow", "EM", None))
        self.actionDBSCAN.setText(_translate("MainWindow", "DBSCAN", None))
        self.actionSOM.setText(_translate("MainWindow", "SOM", None))

        self.actionPca.setText(_translate("MainWindow", "PCA", None))
        self.actionSvd.setText(_translate("MainWindow", "SVD", None))

        self.actionAddRow.setText(_translate("MainWindow", "Satır Ekle", None))
        self.actionAddClm.setText(_translate("MainWindow", "Sütun Ekle", None))
        self.actionDelRow.setText(_translate("MainWindow", "Satır Sil", None))
        self.actionDelClm.setText(_translate("MainWindow", "Sütun Sil", None))

        self.actionHakkinda.setText(_translate("MainWindow", "Hakkında", None))

        self.actionOrnekVeri.setText(_translate("MainWindow", "Örnek Verisetleri", None))

        self.actionHelp.setText(_translate("MainWindow", "PIVA Yardım", None))

from matplotlibwidget import MatplotlibWidget

### DIALOG SINIFLARI ###
class StartDialogPieChart(QtGui.QDialog, Dlg_PieChartParams.Ui_PieChartParams):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

class StartDialogBarChart(QtGui.QDialog, Dlg_BarChartParams.Ui_BarChartParams):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

class StartDialogBoxPlot(QtGui.QDialog, Dlg_BoxPlotParams.Ui_BoxPlot):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

class StartDialogHistogram(QtGui.QDialog, Dlg_HistogramParams.Ui_HistogramParams):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

class StartDialogScatter(QtGui.QDialog, Dlg_ScatterParams.Ui_ScatterParams):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

class StartDlgNormQuan(QtGui.QDialog, Dlg_Norm_Quan.Norm_Quan_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

class StartDlgNormProbs(QtGui.QDialog, Dlg_Norm_Probs.Norm_Probs_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

class StartDlgNormPlot(QtGui.QDialog, Dlg_Norm_Plot.Norm_Plot_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

class StartDlgTChiQuan(QtGui.QDialog, Dlg_T_Chi_Quan.Ui_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

class StartDlgTChiProbs(QtGui.QDialog, Dlg_T_Chi_Probs.Ui_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

class StartDlgTChiPlot(QtGui.QDialog, Dlg_T_Chi_Plot.Ui_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

class StartDlgFQuan(QtGui.QDialog, Dlg_F_Quan.Ui_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

class StartDlgFProbs(QtGui.QDialog, Dlg_F_Probs.Ui_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

class StartDlgFPlot(QtGui.QDialog, Dlg_F_Plot.Ui_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

class StartDlgAboutPiva(QtGui.QDialog, Dlg_AboutPIVA.Ui_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)

### Kümeleme ###

class StartKmeans(QtGui.QDialog, k_means.Kmeans):
    def __init__(self, dataset, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self, dataset)

class StartKmedoids(QtGui.QDialog, k_medoids.Kmedoids):
    def __init__(self, dataset, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self, dataset)


class StartFuzzy(QtGui.QDialog, fuzzy_c_mean.Fuzzy):
    def __init__(self, dataset, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self, dataset)


class StartHiearachy(QtGui.QDialog, hierarchical.Hierarchical):
    def __init__(self, dataset, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self, dataset)



class StartDbscan(QtGui.QDialog, dbscan.DBS):
    def __init__(self, dataset, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self, dataset)


class StartSom(QtGui.QDialog, Som.SOM):
    def __init__(self, dataset, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self, dataset)


class StartEm(QtGui.QDialog, em.EM):
    def __init__(self, dataset, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self, dataset)

class StartPca(QtGui.QDialog, pca.PCA):
    def __init__(self, dataset, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self, dataset)



class StartSvd(QtGui.QDialog, svd.SVD):
    def __init__(self, dataset, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self, dataset)


class StartDialogClm(QtGui.QDialog, New_Column.Ui_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)


        ### MAIN ###
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

