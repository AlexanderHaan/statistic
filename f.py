# - *- coding: utf- 8 - *-
"""
Functions for Main
"""
import math
import tkinter as tk


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


def wvert(array):
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
        a = float(array.count(i)) / float(len(array))
        matrix[2].append(a)
    return matrix


def antwort(array):
    x = "\
    Anzahl der Versuche: %i\n\
    Mittelwert: %g\n\
    Varianz: %g\n\
    Standartabweichung: %g\n\
    Wahrscheinlichkeitsverteilung: \
    " % (len(array),
         mittelwert(array),
         varianz(array),
         standartabweichung(array))
    return x


class TkTabelle:

    def __init__(self, frame, zeilen, spalten):

        self.frame = frame

        self.zeilen = zeilen
        self.spalten = spalten
        self.tabelle = []

        for z in range(zeilen):

            self.tabelle.append([])

            for s in range(spalten):

                entry = tk.Label(frame)
                entry.grid(row=z, column=s)
                self.tabelle[-1].append(entry)

    def einfuegen(self, zeile, spalte, text):
        '''Fügt text ein'''

        self.tabelle[zeile-1][spalte-1]['text'] = text


def t_erst(f, a):
    t = TkTabelle(f, len(a), len(a[0]) + 1)
    t.einfuegen(1, 1, 'X')
    t.einfuegen(2, 1, "abs. Häuf.")
    t.einfuegen(3, 1, "P(X=xi)")
    for z in range(len(a)):
        for s in range(len(a[z])):
            t.einfuegen(z+1, s+2, str(a[z][s]))
    return t
