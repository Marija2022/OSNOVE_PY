#Napisati program koji od korisnika traži unos polumjera kružnice te ispisuje njezinu površinu i opseg.


pi=3.14
polumjer=float(input("Unesite polumjer kružnice: "))
# polumjer=input("Unesite polumjer kružnice: ")
# polumjer=float(polumjer)

opseg=2*polumjer*pi

povrsina=polumjer*polumjer*pi

print("Opseg kružnice je ", opseg)
print("Površina kružnice je: ", povrsina)