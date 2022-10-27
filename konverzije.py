broj="5"
rijec="bla" #ovo je nekakav komentar

broj_int=int(broj)
print(type(broj_int)) #funkcija type nam ispisuje kojeg je varijabla tipa

broj_float=float(broj)
print(broj_float, type(broj_float))

broj_2=10
broj_2_string=str(broj_2)
print(broj_2_string, type(broj_2_string))

print(bool(broj))
print(bool(rijec))
print(bool(broj_2))
print(bool("False"))
print(bool(""))
print(bool(" "))
print(bool(0))

broj_2_binarni=bin(broj_2)
print(broj_2_binarni)
broj_2_heksadekadski=hex(broj_2)
print(broj_2_heksadekadski)



bla="F"
bla_dekadski=int(bla, base=16)
print(bla_dekadski)