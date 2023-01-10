from fruitmand import fruitmand

names = []
colors = ""
weight = ""

for i in fruitmand:
    names.append(i['name'])
names.sort(key=len, reverse=True)

for i in fruitmand:
    if i['name'] == names[0]:
        colors += i['color']
        weight += i['weight']

letter_amount = len(names[0])

print(f"De '{names[0]}' ({letter_amount} letters) heeft een {colors[0]} kleur en een gewicht van {weight[0]}G")