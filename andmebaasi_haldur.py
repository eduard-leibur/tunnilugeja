import sqlite3


class Andmehaldur:
    def __init__(self, andmebaas):
        self.ühendus = sqlite3.connect(andmebaas)
        self.kursor = self.ühendus.cursor()

    def loo_tabel(self):
        self.kursor.execute("CREATE TABLE töö(kuupäev, aeg, selgitus)")

    def lisa_rida(self, kuupäev, aeg: int, selgitus):
        self.kursor.execute("INSERT INTO töö(kuupäev, aeg, selgitus) VALUES(?, ?, ?)", (kuupäev, aeg, selgitus))

    def tühjenda_tabel(self):
        self.kursor.execute("DELETE FROM töö")

    def väljumine(self):
        self.ühendus.commit()
        self.kursor.close()
        self.ühendus.close()
