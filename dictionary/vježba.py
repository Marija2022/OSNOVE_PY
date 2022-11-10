osoba = {
    "ime": "Ivica",
    "prezime": "Ivić",
    "adresa": {
        "ulica": "Ilica",
        "broj": 1,
        "grad": "Zagreb",
        "poštanski broj": 10000
    },
    "omiljene_ boje": ["crvena", "plava", "zelena"],
    "punoljetan": True
}

print(f"{osoba.get('ime')} {osoba.get('prezime')} stanuje na sljedećoj adresi: ")
for info in osoba["adresa"].values():
    print(info)

print(f"Ima {len(osoba['omiljene_ boje'])} omiljene boje, a to su: ")

for boja in osoba["omiljene_ boje"]:
    print(boja)

print(osoba["omiljene_ boje"][0])