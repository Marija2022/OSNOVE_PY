# struktura podataka koja se sastoji od ključa key i vrijednosti value

import os


osoba = {
    "ime": "Ivica",
    "prezime": "Ivić",
    "grad": "Zagreb",
}

print(osoba)

# pristup elementu radimo putem ključa

print(osoba["ime"])
print(osoba.get("ime"))

# dodavanje novog ključa u riječnik

osoba["datum_rođenja"] = "01.01.1990."
print(osoba)

# pristup elementu koji ne postoji
# print(osoba["spol"])

print(osoba.get("spol", "-"))

# promjena vrijednosti postojećeg
osoba["ime"] = "Ivan"
print(osoba)

print(len(osoba))

# prolazak kroz sve elemente u dictionaryu
for podatak in osoba:
    print(f"{podatak} je {osoba[podatak]}")

# prolazak kroz KLJUČEVE
for key in osoba.keys():
    print(key)

# prolazak kroz VRIJEDNOSTI
for value in osoba.values():
    print(value)


# prolazak kroz PAROVE KLJUČEVA I VRIJEDNOSTI
for key, value in osoba.items():
    print(key, value)
    