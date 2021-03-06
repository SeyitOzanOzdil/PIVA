
import os
import Utils


import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure
from PyQt4 import QtCore, QtGui
import numpy as np
from pylab import *

from matplotlib.gridspec import GridSpec


#Piechart cizdiren fonksiyon. Parametre olarak pie uzerindeki label'lari ve yuzde oranlarini aliyor
def CreatePieChart(labels,sizes):    

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

        # clear the axes and redraw the plot anew
        #
        axes.clear() 
          
        explode=(0, 0, 0, 0)             
        
        axes.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
               
        canvas.draw()

        return main_frame

        
#Barchart cizdiren fonksiyon  (stdDev opsiyonal, default'u None)
def CreateBarChart(values, wdth, stdDev, labels):

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
        
        x = np.arange(len(values))

        # clear the axes and redraw the plot anew
        #
        axes.clear()                
        
        axes.bar(
            left=x, 
            height=values, 
            width=wdth, 
            align='center', 
            alpha=0.4,
            )

        axes.set_xticks(x)
        axes.set_xticklabels(labels, rotation = 30 )
               
        canvas.draw()

        return main_frame

#y ekseni boyunca boxplot ciziyor
def CreateBoxPlot(serie, features):

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
               
        # clear the axes and redraw the plot anew
        #
        axes.clear()                
        
        bp = axes.boxplot(serie, 0, 'gD', patch_artist = True)

        for box in bp['boxes']:
            box.set(color='#7570b3', linewidth=2)
            box.set( facecolor = '#1b9e77' )

        for whisker in bp['whiskers']:
            whisker.set(color='#7570b3', linewidth=2)

        for cap in bp['caps']:
            cap.set(color='#7570b3', linewidth=2)

        for median in bp['medians']:
            median.set(color='#b2df8a', linewidth=2)

        for flier in bp['fliers']:
            flier.set(marker='o', color='#e7298a', alpha=0.5)

        axes.set_xticklabels(features)

        axes.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
              alpha=0.5)
        axes.set_axisbelow(True)
               
        canvas.draw()

        return main_frame

#histogram cizdiren fonksiyon
def CreateHistogram(serie, binCount): 

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
               
        # clear the axes and redraw the plot anew
        #
        axes.clear()                
        
        axes.hist(serie, binCount, facecolor='green')

        axes.yaxis.grid(True, linestyle='-', which='major', color='lightgrey')
        axes.set_axisbelow(True)
               
        canvas.draw()

        return main_frame

def CreateScatter(valueList1, valueList2):

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
               
        # clear the axes and redraw the plot anew
        #
        axes.clear()                       
        
        axes.scatter(valueList1, valueList2, color="blue", edgecolor="none")
               
        canvas.draw()

        return main_frame

def CreateLinePlot(x,y):

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
               
        # clear the axes and redraw the plot anew
        #
        axes.clear()                       
        
        axes.plot(x, y)
               
        canvas.draw()

        return main_frame

def Cluster(plot_memroy, features, value):
    main_frame = QtGui.QWidget()
    dpi = 100
    fig = Figure((5.0, 4.0), dpi=dpi)
    canvas = FigureCanvas(fig)
    canvas.setParent(main_frame)
    ax = fig.add_subplot(111)
    mpl_toolbar = NavigationToolbar(canvas, main_frame)
    hbox = QtGui.QHBoxLayout()
    vbox = QtGui.QVBoxLayout()
    vbox.addWidget(canvas)
    vbox.addWidget(mpl_toolbar)
    vbox.addLayout(hbox)
    main_frame.setLayout(vbox)
    # clear the axes and redraw the plot anew
    #
    indis = []
    for i in range(len(features)):
        if features[i] in value:
            indis.append(i)

    for z in range(len(plot_memroy)):
        print z
        ax.clear()
        colors = ['b', 'r', 'y', 'g']

        clusters = plot_memroy[z][0]
        centers = plot_memroy[z][1]

        if len(indis) == 2:
            for i in range(len(clusters)):
                for j in range(len(clusters[i])):
                    ax.scatter(clusters[i][j][indis[0]], clusters[i][j][indis[1]], c=colors[i])
                ax.scatter(centers[i][indis[0]], centers[i][indis[1]], s=80, c=colors[i], marker='*', label='%d. Kume'%(i+1))
            ax.set_xlabel(value[0])
            ax.set_ylabel(value[1])


        canvas.draw()

    return main_frame

def CreateRegression(x, y):

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

    m, b = np.polyfit(x, y, 1)

    yp = polyval([m, b], x)

    axes.plot(x, yp)
    axes.scatter(x,y)
    axes.grid(True)
    axes.set_xlabel('x')
    axes.set_ylabel('y')

    canvas.draw()

    return main_frame

def CreateAnovaResult(x_plot, y_plot, x_fcrit, y_fcrit, F_critical):

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

    # Plot the F-Distribution for dfB and dfW

    axes.fill_between(x_plot, y_plot, alpha=.2)
    axes.plot(x_plot, y_plot)
    # Plot the F-critical value at alpha .05
    axes.fill_between(x_fcrit, y_fcrit, alpha=.5)
    axes.text(F_critical, .07, '$F_{critical}=$'+str(F_critical))
    axes.set_xlabel(u'F-degerleri')
    axes.set_ylabel(u'Olasilik')

    canvas.draw()
    return main_frame