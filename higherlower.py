"""
File: higherlower-gui.py
Author: Rachel, Bradley
Purpose: Higher Lower Game
"""
import random
from breezypythongui import EasyFrame


class HigherLower(EasyFrame):
    """
    higher lower guessing game with a GUI
    """
    def __init__(self):
        """
        sets up GUI
        """
        self.count = 0
        self.number = random.randint(0, 100)
        self.message = ""
        EasyFrame.__init__(self,
                           width=350,
                           height=150,
                           title="Higher Lower Guessing Game")
        self.titleLabel = self.addLabel(text="Please guess an integer between 0 and 100:",
                                        row=0,
                                        column=0,
                                        columnspan=2,
                                        sticky="NSEW")
        self.guess = self.addIntegerField(value=0,
                                          row=1,
                                          column=0,
                                          sticky="NSEW")
        self.button = self.addButton(text="GUESS",
                                     row=1,
                                     column=1,
                                     command=self.higher_lower)
        self.output = self.addLabel(text="",
                                    row=2,
                                    column=0,
                                    columnspan=2,
                                    foreground="#000000",
                                    sticky="NSEW")

    def higher_lower(self):
        try:
            guess = self.guess.getNumber()
            if guess < 0:
                self.message = "ERROR! Try again with a higher number"
                foreground = "red"
            elif guess > 100:
                self.message = "ERROR! Try again with a lower number"
                foreground = "red"
            else:
                self.count += 1
                if guess == self.number:
                    self.message = f"Congrats you took {self.count} guesses"
                    foreground = "green"
                    return
                elif guess > self.number:
                    self.message = "Your number is too high, guess again"
                    foreground = "orange"
                else:
                    self.message = "Your number is too low, guess again"
                    foreground = "blue"
        except ValueError:
            self.message = "ERROR! Try again with a valid number"
            foreground = "red"
        finally:
            self.output["text"] = self.message
            self.output["foreground"] = foreground


def main():
    HigherLower().mainloop()


if __name__ == "__main__":
    main()
