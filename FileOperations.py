
from PyQt4 import QtCore, QtGui
import TableOperations
#import xlrd
import csv
import guidata

import DataSet
import Errors
import Utils
import os

from Dlg_DatasetParams import Ui_Dialog

def OpenNewFile(self, path):

    hasFeatureLine = True
    seperator = " "
    deleteBadData = False

    if path == None:
        try:
            fileInfo = QtCore.QFileInfo(QtGui.QFileDialog.getOpenFileName(self, "Dataset Dosyasini Ac", "Dosya Adi"))
        except Exception:
            Errors.ShowWarningMsgBox(self, Exception.message)

        fileSuffix = fileInfo.completeSuffix()
        if not ((fileSuffix == "txt") or (fileSuffix == "xls") or (fileSuffix == "csv")):
            Errors.ShowWarningMsgBox(self, "Lutfen gecerli bir dosya aciniz")
            return 0,0
    
        dlg = StartDialog()
    
        if dlg.exec_():       
            hasFeatureLine, seperator, deleteBadData = dlg.GetValues()

    else:
        try:
            fileInfo = QtCore.QFileInfo(path)
        except Exception:
            Errors.ShowWarningMsgBox(self, Exception.message)

        fileSuffix = fileInfo.completeSuffix()
        if not ((fileSuffix == "txt") or (fileSuffix == "xls") or (fileSuffix == "csv")):
            Errors.ShowWarningMsgBox(self, "Lutfen gecerli bir dosya aciniz")
            return
    
    self.WriteLog("Dosya acma islemi basarili")
    self.WriteLog("Acilan dosya: " + fileInfo.fileName() )
    if fileSuffix == "txt":
        dataSet = __InterpretTxtFile(self, fileInfo.filePath(), hasFeatureLine, seperator, deleteBadData)
    elif fileSuffix == "xls":
        dataSet = __InterpretXlsFile(self, fileInfo.filePath(), hasFeatureLine, seperator, deleteBadData)
    elif fileSuffix == "csv":
        dataSet = __InterpretCsvFile(self, fileInfo.filePath(), hasFeatureLine, seperator, deleteBadData)
    else:
        self.WriteLog("Dosya parse isleminde hata")       
        return
    self.WriteLog("Dosya basarili bir sekilde parse edildi")             
    return dataSet, fileInfo

def __InterpretTxtFile(self, filePath, hasFeatureLine, seperator, deleteBadData):
    try:
        fptr = open(filePath, 'r')
    except Exception:
        Errors.ShowWarningMsgBox(self, Exception.message)

    lines = fptr.readlines()

    lineCount = len(lines)

    newLines = list()

    for i in range(lineCount):
        newLineArray = lines[i].split(" ")
        if not (seperator == ""):
            newLineArray = lines[i].split(seperator)
        if deleteBadData:
            if newLineArray.count(" ") is not 0 or newLineArray.count("") is not 0:
                continue
        newLine = ",".join(newLineArray)
        newLines.append(newLine)

    for tmpLine in newLines:

        if tmpLine.count("\n") > 0:
            tmp = tmpLine.replace("\n","")
            index = newLines.index(tmpLine)
            newLines[index] = tmp

    ourDataSet = DataSet.DataSet(newLines, hasFeatureLine)

    fptr.close()

    return ourDataSet

'''def __InterpretXlsFile(self, filePath, hasFeatureLine, seperator, deleteBadData):

    lines = list()

    try:
        book = xlrd.open_workbook(filePath)
    except Exception:
        Errors.ShowWarningMsgBox(self, Exception.message)

    sheet = book.sheet_by_index(0)

    for rowIndex in xrange(sheet.nrows):
        row = sheet.row(rowIndex)
        line = str(row[0].value)
        rowCount = len(row)
        for i in range(1,rowCount):
            line = line + " " + str(row[i].value)
        lines.append(line)

    newLines = list()
    for i in range(len(lines)):
        newLineArray = lines[i].split(" ")
        newLine = ",".join(newLineArray)
        newLines.append(newLine)

    ourDataSet = DataSet.DataSet(newLines, hasFeatureLine)

    return ourDataSet'''
    
def __InterpretCsvFile(self, filePath, hasFeatureLine, seperator, deleteBadData):

    lines = list()

    with open(filePath, "r") as file:

        flines = file.readlines()
        
        lineCount = len(flines)

        for line in flines:
            lines.append(line)        

    ourDataSet = DataSet.DataSet(lines, hasFeatureLine)

    return ourDataSet

def CreateAndWriteFile(self, table, features): #line
    filters = [
        'CSV file (*.csv)',
        'TXT files (*.txt)',
    ]
    try:
        file, filter = QtGui.QFileDialog.getSaveFileNameAndFilter(self, "Dosya Yolu Seciniz", os.getcwd(),
                                                                  ";;".join(filters))

    except Exception:
        Errors.ShowWarningMsgBox(self, Exception.message)

    strPath = file
    if strPath.contains(".txt"):
        fptr = open(strPath, 'w')
        for feature in features:
            fptr.write(feature)
            if feature != features[-1]:
                fptr.write(" ")
        fptr.write('\n')
        for row in range(table.rowCount()):
            for clm in range(table.columnCount()):
                line = table.item(row, clm).text()
                fptr.write(line)
                if line != table.item(row, (table.columnCount()-1)).text():
                    fptr.write(' ')
            fptr.write("\n")
        fptr.close()

    elif strPath.contains(".csv"):
        cs = csv.writer(open(strPath, "w"))
        pmt = []
        for feature in features:
            pmt.append(feature)
        cs.writerow(pmt)
        for row in range(table.rowCount()):
            tmp = []
            for clm in range(table.columnCount()):
                line = table.item(row, clm).text()
                tmp.append(line)
            cs.writerow(tmp)

    self.WriteLog("Dosya yazma islemi basarili")
    self.WriteLog("Yazilan dosya yolu: " + strPath)



class StartDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
