# Het is idee is dat de game een soort parodie is op swordt art online. (is een soort Vr game)
# De game begin met dat je een avatar moet kiezen. Gender/Class/Name
# Met elke Class komen ander Weapons.
# De game zelf begin zo "Je wordt wakker in een vreemde wereld alles wat je ziet is dat je in een bos met een weg aan het einde van de weg zie je een kruispunt. Je kan naar links of rechts gaan. Waar ga je heen?"
# je kiest of je links of rechts wil gaan en dan krijg je een random event. (bijvoorbeeld een monster)
# Als je een monster verslaat kan je door naar de volgende naar ongeveer 2 mobs kom je bij de end boss (bijvoorbeeld een demon)
# Als je de end boss verslaat kom je bij een einde van de game. (bijvoorbeeld een portal)
# Als je de portal in gaat kom je weer terug in de echte wereld. (bijvoorbeeld een kamer met een computer)
#
from multiprocessing.connection import wait
import sys
import random
import os
import time
from turtle import clear


def clear_console():
    os.system('cls')


clear_console()

# MOBS :
#
# 1. Wolf
# 2. Green Goblin
# 3. Horned Beer
# 4. Demon | Final Boss

# HP Variables:
PlayerHP = 100
#-------------------#
WolfHP = 75
GreenGoblinHP = 100
HornedBeerHP = 150
DeMoN = 250
#-------------------#

print('Welkom tot de wereld van Sword Art Online.')
input('ENTER om verder te gaan')
clear_console()
time.sleep(2)
print('LINK START!!!!!!!!!!!')
time.sleep(1)
clear_console()
naam = input("Wat is uw naam: ")
gender = input('Kies je geslacht: Man/Vrouw: ').lower()
if gender == 'man':
    gender = 'Mannelijke'
elif gender == 'vrouw':
    gender = 'Vrouwelijke'
else:
    print('Je hebt geen geldige keuze gemaakt')
    sys.exit()
###########################################################################
klasse = input('Kies je klasse: Warrior/Mage/Archer: ')
if klasse == 'Warrior':
    Attack = ['Een: Slash', 'Twee: Stab', 'Drie: Punch']
    een = random.randint(10, 20)  # Slash
    twee = random.randint(10, 20)  # Stab
    drie = random.randint(10, 20)  # Punch
if klasse == 'Mage':
    Attack = ['Een: Fireball', 'Twee: Iceball', 'Drie: Lightning']
    een = random.randint(10, 20)  # Fireball
    twee = random.randint(10, 20)  # Iceball
    drie = random.randint(10, 20)  # Lightning
if klasse == 'Archer':
    Attack = ['Een: Arrow', 'Twee: Piercing Arrow', 'Drie: Explosive Arrow']
    een = random.randint(10, 20)  # Arrow
    twee = random.randint(10, 20)  # Piercing Arrow
    drie = random.randint(10, 20)  # Explosive Arrow
###########################################################################
print(f'Je bent een {gender} {klasse} genaamd {naam} ')
###########################################################################
time.sleep(5)
clear_console()
start = input('Start het spel: Ja/Nee: ').lower()
if start == 'nee':
    print('Het spel is gestopt')
    raise sys.exit()
###########################################################################
elif start == 'ja':
    print('Het spel is gestart.')
    print('')
    time.sleep(1)
    print('Je bent wakker geworden in een vreemde wereld.')
    time.sleep(2)
    print('Naast je ligt een tas, je opent de tas er zitten wapens in. ')
    time.sleep(2)
    print('Het enige wat je ziet is een weg.')
    time.sleep(2)
    print('Je loop de weg af todat, o Nee.')
    time.sleep(2)
    print('Je komt een wild dier tegen.')
    time.sleep(2)
    print('Je doet je best om het dier te indentificeren.')
    time.sleep(2)
    print('Je heb even goed gekeken en je ziet dat het een wolf is.')
    time.sleep(2)
    print('KUT!!!!!, de wolf heeft je gezien je moet nu wel vechten anders ga je dood.')
    time.sleep(2)
    print('FIGHT!!!!')
##############################################################################################
while WolfHP >= 0:  # battle loop
    clear_console()
    enemydmg = random.randint(5, 10)
    print(f'''
    _______________________________________________________________________________________
    Battle:
                    {naam} Hp = {PlayerHP}            Wolf Hp = {WolfHP}

                        Kies Aub eem van de onderste opties: Een/Twee/Drie
                            {Attack}          ''')


    attackchoice = input(': ').lower()
    if attackchoice == 'een':
        WolfHP = WolfHP - een
        PlayerHP = PlayerHP - enemydmg
    elif attackchoice == 'twee':
        WolfHP = WolfHP - twee
        PlayerHP = PlayerHP - enemydmg
    elif attackchoice == 'drie':
        WolfHP = WolfHP - drie
        PlayerHP = PlayerHP - enemydmg
    
    if PlayerHP <= 0:
        input('Je bent dood gegaan de game is nu afgelopen klik Enter om te stoppen')
        sys.exit()
    if WolfHP <= 0:
        print('Je hebt je tegenstander verslagen je kan nu door lopen')
        break
#############################################################################################
time.sleep(4)
clear_console()
print('Je loop dooren voor je zie je een berg')
time.sleep(1)
print('Nee WACHT "Shock Face"')
time.sleep(1)
print('Het is een Vulkaan, Shit ik moet weg hier')
time.sleep(1)
print('Je draait om en gaat via een bos pad terug')
time.sleep(1)
print('Je ziet een soort bos huisje met allemaal posters')
time.sleep(1)
input('Klik ENTER om op de poster te kijken')
time.sleep(1)
print('''
                     BOUNTY
             -----------------------
                  Naam: Skynrad
            Award: 420000 Goud Stukken
              ---------------------
           Locatie: Boven op de Vulkaan  ''') # vserhaal idee is ongveer lord of de rings vibe waar nog 1 boss fight komts ja doe toekomstige Finn