Naam = input('Wat is uw naam?')
Gender = input('Wat is uw gender? ').lower
if Gender ==  ('man'):
    snor1 = input('Heeft u een snor? ').lower
    if snor1 == 'ja':
        snor2 = int(input('Hoe breed is je snor in cm? '))
if Gender == ('vrouw'):
    Kapsel1 = input('Wat voor soort haar heeft u? ')
    Kapsel2 = input('Wat voor kleur haar heeft u? ')
    Kapsel3 = int(input('Hoelang is uw haar in cm? '))
if Gender != 'man' or 'vrouw':
    raise NameError('Je bent niet welkom hier schoft') 
hoed = input("Heeft u een hoge hoed? ").lower
Rijbewijs = input("heeft u een geldig vrachtwagenbewijs? ").lower
lengte = int(input("Hoelang bent u? "))
gewicht = int(input('Hoeveel weegt u? '))
if gewicht >= 200 :
    raise NameError ('U bent te zwaar om door te gaan het gebouw zou instorten')
MBO = input('Bent u in bezit van een Diploma MBO-4? ')
if mbo <= 4:
    raise NameError('We zijn geen jostiband hier dumbass')
Certificaat = input('Heeft Certificaat Overleven met gevaarlijk personeel? ').lower
Dieren_dressuur = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? '))
jongleren = int(input('Hoeveel jaar ervaring heeft u met jongleren? '))
acrobatiek = int(input('Hoeveel jaar praktijkervaring heeft u met acrobatiek? '))
brie = input('Houd u van een lekker crackertje met brie? ').lower
opa = input('Houd u van uw opa? ')
vrienden = int(input('hoeveel vrienden heeft u? '))
if vrienden == 0:
    raise NameError('Je bent oprecht een loser')
familie = int(input('Hoeveel broertjes/zusjes heeft u? '))

if (Gender == 'man') or(Gender == 'vrouw' and Kapsel1 == 'krullen' and Kapsel2 == 'rood' and Kapsel3 >= 20) and  hoed == 'ja' and Rijbewijs == 'ja' and lengte >= 150 and gewicht >= 90 and MBO == 'ja' and Certificaat == 'ja' and Dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3 and brie == 'ja' and opa == 'nee' and vrienden >= 4 and familie >= 1:
    print('Je bent goedgekeurd')
else:
    print('Je hebt de sollicitaie is fout ingevuld probeer het later opnieuw.')