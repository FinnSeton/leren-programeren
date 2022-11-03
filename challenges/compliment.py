import random
oldcomp = 0
newcomp = 0
naam = input("Wat is uw naam? ")
aantal = int(input("Hoevaak wilt je het? "))
for i in range(aantal):
    
    newcomp = random.randint(1, 6)
    if newcomp == 1:
        compliment = "Je bent een mooie persoon"
    elif newcomp == 2:
        compliment = "Je kleren zijn mooi"
    elif newcomp == 3:
        compliment = "Jij bent echt mooi"
    elif newcomp == 4:
        compliment = "Je bent zo cool"
    elif newcomp == 5:
        compliment = "jij kan zo goed programmeren"
    print(f"{compliment}: {naam}")