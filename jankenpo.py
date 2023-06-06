import random

class jankenpo_logic:

    def __init__(self):
        self.user_wins = 0
        self.comp_wins = 0
        self.comp_choice = ""
        self.options = ["rock", "paper", "scissors"]

    def play_round(self, user_choice):
        self.comp_choice = self.options[random.randint(0, 2)]

        if user_choice == "rock" and self.comp_choice == "scissors":
            self.user_wins += 1
            return "won"
        elif user_choice == "scissors" and self.comp_choice == "paper":
            self.user_wins += 1
            return "won"
        elif user_choice == "paper" and self.comp_choice == "rock":
            self.user_wins += 1
            return "won"
        elif user_choice == self.comp_choice:
            return "tie"
        else:
            self.comp_wins += 1
            return "loss"

        #if self.user_wins > self.comp_wins:
        #    print("You won! Thanks for playing!")
        #else:
        #    print("You lost. Thanks for playing still!")

    def getUserWins(self):
        return self.user_wins

    def getComputerWins(self):
        return self.comp_wins

    def getCompChoice(self):
        return self.comp_choice
