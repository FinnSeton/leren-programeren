from random import random
import sys, os

os.system('cls')

# MOBS :
#
#1. Wolf
#2. Green Goblin
#3. Slime
#4. Horned Beer
#5. Demon | Final Boss

#HP Variables:
PlayerHP = 100 
#-------------------#
WolfHP = 75
GreenGoblinHP = 100
SlimeHP = 125
HornedBeerHP = 150
DeMoN = 250

print('Welkom tot de wereld van Sword Art Online.')
########################################################################## | Done
input('ENTER om verder te gaan')
print('LINK START!!!!!!!!!!!')
########################################################################## | Done
naam = input("Wat is uw naam")
gender = input('Kies je geslacht: Man/Vrouw: ').lower()
if gender == 'man':
    gender = 'Mannelijke'
elif gender == 'vrouw':
    gender = 'Vrouwelijke'
###########################################################################
klasse = input('Kies je klasse: Warrior/Mage/Archer: ') # door de input word de klasse gekozen / Done
if klasse == 'Warrior':
    Attacks= ['Slash', 'Stab', 'Punch']
    slash = random.randint(10, 20)
    stab = random.randint(10, 20)
    punch = random.randint(10, 20)
elif klasse == 'Mage':
    Attacks = ['Fireball', 'Iceball', 'Lightning']
    fireball = random.randint(10, 20)
    iceball = random.randint(10, 20)
    lightning = random.randint(10, 20)
elif klasse == 'Archer':
    Attacks = ['Arrow', 'Piercing Arrow', 'Explosive Arrow']
    arrow = random.randint(10, 20)
    piercingarrow = random.randint(10, 20)
    explosivearrow = random.randint(10, 20)
###########################################################################
print(f'Je bent een {gender} genaamd {naam} en je klasse is een {klasse}')
###########################################################################
print('')
input = input('Start het spel: Ja/Nee: ').lower()
if input == 'nee':
    print('Het spel is gestopt')
    raise SystemExit
elif input == 'ja':
    print('Het spel is gestart')
    print('')
    print('Je bent wakker geworden in een vreemde wereld.')
    print('Je bent in een bos beland en je ziet een huisje.')
    huisje = input('Ga je naar het huisje toe: Ja/Nee: ').lower() # moet nog een nee elif krijgen
    if huisje == 'ja':
        print('Je betreed het huisje')
        keuze1 = input('Je ziet een bar mevrouw en een vreemde man tegen wie ga je praten? Bar mevrouw / Vreemde man: ').lower() # moet nog een nee elif krijgen
        if keuze1 == 'bar mevrouw':
            print('Je praat met de bar mevrouw')
            print('Ze vraagt of je een drankje wilt')
            drankje = input('Wil je een drankje: Ja/Nee: ').lower() # moet nog een nee elif krijgen
            if drankje == 'ja':
                print('Je krijgt een drankje')
                print('Je voelt je beter')
                mes =input('je ziet een mes liggen op een van de tafels wil je het Stelen: Ja/Nee: ').lower()
                if mes == 'ja':
                    print('Je steelt het mes')
                    print('Niemand ziet het goedzo')
                    print('Je loopt naar buiten')
                elif mes == 'nee':
                    print('Je loopt naar buiten')
                print('Je gaat weer verder')
                print('')
                print('Je komt een kruispunt tegen')
                kruispunt = input('Ga je naar links of rechts: Links/Rechts: ').lower() # moet nog een rechts elif krijgen
                if kruispunt == 'links':
                    print('Je gaat naar links')
                    print('Je komt een wild dier tegen')
                    print('wil jij het dier indentificeren of aanvallen')
                    print('als je hem indentificeert weet je wat je te vechten staat je hebt wel een kans dat je ondekt wordt') 
                    input('als je aanvalen kiest heb je het effect van suprise : Identificeren/Aanvallen: ').lower() # moet nog een aanvallen elif krijgen
                    if input == 'identificeren':
                        enemy = 'Wolf'
                        print('Je heb even goed gekeken en je ziet dat het een wolf is')
                        print('KUT!!!!! de wolf heeft je ontdekt je moet nu wel vechten anders ga je dood')
                        print('FIGHT!!!!')
                        print(f'''
                        {naam} Hp = {PlayerHP}              {enemy} Hp = {WolfHP}

                        
                        
                        ''')
