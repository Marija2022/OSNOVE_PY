# Napisati program koji od korisnika traži unos cijelog broja i ispisuje je li broj veći od 10.

"""
broj = int(input("Unesite cijeli broj: "))

if broj > 10:
    print(f"Broj {broj} je veći od 10.")
elif broj == 10:
    print(f"Unijeli ste broj {broj}.")
else: 
    print(f"Broj {broj} je manji od 10.")
"""


#Napisati program koji traži od korisnika unos cijelog broja i ispisuje je li taj broj manji od 10, između 10 i 50 ili je veći od 50.
"""
a = int(input("Unesite cijeli broj: "))

if a < 10:
    print(f"Broj {a} je manji od 10.")
elif a >= 10 and a <= 50:
    print(f"Broj {a} je između 10 i 50.")
else: 
    print(f"Broj {a} je veći od 50.")
"""

moj_string = "bla"
moj_intiger = 5
moj_prazni_string = "" # False
moj_razmak = " "
moj_nula = 0 # False
moj_float = 1.5
moj_float_0 = 0.0 # False
moj_none = None # False
moja_lista = [1, 2]
moja_lista_nula = [0]
moja_prazna_lista = [] # False
moj_prazan_dictionary = {} # False
moj_prazni_tuple = () # False

if moj_string:
    print("Uvjet je ispunjen.")
else:
    print("Uvijet nije ispunjen.")

# Python evaluira kao False prazne strukture i nula (None)

