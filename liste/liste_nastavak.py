# Kreirajte listu s brojevima od 1 do 100.

# U ovu svrhu ćemo koristiti funkciju range

lista = []

for broj in range (100, 201, 2):
    lista.append(broj)

# print(lista)


# Kreirajte listu s brojevima od 100 do 1.

lista_100_1 = []

for broj in range (100, 0, -1):
    lista_100_1.append(broj)

# print(lista_100_1)

# slice

test_lista_1 = [1, 2, 3]

# test_lista.clear() # briše sve elemente iz liste


test_lista_2 = test_lista_1.copy()
print(test_lista_2)


test_lista_3 = [5, 7, 5, 8]
print(test_lista_3.count(10))

print(test_lista_3.index(8))

test_lista_4 =[7, 2]

# test_lista_3.append(test_lista_4)


test_lista_3.extend(test_lista_4)
print(test_lista_3)

test_lista_3.sort(reverse=True) #obrnuti redoslijed
print(test_lista_3)