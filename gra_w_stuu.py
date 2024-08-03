# :3

import random

def cos():
    print("Gra: Zgadnij wiek dziewczyny stuu")
    print("")
    print("Dobra zasady są takie:")
    print("1. Miej więcej niż 5 IQ")
    print("2. Oblicz jaka będzie lidczba sposobem matematycznym jakimiś kosinusami lub chuj wie czym")

    zagadka = random.randint(1, 100)
    szansze_ostateczne = 0
    zgadniencie_cwela = False

    while not zgadniencie_cwela:
        try:
            jego_ostatnie_szare_komurki = int(input("Podaj swoją liczbę którą obliczyłeś sposobem matematycznym: "))
        except ValueError:
            print("Pojeb?")
            continue

        szansze_ostateczne += 1

        if jego_ostatnie_szare_komurki < zagadka:
            print("coś mało tak jak stuu lubi :3 Więcej chyba że jesteś stuu")
        elif jego_ostatnie_szare_komurki > zagadka:
            print("za dużo stuu nie lubi takich")
        else:
            zgadniencie_cwela = True
            print(f"Gratulacje! obliczyłeś to jakoś XD Wiek hot dziewczyny stuu był {zagadka} w {szansze_ostateczne} próbach.")

if __name__ == "__main__":
    cos()
