# Napiši program koji od korisnika traži unos imena i te ispisuje pozdrav ime


ime=input("Unesite svoje ime: ")
print("Pozdrav", ime)


# Napišite program koji od korisnika traži unos sljedećih podataka:

# ime
# prezime
# godina rođenja
# država rođenja
# status radnog odnosa
# spol
# Sve unesene podatke je potrebno ispisati.

ime = input("Unesite svoje ime: ")
prezime=input("Unesite svoje prezime: ")
godine=input("Unesite godinu rođenja: ")
drzava=input("Unesite državu rođenja: ")
radni_status=input("Upišite stataus radnog odnosa: ")
spol=input("Upišite spol: ")

print("Bok ", ime, prezime)
print("Rođen si ", godine, "u ", drzava)
print("Radni status ti je: ", radni_status, "a spol: ", spol)