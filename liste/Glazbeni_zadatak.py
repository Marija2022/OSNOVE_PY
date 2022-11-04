from operator import mod


tonovi = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]

print(f"Glazbena abeceda sastoji se od sljedećih tonova: {tonovi}")
početni_ton = input("Unesite početni ton: ")


# tonovi = tonovi + tonovi
# tonovi.extend(tonovi)
# Ovo su načini kako možemo proširiti abecedu.


indeks_prvog_tona = tonovi.index(početni_ton)
print("Indeks prvog tona je: ", indeks_prvog_tona)

indeks_drugog_d_tona = (indeks_prvog_tona+4) % 12
print("Indeks drugog d tona je: ", indeks_drugog_d_tona)

indeks_drugog_m_tona = (indeks_prvog_tona+3) % 12
print("Indeks drugog m tona je: ", indeks_drugog_m_tona)

indeks_trećeg_tona = (indeks_prvog_tona+7) % 12
print("Indeks trećeg tona je: ", indeks_trećeg_tona)

dur_akord = početni_ton, tonovi[indeks_drugog_d_tona], tonovi[indeks_trećeg_tona]
mol_akord = početni_ton, tonovi[indeks_drugog_m_tona], tonovi[indeks_trećeg_tona]



print(f"Dur akord je: {dur_akord}")
print(f"Mol akord je: {mol_akord}")