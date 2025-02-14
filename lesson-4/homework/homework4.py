import random

def play_game():
    number = random.randint(1, 100)  
    attempts = 10 

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("You guessed it right!")
            return 

    print("You lost. Want to play again?")

while True:
    play_game()
    retry = input("Do you want to play again? (Y/YES/y/yes/ok): ").strip().lower()
    if retry not in ["y", "yes", "ok"]:
        print("Thanks for playing! Goodbye.")
        break