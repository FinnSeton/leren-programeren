iphone13 = int(input("Prijs Iphone 13: "))
SamsungGS22 = int(input("Prijs Samsung Galaxy S22: "))
berekening = iphone13 - SamsungGS22
print("")
if iphone13 > SamsungGS22:
    print(f"De Iphone 13 is het duurst, de telefoon kost:{iphone13}")
    print(
        f"De Samsung Galaxy S22 is het goedkoopst, de telefoon kost: {SamsungGS22} Euro")
elif iphone13 < SamsungGS22:
    print(
        f"De Samsung Galaxy S22 is het duurst, de telefoon kost:{SamsungGS22} Euro ")
    print(f"De Iphone 13 is het goedkoopst, de telefoon kost: {iphone13} Euro")

if iphone13 > 900 or SamsungGS22 > 900:
    print("Het advies is dus geen telefoon te kopen, ze zijn te duur.")
elif berekening > 50:
    print(
        f"Het advies is dus de Samsung Galaxy S22 te kopen. Deze is namelijk {berekening} goedkoper / duurder dan de Iphone 13")
else:
    print(
        f"Het advies is dus de Iphone 13 te kopen. Deze is namelijk {berekening} euro goedkoper / duurder dan de Samsung Galaxy S22")
