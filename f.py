# - *- coding: utf- 8 - *-
"""
Functions for Main
"""
import math
import tkinter as tk


def mittelwert(array):
    """Mittelwert berechnen"""
    mittel = 0.0
    for num in array:
        mittel += float(num)
    mittel = mittel / len(array)
    return mittel


def varianz(array):
    """Varianz berechnen"""
    # pylint: disable=invalid-name
    v = 0.0
    m = mittelwert(array)
    for i in array:
        v += pow(float(i) - m, 2)
    v = v / len(array)
    return v


def standartabweichung(array):
    """Standartabweichung berechnen"""
    return math.sqrt(varianz(array))


def wvert(array):
    """Wahrscheinlichkeitsverteilung"""
    # pylint: disable=invalid-name
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
        matrix[2].append(round(a, 3))
    return matrix


def antwort(array):
    """Antwort ausgeben"""
    # pylint: disable=invalid-name
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
    """Tabelle für tkinter"""
    # pylint: disable=invalid-name
    # pylint: disable=too-few-public-methods

    def __init__(self, frame, zeilen, spalten):

        self.frame = frame

        self.zeilen = zeilen
        self.spalten = spalten
        self.tabelle = []

        for z in range(zeilen):

            self.tabelle.append([])

            for s in range(spalten):

                f = tk.Frame(frame,
                             bg='black')
                entry = tk.Label(f,
                                 justify='left')
                f.grid(row=z, column=s, sticky='w,e')
                if z == 0 and s != spalten-1:
                    entry.pack(fill='both',
                               padx=(0, 2))
                elif s == spalten-1 and z == 0:
                    entry.pack(fill='both')
                elif s == spalten-1 and z != 0:
                    entry.pack(fill='both',
                               pady=(2, 0))
                else:
                    entry.pack(fill='both',
                               padx=(0, 2),
                               pady=(2, 0))
                self.tabelle[-1].append(entry)

    def einfuegen(self, zeile, spalte, text):
        '''Fügt text ein'''

        self.tabelle[zeile-1][spalte-1]['text'] = text


def t_erst(f, a):
    """Tabelle erstellen"""
    # pylint: disable=invalid-name
    # pylint: disable=consider-using-enumerate
    t = TkTabelle(f, len(a), len(a[0]) + 1)
    t.einfuegen(1, 1, 'X')
    t.einfuegen(2, 1, "abs. Häuf.")
    t.einfuegen(3, 1, "P(X=xi)")
    for z in range(len(a)):
        for s in range(len(a[z])):
            t.einfuegen(z+1, s+2, str(a[z][s]))
    return t
