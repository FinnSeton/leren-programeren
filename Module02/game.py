import sys
import random
import os
import time

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
    printDelay(f'{naam} Ik kom hier voor de bounty op zijn hoofd en jij staat in mijn weg')
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
time.sleep(2)
printDelay('Bedankt voor het spelen van mijn game')
printDelay('Hier heb je een twerkende among us voor de rest van je leven')
input('Klik ENTER om de among us te zien')
clear_console()
while 1+1 == 2:
    print('''
    .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  .
    .       .       .       .       .       .       .       .      :t@888888888X;.  .       .       .       .       .       .       .       .       .  
        .  .    .  .    .  .    .  .    .  .    .  .    .  .    .@@% %X;:.:.....:;8; XSX.. .    .  .    .  .    .  .    .  .    .  .    .  .    .  .     
    .       .       .       .       .       .       .      .%%X XX@@88888@8@888@@88@8@S@X.@t@:      .       .       .       .       .       .       .  . 
    .  .    .  .    .  .    .  .    .  .    :8.XX .XSXS%;@X88888tX.S8@ 8 8 8@   8;8 8S@8XS%8 .@.    .  .    .  .    .  .    .  .    .  .    .  .    .  
    .    .  .    .  .    .  .    .  .    . %:t::t8888.S  ;88   S88888         8  .  8 ..8 8@88:XXX  .    .  .    .  .    .  .    .  .    .  .    .      
        .       .       .       .       . ;t 8%8@8%X.8@8.@88. ..  8  .8.8::. :....S@   .. .  ..S88t8 8.  .      .       .       .       .       .    .  . 
    .   . .    .  .    .  .    .  .  .88@SX8tS@@8888X88;8 . ::  .. :.:.:. 88... 88.:...:.. ::8..X88.t.:   .    .  .    .  .    .  .    .  .    .  .     
        .     .    .  .    .  .    .  :%%;88   888@8%88%8:.::::.:.. 8 8::. :88.::  ...:8  :.:.:.:...X8X;8;.   .    .  .    .  .    .  .    .  .       . . 
    .    .   .       .       .    .S:;88%...  8@@88@..:8:...:..::8  :.:::.  :.::. ;.   .. ::. 8     8S::8 .   .      .       .       .       .  .       
        .   .   .  .    .  .    . 8.;88; :..:.@8t8888:8;.::.:.::.:..:.:.:.. S8 .::;;t 8t8 S8@S8@8@@8@@888X@;     .  .   .  .    .  .    .  .    .  . .  .
    .    .      .   .   .   .   88.8@8.:.:: 88.8t...::::.:.::.:..:.:.:..::8@8tS8@88@888888@8888X888888@88t8. .    .     .   .   .   .   .   .           
        .     . .   .   .   .   .@t:8%...::..@8;8@ 8;:. :::.:.:..::.:.:.::;%X@SS88888888888888888888@88888@8;8;  .    . .   .   .   .   .   .   .  .  . . 
    .   .           .       . ;::88.:.:.:.:%:8@88;.::::.::.:.::.:.::tS8@8@88888888@8@8@88@88@88@8 @88@888@@; %   .          .       .       .     .     
        .   . .  . .     . .    .:X@ .::.:..@X%8;8;.:.:.:..::8:.:..;%8X@@888X888X8888888%88S88%8%88888 @8X88@8.@.    .  . .      . .     . .     .     .  
    .         .    .       .  8.8..:...:.:S:8X8.. ::.:.::.::::.tX8@888888888X8888888S888 X888888@888888888888;.. .        .  .     .       .  .  .     .
        . .  .    .   . .      8.8  .:.:..@X8888::::. ::.:.. :;@X8888888888@888 @8888888888@88X8888S88@88S888@8;:   . .  .   .   .    . .           . .  
    .          .         . . .8::8 .:::. 8;8%8:.:8::::.:.:::t8@888@8888%888888888888888888888888888888@888@888X88.        .   .   .      . . .  .       
        .  . . .    . .  .   :8.S:8:;888XS8@.88..:.:.:.. ::.:t8@88888888X88888S888888888@88S888888S88888888 @8X8%t     . .            .  .       .  .  .  
    .           .        .XS:t8S; 888.S:;.X88:8::. :::::.:S88888X888X8888S888888888888%8888@8X8888888S888@888@88t;.      .  .  . .    .   .  .     .   .
        . .  .  .    . . . tS: 8ttX8S@;8.%@.8X88;.::::.::. 88888@888@@88888@88%8@8@88888@888888888888888888S888888X8@  .    .   .    .    .       .    .  
    .       .   .        S8;8.%S888@@8@@.S8X::::.:.:..::8888888X8@S888 888888888888 8X88 @8888X8888X8S8888888888@;t    .    .    .   .     .  .   .     
        . .        .  .    @8;X: %:@8SX888;88 8.:..:.::.%X888X8 X888888@888@888888X888888888 88888888888888 8@8@88X:t  .  .     .   .   .  .     .   .  .
    .      . . .    .  .   .:;  %;t8S;%;8tX;.::.::8:.:;8X88888@88888S888888888X88@8888S8888@88888888888888888@888@:%       .  .      .      . .         
        .  .       .      .       .888@S88;S@X..::.:.::.@@88X88888X88888 8888888888888888888@8@888888S@X8@8@%888S8@StX.  .  .     . .     .        . . .  
    .      .  .    .  .   .      . X88888%8X8..:.. ::%88888888S88X888888888S888888888 8@8@88888S888@888888888888;XX     .   .       .  .  . .  .       .
        . .       .    .     .   .   ;@@8888%8 . ::::::888X88888888888S8888@8888@8@88S8888X8888S88S8@888888888888888@8X         .  .               .   .  
    .     .  .    .    . .   .   .  :;@888tt::8;.:.:%X888888 @8@8888888@8888@8888S88888@888S888888888X888S88@8888@88X.  . .  .    .  .  .  . .     .    
        .    .  .    .          .    :8.88tt88@8;:.:.@888S8@888X8@888X8888X88 888888888@8@88888X88@88888S88888@S88X8XX       .  .    .    .     . .    . 
    .    .       .    .  . .     .   :%%8%%@8;::. :t888888S@88888888888888 X@8888888@8888888X88888888888888888888X@8@ .  .       .    .     .      .    
        .    . .    .          .    .    S:X@.%;8::::S88X8888S88888888 88888888 @88@8@888888888888888 @888@t8888888.8SS   .  .  .    .    . .   .  .   .  
    .   .      .    . . .  .   .   .   :X;::8X8;:.: 8888888888S888888888@8888@8@888888X8888@88S88S8@888888888S88888X%.          .    .      .   .     . 
        .   .  .   .           .   .   .   %8.:88;.:SS88X88888S888888888888@8S88888888888888@8:888888%888X8888888@8@@88  .  . . .   .    .  .       . .   
    .          .   .  .  . .   .   .   .  .t:;8;88@8888888888888 8888X88888888@888 8@88888S88@88S8888888888@88@88 88X.          .   .    .   . .       .
        . . . .    .                  .   ..;X.8X;888X88888S888 X@88888888888888S8888888X8888888 X88S8@8@8X888888888X%   . .  .    .   .    .     .  .   
    .           .   .  . .  . . . .         @8 @8;8@8888 @88@8888888S888%888@888%888@88888888S8@8X8888888888888S8@Xt; .        .        .     .       . 
        .  .  .  .      .             . .   .  %X:%X888888@8888@888888888888@888X@8 888S88 8@888888888 88888S888 X88@;;   .  . .   .  . .   .    .  . .   
    .     .      .  .    . .  .  .      .     %@X888X8888:8X88@88888888 @8X@8888888888888888888 8@8@888888@8@88888X;;     .        .        .    .     .
        . .    .    .    .     .     .  .    .   X88888888888888888@8888888@88888888888888888X888888@88%888@8XtX88X@;X .  .    . . .    . . .   .     .   
    .      .   .    .    .     .        .    .  t@888X88@88888888888888888@88 @888X88@88SX @8;S88@8888888@@8888888.S       .        .       .   .     . 
        .     .   .    .    .    . . . .   .    .  XS8888888S8888@888S88888888@8@8@8X8S88;X8S;St@888S88@8@8888888.888.  . .    .  .     .  .       . .   
    .    . .   .   .    .   . .             .   . %8X8888888X888X888888888888888888Xt;S8;S8..@.X88888@8X%888888 :;.        .       . .       . .       .
        .          .   .    .      .  .  . .    .    ;;8888 8X8XS8888888@8@888S8@ 8%88%8X8.     %t;XX8S88888888888S.;. .  .    . . .     . .  .    . . .  
    .   .  . .         .     .        .    .       :8;X8888888888S888888X8X8888S@S @%S      . .8.S8@888888888S%X8X        .         .          .        
        .        .  . .    . .   . . .     .   .  .  . :tX88888888888888888X@@@Xt8%   .  .  .     ;8XX888S8@X88@X % .  .  .   .  .  .   .  . .     .  .  .
    .    .  .   .     .      .       .  .     .       S;S888888888X888 @8X8S@  . .    .     .    : tX88888@S8S8       .   .         .        . .        
        .   .  .    .    .  .    .  .      . .    . .  ;8%888888@8888888888@..     . .   . .   . . :: 88: X.8%       .       . . .      .  .       .  .  
    .    .       .   .    .   .      . .       .        t8S8888%8888S8 88t@     .     .     .       .:                 . .        .  .   .  .  .   .   .
        .     .  .   .   .        . .      .  .    .  . . .@X@88888 88@8@8 888       .    .      .   .             . . .     .  .  .     .      .  .   .  
    ''')
    time.sleep(0.15)
    clear_console()
    print('''
        .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  .
      .       .       .       .       .       .       . ::::.  .      .       .       .       .       .       .       .       .       .       .       .  
        .  .    .  .    .  .    .  .    .  .    . %8;XS %@SS% @@;8t :@XSS8. .    . .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .     
     .       .       .       .       .      :%S 8.8@S@88X:S8888S;:;8@@8S8X88t  8@@S%@@X   ;%%SSS%t;  8@@S ;8X; .     .       .       .       .       .  . 
      .  .    .  .    .  .    .  .    .%t8t8%8888888@SSX88S8t@88888888@X;%S8888@88S88@@t;tS88@888888X88X8@X%@@.@:@%.  .  .    .  .    .  .    .  .    .  
      .    .  .    .  .    .  .    .  .:@.:88888t8;%t;%88S;%S888S8:8S%8%;t8%S8%8S%tt:8 S.8:88@.  8@88;8:;8%S888X%::8 tt    .  .    .  .    .  .    .      
        .       .       .       .   .8 %888S8S8Stt;t8@X;8888@;8%8X;%8S8S@8X8888X;;;t8:@88S88t;tt8%8%88;;tt:.8:8:X8888%8;8tS .   .       .       .    .  . 
      .   . .    .  .    .  .    . t8%88;:ttt%8S@%t88S888@t;t8X8X8S@X8X8@8888@@@S8XS88%SS8@%8%88X8X8@8St8St8%8;8%8ttSS@88;%S Xt   . .    .  .    .  .     
        .     .    .  .    .  .   .S:8@t; S8S8X8X8@8%@8@8888X8X88@8@8@88@8@@88@@8X8@:8X;t%t8X8@88@8@@@8@@88@8S8X8S;:8;8%8X88..X::     .    .  .       . . 
      .    .   .       .       . .Xt@Stt%8S8X88@8@888X8888@8;88888@88@8@@@88@8888@@88;8t; S88@88888@@@88@88@@888@8S888X8;8%X888%%%S.   .       .  .       
        .   .   .  .    .  .    .%88X;t8X8X8888@@88888t8@888X8S888@88@8@@@8X8X@88@: t8S%8888@@@88@8888X@@88@8888@@8@888X88t8t:8%;@X8.   .  .    .  . .  .
      .    .      .   .   .   . %S:8Stt8X8@8@@8@88@8888%8X888888SSt888@@88S88%88:8:; S88X8888@88@8@@@@8@8@@88@@@8@@@@8888888X8XS%@8 8t    .   .           
        .     . .   .   .   .   S;88888@888@88@@@8@@@S@@8@@8%88888X888X8S@8888%:tt8S8X8@8@@@@@@8@@@8@@@@@88@X8@@@8@8@@@88@888@8%ttXXS@8%    .   .  .  . . 
      .   .           .         S:88S888@88@@8@88@@888S8XSX8XS88@8888888%88%;:t8%8X8@8@8@8@8@88@@8@@8@8@@@8@@@8@@@@@8@@@88@88@88X%8%8;.8;.    .     .     
        .   . .  . .     . .  . S:888@888@8@@@@@8@@@888@8S88S888SX88888%:.t;tt8X8X88@88@88@@@@8@@@88@@@8@@@8@@@8@8@@@8@@@8@@8@888888S8;tSS .     .     .  
      .         .    .       .  S.@@8888@@@8@8@@@8@@@88@@8X8@t88%%S;X;8ttttt8S8X888@@@88@8@8@@@8@@@8@88@8@@@8@@@@@8@888@@@88@@@8@88@X8X8X8S  .  .  .     .
        . .  .    .   . .    .8:::8@@8888888@8@@@8@@@88@8888@88888t:ttt8%;%88@888@8@@@8@@@@8@@@8@@@@@8@@8@@@8@8@@@@@@@8@@@8@88@@@8888X88%X;         . .  
       .          .         . .;@:8 ;:;8t8X888888@@@8@@@8@88@88@88@8St88X8@X8@8@@@88@8@@@@8@@@8@@@8@8@@@@@@8@@@@@8@8@8@@@8@@@@@8@88@8@88@8%%SS  . .  .     
        .  . . .    . .  .  8 St.X:%%%S@X8;8@8@@8@@@8@@@@@8@@88@8888888888@@88@88@8@@8@8@@8@@@8@@@@@8@8@88@8@8@@@88@@8@@@8@8@@@@@8@@@8@888S:8:         .  
       .           .        X@;8%.tS888@X ;8Xt888@8@@@8@8@@@88@8@@8@88@88@88@@@@@8@@@@@@@88@8@@@8@8@@@@@@@8@@@@8@@@8@@@8@@@@@8@8@@@@88888888X;:.  . . .   .
        . .  .  .    . . . X;8X%%S8%8 S 888@8@888@8@@@@@8@@@8@@@@@@@88@88@8@8@88@@8@8@88@X@@8@@@@@8@8@8@@@8@88@8@@@8@@@8@8@@@@@8@88@8888888tt:..       .  
      .       .   .        S8%:S88;S 8888@X88@8@88@8@8@@@8@@@@8@8@88@8@@8@@@@@@8@@@@@@@8@8@@@8@8@88@@@@8@@@@@88@8@@@8@@@@@8@8@@8888888888.8888@  .  .     
        . .        .  .    %@S88@  X88%S888S888@@@@@@8@@@8@8@@@@@@8@@@@@@8@8@@@8@8@8@@@@@8@@@@@@@8@8@@@8@8@@@8@@8@@@8@8@88@8888888 X888@X8@8:@.      .  .
       .      . . .    .  .   ;@@:%888%@X:88888@8@8@8@@@8@88@@8@8@88@@8@8@@@@@8@@@@@@@8@8@@@8@8@8@@@@@8@@@@@8@@@88@8@@@@@88888888888@888@8888%X::  .       
        .  .       .       .     .    :%t%8@8888@@888@88@@8@@@@@@@8@@@@@8@8@@@8@8@8@@@@@8@@@@@888@8@@@8@8@@@8@@@88@88888888X888888888888@88@;@:..   . . . 
      .      .  .    .  .    .  .       tt888888@88@@888@@@8@8@8@@@8@8@@@@@8@@@@@@@8@8@@@8@8@@@@@@@8@@@888@@@8@@@88@888888888888888888%88888X%..  .       
        . .       .    .  .       .  .   :%88888%@@88888888@@@@@8@@@@@8@8@@@8@8@8@@@888@@@888@8@8@@@8@@@@@8888888888S88888888888@8888@@888X88;t.    .  .  
      .     .  .    .       .  .          8;@88888888888@@8@8@88@8@8@@@888@@@@@888@@@@@8@@@@@@@@@8@@@888@888888@8@%@888@8888X88X888X888S8@8SX;:  .       .
        .    .  .    .  .       . .  .   tX;X888S8888888@@@@@@8@@@@8@@@@@8@8@@@@@8@8@@@8@8@8@888888@8888888 888@888S8@8@.8X88888888888888S8tt%.   . .  . 
      .    .       .    .  . .       .  .    8888888S8888888@88@@8@@@8@8@@@@@888@@@@@8@88888@88888888@ @88888@888888888@8X8888 @888 88@888XS@X            
        .    . .    .          .  .           t8888888X88 S8@@8@@888@8@88@8888@888888888888888@:88 8@8@88S888888X8888 8888888888888X8888 8SS    . .  . .  
      .   .      .    .  .  .       .  .  .  .t@@.8888888888888888888888@88888888S888888S88@888X88@888S8888888S888888@88 @8888%8888888@8@S@88.           .
        .   .  .   .   .      . .           .  8S88888888@8S8S88888888888@8S8%88888888 @888888888888 X88S88@8@8888XX88S88888S8888@8S8@88@88@.  .   . .    
      .          .   .   . .      .  .  . .   ..88S8@8888888888@88888888@8X88888%8888X88888888888888888 @888@888XX88888888S88888X88888X88SS  .   .     .  
        . . . .    .        .  .     .     .    @@%8888S888888S888X8888X88888888888@S88 888888@8888 88@88%8888@8S888 @88888X8888888888S@:.    .    .   . 
      .           .    .  .       . .    .        8 %@8888@8888888888S8@888888%88@888888@88888@8X8 X@88888888 888888888@8%8X8@888888 X8 S         .   .   
        .  .  .  .   .   .  . . .      .   .  .    .X;88888888@888888888888@8888@88S888@8@88888@88888888888888888@8888.88888@8@8 88@8SS       . .        .
      .     .      .   .           .     .     .    ;%@88888888 8@8X88888@@888S88X888888@8@8888S888888@8888888@8888X888@888@8@8X@88S:%             . . .  
        . .    .          .  .  .    . .    .    .    8.XS8888@88888888@@8888 X88S@ @8888888888@88888@8@88X88@8X888%@88S88@888@8 :8: .     . .  .         
      .      .   .  . .    .     .  .     .   .    . ..:@:888X8888%88@8888888@88888@88S8888%@88%88@8X888888888888S8888888 888@8:..  .    .       .  .  .  
        .     .   .    .     .        .    .   .       :X%88S888S8888888888888888888X@8888888@8888888888888888888888888@XX%S.S. .    .    . . .     .   .
     .    . .   .    .   .  .  . .  .   .    .    .  .   %888@888888 88@8@%888888%88@8@88 @8888888888 @888@888 8X888SX88@;:8.    .    . .       . .      
        .           .   .           .     .     .   .   . . X8@;X8@88X888@88@888@888@888888888 88@888X88@888@ 8S@@%X88888S88.   .   .      . .        . . 
     .   .  . .  .       . .  .  .   . .   .     .        :8:888@:8S888X8888@8XS8888888%88 88@88888888 8;888X8888@8@888X@:.         .  .      .  .  .    
        .        .   . .      .              . .     . .   .%t:X8888888;;88@;888;@8@8@888X888X@8888S%888@SXtX888@888@88%@%   .  . .    .  .  .   .      . 
        .    .  .    .     .  .   .  . .  . .      . .     .  . ;X888888%88888X@8S%@@88888888888Xtt888:8 8t:;tSS88S%S8;8@: .          .          .   .  .   
        .   .  .     .          .          .  .      .      ::;8@8 8888888888@8@8:888 8XSX8 :t8@XSt:.    .8@Xt t:8S:.    .  . .  .   .  . . .       .   .
        .    .      .    .  .  . .    . .  .        .  .   . .  8SX88@88 X888888888@8@      . .    .     .   .:.         .            .           . .    .  
        .     .     .    .        .     .  . .  .      .     . t;@8S88@8S8 8888 8Xt.                                .    . .  . . .   . .  .  .     .     
    ''')
    time.sleep(0.15)
    clear_console()
    print('''
        .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  .  .
    .       .       .       .       .       .       .       .       .       .       .       .       .       .       .       .       .       .       .  
        .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .     
    .       .       .       .       .       .       .       .       .       .       .       .       .       .       .       .       .       .       .  . 
    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  
    .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .      
        .       .       .       .       .       .      :%@888@S;..      .       .       .       .       .       .       .       .       .       .    .  . 
    .   . .    .  .    .  .    .  .    .  .   .%X%8;@8@S888X888%  8%t%%%%..    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .     
        .     .    .  .    .  .    .  .    .  .@S@.:S888@SS .S@@8@;.:@@%@SX;S@ .     . .     . .     . .     . .     . .     . .     . .     . .      . . 
    .    .   .       .       .       .   tS@Xt8888XX8@    ;X88Xt@XX88888@8X8S ;t;.S8@%;:.       .       .       .       .       .       .       .       
        .   .   .  .    .  .    .  .   :X 8%88S;  8    ;X88%8888tS 8 8@@@ .tSS8X%:;8@S888S.X%:8%.  .  .   .  .  .  .  .   .  .  .  .  .   .  .  .  . .  .
    .    .      .   .   .   .   .   ..8;%X8. .. .... S %t88t.      8    :. :88.88@.X8%S%X8XXt;8 :8:    .     .         .     .         .     .          
        .     . .   .   .   .   .   . X X88:. .. 8 ..X88@%8S8.:.  .  .:.. 8  ....  %%;@t8.  8tX88S8%S  8t   .     .  . .    .     .  . .    .     .  . .  
    .   .           .       .      8@%8t ...::8  ...S8X88.8:.::.:. ::. .8 ::S  .::.XSX88@X88   8t8S%X88t8X: .    .      .   .    .      .   .  .       .
        .   . .  . .     . .     . .;;:88.:.::.:..:.:88 8@8@S8 .:.. ;:. 8@ ..   ..::. 8:8%;8;.:..:  :::t@8t;tt; .    .  .   .   .    .  .   .      .  .   
    .         .    .       .       :88..::.:.. ::.  @88888X@@:.::::. .8 .:.   :..:.:@@8S%8:..:.. 88 :  8t88%8X;t     .      .   .       .    .    .   . 
        . .  .    .   . .     . . ..:88 .:.:.::;..::  @8X8@88%8:.:.. 8  ...:.:..S@t88t@88X8 ::.::8  ...8  ::88;8X X:.   . .    .   . . .    .   .    .   
    .          .         . .     ::%88::. ::.:.::.:.  .X88888S8:.::8  ..::..:S8%t;SX8%  8 ..:..:.... ; .:. 8. XXt; %       .             .   .   .     .
        .  . . .    . .  .     .  .::%@8..:.:.:8:.:..:..:8888X88@88X88.:8::@88S@@88S8t8..   :..::. :::.::.::....;:8;@8SS  .    . . .  .  .       .   .    
    .           .        .       :.tt88 888..:.:.::.::  X@8X88@888t.;X88XXS:8@St8: : ....8@8:..::..:..:..::..S8 .:X8@@8%  .          .    . .        .  
        . .  .  .    . . .   .  .  88:t@88@t@8 ::.:.:..:.  8@@8S8@@S@8:8%%8@S: . :S@ .:... @ ..:.:.:..::.::.::8@8.:   88:;@   .  .  .    .      . . .   . 
    .       .   .           .  8 8@8 88t:%;888.:.:.:..:.  8X888@X8@8SX88t8....:  8 ....: .. :::.:.::.:..:...8. :. ::;@8;SX.      .  .    .  .       .   
        . .        .  .  . .  % 8 8:;88S@XX8@;.8::8:.:..:. .:8 8@X8S;S@ .. ...:..8.:..88.:. ;:.::8:.:..::.::.:. ::.:. t;@8t8;  .       .    .   .  .    .
    .      . . .    .        S;8;%88S%%888%8@8;.:.::.::..:. 8  :: :  8 ....:.. :.:. .88.::::.:.::::.::.:..::. 88 8 .:::.XXt t  .  .  .  .    .       .  
        .  .       .    .  . . .;S;@@@X88@:  @..:8;:.:..:..:.......:    :...:.:::::. 8   :.:.. ::. :.:.:..:...:8   8 .:.::8%:;       .      .     .  .    
    .      .  .    .         ::S88SS@ 8@S;..8:.:.::.:..;:.:...:...:.:....:.:.:..::8   8  .::::. ;:.:..::.::.:..: ...:..:8:88:8. .     .     .  .     .  
        . .       .    . . .  .  .:S;.t8t@X88S8;:8:.:..;X@t:.::.:.:.:..:.:.. ::.::.:..:8  ::.:.. ;.:..:...: :.. :::.::.::.;; 88:X.  .    . .       . .   .
    .     .  .    .            .     :X:X88X8t;8;..:8 %@ :..::. ::......::::.:.:.. ::....:..::::..:..::.::.::::.::.::.::8X8888t8   . .     . .       .  
        .    .  .    .  .  .  .   . .  ;8t8888888;;::X88X .::..:::. :::.:.:.. ::.::::. :::.::.:..:..::.:8:::.:.::.::.:..t88888@%X:       .      . .      
    .    .       .       .           .  8tS88888@SXXS888 :.:..:.. ;..:.8  ::.:.:.:..:::.:..:..::.::..:.::.::.:.::....:t8@8888@@;;  .  .   .  .     .  . 
        .    . .    .  . .   . . .  .     .%S;88888X8X88  :.:.::.::.:.:. 8 ..:.. ::.:.:.:..:..::.:..:...:.:...:8:....:8tXX88888@%%@       .      .    .   
    .   .      .    .                     t%88;8@@X8888:. ::.:..:.. :: ...:.::::. ::.:.:..::.:..:8.:..:..:..:.:..:.:SX888888888X:;. . .    . .   .    . 
        .   .  .   .     . .  .  . . . . .    t%@8X%88%%:::::.:.:..::::. :S8 8::.. ;.:.8:.:..:..:88;:.::.::.::. ::::S88888@8:S888XS%       .        .     
    .          .   .         .            .  .@@:%8XS8X8;.. ::.::.:.. 8@@8  :.:::...::::.:..:88t::.:.:..:..::::.t@X88888888888X@8% .  .    .  . .   .  .
        . . . .       . .  .     .  .  . .     ..;8888888t::::.:.:..::8 8  ::::.:..:.. :.:.::.;:.:. ::.::.::.:.;X8@8888888@888S8X%%      .         .   . 
    .           . .      .  .  .     .     . . ;888888X88X8%8::..::.:.. ..:..:..:..::::.:..::8:.::.:.:.::.:tSSX8@888@88@888S88S%S  . .    . .  .    .   
        .  .  .  .    .  .         .  .    .     ;8888888888888t8;8:::. ::.:.::.::.:....:..::.:.::.::8::..;%@8X8888888X8@88S88@8@%8      .      .   .     
    .     .       .   .   .  .    .    .   . tSt88888@8 88888@88St:;:::. ;..:..:..::.:.::.:.. 8::.:8t;S@8X@88888@8@88X8S8888S%8 :  . .   .  .   .    .  
        . .    .  .   .   .   .  .     .   .   8@8888888@8@%88888@88@X8@SSt;::.:..:..:.. ::.::;;tt%XX88888@88888888 88888888S8X8@X       .           .   .
    .      .   .          .     .  .       . t:S@88@8@888888X888888888tX@888@%S%t%tt%%%%S@88@X8@888888@888888S8X88888888S8888;.  .  .    . . . .  .     
        .     .   . .  .      .       . .     S;@8@88.88888 @88.88888888888888X888X888X88888@88888@88X8888@8.88888@88X8888S88;X.       .             . . 
    .    . .         .  .  .   . .       . . X:8@8888888 X88S@@88X8 888888888888888888X888888@888888888X8888888888888@88888t;. .  . .   .  .  . .       
        .       . .  .     .   .     . .  .    X:88888888888888888888888 @%888@8@8888@88888X88888@8 888888888888S8888XX88 :88X     .    .           .  .  
    .   .  .          .    .    .          . X;8888 @8X8888%8@888S88888888888888@8 X888X88X8 @S888888@8 888X88@8@S@88 8:8S%  .      .    . . .  .   .  .
        .      .  . .  .  .     .   .  . .    .%X%@8888888888888S88888 X888%8888888888@8888888888888 8@8888888X888888S88X8;t .   . .     .          .     
    .    . .        .     .     .        .    X:8@888888S8888888888888@88@88 8888888 88@%888888888@88888888888888S88@t.; .         . .    .  . .     .  
        .     . .  .    .    . .    . .  .  .  88@8888S@88888888%8888888X888888888888@88888 8X8@;S88888888@8888S8SS%@ S.    .  . .      .         .  .   
    .    .           .   .       .           . @X8.8888 X8@%88888 @ 888888S888888X88X88888888888888S888@8:888 .88;.; .   .        .  .   . .  .    .   .
        .    .  . . .    .   .  .    .  .  . .    S X8888888888 888888888X8888 88888S888X8 88 8888S88888t8@ :;8S8Xt  .   .   .  .  .     .     .  .    .  
    ''')
    time.sleep(0.15)
    clear_console()