# GroupA
print('Welke landen spelen er in GroupA')
land1 = input('Land 1 is? ')
land2 = input('Land 2 is? ')
land3 = input('Land 3 is? ')
#####################################
score1 = 0
score2 = 0
score3 = 0
#####################################
print('Wedstrijd 1 voer in hoeveel doelpunten elk land heeft gehaald')
Ws1land1 = int(input(f"{land1} : "))
Ws1land2 = int(input(f"{land2} : "))
print('Wedstrijd 2 voer in hoeveel doelpunten elk land heeft gehaald')
Ws2land1 = int(input(f"{land2} : "))
Ws2land2 = int(input(f"{land3} : "))
print('Wedstrijd 3 voer in hoeveel doelpunten elk land heeft gehaald')
Ws3land1 = int(input(f"{land1} : "))
Ws3land2 = int(input(f"{land3} : "))
######################################
if Ws1land1 >= Ws1land2:
    score1 += 3
elif Ws1land1 <= Ws1land2:
    score2 += 3
if Ws2land1 >= Ws2land2:
    score2 += 3
elif Ws2land1 >= Ws2land2:
    score3 += 3
if Ws3land1 >= Ws3land2:
    score1 += 3
elif Ws3land1 >= Ws3land2:
    score3 += 3

print(score1)
print(score2)
print(score3)