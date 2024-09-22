import random


def guessing_game():
    """
    Guessing Game: Generates a random number between 1 and 100.
    The user gets 5 tries to guess the number. Provides feedback whether
    each guess is too high or too low.

    Author: Nick Costello
    """
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    attempts_left = 5

    while attempts_left > 0:
        print(f"You have {attempts_left} tries left.")
        try:
            guess = int(input("Guess what it is: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == number_to_guess:
            print("You got it!")
            return
        elif guess < number_to_guess:
            print("Nope! Too low.")
        else:
            print("Nope! Too high.")

        attempts_left -= 1

    print(f"Nope! You lost. The number was {number_to_guess}")





