# coding: utf8
import tkinter as tk


class Main:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Hauptmenü")
        self.urliste_button = tk.Button(self.master, text="Urliste" +
                                        " in Wahrscheinlichkeitsverteilung",
                                        command=self.zur_urliste)

        self.urliste_button.pack()

        self.master.mainloop()

    def zur_urliste(self):
        self.master.destroy()
        urliste()


class Urliste:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Urliste")
        self.text_urliste = tk.Text(self.master, height=2)
        self.berechnen_button = tk.Button(self.master, text="Berechnen",
                                          command=self.berechnen)
        self.label = tk.Label(self.master, text="")
        self.zurueck_Button = tk.Button(self.master, text="Zum Hauptmenü",
                                        command=self.zurueck)

        self.text_urliste.pack()
        self.berechnen_button.pack()
        self.label.pack()
        self.zurueck_Button.pack()

        self.master.mainloop()

    def berechnen(self):
        liste = self.text_urliste.get("1.0", "end-1c")
        liste = liste.replace(" ", "")
        urliste_array = liste.split(",")
        try:
            _mittelwert = Urliste.mittelwert(urliste_array)
            self.label['text'] = str(_mittelwert)
        except ValueError:
            self.label['text'] = 'Falsche Eingabe'
        pass

    def mittelwert(array):
        mittelwert = 0.0
        for num in array:
                mittelwert += float(num)
        mittelwert = mittelwert / len(array)
        return mittelwert

    def zurueck(self):
        self.master.destroy()
        main()


def main():
    Main()


def urliste():
    Urliste()


if __name__ == '__main__':
    main()
