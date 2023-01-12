namen = []
aantalnamen = 0
meernamen = "ja"
lootjeaantal = 1
keuze1 = 0
keuze2 = 1 

while meernamen == "ja":
        naaminput = input("Geef een naam: ").capitalize()
        if naaminput in namen:
            print("Deze naam is al ingevoerd.")
        elif naaminput not in namen:
            namen.append(naaminput)
            aantalnamen += 1
            if aantalnamen >= 3:
                meernamen = input("Wil je nog meer namen invoeren? (ja/nee): ").lower()

try:
    print(f"Er zijn {aantalnamen} namen ingevoerd.")
    while lootjeaantal != aantalnamen:
        print(f"Lootje {lootjeaantal}")
        print(f"{namen[keuze1]} | {namen[keuze2]}")
        lootjeaantal += 1
        keuze1 += 2
        keuze2 += 2
except:
    print(f"Er is 1 iemand over {namen[-1]} ")