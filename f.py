"""
Functions for Main
"""
import math


def mittelwert(array):
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


def wahrscheinlichkeitsverteilung(array):
    matrix = [
             [],
             [],
             []
    ]
    for i in array:
        if i not in matrix[0]:
            matrix[0].append(i)
    matrix[0].sort(key=float)
    for i in matrix[0]:
        matrix[1].append(array.count(i))
        matrix[2].append(round(array.count(i) / len(array), 3))
    return matrix


def antwort(array):
    x="\
    Anzahl der Versuche: %i\n\
    Mittelwert: %g\n\
    Varianz: %g\n\
    Standartabweichung: %g\n\
    Wahrscheinlichkeitsverteilung: \n\
    %s\n\
    %s\n\
    %s\
    " % (len(array), mittelwert(array), varianz(array), standartabweichung(array),
         str(wahrscheinlichkeitsverteilung(array)[0]),
         str(wahrscheinlichkeitsverteilung(array)[1]),
         str(wahrscheinlichkeitsverteilung(array)[2]))
    return x
