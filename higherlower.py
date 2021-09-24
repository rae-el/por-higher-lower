"""
File: higherlower.py
Author: Rachel
Purpose: Higher Lower Game
"""
import random


def main():
    try:
        guess = int(input(">"))
        higher_lower(guess, number)
    except ValueError:
        print("ERROR! Try again")


def higher_lower(guess, number):
    if guess == number:
        print("Congrats")
        return
    elif guess > number:
        print("Your number is too high, guess again")
        main()
    else:
        print("Your number is too low, guess again")
        main()


if __name__ == "__main__":
    number = random.randint(0, 100)
    print("Please enter an integer between 0 and 100:")
    main()
