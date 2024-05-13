import tkinter as tk
from tkinter import messagebox
import random
import time

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.time_remaining = 30

        # Configure colors
        self.background_color = "#f0f0f0"
        self.button_color = "#4caf50"
        self.label_color = "#333"
        self.font_color = "#333"  # Updated font color for better contrast

        # Configure main frame
        self.frame = tk.Frame(master, bg=self.background_color)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Guess label
        self.label = tk.Label(self.frame, text="Guess a number between 1 and 100:", bg=self.background_color, fg=self.font_color)
        self.label.pack(pady=(20, 5))

        # Entry widget
        self.entry = tk.Entry(self.frame)
        self.entry.pack(pady=(0, 10))

        # Guess button
        self.button = tk.Button(self.frame, text="Guess", command=self.check_guess, bg=self.button_color, fg=self.font_color)
        self.button.pack()

        # Timer label
        self.timer_label = tk.Label(self.frame, text="Time remaining: 30 seconds", bg=self.background_color, fg=self.font_color)
        self.timer_label.pack(pady=(10, 0))

        # Number of guesses label
        self.guesses_label = tk.Label(self.frame, text=f"Number of guesses: {self.attempts}", bg=self.background_color, fg=self.font_color)
        self.guesses_label.pack()

        # Restart button
        self.restart_button = tk.Button(self.frame, text="Restart", command=self.restart_game, bg=self.button_color, fg=self.font_color)
        self.restart_button.pack(pady=(10, 0))

    def start_timer(self):
        self.timer_label.after(1000, self.update_timer)

    def update_timer(self):
        if self.time_remaining > 0 and self.attempts > 0:  # Start timer only if attempts are made
            self.time_remaining -= 1
            self.timer_label.config(text=f"Time remaining: {self.time_remaining} seconds")
            if self.time_remaining == 5:
                messagebox.showinfo("Time Alert", "Time is almost up!")
            self.timer_label.after(1000, self.update_timer)

    def check_guess(self):
        guess = self.entry.get()
        self.entry.delete(0, tk.END)  # Clear the entry field after guessing
        self.attempts += 1
        self.guesses_label.config(text=f"Number of guesses: {self.attempts}")

        try:
            guess = int(guess)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        if guess == self.secret_number:
            result = f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts."
            messagebox.showinfo("Congratulations!", result)
            self.reset_game()
            return
        elif guess < self.secret_number:
            result = "Too low! Try again."
        else:
            result = "Too high! Try again."

        messagebox.showinfo("Result", result)

        if self.attempts == 1:  # Start timer after the first guess
            self.start_timer()

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.time_remaining = 30
        self.timer_label.config(text="Time remaining: 30 seconds")
        self.guesses_label.config(text=f"Number of guesses: {self.attempts}")

    def restart_game(self):
        response = messagebox.askquestion("Restart Game", "Are you sure you want to restart the game?")
        if response == 'yes':
            self.reset_game()

root = tk.Tk()
app = GuessingGame(root)
root.mainloop()