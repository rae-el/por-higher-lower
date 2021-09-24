"""
File: higherlower.py
Author: Rachel & Brad
Purpose: Higher Lower Game
"""
import random

count = 0


def main(count):
    try:
        guess = int(input(">"))
        if guess > 100:
            print("The number is between 0 and 100, try again:")
            main(count)
        elif guess < 0:
            print("The number is between 0 and 100, try again:")
            main(count)
        else:
            count += 1
            higher_lower(guess, number, count)
    except ValueError:
        print("ERROR! Numbers only! Try again")
        main(count)


def higher_lower(guess, number, count):
    if guess > number:
        print("Your number is too high, guess again")
        main(count)
    elif guess < number:
        print("Your number is too low, guess again")
        main(count)
    else:
        print("Congrats! You took " + str(count) + " turns!")
        return


if __name__ == "__main__":
    number = random.randint(0, 100)
    print("Please enter an integer between 0 and 100:")
    main(count)
