"""
Functions for Main
"""


def mittelwert(array):
    """Berechnet Mittelwert"""
    mittel = 0.0
    for num in array:
        mittel += float(num)
    mittel = mittel / len(array)
    return mittel

def antwort(array):
    x = "\
    Mittelwert: %g\
    " % mittelwert(array)
    return x