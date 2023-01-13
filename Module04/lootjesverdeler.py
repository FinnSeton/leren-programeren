import random

namen = []
meernamen = "ja"
lootjeaantal = 0
keuze1 = 0
keuze2 = 1

while meernamen == "ja":
    naaminput = input("Geef een naam: ").capitalize()
    if naaminput in namen:
        print("Deze naam is al ingevoerd.")
    elif naaminput not in namen:
        namen.append(naaminput)
        random.shuffle(namen)
        if len(namen) >= 3:
            while meernamen != 'nee' and 'ja':
                meernamen = input(
                    "Wil je nog meer namen invoeren? (ja/nee): ").lower()

try:
    while lootjeaantal != len(namen):
        lootjeaantal += 1
        print(f"Lootje {lootjeaantal}")
        print(f"{namen[keuze1]} heeft {namen[keuze2]}")
        keuze1 += 1
        keuze2 += 1
except:
    print(f"{namen[-1]} heeft {namen[0]}")
