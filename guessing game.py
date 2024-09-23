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


def rock_paper_scissors():
    ''' Joji Morikawa '''

    print("enter choice as an integer: paper(1), scissors(2), rock(3):")
    userVal = int(input())
    computerVal = random.randint(1, 3)

    userValName = ""
    computerValName = ""
    output = ""

    if (userVal == 1):
        userValName = "paper"
        if computerVal == 3:
            computerValName = "Rock"
            output = "You win!"
        elif computerVal == 2:
            computerValName = "Scissors"
            output = "You lose XD"
        elif computerVal == 1:
            computerValName = "Paper"
            output = "Its a tie!"
    elif (userVal == 2):
        userValName = "Scissors"
        if computerVal == 3:
            computerValName = "Rock"
            output = "You lose :("
        elif computerVal == 2:
            computerValName = "Scissors"
            output = "Its a tie ;)"
        elif computerVal == 1:
            computerValName = "Paper"
            output = "You win!"
    elif (userVal == 3):
        userValName = "Rock"
        if computerVal == 3:
            computerValName = "Rock"
            output = "its a tie :v"
        elif computerVal == 2:
            computerValName = "Scissors"
            output = "You win!"
        elif computerVal == 1:
            computerValName = "Paper"
            output = "You lose :p"
    else:
        print("Invalid Input")

    print("You:", userValName, "vs", computerValName)
    print(output)


# else:
#  print(":(")


if __name__ == "__main__":
    print("which game would you like to play? 1. Guessing Game(1), 2. Rock-paper-scissors(2):")
    game = int(input())
    while (game != -1):
        if (game == 1):
            guessing_game()
        elif (game == 2):
            rock_paper_scissors()
        else:
            print("Invalid input!!")
        print("which game would you like to play? 1. Guessing Game(1), 2. Rock-paper-scissors(2), Quit(-1): ")
        game = int(input())

    print("gg:)")






