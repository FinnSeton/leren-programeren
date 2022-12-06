import random

rounds = 0
userInput = ""
points = 0


while rounds < 3 and userInput != "quit":
    rounds += 1
    tries = 0
    geraden = False
    print(f"rounds: {rounds}")
    randomNum = random.randint(1, 1000)
    print(randomNum)
    while tries <= 3 and userInput != "quit" and geraden == False :
        print(f"\ntries: {tries}")
        userInput = input("enter a whole number between 1-1000: ")
        tries += 1
        if userInput != "quit":
            userInput = int(userInput)
            difference = abs(randomNum - userInput)
            if randomNum == userInput:
                print("correct!")
                points += 1
                geraden = True
            elif difference < 20 and randomNum < userInput:
                print("wrong, you're very warm, try smaller")
            elif difference < 20 and randomNum > userInput:
                print("wrong, you're very warm, try bigger")
            elif difference < 50 and randomNum < userInput:
                print("wrong, you're warm, try smaller")
            elif difference < 50 and randomNum > userInput:
                print("wrong, you're warm, try bigger")
            elif randomNum < userInput:
                print("Wrong, try smaller")
            else:
                print("Wrong, try bigger")

print(f"\npoints: {points}")