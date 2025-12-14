import random

def guess_the_number_game():
    secret_number = random.randint(1, 100)
    guess = 0

    print("Try to guess the number I've chosen between 1 and 100.")

    while guess != secret_number:
# Get the user's guess
        guess = int(input("Enter your guess (1-100): "))

        if guess < secret_number:
            print("Go Up")
        elif guess > secret_number:
            print("Go Down")
        else:
# Correct guess
            print(f"\n You guessed it right: {secret_number}")

guess_the_number_game()