import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5  # Maximum number of attempts
    
    print("Welcome to Guess the Number Game!")
    print("I've selected a random number between 1 and 100. Can you guess it?")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low! Try guessing higher.")
        else:
            print("Too high! Try guessing lower.")
    else:
        print(f"Sorry, you've run out of attempts! The correct number was {secret_number}.")

# Start the game
guess_the_number()
