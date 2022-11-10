programski_jezik={
    "naziv": "Python",
    "tezina": "srednje",
    "trenutna_verzija": 3.11,
    "godina_nastanka": 1994.
}

print(programski_jezik["naziv"])
print(programski_jezik.get("godina_nastanka", "Nepoznato"))

# izbacivanje zapisa sa određenim ključem iz dictionarya
programski_jezik.pop("godina_nastanka")
print(programski_jezik)

# programski_jezik.pop("bla")

dodatni_info = {
    "autor": "Guido Van Rosum",
    "naziv": "Python 3",
    "značajke": ["fleksibilnost", "čitljivost", "primjena"]
}

programski_jezik.update(dodatni_info)
print(programski_jezik)

dodatni_info_2 = dodatni_info.copy()

dodatni_info["naziv"] = "Python 3"
print(dodatni_info)
print(dodatni_info_2)

# clear briše sve parove ključeva i vrijednosti iz dicrionarya
dodatni_info_2.clear()

print(dodatni_info["značajke"][2])