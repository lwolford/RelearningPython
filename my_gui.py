import time

import customtkinter as ctk
import tkinter as tk
from jankenpo import jankenpo_logic

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class rpsgui:
    def __init__(self):
        self.jankenpo = jankenpo_logic()

        self.root = ctk.CTk()
        self.root.title("Rock-Paper-Scissors")
        self.root.geometry("600x350")
        self.root.resizable(False, False)

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(master=self.frame, text="Tester")
        self.label.pack(pady=12, padx=10)

        self.rock_button = ctk.CTkButton(master=self.frame, text="Rock", width=100, height=100, command=self.rock)
        self.paper_button = ctk.CTkButton(master=self.frame, text="Paper", width=100, height=100, command=self.showButtons)
        self.scissors_button = ctk.CTkButton(master=self.frame, text="Scissors", width=100, height=100, command=self.jankenpo.scissors)

        self.showButtons()

    def hideButtons(self):
        self.rock_button.place_forget()
        self.paper_button.place_forget()
        self.scissors_button.place_forget()

    def showButtons(self):
        self.rock_button.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
        self.paper_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.scissors_button.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

    def rock(self):
        self.hideButtons()
        self.jankenpo.rock()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = rpsgui()
    game.run()

