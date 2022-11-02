uur = 0
min = 0
while uur <= 11:
    if min == 60:
        uur = uur + 1
        min = 0
    min = min + 1
    ap = ('AM')
    print (ap, uur, min)
else:
    while uur <= 23:
        if min == 60:
            uur = uur + 1
            min = 0
        min = min + 1
        ap = ('PM')
        print (ap, uur, min)
    