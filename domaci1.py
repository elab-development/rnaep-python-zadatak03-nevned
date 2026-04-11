import random
import math


proizvodi = ["Laptop", "Mis", "Tastatura", "Monitor", "Slusalice", "Podloga", "Zvucnici", "Kamera"]


cene = {
    "Laptop": 950.99,
    "Mis": 19.99,
    "Tastatura": 45.50,
    "Monitor": 150.00,
    "Slusalice": 59.90,
    "Podloga": 12.00,
    "Zvucnici": 85.00,
    "Kamera": 40.25
}


print("--- Ponuda proizvoda ---")
for proizvod, cena in cene.items():
    print(f"{proizvod} - {cena} €")


print("\n--- Analiza budžeta ---")
try:
    budzet = float(input("Unesite vaš budžet u evrima: "))
    print(f"Sa budžetom od {budzet} € možete priuštiti:")
    za_kupovinu = []
    for proizvod, cena in cene.items():
        if cena <= budzet:
            print(f"- {proizvod} ({cena} €)")
            za_kupovinu.append(proizvod)
    
    if not za_kupovinu:
        print("Nažalost, ne možete priuštiti nijedan proizvod.")
except ValueError:
    print("Greška: Molimo unesite brojčanu vrednost za budžet.")


def najskuplji_proizvod(cenovnik):
    najskuplji = max(cenovnik, key=cenovnik.get)
    return najskuplji, cenovnik[najskuplji]

ime_naj, cena_naj = najskuplji_proizvod(cene)
print(f"\nNajskuplji proizvod je: {ime_naj} sa cenom od {cena_naj} €")


slucajan_izbor = random.choice(proizvodi)
print(f"Korisniku je privukao pažnju proizvod: {slucajan_izbor}")

prosecna_cena = sum(cene.values()) / len(cene)
print(f"Prosečna cena svih proizvoda je: {math.fsum([prosecna_cena]):.2f} €")



prodati_komadi = [10, 50, 30, 15, 25, 100, 12, 20] 
ukupan_prihod = 0

for i in range(len(proizvodi)):
    naziv = proizvodi[i]
    cena_stavke = cene[naziv]
    kolicina = prodati_komadi[i]
    ukupan_prihod += cena_stavke * kolicina

print(f"Ukupan prihod od prodaje je: {ukupan_prihod:,.2f} €")


novi_proizvod = "Tablet"
nova_cena = 75.00
proizvodi.append(novi_proizvod)
cene[novi_proizvod] = nova_cena

print("\n--- Ažurirana lista proizvoda ---")
print(proizvodi)


print("\n--- Proizvodi sortirani po ceni (rastuće) ---")
sortirani_proizvodi = sorted(cene.items(), key=lambda stavka: stavka[1])

for proizvod, cena in sortirani_proizvodi:
    print(f"{proizvod} - {cena} €")