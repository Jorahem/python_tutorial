import random

target = random.randint(1,100)

while True:
    usernumer = int(input("Guess the number between 1 to 100:"))
    if(target == usernumer):
        print("success: correct Guess!!")
        break

    elif(target > usernumer):
        print("your guess is too low")

    else:
        print("your guess is too high")

print("---------GAME OVER---------")