from andmebaasi_haldur import Andmehaldur
import datetime

print("1 - sisesta töötunde\n"
      "2 - kuva töötunnid\n"
      "3 - lõpeta töö")

while __name__ == "__main__":
    sisend = input("Vali tegevus: ")
    if sisend == "1":

        tunde = int(input("Mitu tundi? "))
        minuteid = int(input("Mitu minutit? "))
        aeg = minuteid + tunde * 60

        kuupäev = input("Kuupäev (\"täna\" või \"dd.mm\"): ")
        if kuupäev.lower() == "täna":
            praegune_aeg = datetime.datetime.now()
            päev = praegune_aeg.strftime("%d")
            kuu = praegune_aeg.strftime("%m")
            kuupäev = str(päev) + "." + kuu

        selgitus = input("Selgitus: ")

        andmebaas = Andmehaldur("andmebaas.db")
        andmebaas.lisa_rida(kuupäev, aeg, selgitus)
        andmebaas.väljumine()
        print("Töötunnid salvestatud!\n")

    elif sisend == "2":
        andmebaas = Andmehaldur("andmebaas.db")
        for andmerida in andmebaas.kõigi_valik():
            nr = andmerida[0]
            kuupäev = andmerida[1]
            aeg = andmerida[3]
            selgitus = andmerida[4]
            if andmerida[2] == 0:
                makstud = "-"
            else:
                makstud = "+"
            if aeg >= 60:
                tunde = aeg // 60
                minuteid = aeg % 60
                aeg = f"{tunde}h {minuteid}min"
            else:
                aeg = str(aeg) + "min"

            print(f"nr.{nr}  {makstud}  {kuupäev}  {aeg}  {selgitus}")

    elif sisend == "3" or sisend == "lõpp" or sisend == "0":
        quit(1)
    else:
        print("Ei saanud aru.")
