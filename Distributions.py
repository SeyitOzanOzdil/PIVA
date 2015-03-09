# -*- coding: utf-8 -*-
import numpy as np
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure
from PyQt4 import QtCore, QtGui

#alpha global tanimlanabilir
# NOTE: PROBABILITY HESAPLARINDA UPPER TAIL SONUCU = 1-LOWER TAIL SONUCU 


#---NORMAL DISTRIBUTION
#Normal Quantiles
#Olasiliklar dizisini (0-1 arasinda olmali), mean ve standart sapmayi parametre olarak aliyor 
def NormalQuantilesLowerTail(probs, mean, std):
    if len(probs)>0 and std>0:

        outputStr = ""
        yArray = []

        for prob in probs:
            outputStr += str(prob)

            if prob>0 and prob<1:
                
                rv = stats.norm(loc = mean, scale = std)
                y = rv.ppf(prob)
                y = "{0:.5f}".format(y)
                yArray.append(y)
            else:
                yArray.append("NaN") 

            if len(probs) >1 and probs.index(prob) < len(probs) - 1 : 
                    outputStr += ", "
            else: 
                    outputStr += "" 

        outputStr += ", mean: " + str(mean) + ", standart sapma: " + str(std) 
        return outputStr, yArray

    elif std <= 0 :
        return False, "Standart sapma 0'dan kucuk olamaz." 
        
    else: 
        return False, "Gecerli olasilik degeri girilmelidir." 

#Normal Probabilities
def NormalProbabilitiesLowerTail(variables, mean, std):
    if len(variables) >0 and std>0:
        
        outputStr = ""
        areas = []

        for var in variables:
            outputStr += str(var)
            
            rv= stats.norm(loc = mean, scale = std)
            area = rv.cdf(var)
            area = "{0:.5f}".format(area)
            areas.append(area)

            if len(variables) >1 and variables.index(var) < len(variables) - 1 : 
                outputStr += ", "
            else: 
                outputStr += "" 

        outputStr += ", mean: " + str(mean) + ", standart sapma: " + str(std) 
        return outputStr, areas

    elif std <= 0:
        return False, "Standart sapma 0'dan kucuk olamaz."
    else:
        return False, "Hesaplama icin gecerli deger(ler) verilmelidir."

#Plot Normal Distribution
#mean ve standart sapmayi parametre olarak aliyor. 
def PlotNormalDistributionDensityFunction(mean, std):
    if std>0:
        #gruplanacak fonk icinde
        main_frame = QtGui.QWidget()
        
        dpi = 100
        fig = Figure((5.0, 4.0), dpi=dpi)
        canvas = FigureCanvas(fig)
        canvas.setParent(main_frame)

        axes = fig.add_subplot(111)
        mpl_toolbar = NavigationToolbar(canvas, main_frame)

        hbox = QtGui.QHBoxLayout()
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(canvas)
        vbox.addWidget(mpl_toolbar)
        vbox.addLayout(hbox)

        main_frame.setLayout(vbox)

        axes.clear()

        #ortak olmayan kisim
        q = 0.0005 #lower or upper tail olasiligi
        sequance = stats.norm.isf(q)

        x = np.linspace(-std*sequance, std*sequance, 100)        #100 rasgele degisken
        gaussian = stats.norm(loc = mean, scale = std)     #mean ve std'ye gore normal dagilim
        y = gaussian.pdf(x)

        axes.plot(x,y)
        canvas.draw()
        

        return main_frame
    else:
        return False, "Standart sapma 0'dan kucuk olamaz."

#mean ve standart sapmayi parametre olarak aliyor. 
def PlotNormalDistributionDistributionFunction(mean, std):
    if std>0:
        main_frame = QtGui.QWidget()
        dpi = 100
        fig = Figure((5.0, 4.0), dpi=dpi)
        canvas = FigureCanvas(fig)
        canvas.setParent(main_frame)

        axes = fig.add_subplot(111)
        mpl_toolbar = NavigationToolbar(canvas, main_frame)

        hbox = QtGui.QHBoxLayout()
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(canvas)
        vbox.addWidget(mpl_toolbar)
        vbox.addLayout(hbox)
        main_frame.setLayout(vbox)

        axes.clear()

        q = 0.0005 #lower or upper tail olasiligi
        sequance = stats.norm.isf(q)

        x = np.linspace(-sequance*3, sequance*3, 100)        #100 rasgele degisken
        gaussian = stats.norm(loc = mean, scale = std)  #mean ve std'ye gore normal da??l?m
        y = gaussian.cdf(x)

        axes.plot(x,y)
        canvas.draw()

        return main_frame

    else: 
        return False, "Standart sapma 0'dan kucuk olamaz."
#---/NORMAL DISTRIBUTION


#---T DISTRIBUTION
#olasiliklar dizisi ve degrees of freedom parametresi aliyor
def TQuantilesLowerTail(probs, df):
    if len(probs)>0 and df>0:

        outputStr = ""
        yArray = []

        for prob in probs:
            outputStr += str(prob)

            if prob> 0 and prob<1:

                rv = stats.t(df, loc = 0, scale = 1)
                y = rv.ppf(prob)
                y = "{0:.5f}".format(y)
                yArray.append(y) 

            else:
                yArray.append("NaN") 
            
            if len(probs) >1 and probs.index(prob) < len(probs) - 1 : 
                    outputStr += ", "
            else: 
                    outputStr += "" 

        outputStr += ", serbestlik derecesi: " + str(df) 
        return outputStr, yArray

    elif df<=0: 
        return False, "Serbestlik derecesi 0'dan kucuk olamaz."
    else: 
        return False, "Gecerli olasilik degeri girilmelidir."

def TProbabilitiesLowerTail(values, df):
    if len(values)>0 and df>0:
        
        outputStr = ""
        areas = []

        for val in values:
            outputStr += str(val)
            
            rv= stats.t(df, loc = 0, scale = 1)   #default loc ve scale degerleri
            area = rv.cdf(val)
            area = "{0:.5f}".format(area)
            areas.append(area)

            if len(values) >1 and values.index(val) < len(values) - 1 : 
                outputStr += ", "
            else: 
                outputStr += "" 

        outputStr += ", serbestlik derecesi: " + str(df) 
        return outputStr, areas

    elif df <= 0:
        return False, "Standart sapma 0'dan kucuk olamaz."
    else:
        return False, "Hesaplama icin gecerli degerler girilmelidir."

# df = degrees of freedom parametresi aliyor
def PlotTDistributionDensityFunction(df): 
    if df>0: 
        main_frame = QtGui.QWidget()
        dpi = 100
        fig = Figure((5.0, 4.0), dpi=dpi)
        canvas = FigureCanvas(fig)
        canvas.setParent(main_frame)

        axes = fig.add_subplot(111)
        mpl_toolbar = NavigationToolbar(canvas, main_frame)

        hbox = QtGui.QHBoxLayout()
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(canvas)
        vbox.addWidget(mpl_toolbar)
        vbox.addLayout(hbox)
        main_frame.setLayout(vbox)

        axes.clear()

        alpha = 0.0005  #R'da o sekilde alinmis, burada da ayni olmasi icin bu deger verildi
        sequance = stats.t.isf(alpha, df)

        x = np.linspace(-sequance, sequance, 100)    #100 adet veri default verildi
        rv = stats.t(df)
        y = rv.pdf(x)

        axes.plot(x,y)
        canvas.draw()

        return main_frame

    else: 
        return False, "Serbestlik derecesi 0'dan kucuk olamaz."

# df = degrees of freedom parametresi aliyor
def PlotTDistributionDistributionFunction(df): 
    if df>0: 
        main_frame = QtGui.QWidget()
        dpi = 100
        fig = Figure((5.0, 4.0), dpi=dpi)
        canvas = FigureCanvas(fig)
        canvas.setParent(main_frame)

        axes = fig.add_subplot(111)
        mpl_toolbar = NavigationToolbar(canvas, main_frame)

        hbox = QtGui.QHBoxLayout()
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(canvas)
        vbox.addWidget(mpl_toolbar)
        vbox.addLayout(hbox)
        main_frame.setLayout(vbox)

        axes.clear()

        alpha = 0.0005  #R'da o sekilde alinmis, burada da ayni olmas? icin bu deger verildi
        sequance = stats.t.isf(alpha, df)

        x = np.linspace(-sequance, sequance, 100)    #100 adet veri default verildi
        rv = stats.t(df)
        y = rv.cdf(x)

        axes.plot(x,y)
        canvas.draw()

        return main_frame

    else: 
        return False, "Serbestlik derecesi 0'dan kucuk olamaz."
#---/T DISTRIBUTION


#---CHI-SQUARED DISTRIBUTION
# df = degrees of freedom parametresi aliyor
def Chi2QuantilesLowerTail(probs, df):
    if len(probs)>0 and df>0:

        outputStr = ""
        yArray = []

        for prob in probs:
            outputStr += str(prob)

            if prob> 0 and prob<1:

                rv = stats.chi2(df, loc = 0, scale = 1)
                y = rv.ppf(prob)
                y = "{0:.5f}".format(y)
                yArray.append(y) 

            else:
                yArray.append("NaN") 
            
            if len(probs) >1 and probs.index(prob) < len(probs) - 1 : 
                    outputStr += ", "
            else: 
                    outputStr += "" 

        outputStr += ", serbestlik derecesi: " + str(df) 
        return outputStr, yArray

    elif df<=0: 
        return False, "Standart sapma 0'dan kucuk olamaz."
    else: 
        return False, "Gecerli olasilik degeri girilmelidir."

def Chi2ProbabilitiesLowerTail(values, df):
    if len(values)>0 and df>0:
        outputStr = ""
        areas = []

        for val in values:
            outputStr += str(val)

            rv = stats.chi2(df, loc=0, scale=1)
            area = rv.cdf(val)
            area = "{0:.5f}".format(area)
            areas.append(area)

            if len(values) >1 and values.index(val) < len(values) - 1 : 
                    outputStr += ", "
            else: 
                    outputStr += "" 

        outputStr += ", serbestlik derecesi: " + str(df) 
        return outputStr, areas

    elif df<=0:
        return False, "Standart sapma 0'dan kucuk olamaz."
    else: 
        return False, "Gecerli olasilik degeri girilmelidir."

def PlotChi2DistributionDensityFunction(df):
    if df>0:
        main_frame = QtGui.QWidget()
        dpi = 100
        fig = Figure((5.0, 4.0), dpi=dpi)
        canvas = FigureCanvas(fig)
        canvas.setParent(main_frame)

        axes = fig.add_subplot(111)
        mpl_toolbar = NavigationToolbar(canvas, main_frame)

        hbox = QtGui.QHBoxLayout()
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(canvas)
        vbox.addWidget(mpl_toolbar)
        vbox.addLayout(hbox)
        main_frame.setLayout(vbox)

        axes.clear()

        alpha = 0.0005
        sequence = stats.chi2.isf(alpha, df)

        x = np.linspace(-sequence, sequence, 1000)
        rv = stats.chi2(df)
        y = rv.pdf(x)

        axes.plot(x,y)
        canvas.draw()

        return main_frame
    else:
        return False, "Serbestlik derecesi 0'dan kucuk olamaz."

def PlotChi2DistributionDistributionFunction(df):
    if df>0:
        main_frame = QtGui.QWidget()
        dpi = 100
        fig = Figure((5.0, 4.0), dpi=dpi)
        canvas = FigureCanvas(fig)
        canvas.setParent(main_frame)

        axes = fig.add_subplot(111)
        mpl_toolbar = NavigationToolbar(canvas, main_frame)

        hbox = QtGui.QHBoxLayout()
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(canvas)
        vbox.addWidget(mpl_toolbar)
        vbox.addLayout(hbox)
        main_frame.setLayout(vbox)

        alpha = 0.0005
        sequence = stats.chi2.isf(alpha, df)

        x = np.linspace(-sequence, sequence, 1000)
        rv = stats.chi2(df)
        y = rv.cdf(x)

        axes.plot(x,y)
        canvas.draw()

        return main_frame
    else:
        return False, "Serbestlik derecesi 0'dan kucuk olamaz."
#---/CHI-SQUARED DISTRIBUTION


#---F DISTRIBUTION
#dfn = degrees of freedom numerator, dfd = degrees of freedom denominator
def FQuantilesLowerTail(probs,dfn,dfd):
    if len(probs)>0 and dfn>0 and dfd>0:
        outputStr = ""
        yArray = []

        for prob in probs:
            outputStr += str(prob)

            if prob> 0 and prob<1:

                rv = stats.f(dfn,dfd, loc = 0, scale = 1)
                y = rv.ppf(prob)
                y = "{0:.5f}".format(y)
                yArray.append(y) 

            else:
                yArray.append("NaN") 
            
            if len(probs) >1 and probs.index(prob) < len(probs) - 1 : 
                    outputStr += ", "
            else: 
                    outputStr += "" 

        outputStr += ", serbestlik derecesi (pay): " + str(dfn) + ", serbestlik derecesi (payda): " + str(dfd)  
        return outputStr, yArray

    elif dfn<=0 or dfd <=0: 
        return False, "Serbestlik dereceleri 0'dan kucuk olamaz."
    else: 
        return False, "Gecerli olasilik degeri girilmelidir."

def FProbabilitiesLowerTail(values, dfn, dfd):
    if len(values)>0 and dfn>0 and dfd>0:
        outputStr = ""
        areas = []

        for val in values:
            outputStr += str(val)

            rv =  stats.f(dfn, dfd, loc = 0, scale=1)
            area = rv.cdf(val)
            area = "{0:.5f}".format(area)
            areas.append(area)

            if len(values) >1 and values.index(val) < len(values) - 1 : 
                    outputStr += ", "
            else: 
                    outputStr += ""

        outputStr += ", serbestlik derecesi (pay): " + str(dfn) + ", serbestlik derecesi (payda): " + str(dfd)  
        return outputStr, areas

    elif dfn<=0 or dfd<=0:
        return False, "Serbestlik dereceleri 0'dan kucuk olamaz."
    else:
        return False, "Hesaplama icin gecerli degerler girilmelidir."

def PlotFDistributionDensityFunction(dfn, dfd):
    if dfn>0 and dfd>0:
        main_frame = QtGui.QWidget()
        dpi = 100
        fig = Figure((5.0, 4.0), dpi=dpi)
        canvas = FigureCanvas(fig)
        canvas.setParent(main_frame)

        axes = fig.add_subplot(111)
        mpl_toolbar = NavigationToolbar(canvas, main_frame)

        hbox = QtGui.QHBoxLayout()
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(canvas)
        vbox.addWidget(mpl_toolbar)
        vbox.addLayout(hbox)
        main_frame.setLayout(vbox)

        alpha = 0.0005
        sequence = stats.f.isf(alpha, dfn, dfd)

        x = np.linspace(-sequence, sequence, 1000)
        rv = stats.f(dfn, dfd)
        y = rv.pdf(x)

        axes.plot(x,y)
        canvas.draw()

        return main_frame
    else: 
        return False, "Serbestlik derecesi 0'dan kucuk olamaz."

#dfn = degrees of freedom numerator, dfd = degrees of freedom denominator
def PlotFDistributionDistributionFunction(dfn, dfd):
    if dfn>0 and dfd>0:
        main_frame = QtGui.QWidget()
        dpi = 100
        fig = Figure((5.0, 4.0), dpi=dpi)
        canvas = FigureCanvas(fig)
        canvas.setParent(main_frame)

        axes = fig.add_subplot(111)
        mpl_toolbar = NavigationToolbar(canvas, main_frame)

        hbox = QtGui.QHBoxLayout()
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(canvas)
        vbox.addWidget(mpl_toolbar)
        vbox.addLayout(hbox)
        main_frame.setLayout(vbox)

        alpha = 0.0005
        sequence = stats.f.isf(alpha, dfn, dfd)

        x = np.linspace(-sequence, sequence, 1000)
        rv = stats.f(dfn, dfd)
        y = rv.cdf(x)

        axes.plot(x,y)
        canvas.draw()

        return main_frame
    else: 
        return False, "Serbestlik derecesi 0'dan kucuk olamaz."
#---/F DISTRIBUTION