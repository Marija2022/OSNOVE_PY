# Ako je snaga mikrovalne pećnice 1.3 kW, a cijena el energije za 1 kWh je 0.95 kn, koliko kuna mjesečno košta uporaba mikrovalne pećnice, ako se koristi 2 sata dbevno?
# Zbog jednostavnosti zaokružimo svaki mjesec na 30 dana
# Ispišite trošak bez i sa PDV-om

# Doradite program iznad tako da od korisnika traži unos trenutne cijene el energije te snagu uređaja za koji želi izračunati potrošnju.


cijena = float(input("Unesite cijenu po kWh: "))
snaga = float(input("Unesite snagu uređaja: "))
dnevna_uporaba = 2
mjesecna_uporaba = dnevna_uporaba * 30

mjesecna_potrosnja = cijena * snaga * dnevna_uporaba * mjesecna_uporaba

print("Cijena bez PDV-a je: ", mjesecna_potrosnja)
print("Cijena s PDV-om je: ", mjesecna_potrosnja * 1.25)