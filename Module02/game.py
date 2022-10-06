# !!!!!!!!!!!!!!!! 2de en 3de battle is kapot
# !!!!!!!!!!!!!!!! 2de en 3de battle is kapot
# !!!!!!!!!!!!!!!! 2de en 3de battle is kapot




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


def printDelay(t: str, d=2):  # function to printDelay with delay
    time.sleep(d)
    print(t)


clear_console()

# MOBS :
# 1. Wolf                   | Done
# 2. Green Goblin           | Done
# 3. Demon | Final Boss     | Done

# HP Variables:
PlayerHP = 100
#-------------------#
WolfHP = 75
GreenGoblinHP = 100
DeMoNHP = 250
#-------------------#

printDelay('Welkom tot de wereld van Sword Art Online.')
input('ENTER om verder te gaan')
clear_console()

printDelay('LINK START!!!!!!!!!!!')
time.sleep(2)
clear_console()
naam = input("Wat is uw naam: ")
gender = input('Kies je geslacht: Man/Vrouw: ').lower()
if gender == 'man':
    gender = 'Mannelijke'
elif gender == 'vrouw':
    gender = 'Vrouwelijke'
else:
    printDelay('Je hebt geen geldige keuze gemaakt')
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
printDelay(f'Je bent een {gender} {klasse} genaamd {naam} ')
time.sleep(3)
###########################################################################
clear_console()
start = input('Start het spel: Ja/Nee: ').lower()
if start == 'nee':
    printDelay('Het spel is gestopt')
    raise sys.exit()
###########################################################################
elif start == 'ja':
    printDelay('Het spel is gestart.')
    printDelay('')
    printDelay('Je bent wakker geworden in een vreemde wereld.')
    printDelay('Naast je ligt een tas, je opent de tas er zitten wapens in. ')
    printDelay('Het enige wat je ziet is een weg.')
    printDelay('Je loop de weg af todat, o Nee.')
    printDelay('Je komt een wild dier tegen.')
    printDelay('Je doet je best om het dier te indentificeren.')
    printDelay('Je heb even goed gekeken en je ziet dat het een wolf is.')
    printDelay(
        'KUT!!!!!, de wolf heeft je gezien je moet nu wel vechten anders ga je dood.')
    printDelay('FIGHT!!!!')
    time.sleep(5)
##############################################################################################
while WolfHP >= 0:  # battle loop
    clear_console()
    PlayerHP = 100
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
clear_console()
printDelay('Je loop dooren voor je zie je een berg')
printDelay('Nee WACHT "Shock Face"')
printDelay('Het is een Vulkaan, Shit ik moet weg hier')
printDelay('Je draait om en gaat via een bos pad terug')
printDelay('Je ziet een soort bos huisje met allemaal posters')
input('Klik ENTER om op de poster te kijken')
clear_console()
printDelay('''
                     BOUNTY
             -----------------------
                  Naam: Skynrad
            Award: 420000 Goud Stukken
              ---------------------
           Locatie: Boven op de Vulkaan  ''')  # verhaal idee is ongveer lord of de rings vibe waar nog 1 boss fight komts ja
############################################################################################
clear_console()
printDelay('Je loopt terug richting naar de vulkaan')
printDelay('Je staat bij de voet van de vulkaan en je ziet een soort van grot')
printDelay('Je loopt naar binnen en je ziet een soort van trap')
printDelay('Je loopt de trap op en je ziet een kamer')
printDelay('Je loopt naar binnen en je ziet iets bewegen in de andere kamer')
printDelay('Ga je het vreemde object aanvallen of ga je weg')
keuze2 = input('aanvallen/ weg: ').lower()
if keuze2 == 'aanvallen':
    printDelay(f'{naam}: Hey wie ben jij')
    printDelay('"Het onbekende mannenetje draait om"')
    printDelay('Hij ziet er niet uit als een normale mens')
    printDelay('Hij ziet er uit als een soort van goblin')
    printDelay(f'{naam}: Wat ben jij?')
    printDelay('?: Ik ben Rango de Goblin')
    printDelay(f'{naam}: Wat doe je hier?')
    printDelay('Rango: Ik ben woon hier wat doe jij hier in godsnaam?')
    printDelay(f'{naam}: Ik ben hier om Skynrad te verslaan')
    printDelay('Rango: Skynrad?')
    printDelay(f'{naam}: Ja Skynrad de Demon')
    printDelay(
        f'{naam} Ik kom hier voor de bounty op zijn hoofd en jij staat in mijn weg')
    printDelay(f'{naam} Ga dood Goblin')
################################################################################################
    while GreenGoblinHP >= 0:  # battle loop
        PlayerHP = 100
        clear_console()
        enemydmg = random.randint(10, 15)
        print(f'''
        _______________________________________________________________________________________
        Battle:
                        {naam} Hp = {PlayerHP}            Rango de Goblin Hp = {GreenGoblinHP}

                            Kies Aub een van de onderste opties: Een/Twee/Drie
                                {Attack}          ''')

        attackchoice2 = input(': ').lower()
        if attackchoice2 == 'een':
            GreenGoblinHP = GreenGoblinHP - een
            PlayerHP = PlayerHP - enemydmg
        elif attackchoice2 == 'twee':
            GreenGoblinHP = GreenGoblinHP - twee
            PlayerHP = PlayerHP - enemydmg
        elif attackchoice2 == 'drie':
            GreenGoblinHP = GreenGoblinHP - drie
            PlayerHP = PlayerHP - enemydmg

        if PlayerHP <= 0:
            input('Je bent dood gegaan de game is nu afgelopen klik Enter om te stoppen')
            sys.exit()
        if GreenGoblinHP <= 0:
            print('Je hebt je tegenstander verslagen je kan nu door ')
        break
################################################################################################
printDelay('Top die is ook weg')
printDelay('Je loopt de kamer in en je ziet een soort van trap')
printDelay('Je loopt de trap op en je beland in een balkon dat over de vulkaan uit kijkt')
printDelay('Je ziet een soort van enorme grot')
printDelay('Er komt een sterke aura uit de grot')
printDelay('Je zit 2 Rode ogen in de grot')
printDelay('Je duikt snel weg en gaat terug naar buiten')
printDelay('Je bent nu weer buiten je gaat verder met het beklimmen van de berg')
printDelay('Je bent nu boven op de berg gekomen je ziet de ingang van de grote grot')
printDelay('SKYNRAD!!!!')
printDelay('Je loopt naar binnen het is donker en in een gaan er allemaal vuur branden')
printDelay('Je ziet hem staan Skynrad')
printDelay('Hij ziet er niet uit als een normale mens')
printDelay('Hij is veel groter net een berg')
printDelay('Hij ziet er uit als een soort van demon')
printDelay('Skynrad: Wie ben jij?')
printDelay(f'{naam}: Ik ben {naam} ik kom hier om jou om te leggen')
printDelay('Skynrad: Ik ben Skynrad de Demon')
printDelay('Skynrad: Haha je bent niet sterk genoeg om mij te verslaan')
printDelay(f'{naam}: Ik ga Jou verslaan al is het de laatste wat ik doe')
printDelay('Skynrad: Haha kom maar op!!!!!')
################################################################################################
while DeMoNHP >= 0:  # battle loop
        clear_console()
        enemydmg = random.randint(10, 15)
        print(f'''
        _______________________________________________________________________________________
        Battle:
                        {naam} Hp = {PlayerHP}            Skynrad de Demon Hp = {DeMoNHP}

                            Kies Aub eem van de onderste opties: Een/Twee/Drie
                                {Attack}          ''')

        attackchoice = input(': ').lower()
        if attackchoice == 'een':
            DeMoNHP = DeMoNHP - een
            PlayerHP = PlayerHP - enemydmg
        elif attackchoice == 'twee':
            DeMoNHP = DeMoNHP - twee
            PlayerHP = PlayerHP - enemydmg
        elif attackchoice == 'drie':
            DeMoNHP = DeMoNHP - drie
            PlayerHP = PlayerHP - enemydmg

        if PlayerHP <= 0:
            input('Je bent dood gegaan de game is nu afgelopen klik Enter om te stoppen')
            sys.exit()
        if DeMoNHP <= 0:
            print('Je hebt Skynrad verslagen ')
        break
printDelay('Gefeliciteerd je hebt de game uitgespeeld')