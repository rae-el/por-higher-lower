"""
File: Assessment-1-HigherLower.py
Author: Rachel, Bradley
Purpose: Higher Lower Game
"""

import random
from breezypythongui import EasyFrame


class HigherLower(EasyFrame):
    """
    Higher-Lower guessing game with a GUI interface.
    """

    def __init__(self):
        """
        Sets up GUI interface.
        """
        self.count = 0  # Sets counter to 0
        self.number = random.randint(0, 100)  # Sets a random number between 0 and 100
        self.message = ""
        EasyFrame.__init__(self,
                           width=350,
                           height=150,
                           title="Higher Lower Guessing Game")  # Visual setup of interface
        self.titleLabel = self.addLabel(text="Please guess an integer between 0 and 100:",
                                        row=0,
                                        column=0,
                                        columnspan=2,
                                        sticky="NSEW")
        self.guess = self.addIntegerField(value=0,
                                          row=1,
                                          column=0,
                                          sticky="NSEW")
        self.button1 = self.addButton(text="GUESS",
                                      row=1,
                                      column=2,
                                      command=self.higher_lower)
        self.guess.bind('<Return>', lambda event: self.higher_lower())  # Binds Enter key to do the same as GUESS button
        self.output = self.addLabel(text="",
                                    row=2,
                                    column=0,
                                    columnspan=2,
                                    foreground="#000000",
                                    sticky="NSEW")
        self.button2 = self.addButton(text="RESET",
                                      row=2,
                                      column=2,
                                      command=self.reset,
                                      state="disabled")

    def higher_lower(self):
        foreground = "red"  # Sets the default colour to red to cover any non-stated changes
        try:
            guess = self.guess.getNumber()  # Retrieves the number inputted into integer field.
            if guess < 0:
                self.message = "ERROR! Try again with a higher number"  # No need to change foreground colour as is red
            elif guess > 100:
                self.message = "ERROR! Try again with a lower number"
            else:
                self.count += 1  # Only adds to count with guesses within range
                if guess == self.number:
                    self.message = f"Congrats you took {self.count} guesses"  # Curly brackets to call variable
                    foreground = "green"
                    self.button1["state"] = "disabled"  # Disables the GUESS button to prevent count increasing
                    self.guess.unbind('<Return>')  # Unbinds the Enter key to prevent further guessing
                    self.guess["state"] = "disabled"  # Disables guessing to prevent count increasing
                    self.button2["state"] = "active"  # Now allows user to click the RESET button to play again
                    return
                elif guess > self.number:
                    self.message = "Your number is too high, guess again"
                    foreground = "orange"
                else:
                    self.message = "Your number is too low, guess again"
                    foreground = "blue"
        except ValueError:
            self.message = "ERROR! Try again with a valid number"  # Prevents anything other than a number
        finally:
            self.output["text"] = self.message
            self.output["foreground"] = foreground  # Red by default

    def reset(self):  # To restart the game
        self.count = 0
        self.guess["state"] = "normal"  # Reactivates the input field
        self.guess.bind('<Return>', lambda event: self.higher_lower())  # Rebinds the Enter key
        self.guess.setValue(0)  # Sets the input field to 0
        self.number = random.randint(0, 100)  # Selects a new number between 0 and 100
        self.message = ""
        self.output["text"] = self.message
        self.button1["state"] = "normal"  # Reactivates the GUESS button
        self.button2["state"] = "disabled"  # Deactivates the RESET button


def main():
    HigherLower().mainloop()


if __name__ == "__main__":
    main()
