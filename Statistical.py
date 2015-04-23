# -*- coding: utf-8 -*-

import numpy

def median(list):
    return numpy.median(list)

def mean(list):
    return numpy.mean(list)

def average(list):
    return numpy.average(list)

def standardDeviation(list):
    return numpy.std(list)

def variance(list):
    return numpy.var(list)

def quantiles(list, yuzde):
    return numpy.percentile(list, yuzde)

def coVariance(list1, list2):
    return numpy.cov(list1, list2)[0][1]

def correlation(list1, list2):
    return numpy.corrcoef(list1, list2)[0, 1]

def minimum(list):
    list.sort()
    return list[0]

def maximum(list):
    list.sort()
    return list[-1]
