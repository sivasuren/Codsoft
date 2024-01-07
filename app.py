import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0
        self.winning_score = 5

        self.load_images()
        self.create_widgets()

    def load_images(self):
        self.rock_img = Image.open("C:/Users/Surend/OneDrive/Desktop/Codsoft/Rock Scissor game/rock.png").resize((100, 100))
        self.paper_img = Image.open("C:/Users/Surend/OneDrive/Desktop/Codsoft/Rock Scissor game/paper.png").resize((100, 100))
        self.scissors_img = Image.open("C:/Users/Surend/OneDrive/Desktop/Codsoft/Rock Scissor game/scissor.png").resize((100, 100))

        self.rock_img = ImageTk.PhotoImage(self.rock_img)
        self.paper_img = ImageTk.PhotoImage(self.paper_img)
        self.scissors_img = ImageTk.PhotoImage(self.scissors_img)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def play_game(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = self.determine_winner(user_choice, computer_choice)

        result_text = (
            f"Your choice: {user_choice}\n"
            f"Computer's choice: {computer_choice}\n\n"
            f"{result}\n"
            f"Score - You: {self.user_score}, Computer: {self.computer_score}"
        )

        messagebox.showinfo("Result", result_text)

        if self.user_score == self.winning_score or self.computer_score == self.winning_score:
            self.show_play_again_button()

    def create_widgets(self):
        self.rock_button = tk.Button(self.window, image=self.rock_img, command=lambda: self.play_game("rock"))
        self.paper_button = tk.Button(self.window, image=self.paper_img, command=lambda: self.play_game("paper"))
        self.scissors_button = tk.Button(self.window, image=self.scissors_img, command=lambda: self.play_game("scissors"))

        self.rock_button.grid(row=0, column=0, padx=10, pady=10)
        self.paper_button.grid(row=0, column=1, padx=10, pady=10)
        self.scissors_button.grid(row=0, column=2, padx=10, pady=10)

    def show_play_again_button(self):
        play_again_button = tk.Button(self.window, text="Play Again", command=self.reset_game)
        play_again_button.grid(row=1, column=0, columnspan=3, pady=10)

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.rock_button['state'] = 'normal'
        self.paper_button['state'] = 'normal'
        self.scissors_button['state'] = 'normal'

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.run()
