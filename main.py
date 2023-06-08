from andmebaasi_haldur import Andmehaldur
import datetime

print("1 - sisesta töötunde\n"
      "2 - kuva töötunnid\n"
      "3 - lõpeta töö")

while True:
    sisend = input("Vali tegevus: ")
    if sisend == "1":

        tunde = int(input("Mitu tundi? "))
        minuteid = int(input("Mitu minutit? "))
        aeg = minuteid + tunde * 60

        kuupäev = input("Kuupäev (või \"täna\"): ")
        if kuupäev.lower() == "täna":
            praegune_aeg = datetime.datetime.now()
            päev = praegune_aeg.strftime("%d")
            kuu = praegune_aeg.strftime("%m")
            kuupäev = str(päev) + "." + kuu

        selgitus = input("Selgitus: ")

        andmebaas = Andmehaldur("andmebaas.db")
        andmebaas.lisa_rida(kuupäev, aeg, selgitus)
        andmebaas.väljumine()

    elif sisend == "2":
        print("Looda vaid.\n")
    elif sisend == "3" or "lõpp":
        break
    else:
        print("Ei saanud aru.\n")
