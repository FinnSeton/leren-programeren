week = ["ma","di","wo","do","vr","za","zo"]
keuze = input("Geef een dag van de week op: ")

while keuze != week[0]:
    print(week[0])
    week.pop(0)