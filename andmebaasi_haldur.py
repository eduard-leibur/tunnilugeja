import sqlite3


class Andmehaldur:
    def __init__(self, andmebaas):
        self.ühendus = sqlite3.connect(andmebaas)
        self.kursor = self.ühendus.cursor()

    def loo_tabel(self):
        self.kursor.execute("""CREATE TABLE töö(
                            kuupäev TEXT NOT NULL,
                            aeg INTEGER NOT NULL,
                            selgitus TEXT,
                            makstud INTEGER NOT NULL
                            )""")

    def lisa_rida(self, kuupäev, aeg: int, selgitus):
        self.kursor.execute("INSERT INTO töö(kuupäev, aeg, selgitus, makstud) VALUES(?, ?, ?, ?)",
                            (kuupäev, aeg, selgitus, False))

    def tühjenda_tabel(self):
        self.kursor.execute("DELETE FROM töö")

    def kõigi_valik(self):
        valik = self.kursor.execute("SELECT rowid, kuupäev, makstud, aeg, selgitus FROM töö")
        return valik

    def väljumine(self):
        self.ühendus.commit()
        self.kursor.close()
        self.ühendus.close()
