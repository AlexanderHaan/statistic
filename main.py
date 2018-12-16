"""
GUI for Main
"""
import tkinter as tk
import f  # Modul


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
        self.frame_top = tk.Frame(self.master)
        self.text_urliste = tk.Text(self.master, height=2)
        self.berechnen_button = tk.Button(self.frame_top, text="Berechnen",
                                          command=self.berechnen)
        self.label = tk.Label(self.master, text="Bitte was eingeben", anchor="w",
                              justify="left")
        self.zurueck_button = tk.Button(self.frame_top, text="Zum Hauptmenü",
                                        command=self.zurueck)
        self.clear_button = tk.Button(self.frame_top, text="Löschen",
                                      command=self.clear)

        self.text_urliste.pack()
        self.frame_top.pack(fill="x")
        self.berechnen_button.pack(side="left")
        self.clear_button.pack(side="left")
        self.zurueck_button.pack(side="right")
        self.label.pack()

        self.master.mainloop()

    def berechnen(self):
        liste = self.text_urliste.get("1.0", "end-1c")
        liste = liste.replace(" ", "")
        urliste_array = liste.split(",")
        try:
            _mittelwert = f.mittelwert(urliste_array)
            self.label['text'] = f.antwort(urliste_array)
        except ValueError:
            self.label['text'] = 'Falsche Eingabe'

    def zurueck(self):
        self.master.destroy()
        main()

    def clear(self):
        self.text_urliste.delete('1.0', 'end')
        self.label['text'] = 'Bitte was eingeben'


def main():
    Main()


def urliste():
    Urliste()


if __name__ == '__main__':
    main()
