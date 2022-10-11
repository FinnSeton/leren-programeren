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

specialtxt = "Je hebt geen specials"
armor = 0

clear_console()

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
###########################################################################
naam = input("Wat is uw naam: ")
try:
    gender = input('Kies je geslacht: Man/Vrouw: ').lower()
    if gender == 'man':
        gender = 'Mannelijke'
    elif gender == 'vrouw':
        gender = 'Vrouwelijke'
    else:
        printDelay('Je hebt geen geldige keuze gemaakt')
        sys.exit()
except:
    printDelay('Je hebt een fout andwoordt gegeven bij gender')
    sys.exit()
###########################################################################
try:
    klasse = input('Kies je klasse: Warrior/Mage/Archer: ')
    if klasse == 'Warrior':
        Attack = ('Een: Slash', 'Twee: Stab', 'Drie: Punch')
        een = random.randint(10, 20)  # Slash
        twee = random.randint(5, 15)  # Stab
        drie = random.randint(3, 10)  # Punch
    if klasse == 'Mage':
        Attack = ('Een: Fireball', 'Twee: Iceball', 'Drie: Lightning')
        een = random.randint(7, 20)  # Fireball
        twee = random.randint(4, 16)  # Iceball
        drie = random.randint(5, 15)  # Lightning
    if klasse == 'Archer':
        Attack = ('Een: Arrow', 'Twee: Piercing Arrow', 'Drie: Explosive Arrow')
        een = random.randint(8, 17)  # Arrow
        twee = random.randint(6, 15)  # Piercing Arrow
        drie = random.randint(7, 16)  # Explosive Arrow
    # # # # # # # # # # # # # # # # # # 
    if klasse == 'debug':
        password = input('Password: ')
        if password == 'Password123':
            Attack = ('Een: Dikke bonker', 'Twee: Nuke', 'Drie: Explosive Boem')
            een = random.randint(9999, 99999)  # Arrow
            twee = random.randint(9999, 99999)  # Piercing Arrow
            drie = random.randint(9999, 99999)  # Explosive Arrow
            def printDelay(t: str, d=0):  # function to printDelay with delay
                time.sleep(d)
                print(t)
        else:
            print('Verkeerd Password Biatch!!!!!!.')
            time.sleep(2)
            sys.exit()
except:
    printDelay('Je hebt een fout andwoordt gegeven bij klasse')
###########################################################################
printDelay(f'Je bent een {gender} {klasse} genaamd {naam} ')
time.sleep(3)
###########################################################################
clear_console()
start = input('Start het spel: Ja/Nee: ').lower()
if start == 'nee':
    printDelay('Het spel is gestopt')
    raise sys.exit()

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
else:
    printDelay('Je hebt geen geldige keuze gemaakt opnieuw starten')
    sys.exit()
##############################################################################################
PlayerHP = 100
while WolfHP >= 0:  # battle loop
    enemydmg = random.randint(5, 15)
    clear_console()
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
    else:
        print('Je hebt geen geldige keuze gemaakt probeer het opnieuw')
        time.sleep(2)

    if PlayerHP <= 0:
        input('Je bent dood gegaan de game is nu afgelopen klik Enter om te stoppen')
        sys.exit()
    if WolfHP <= 0:
        print('Je hebt je tegenstander verslagen je kan nu door lopen')
        PlayerHP  = 100 + armor
        break
#############################################################################################
clear_console()
printDelay('Je loop door en voor je zie je een berg')
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
           Locatie: Boven op de Vulkaan  ''')
printDelay('')
input('Klik ENTER om verder te gaan')
############################################################################################
clear_console()
printDelay('Je loopt terug richting naar de vulkaan')
printDelay('Je staat bij de voet van de vulkaan en je ziet een soort van grot')
printDelay('Je loopt naar binnen en je ziet een soort van trap')
printDelay('Je loopt de trap op en je ziet een kamer')
printDelay('Je loopt naar binnen en je ziet iets bewegen in de andere kamer')
printDelay('Ga je het vreemde object aanvallen of ga je weg')
keuze = input('Aanvallen/Weg: ').lower()
clear_console()
if keuze == 'aanvallen':
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
    PlayerHP = 100
    while GreenGoblinHP >= 0:  # battle loop
        enemydmg = random.randint(5, 15)
        clear_console()
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
        else:
            print('Je hebt geen geldige keuze gemaakt probeer het opnieuw')
            time.sleep(2)

        if PlayerHP <= 0:
            input('Je bent dood gegaan de game is nu afgelopen klik Enter om te stoppen')
            sys.exit()
        if GreenGoblinHP <= 0:
            print('Je hebt je tegenstander verslagen je kan nu door ')
            PlayerHP  = 100 + armor
            break
################################################################################################
    printDelay('Top die is ook weg')
    printDelay('Je loopt de kamer in en je ziet een soort van trap')
    printDelay('Je loopt de trap op en je beland in een balkon dat over de vulkaan uit kijkt')
    printDelay('op het balkon staat een kist')
    input('Klik ENTER om de kist te openen')
    time.sleep(2)
    clear_console()
    printDelay('Je opent de kist en zit een soort staff in en armor')
    staff = input('Wil je de staff menemen Ja/Nee: ').lower()
    if staff == 'ja':
        specialtxt = 'Gebruik je special weapon type: Special'
        special = random.randint(20, 30)
    elif staff == 'nee':
        specialtxt = 'Je hebt geen special weapons/abilities'
    else:
        printDelay('Verkeerde input')
################################################################################################
    armor = input('Wil je de armor meenemen Ja/Nee: ').lower()
    if armor == 'ja':
        armor = 100
    elif armor == 'nee':
        armor = 0
        printDelay('Je laat de armor liggen')
    else:
        printDelay('Verkeerde input')
################################################################################################
    printDelay('Je ziet een soort van enorme grot')
    printDelay('Er komt een sterke aura uit de grot')
    printDelay('Je zit 2 Rode ogen in de grot')
    printDelay('Je duikt snel weg en gaat terug naar buiten')
################################################################################################
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
input('Klik ENTER om de battle te starten')
################################################################################################
while DeMoNHP >= 0:  # battle loop
        clear_console()
        enemydmg = random.randint(0, 10)
        print(f'''
        _______________________________________________________________________________________
        Battle:
                        {naam} Hp = {PlayerHP}            Skynrad de Demon Hp = {DeMoNHP}

                            Kies Aub eem van de onderste opties: Een/Twee/Drie
                                {Attack}        {specialtxt}                                              ''')

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
        elif attackchoice == 'special':
            DeMoNHP = DeMoNHP - special
            PlayerHP = PlayerHP - enemydmg
        else:
            print('Je hebt geen geldige keuze gemaakt probeer het opnieuw')
            time.sleep(2)

        if PlayerHP <= 0:
            input('Je bent dood gegaan de game is nu afgelopen klik Enter om te stoppen')
            sys.exit()
        if DeMoNHP <= 0:
            print('Je hebt Skynrad verslagen ')
            PlayerHP  = 100 + armor
            break
printDelay('Gefeliciteerd je hebt de game uitgespeeld')
time.sleep(1)
clear_console()
time.sleep(3)
print('LINK STOP!!!!!!!!!!!')
sys.exit()