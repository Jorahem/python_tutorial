import random

def game():
    number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")
            break
            
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        game()
    else:
        print("Thanks for playing! Goodbye.")

game()