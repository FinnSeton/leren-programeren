answer = input("Is de kaas geel?: ") 
if answer == "ja": 
     answer = input("Zitten ergaten in?: ") 
     if answer == "ja": 
         answer = input("Is de kaas belagelijk duur?: ") 
         if answer == "ja": 
          print("Emmenthaler")
         elif answer == "nee": 
          print("Leerdammer")
     elif answer == "nee": 
         answer = input("Is de kaas  hard als steen?: ") 
         if answer == "ja": 
          print("Parmigiano Reggiano")
         elif answer == "nee": 
          print("Goudse Kaas")


elif answer == "nee": 
 answer = input("Heeft de kaasblauweschimmel?: ") 
 if answer == "ja": 
         answer = input("Heeft de kaas een korst?: ") 
         if answer == "ja": 
          print("Blue de Rochbaron")
         elif answer == "nee": 
          print("Foume d'Ambert")
 elif answer == "nee": 
         answer = input("Heeft de kaaseen korst?: ") 
         if answer == "ja": 
          print("Camembert")
         elif answer == "nee": 
          print("Mozzarella")