from PyQt4 import QtCore, QtGui


def CreateTable(parent, columnCount, rowCount, columnHeaders):

    table = QtGui.QTableWidget(parent)

    table.setColumnCount(columnCount)
    table.setRowCount(rowCount)

    if not len(columnHeaders) == 0:
        table.setHorizontalHeaderLabels(columnHeaders)

    return table