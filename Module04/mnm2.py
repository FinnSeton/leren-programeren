import random

kleuren = ["Rood", "Blauw", "Groen", "Geel", "Bruin"]
output = {}

aantal = int(input("Hoeveel M&M's?: "))

for i in range(aantal):
    a = random.randint(0, len(kleuren)-1)
    output[kleuren[a]] = output.get(kleuren[a], 0) + 1

print(output)