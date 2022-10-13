uitgraven = 25 #per m3
afvoeren = 32.50 #per m3
km = 60
lengte = 8
breedte = 3
diepte = 1.5
m3 = lengte * breedte * diepte
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


print(f'Offerte voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud: {m3} m3)')
print(f'Uitgraven: {uittot} euro')
print(f'Afvoeren grond: {aftot} euro')
print(f'Voorrijkosten: {voorijkosten} euro')
print(f'Totaal: {tot} euro')