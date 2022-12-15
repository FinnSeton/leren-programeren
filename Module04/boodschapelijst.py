boodschappen = {}
userinput = True

while userinput:
    userinput = input("wilt je iets toevoegen?(j/n): ").lower()
    if userinput == 'n':
        userinput = False
    else:
        grocery = input("Wat wilt u toevoegen: ").capitalize()
        amount = int(input("Hoeveel wilt u er van toevoegen: "))
        if grocery in boodschappen:
            boodschappen[grocery] += amount
        else:
            boodschappen[grocery] = amount

print(f'-[ BOODSCHAPPENLIJSTJE ]-\n')
for grocery in boodschappen:
    amountString = str(boodschappen[grocery])
    print(f"{amountString:>4}x {grocery}")
print(f'\n-------------------------')