# Het is idee is dat de game een soort parodie is op swordt art online. (is een soort Vr game)
# De game begin met dat je een avatar moet kiezen. Gender/Class/Name
# Met elke Class komen ander Weapons.
# De game zelf begin zo "Je wordt wakker in een vreemde wereld alles wat je ziet is dat je in een bos met een weg aan het einde van de weg zie je een kruispunt. Je kan naar links of rechts gaan. Waar ga je heen?"
# je kiest of je links of rechts wil gaan en dan krijg je een random event. (bijvoorbeeld een monster)
# Als je een monster verslaat kan je door naar de volgende naar ongeveer 2 mobs kom je bij de end boss (bijvoorbeeld een demon)
# Als je de end boss verslaat kom je bij een einde van de game. (bijvoorbeeld een portal)
# Als je de portal in gaat kom je weer terug in de echte wereld. (bijvoorbeeld een kamer met een computer)
#
import sys
import random

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

print('Welkom tot de wereld van Sword Art Online.')
# | Done
input('ENTER om verder te gaan')
print('LINK START!!!!!!!!!!!')
# | Done
naam = input("Wat is uw naam")
gender = input('Kies je geslacht: Man/Vrouw: ').lower()
if gender == 'man':
    gender = 'Mannelijke'
elif gender == 'vrouw':
    gender = 'Vrouwelijke'
else:
    print('Je hebt geen geldige keuze gemaakt')
    sys.exit()
###########################################################################
# door de input word de klasse gekozen / Done
klasse = input('Kies je klasse: Warrior/Mage/Archer: ')
if klasse == 'Warrior':
    Attacks = ['Een: Slash', 'Twee: Stab', 'Drie: Punch']
    een = random.randint(10, 20)  # Slash
    twee = random.randint(10, 20)  # Stab
    drie = random.randint(10, 20)  # Punch
if klasse == 'Mage':
    Attacks = ['Een: Fireball', 'Twee: Iceball', 'Drie: Lightning']
    een = random.randint(10, 20)  # Fireball
    twee = random.randint(10, 20)  # Iceball
    drie = random.randint(10, 20)  # Lightning
if klasse == 'Archer':
    Attacks = ['Een: Arrow', 'Twee: Piercing Arrow', 'Drie: Explosive Arrow']
    een = random.randint(10, 20)  # Arrow
    twee = random.randint(10, 20)  # Piercing Arrow
    drie = random.randint(10, 20)  # Explosive Arrow
###########################################################################
print(f'Je bent een {gender} genaamd {naam} en je klasse is een {klasse}')
###########################################################################
print('')
input = input('Start het spel: Ja/Nee: ').lower()
if input == 'nee':
    print('Het spel is gestopt')
    raise sys.exit()
elif input == 'ja':
    print('Het spel is gestart')
    print('')
    print('Je bent wakker geworden in een vreemde wereld.')
    print('Naast je ligt een tas, je opent de tas er zitten wapens in. ')
    print('Het enige wat je ziet is een weg met aan het einde een kruispunt.')
    print('Je loopt naar het kruispunt je hebt 2 opties')
    # moet nog een rechts elif krijgen
    kruispunt = input('Ga je naar links of rechts: Links/Rechts: ').lower()
    if kruispunt == 'links':
        print('Je gaat naar links')
        print('Je komt een wild dier tegen')
        # moet nog een aanvallen elif krijgen
        print('je doet je best om het dier te indentificeren')
        print('Je heb even goed gekeken en je ziet dat het een wolf is')
        print('KUT!!!!!, de wolf heeft je ontdekt je moet nu wel vechten anders ga je dood')
        print('FIGHT!!!!')
        ###########################################################################
while WolfHP >= 0:
    enemydmg = random.randint(5, 10)
    print(f'''
    _______________________________________________________________________________________
    Battle:
                            {naam} Hp = {PlayerHP}              Wolf Hp = {WolfHP}

                            Kies Aub eem van de onderste opties:
                                {Attacks}          ''')

    attackchoice = input(': ').lower()
    if attackchoice == 'een':
        print(f'{naam} heeft {een} Damage gedaan')
        print(f'Wolf heeft {enemydmg} Damage gedaan')
    elif attackchoice == 'twee':
        print(f'{naam} heeft {twee} Damage gedaan')
        print(f'Wolf heeft {enemydmg} Damage gedaan')
    elif attackchoice == 'drie':
        print(f'{naam} heeft {drie} Damage gedaan')
        print(f'Wolf heeft {enemydmg} Damage gedaan')
    WolfHP = WolfHP - een
    PlayerHP = PlayerHP - enemydmg
    if PlayerHP <= 0:
        print('Je bent dood gegaan de game is nu afgelopen') 
        sys.exit()
    if WolfHP <= 0:
        print('Je hebt je tegenstander verslagen je kan nu door lopen')
        break
