

vozila = [
    {
        "ID": 1,
        "Tip": "Kamion",
        "Proizvođač": "Iveco",
        "Registarska_oznaka": "OS 001 ZZ",
        "Godine_prve_registracije": 2015,
        "Cijena_u_EUR": 45.000
    }
    {
        "ID": 2,
        "Tip": "Kamion",
        "Proizvođač": "Iveco",
        "Registarska_oznaka": "OS 002 ZZ",
        "Godine_prve_registracije": 2015,
        "Cijena_u_EUR": 47.000
    }
    {
        "ID": 3,
        "Tip": "Tegljač",
        "Proizvođač": "MAN",
        "Registarska_oznaka": "RI 001 ZZ",
        "Godine_prve_registracije": 2018,
        "Cijena_u_EUR": 78.000
    }
    {
        "ID": 4,
        "Tip": "Tegljač",
        "Proizvođač": "MAN",
        "Registarska_oznaka": "RI 002 ZZ",
        "Godine_prve_registracije": 2020,
        "Cijena_u_EUR": 97.000
    }
]

print("ID\t Tip Proizvođač Registarska oznaka")

# for index, vozilo in enumerate(vozila):
#   print(f"{index+1}\t {vozilo['Tip']}\t ...)

for vozilo in vozila:
   
    print(f"{vozilo['ID']}\t{vozilo['Tip']}{vozilo['Proizvođač']}{vozilo['Registarska_oznaka']}{vozilo['Godine_prve_registracije']}{vozilo['Cijena_u_EUR']}")
    