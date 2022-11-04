layout = '50 '
getal = 50
aantal = 50
while aantal < 1000:
    getal += 1
    aantal += getal
    layout += f'+ {getal} '
    print(f'{layout} = {aantal}')