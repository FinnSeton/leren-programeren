try:
    smallpizza = int(input("Hoeveel Small Pizza's wil je: "))
except :
    print("Dat is geen nummer!")
    smallpizza = 0
try:  
    mediumpizza = int(input("Hoeveel Medium Pizza's wil je: "))
    mediumpizza = 0
except :
    print("Dat is geen nummer!")
try:    
    largepizza = int(input("Hoeveel Large Pizza's wil je: "))
except :
    print("Dat is geen nummer!")
    largepizza = 0
#################################################################
smallpizzaprice = float (7.99)
mediumpizzaprice = float (11.99)
largepizzaprice = float (13.99)
totaal = smallpizza*smallpizzaprice + mediumpizza*mediumpizzaprice + largepizza*largepizzaprice
#################################################################
print("")
print("")
print("Geselcteerde Pizza's")
print(f"{smallpizza} Small Pizza's")
print(f"{mediumpizza} Medium Pizza's")
print(f"{largepizza} Large Pizza's")
print("")
print("-----------------------------")
print("|         Bonnetje          |")
print("|                           |")
print(f"| Small Pizza : {smallpizza*smallpizzaprice} Euro  |")
print(f"| Medium Pizza : {mediumpizza*mediumpizzaprice} Euro |")
print(f"| Large Pizza : {largepizza*largepizzaprice} Euro  |")
print("|                           |")
print(f"| Totaal : {totaal} Euro       |")
print("-----------------------------")
