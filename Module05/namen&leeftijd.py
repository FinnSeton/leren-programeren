keuze = ''
list = []
def functie():
        name = input('Voer een naam in? ')
        age = input(f'Voer de leeftijd voor {name} in? ')
        dic = {}
        dic["name"] = name
        dic["age"] = age
        list.append(dic)

while keuze != 'stop':
    functie()
    keuze = input('Toets enter om door te gaan of stop om te printen:').lower()
    if keuze == 'stop':
        x = len(list)
        aantal = 0
        for z in range(0, x):
            print(f'{list[aantal]["name"]} is {list[aantal]["age"]}')
            aantal =+ 1