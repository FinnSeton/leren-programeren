uitgraven = 25 #per m3
afvoeren = 32.50 #per m3
km = 60
tegelmeerpijs = 0
lengte = input(int('Voer de lengte in van je zwembad'))
breedte = input(int('Voer de breedte in van je zwembad'))
diepte = input(int('Voer de diepte/hoogte in van je zwembads'))
tegeloptie = 'Zelf kiezen'#input('Wil u uw tegel Rood/Standaard/Zelf kiezen.').lower()
m3 = lengte * breedte * diepte
m2 = lengte * breedte
uittot = uitgraven * m3
aftot = afvoeren * m3
tot = uittot + aftot

if m3 <= 20 and km <= 50:
    voorrijkosten = km * 1.25 + 100
elif m3 <= 20 and km >= 50:
    voorijkosten = km * 1.15 + 100
elif m3 >= 20 and km <= 50:
    voorijkosten = km * 2.15 + 250
elif m3 >= 20 and km >= 50:
    voorijkosten = km * 2.05 + 250

if m3 <= 20:
    tegelm2 = 250
    if tegeloptie == 'standaard':
        tegelmeerpijs = 0
    elif tegeloptie == 'zelf kiezen':
        tegelmeerpijs = 100
    elif tegeloptie == 'rood':
        tegelmeerpijs = 25 * m2
elif m3 >= 20:
    tegelm2 = 200
    if tegeloptie == 'standaard':
        tegelmeerpijs = 0
    elif tegeloptie == 'zelf kiezen':
        tegelmeerpijs = 125
    elif tegeloptie == 'rood':
        tegelmeerpijs = 20 * m2
Tegeltot = m2 * tegelm2 + tegelmeerpijs


print(f'Offerte voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud: {m3} m3)')
print(f'Uitgraven: {uittot} euro')
print(f'Afvoeren grond: {aftot} euro')
print(f'Voorrijkosten: {voorijkosten} euro')
print(f'Beton + Tegels {m2} m2: {Tegeltot} euro')
print(f'Totaal: {tot} euro')