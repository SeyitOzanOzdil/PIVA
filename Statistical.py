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

def coVariance(list1, list2):
    return numpy.cov(list1, list2)

def correlation(list1, list2):
    return numpy.correlate(list1, list2)
