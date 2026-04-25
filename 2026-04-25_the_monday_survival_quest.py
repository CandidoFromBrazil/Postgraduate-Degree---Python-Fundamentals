import tkinter as tk
from tkinter import messagebox
import random

class CorporateGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Intern Simulator 2026")
        self.root.geometry("400x300")
        
        self.energy = 100
        self.reputation = 0
        
        # UI Elements
        self.label = tk.Label(root, text="Welcome, Intern #42069!", font=("Arial", 14, "bold"))
        self.label.pack(pady=10)
        
        self.stats_label = tk.Label(root, text=f"Energy: {self.energy} | Rep: {self.reputation}")
        self.stats_label.pack()

        self.story_text = tk.Label(root, text="The CEO is walking toward you. Quick!", wraplength=350)
        self.story_text.pack(pady=20)

        # Buttons
        self.btn_work = tk.Button(root, text="Pretend to type fast", command=self.work, width=20)
        self.btn_work.pack(pady=5)

        self.btn_coffee = tk.Button(root, text="Hide in the kitchen", command=self.hide, width=20)
        self.btn_coffee.pack(pady=5)

    def update_stats(self):
        self.stats_label.config(text=f"Energy: {self.energy} | Rep: {self.reputation}")
        if self.energy <= 0:
            messagebox.showinfo("Game Over", "You collapsed from exhaustion. Your boss replaced you with a script.")
            self.root.destroy()
        elif self.reputation >= 50:
            messagebox.showinfo("Victory", "You've been promoted to Junior Coffee Fetcher!")
            self.root.destroy()

    def work(self):
        outcome = random.choice([
            ("You typed 'asdfasdf' really fast. Boss is impressed.", 5, -20),
            ("You accidentally sent a cat meme to the CEO.", -10, -10),
            ("You solved a bug but forgot to save.", 2, -30)
        ])
        self.update_game(outcome)

    def hide(self):
        outcome = random.choice([
            ("You found a stale donut. +20 Energy!", 0, 20),
            ("You got caught by the HR manager. Awkward.", -5, -5),
            ("You successfully avoided eye contact. 0 work done.", 1, 10)
        ])
        self.update_game(outcome)

    def update_game(self, outcome):
        msg, rep_change, energy_change = outcome
        self.reputation += rep_change
        self.energy += energy_change
        self.story_text.config(text=msg)
        self.update_stats()

if __name__ == "__main__":
    root = tk.Tk()
    game = CorporateGame(root)
    root.mainloop()