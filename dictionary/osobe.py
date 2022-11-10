# Napisati program koji će od korisnika tražiti unos podatke o 5 osoba.

# Svaka osoba treba imati sljedeće podatke: 1. ime, 2. prezime, 3. spol, 4. datum rođenja, 5. mjesto stanovanja, 6. zanimanje

# Nakon unesenih podataka program treba ispisati podatke o svim unesenim osobama u sljedećem obliku:

# ************
# OSOBA 1
# ime
# ...

from inspect import indentsize
from operator import index


osobe =[]

for i in range(2):
    print(f"OSOBA {i+1}")
    ime = input("Unesite ime: ")
    prezime = input("Unesite prezime: ")
    spol = input("Unesite spol: ")
    datum_rođenja = input("Unesite datum_rođenja: ")
    mjesto_stanovanja = input("Unesite mjesto_stanovanja: ")
    zanimanje = input("Unesite zanimanje: ")

    osoba = {
        "ime": ime,
        "prezime": prezime,
        "spol": spol,
        "datum_rođenja": datum_rođenja,
        "mjesto_stanovanja": mjesto_stanovanja,
        "zanimanje": zanimanje
    }

    osobe.append(osoba)

# print(osobe)

for index, osoba_dictionary in enumerate(osobe):
    print("*" * 20)
    print(f"OSOBA {index + 1}")
    print(f"ime: {osoba_dictionary['ime']}")
    print(f"prezime: {osoba_dictionary['prezime']}")
    print(f"spol: {osoba_dictionary['spol']}")
    print(f"datum_rođenja: {osoba_dictionary['datum_rođenja']}")
    print(f"mjesto_stanovanja: {osoba_dictionary['mjesto_stanovanja']}")
    print(f"zanimanje: {osoba_dictionary['zanimanje']}")
    print("*" * 20)