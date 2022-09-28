naam = input("Wat is u naam? ")
gender = input("Man/Vrouw/Anders ").lower
if gender == ("man"):
    snor = input("Hoe breed is jou snor in cm? ")
if gender == ("vrouw"):
    haar1 = input("Heb jij rood gekleurd haar Ja/Nee ").lower
    haar2 = input("Heb jij gekruld haar Ja/Nee ").lower
    haar3 = input("Hoelang is je haar ")
if gender == ("anders"):
    print ("Hier doen we dus precies niks mee (;")
pronounce = input("Pronounce ")
input("als je 13 bent paars of slavink ")
lengte = int(input("Hoe lang bent u in hele cm? "))
gewicht = int(input("Wat is uw lichaams gewicht in hele kg? "))
hoed = str(input("Heeft u een hoge hoed? Ja/Nee ")).lower
input("wat is je favoriete kaas Brie/Gouda/Oud/Jong/Blauw/Paars/Furry/Femboy/Auto/Boeing747/Mustang/Duikboot Dan").lower
praktijkervaringdieren = int(input("Hoeveel jaar pratijk ervaring met dieren-dressuur heeft u? "))
praktijkervaringjongleren = int(input("Hoeveel jaar heeft u met jongleren? "))
praktijkervaringacrobatiek = int(input("Hoeveel jaar pratijk ervaring heeft u met acrobatek? "))
diploma = str(input("Welke MBO Diploma heeft u? 1/2/3/4 "))
vrachtwagenrijbewijs = str(input("Bent u in bezit van een vrachtwagen rijbewijs? Ja/Nee ")).lower
certificaat = str(input("Heeft u een certificaat voor overleven met gevaarlijk personeel? Ja/Nee ")).lower

if lengte < int("150") or gewicht < int("90") or praktijkervaringdieren < int("4") or hoed == ("nee") or praktijkervaringjongleren < ("5") or praktijkervaringacrobatiek < ("3") or diploma != ("4") or vrachtwagenrijbewijs != ("ja") or haar1 != ("ja") or haar2 != ("ja") or haar3 < ("20") or snor < ("10") or certificaat != ("ja"): 
    print("Uw solicitatie is afgewezen probeer het later opnieuw.")  
elif lengte > int("150") or gewicht > int("90") or praktijkervaringdieren > int("4") or hoed != ("nee") or praktijkervaringjongleren > ("5") or praktijkervaringacrobatiek > ("3") or diploma == ("4") or vrachtwagenrijbewijs == ("ja") or haar1 == ("ja") or haar2 == ("ja") or haar3 > ("20") or snor > ("10") or certificaat == ("ja"): 
    print("Goedgekeurt Stuur snel je CV op.")
