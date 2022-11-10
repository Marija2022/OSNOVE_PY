moj_prvi_tuple = (1, 2, 3)

print(moj_prvi_tuple[0]) # dohvat elementa radi isto kako kod liste
print(moj_prvi_tuple[0:2]) # slice radi isti kao i kod liste
# print(moj_prvi_tuple[4]) greška ako dohvaćamo element na indeksukoji ne postoji


print(moj_prvi_tuple.count(4)) # vraća koliko se puta element pojavljuje u tuple-u
print(moj_prvi_tuple.index(2)) # vraća indeks prvog pojavljivanaja elementa