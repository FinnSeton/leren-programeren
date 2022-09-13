


aantaltickets = float(input("Hoeveel tickets wil je: "))
VRtijd = float(input("Hoelang wil je VR doen: "))

ticketprice = 7.45
VRpermin = 0.074
rond = round(VRpermin * VRtijd * aantaltickets)
totaal = rond + ticketprice * aantaltickets

print('')
print('Totaal Kosten uitje')
print('')
print(f'Toegang koste zijn { ticketprice * aantaltickets } Euro')
print(f'VIP-VR-GameSeat koste zijn { (rond) } Euro')
print('')
print(f'Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {totaal} euro')