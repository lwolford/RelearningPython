import random

class jankenpo_logic:

    def __init__(self):
        self.user_wins = 0
        self.comp_wins = 0
        self.options = ["rock", "paper", "scissors"]

    def play_round(self, user_choice):
        comp_choice = self.options[random.randint(0, 2)]

        if user_choice == "rock" and comp_choice == "scissors":
            self.user_wins += 1
            print("You won round", str(self.user_wins + self.comp_wins) + ".")
        elif user_choice == "scissors" and comp_choice == "paper":
            self.user_wins += 1
            print("You won round", str(self.user_wins + self.comp_wins) + ".")
        elif user_choice == "paper" and comp_choice == "rock":
            self.user_wins += 1
            print("You won round", str(self.user_wins + self.comp_wins) + ".")
        elif user_choice == comp_choice:
            print("There was a tie. Pretend this round didn't happen.")
        else:
            self.comp_wins += 1
            print("The computer won round", str(self.user_wins + self.comp_wins) + ".")

        #if self.user_wins > self.comp_wins:
        #    print("You won! Thanks for playing!")
        #else:
        #    print("You lost. Thanks for playing still!")

    def rock(self):
        self.play_round("rock")

    def paper(self):
        self.play_round("paper")

    def scissors(self):
        self.play_round("scissors")

    def getUserWins(self):
        return self.user_wins

    def getComputerWins(self):
        return self.comp_wins
