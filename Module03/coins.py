# name of student: Finn Seton
# number of student: 99071540
# purpose of program: om te kijken hoeveel wisselgeld je terug krijgt 
# function of program: bereken hoeveel wisselgeld je krijgt en hoeveel je krijgd
# structure of program: hij ontvanged int's van de inputs en berekend hoeveel je moet geven en hoeveel je terug krijgt

toPay = int(float(input('Amount to pay: ')) * 100)  # toPay is een user input * 100
paid = int(float(input('Paid amount: ')) * 100)  # paid is een user input * 100
change = paid - toPay  # change een var paid - var toPay
amountReturned = ""
payed = [500, 300, 200, 50, 20, 10, 5, 2, 1]
payedString = ""

if change > 0:  # Checked of var change is groter dan 0
    coinValue = 500  # giving coinValue a value

    while change > 0 and coinValue > 0:  # Checked of change is groter dan 0 en coinValue is groter dan 0
        nrCoins = change // coinValue  # var nrCoins is change gedeeld door coinValue met extra's
        if nrCoins > 0:  # check of nrCoins is groter dan 0
            print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!')  # print a string
            nrCoinsReturned = int(input('How many coins of ' + str(coinValue) + ' cents did you return? '))  #
            change -= nrCoinsReturned * coinValue  #
            amountReturned += str(coinValue) + " x" + str(nrCoinsReturned) + "\n"

        # comment on code below: coinValue gaat van 500 naar 0
        if coinValue == 500:
            coinValue = 300
        elif coinValue == 300:
            coinValue = 200
        elif coinValue == 200:
            coinValue = 50
        elif coinValue == 50:
            coinValue = 20
        elif coinValue == 20:
            coinValue = 10
        elif coinValue == 10:
            coinValue = 5
        elif coinValue == 5:
            coinValue = 2
        elif coinValue == 2:
            coinValue = 1
        else:
            coinValue = 0

if change > 0:  # Checks if change is greater than 0
    print('Change not returned: ', str(change) + ' cents')

else:
    print('done')
print(amountReturned)