"""
Functions for Main
"""
import math


def mittelwert(array):  # Hi wie gehtś
    mittel = 0.0
    for num in array:
        mittel += float(num)
    mittel = mittel / len(array)
    return mittel


def varianz(array):
    v = 0.0
    m = mittelwert(array)
    for i in array:
        v += pow(float(i) - m, 2)
    v = v / len(array)
    return v


def standartabweichung(array):
    return math.sqrt(varianz(array))


def antwort(array):
    x = "\
    Mittelwert: %g\n\
    Varianz: %g\n\
    Standartabweichung: %g\
    " % (mittelwert(array), varianz(array), standartabweichung(array))
    return x
