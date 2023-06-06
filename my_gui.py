import customtkinter as ctk
import tkinter as tk
from jankenpo import jankenpo_logic
from PIL import Image

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")


class rpsgui:
    def __init__(self):
        self.jankenpo = jankenpo_logic()

        self.root = ctk.CTk()
        self.root.title("Rock-Paper-Scissors")
        self.root.geometry("600x350")
        self.root.resizable(False, False)

        self.frame = ctk.CTkFrame(master=self.root, fg_color="#FF6961")
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(master=self.frame, text="Tester")
        self.label.pack(pady=2, padx=10)

        self.score_display = "• • • • •"
        self.win_label = ctk.CTkLabel(master=self.frame, text=self.score_display, font=("Arial", 25))
        self.win_label.pack(pady=2, padx=10)

        rock_image = ctk.CTkImage(light_image=Image.open("Rock.png"), dark_image=Image.open("Rock.png"),
                                  size=(100, 100))
        paper_image = ctk.CTkImage(light_image=Image.open("Notebook Paper.png"),
                                   dark_image=Image.open("Notebook Paper.png"), size=(71, 100))
        scissors_image = ctk.CTkImage(light_image=Image.open("Scissors.png"), dark_image=Image.open("Scissors.png"),
                                      size=(100, 100))

        self.rock_button = ctk.CTkButton(master=self.frame, text="", image=rock_image, fg_color="transparent",
                                         hover_color="#C9A9A6", width=100, height=100, command=self.rock)
        self.paper_button = ctk.CTkButton(master=self.frame, text="", image=paper_image, fg_color="transparent",
                                          width=100, height=100, command=self.paper)
        self.scissors_button = ctk.CTkButton(master=self.frame, text="", image=scissors_image, fg_color="transparent",
                                             width=100, height=100, command=self.scissors)

        self.showButtons()

    def update(self):
        self.root.update()
        self.frame.update()
        self.rock_button.update()
        self.paper_button.update()
        self.scissors_button.update()
        self.win_label.update()

    def hideButtons(self):
        self.rock_button.place_forget()
        self.paper_button.place_forget()
        self.scissors_button.place_forget()

    def showButtons(self):
        self.rock_button.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
        self.paper_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.scissors_button.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

    def gui_reset(self, result, choice):
        result_message = self.message(result, choice)
        label2 = ctk.CTkLabel(master=self.frame, text=result_message)
        label2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        self.tally(result)
        self.win_label.configure(text=self.score_display)
        self.update()
        self.root.after(3000, label2.place_forget)
        if self.jankenpo.getUserWins() < 3 and self.jankenpo.getComputerWins() < 3:
            self.root.after(3000, self.showButtons)
        else:
            if self.jankenpo.getUserWins() > self.jankenpo.getComputerWins():
                print("This is where a YOU WIN screen will show")
            else:
                print("This is where a YOU LOSE screen will show")

    def rock(self):
        self.hideButtons()
        self.gui_reset(self.jankenpo.play_round("rock"), self.jankenpo.getCompChoice())

    def paper(self):
        self.hideButtons()
        self.gui_reset(self.jankenpo.play_round("paper"), self.jankenpo.getCompChoice())

    def scissors(self):
        self.hideButtons()
        self.gui_reset(self.jankenpo.play_round("scissors"), self.jankenpo.getCompChoice())

    def message(self, result, choice):
        if result == "won":
            return "Your opponent chose " + choice + ". You won round " + \
                   str(self.jankenpo.getUserWins()+self.jankenpo.getComputerWins()) + "!"
        elif result == "loss":
            return "Your opponent chose " + choice + ". You lost round " + \
                   str(self.jankenpo.getUserWins() + self.jankenpo.getComputerWins()) + "."
        else:
            return "Your opponent chose " + choice + ". Since there was a tie, pretend this round didn't happen"

    def tally(self, result):
        if result == "won":
            update_index = self.score_display.find("•")
            self.score_display = self.score_display[:update_index] + "W" + self.score_display[update_index + 1:]
        elif result == "loss":
            update_index = self.score_display.rfind("•")
            if update_index+1 == len(self.score_display):
                self.score_display = self.score_display[:update_index] + "L"
            else:
                self.score_display = self.score_display[:update_index] + "L" + self.score_display[update_index + 1:]

    def run(self):
        self.update()
        self.root.mainloop()


if __name__ == "__main__":
    game = rpsgui()
    game.run()

