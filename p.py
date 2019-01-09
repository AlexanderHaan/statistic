"""Funktionen für Wahrscheinlichkeitsverteilungen mit
relativen Wahrscheinlichkeiten"""
# pylint: disable=invalid-name
# pylint: disable=consider-using-enumerate
import math


def mitt(a, b):
    """Mittelwert berechnen"""
    mi = 0.0

    for i in range(len(a)):
        mi += a[i] * b[i]

    return mi


def varianz(a, b):
    """Varianz berechnen"""
    ant = 0.0
    m = mitt(a, b)

    for item in range(len(a)):
        ant += math.pow(a[item] - m, 2) * b[item]

    return ant


def stand_abw(a, b):
    """Standartabweichung berechnen"""
    return math.sqrt(varianz(a, b))


def antwort(a, b):
    """Antwort ausgeben"""
    x = "\
    Mittelwert: %g\n\
    Varianz: %g\n\
    Standartabweichung: %g\
    " % (mitt(a, b),
         varianz(a, b),
         stand_abw(a, b))
    return x
