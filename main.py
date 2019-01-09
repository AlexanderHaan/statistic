# - *- coding: utf- 8 - *-
"""
GUI for Main
"""
import tkinter as tk
import f  # Modul
import p


class Main:
    """Hauptseite"""
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
        """Zur Urliset"""
        self.master.destroy()
        urliste()

    def zu_wvert(self):
        """Zur Urliste"""
        self.master.destroy()
        wvert()


class Urliste:
    """Urliste"""
    # pylint: disable=too-many-instance-attributes
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
        """berechnen mit packing"""
        # pylint: disable=attribute-defined-outside-init
        liste = self.text_urliste.get("1.0", "end-1c")
        liste = liste.replace(" ", "")
        urliste_array = liste.split(",")
        try:
            self.label['text'] = f.antwort(urliste_array)
            try:
                self.table_frame.pack_forget()
                self.table_frame.destroy()
                self.table_frame = tk.Frame(self.master)
            except Exception as err:  # pylint: disable=broad-except
                print(err)
            self.table = None
            self.table = f.t_erst(self.table_frame,
                                  f.wvert(urliste_array))
            self.table_frame.pack(fill='x',
                                  padx=(20, 0),
                                  anchor='w')
        except Exception as err:  # pylint: disable=broad-except
            self.label['text'] = 'Falsche Eingabe'
            print(err)

    def zurueck(self):
        """Verlassen"""
        self.master.destroy()
        main()

    def clear(self):
        """Löschen"""
        # pylint: disable=attribute-defined-outside-init
        self.text_urliste.delete('1.0', 'end')
        self.label['text'] = 'Bitte was eingeben'
        self.table = None
        self.table_frame.destroy()
        self.table_frame = tk.Frame(self.master)


class Wvert:
    """Wahrscheinlichkeitsverteilung"""
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=broad-except
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
        self.zuw_button = tk.Button(self.frame_top,
                                    text='Mit relativer Wahrscheinlichkeit',
                                    command=self.zuw)
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
        self.zuw_button.pack(side="right")

        self.label.pack(fill='x')

        self.master.mainloop()

    def berechnen(self):
        """berechnen und packing"""
        # pylint: disable=consider-using-enumerate
        # pylint: disable=attribute-defined-outside-init
        liste = self.text_a.get("1.0", "end-1c")
        liste = liste.replace(" ", "")
        array_a = liste.split(",")
        liste = self.text_b.get("1.0", "end-1c")
        liste = liste.replace(" ", "")
        array_b = liste.split(",")

        try:
            array = []
            for i in range(len(array_a)):
                for _n in range(int(array_b[i])):
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
        except Exception as err:
            self.label['text'] = 'Falsche Eingabe'
            print(err)

    def zurueck(self):
        """Verlassen"""
        self.master.destroy()
        main()

    def zuw(self):
        """Zu der Wahrscheinlichkeitsverteilung mit relativer Häufigkeit"""
        self.master.destroy()
        wvert_w()

    def clear(self):
        """Löschen"""
        # pylint: disable=attribute-defined-outside-init
        self.text_a.delete('1.0', 'end')
        self.text_b.delete('1.0', 'end')
        self.label['text'] = 'Bitte was eingeben'
        self.table = None
        self.table_frame.destroy()
        self.table_frame = tk.Frame(self.master)


class Wvert_w:

    """Wahrscheinlichkeitsverteilung mit Wahrcheinlichkeiten"""
    # pylint: disable=invalid-name
    # pylint: disable=too-many-instance-attributes

    def __init__(self):
        # Setting
        self.master = tk.Tk()
        self.master.title('Wahrscheinlichkeitsverteilung' +
                          ' mit Wahrscheinlichkeiten')
        self.f_a = tk.Frame(self.master)
        self.f_b = tk.Frame(self.master)
        self.t_a = tk.Text(self.f_a, height=1)
        self.t_b = tk.Text(self.f_b, height=1)

        self.f_top = tk.Frame(self.master)
        self.berechnen_button = tk.Button(self.f_top,
                                          text="Berechnen",
                                          command=self.berechnen)
        self.zurueck_button = tk.Button(self.f_top,
                                        text="Zum Hauptmenü",
                                        command=self.zurueck)
        self.zuw_button = tk.Button(self.f_top,
                                    text='Mit absoluter Häufigkeit',
                                    command=self.zuw)
        self.clear_button = tk.Button(self.f_top,
                                      text="Löschen",
                                      command=self.clear)
        self.label = tk.Label(self.master,
                              text="Bitte was eingeben",
                              anchor="w",
                              justify="left")
        self.f_table = tk.Frame(self.master)

        # Packing
        self.f_a.pack(fill='x')
        tk.Label(self.f_a, text='X: ').pack(side='left')
        self.t_a.pack(side='right')

        self.f_b.pack(fill='x')
        tk.Label(self.f_b, text='P(X = xi): ').pack(side='left')
        self.t_b.pack(side='right')

        self.f_top.pack(fill='x')
        self.berechnen_button.pack(side='left')
        self.clear_button.pack(side='left')
        self.zurueck_button.pack(side='right')
        self.zuw_button.pack(side='right')

        self.label.pack(fill='x')

        self.master.mainloop()

    def berechnen(self):
        """Berechnet alle Infos"""
        li = self.t_a.get('1.0', 'end')
        li = li.replace(' ', '')
        arr_a = li.split(',')
        li = self.t_b.get('1.0', 'end')
        li = li.replace(' ', '')
        arr_b = li.split(',')

        try:
            arr_a = list(map(float, arr_a))
            arr_b = list(map(float, arr_b))
            self.label['text'] = p.antwort(arr_a, arr_b)
        except Exception as e:
            raise e

    def clear(self):
        """Löscht Inhalt"""
        self.t_a.delete('1.0', 'end')
        self.t_b.delete('1.0', 'end')
        self.label['text'] = 'Bitte was eingeben'

    def zurueck(self):
        """Zum Hauptmenü"""
        self.master.destroy()
        main()

    def zuw(self):
        """Zur Wahrscheinlichkeitsverteilung mit abs. Haüf."""
        self.master.destroy()
        wvert()


def main():
    """Methode"""
    Main()


def urliste():
    """Methode"""
    Urliste()


def wvert():
    """Methode"""
    Wvert()


def wvert_w():
    """Methode"""
    Wvert_w()


if __name__ == '__main__':
    main()
