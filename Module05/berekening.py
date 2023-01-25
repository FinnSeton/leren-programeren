#variables
gebruiker_nummer = 0
meer_rondes = True

#functions
def plus(nummer1: float, nummer2: float):
    print(f"{nummer1} + {nummer2} = {float(nummer1) + float(nummer2)}")
    return nummer1 + nummer2

def min(nummer1: float, nummer2: float):
    print(f"{nummer1} - {nummer2} = {float(nummer1) - float(nummer2)}")
    return nummer1 -nummer2

def keer(nummer1: float, nummer2: float):
    print(f"{nummer1} * {nummer2} = {float(nummer1) * float(nummer2)}")
    return nummer1 * nummer2

def delen(nummer1: float, nummer2: float):
    print(f"{nummer1} / {nummer2} = {float(nummer1) / float(nummer2)}")
    return nummer1 / nummer2

#while loop
while meer_rondes:
    keuze = input("""wat wil je doen?
    #     A) getallen optellen
    #     B) getallen aftrekken
    #     C) getallen vermenigvuldigen
    #     D) getallen delen
    #     E) getal ophogen
    #     F) getal verlagen
    #     G) getal verdubbelen
    #     H) getal halveren
    #     Kies: """).upper()

    if gebruiker_nummer:
        n1 = float(input("Welk getal: "))
        n2 = gebruiker_nummer
    elif keuze == "A" or keuze == "B" or keuze == "C" or keuze == "D":
        n1 = float(input("Getal 1: "))
        n2 = float(input("Getal 2: "))
    else:
        n1 = float(input("Welk getal: "))

    if keuze == "A":
        gebruiker_nummer += float(plus(n1, n2))
    elif keuze == "B":
        gebruiker_nummer += min(n1, n2)
    elif keuze == "C":
        gebruiker_nummer += keer(n1, n2)
    elif keuze == "D":
        gebruiker_nummer += delen(n1, n2)
    elif keuze == "E":
        gebruiker_nummer += plus(n1, 1)
    elif keuze == "F":
        gebruiker_nummer += min(n1, 1)
    elif keuze == "G":
        gebruiker_nummer += keer(n1, 2)
    elif keuze == "H":
        gebruiker_nummer += delen(n1, 2)

    meer_rondes = input(f"Do you want to do something with {gebruiker_nummer}? (Y/N): ").upper()
    if meer_rondes == "N":
        meer_rondes = False
    elif meer_rondes == "Y":
        meer_rondes = True
    else:
        print("Invalid answer")