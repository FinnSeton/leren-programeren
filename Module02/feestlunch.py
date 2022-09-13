# Variables
############################################################
croissantpp = float(0.39)
stokbroodpp = float(2.78)
kortingsbon = float(0.50)
#############################################################
croissant = float(input("Hoeveel Croissantjes wil je "))
stokbrood = float(input("Hoeveel Stokbrooden wil je "))
kortingscodes = float(input("Hoeveel Kortingscodes heb je "))
#############################################################
#Berekeningen
croissantberekening = croissantpp * croissant
stokbroodberekening = stokbroodpp * stokbrood
totaal = croissantberekening + stokbroodberekening - kortingsbon * kortingscodes

print(f"|--------------------------| ")
print("|        Berekening        |")
print(f"|                          | ")
print(f"|  Croissantjes: {(croissantberekening)} euro | ")
print(f"|    Stokbrood: {(stokbroodberekening)} euro | ")
print(f"|--------------------------| ")
print(f"|  Kortingscodes: {( kortingsbon * kortingscodes )} euro | ")
print(f"|       Totaal: {(totaal)} euro | ")
print(f"|--------------------------| ")