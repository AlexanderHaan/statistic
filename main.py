# - *- coding: utf- 8 - *-
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
        self.wvert_button = tk.Button(self.master,
                                      text='Wahrscheinlichkeitsverteilung ' +
                                      'eingeben',
                                      command=self.zu_wvert)

        self.urliste_button.pack()
        self.wvert_button.pack()

        self.master.mainloop()

    def zur_urliste(self):
        self.master.destroy()
        urliste()

    def zu_wvert(self):
        self.master.destroy()
        wvert()


class Urliste:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Urliste")
        self.frame_top = tk.Frame(self.master)
        self.frame_text = tk.Frame(self.master)
        self.text_urliste = tk.Text(self.frame_text, height=2)
        self.berechnen_button = tk.Button(self.frame_top,
                                          text="Berechnen",
                                          command=self.berechnen)
        self.zurueck_button = tk.Button(self.frame_top,
                                        text="Zum Hauptmenü",
                                        command=self.zurueck)
        self.clear_button = tk.Button(self.frame_top,
                                      text="Löschen",
                                      command=self.clear)
        self.label = tk.Label(self.master,
                              text="Bitte was eingeben",
                              anchor="w",
                              justify="left")
        self.table_frame = tk.Frame(self.master)

        # Packing
        self.frame_text.pack(fill='x')
        tk.Label(self.frame_text, text='Urliste: ').pack(side='left')
        self.text_urliste.pack(side='right')

        self.frame_top.pack(fill="x")
        self.berechnen_button.pack(side="left")
        self.clear_button.pack(side="left")
        self.zurueck_button.pack(side="right")

        self.label.pack(fill='x')

        self.master.mainloop()

    def berechnen(self):
        liste = self.text_urliste.get("1.0", "end-1c")
        liste = liste.replace(" ", "")
        urliste_array = liste.split(",")
        try:
            self.label['text'] = f.antwort(urliste_array)
            try:
                self.table_frame.pack_forget()
                self.table_frame.destroy()
                self.table_frame = tk.Frame(self.master)
            except Exception:
                pass
            self.table = None
            self.table = f.t_erst(self.table_frame,
                                  f.wvert(urliste_array))
            self.table_frame.pack(fill='x',
                                  padx=(20, 0),
                                  anchor='w')
        except Exception as e:
            self.label['text'] = 'Falsche Eingabe'
            print(e)

    def zurueck(self):
        self.master.destroy()
        main()

    def clear(self):
        self.text_urliste.delete('1.0', 'end')
        self.label['text'] = 'Bitte was eingeben'
        self.table = None
        self.table_frame.destroy()
        self.table_frame = tk.Frame(self.master)


class Wvert:
    """Wahrscheinlichkeitsverteilung"""

    def __init__(self):

        # Setting
        self.master = tk.Tk()
        self.master.title('Wahrscheinlichkeitsverteilung')
        self.frame_a = tk.Frame(self.master)
        self.frame_b = tk.Frame(self.master)
        self.text_a = tk.Text(self.frame_a, height=1)
        self.text_b = tk.Text(self.frame_b, height=1)
        self.frame_top = tk.Frame(self.master)
        self.berechnen_button = tk.Button(self.frame_top,
                                          text="Berechnen",
                                          command=self.berechnen)
        self.zurueck_button = tk.Button(self.frame_top,
                                        text="Zum Hauptmenü",
                                        command=self.zurueck)
        self.clear_button = tk.Button(self.frame_top,
                                      text="Löschen",
                                      command=self.clear)
        self.label = tk.Label(self.master,
                              text="Bitte was eingeben",
                              anchor="w",
                              justify="left")
        self.table_frame = tk.Frame(self.master)

        # Packing
        self.frame_a.pack(fill='x')
        tk.Label(self.frame_a, text="X: ").pack(side='left')
        self.text_a.pack(side='right')

        self.frame_b.pack(fill='x')
        tk.Label(self.frame_b, text="abs. Häufigkeit: ").pack(side='left')
        self.text_b.pack(side='right')

        self.frame_top.pack(fill="x")
        self.berechnen_button.pack(side="left")
        self.clear_button.pack(side="left")

        self.zurueck_button.pack(side="right")
        self.label.pack(fill='x')

        self.master.mainloop()

    def berechnen(self):
        liste = self.text_a.get("1.0", "end-1c")
        liste = liste.replace(" ", "")
        array_a = liste.split(",")
        liste = self.text_b.get("1.0", "end-1c")
        liste = liste.replace(" ", "")
        array_b = liste.split(",")

        try:
            array = []
            for i in range(len(array_a)):
                for n in range(int(array_b[i])):
                    array.append(int(array_a[i]))

            self.label['text'] = f.antwort(array)
            try:
                self.table_frame.pack_forget()
                self.table_frame.destroy()
                self.table_frame = tk.Frame(self.master)
            except Exception:
                pass
            self.table = None
            self.tabel = f.t_erst(self.table_frame,
                                  f.wvert(array))
            self.table_frame.pack(fill='x',
                                  padx=(20, 0),
                                  anchor='w')
        except Exception as e:
            self.label['text'] = 'Falsche Eingabe'
            print(e)

    def zurueck(self):
        self.master.destroy()
        main()

    def clear(self):
        self.text_a.delete('1.0', 'end')
        self.text_b.delete('1.0', 'end')
        self.label['text'] = 'Bitte was eingeben'
        self.table = None
        self.table_frame.destroy()
        self.table_frame = tk.Frame(self.master)


def main():
    Main()


def urliste():
    Urliste()


def wvert():
    Wvert()


if __name__ == '__main__':
    main()
