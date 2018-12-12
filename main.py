"""
GUI for Main
"""
import tkinter as tk


def mittelwert(array):
    """Berechnet Mittelwert"""
    mittel = 0.0
    for num in array:
        mittel += float(num)
    mittel = mittel / len(array)
    return mittel


class Main:  # pylint: disable=too-few-public-methods
    """Hauptseite wird erstellt"""
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Hauptmenü")
        self.urliste_button = tk.Button(self.master, text="Urliste" +
                                        " in Wahrscheinlichkeitsverteilung",
                                        command=self.zur_urliste)

        self.urliste_button.pack()

        self.master.mainloop()

    def zur_urliste(self):
        """Zu Urliste()"""
        self.master.destroy()
        urliste()


class Urliste:
    """Urliste wird erstellt"""
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Urliste")
        self.text_urliste = tk.Text(self.master, height=2)
        self.berechnen_button = tk.Button(self.master, text="Berechnen",
                                          command=self.berechnen)
        self.label = tk.Label(self.master, text="")
        self.zurueck_button = tk.Button(self.master, text="Zum Hauptmenü",
                                        command=self.zurueck)

        self.text_urliste.pack()
        self.berechnen_button.pack()
        self.label.pack()
        self.zurueck_button.pack()

        self.master.mainloop()

    def berechnen(self):
        """bei berechnen_button"""
        liste = self.text_urliste.get("1.0", "end-1c")
        liste = liste.replace(" ", "")
        urliste_array = liste.split(",")
        try:
            _mittelwert = mittelwert(urliste_array)
            self.label['text'] = str(_mittelwert)
        except ValueError:
            self.label['text'] = 'Falsche Eingabe'

    def zurueck(self):
        """Zum Main"""
        self.master.destroy()
        main()


def main():
    """Hier fängt das Programm an."""
    Main()


def urliste():
    """Hier wird die Seite für die Urliste erstellt"""
    Urliste()


if __name__ == '__main__':
    main()
