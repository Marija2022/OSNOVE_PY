# Napisati program koji provjerava je li uneseni broj paran ili neparan

a = int(input("Unesite cijeli broj: "))

if a % 2 == 0:
    print(f"Broj {a} je paran.")
else:
    print(f"Broj {a} je neparan.")

"""
if not (a % 2):
    print(f"Broj je paran.")
else:
    print(f"Broj je neparan")
"""