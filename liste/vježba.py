# 1. Kreirati listu u kojij će biti svaki treći broj između 1 i 30.



lista_1 = []
for broj in range (2, 30, 3):
    lista_1.append(broj)

print(lista_1)


# 2. Kreirati novu listu na temelju liste iz prethodnog zadataka tako da vrijednost svakog elementa uvećate dvostruko.

lista_2 = []
for broj in lista_1:
    lista_2.append(broj*2)

print(lista_2)


# 3. Napisati program koji ispisuje zbr0j svih elemenata iz liste u drugom zadataku.

sum = 0
for broj in lista_2:
    sum = sum + broj
    
print(sum)

# 4. Napisati program koji od korisnika traži unos jednog broja koji želi izbaciti iz liste iz zadatka 2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
# Izbaciti uneseni broj i ispišite novo stanje liste.

x = int(input("Unesite broj koji želite izbaciti iz liste_2: "))
lista_2.remove(x)
print(lista_2)