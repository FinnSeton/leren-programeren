import random

kleuren = ("oranje ", "blauw ", "groen ", "bruin ")
aantal = int(input("Hoeveel M&M's?: "))

Eminem = []
for i in range(aantal):
    random_num = random.randint(0, 3)
    random_color = kleuren[random_num]
    Eminem.append(random_color)

print(Eminem)