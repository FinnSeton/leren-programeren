from random import randint
import os 
from turtle import clear
from time import sleep

punt = 0
for i in range (20):
    computer_numer = randint(1,1000)
    rounds = 0
    while rounds <= 10:
        player_number = int(input('type een nummer tussen 1 en 1000  '))
        if player_number < computer_numer:
            print('>')
        elif player_number > computer_numer:
            print('<')
        elif player_number == computer_numer:
            print('correct +1 point')
            sleep(3)
            punt += 1
            break
        rounds += 1
        print(computer_numer)
        verschil = computer_numer - player_number
        print(verschil)
        if verschil <= 50:
            if verschil <= 20:
                print('erg warm')
            elif verschil <= 50:
                print('warm')
        if verschil >= -50:
            if verschil >= -20:
                print('erg warm')
            elif verschil >= -50:
                print('warm')
        else:
            print('koud')
            

    os.system('cls')
    input('wil je nog een keer ')
    print('volgende ronde')

print(punt)