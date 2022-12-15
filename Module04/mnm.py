import random

kleuren = ("oranje ", "blauw ", "groen ", "bruin ")
aantal = int(input("Hoeveel M&M's?: "))

Eminem = []
for i in range(aantal):
    Eminem.append(random.randint(0, 3))

print(Eminem)