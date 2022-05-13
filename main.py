import random
from tkinter import *

root = Tk()
root.title("Rock, Paper, Scissors")
root.configure(bg="white")

computer_score = 0

user_score = 0


def results(user_choice):
    global computer_score, user_score
    choices = ["rock", "paper", "scissors"]
    random_num = random.randint(0, 2)
    computer_choice = choices[random_num]

    if computer_choice == user_choice:
        results_label.config(fg="blue", text="result: tie")
    elif computer_choice == "rock" and user_choice == "paper":
        user_score += 1
        user_score_label.config(text="player:" + str(user_score))
        results_label.config(fg="green", text="result: player won")
    elif computer_choice == "scissors" and user_choice == "rock":
        user_score += 1
        user_score_label.config(text="player:" + str(user_score))
        results_label.config(fg="green", text="result: player won")
    elif computer_choice == "paper" and user_choice == "scissors":
        user_score += 1
        user_score_label.config(text="player:" + str(user_score))
        results_label.config(fg="green", text="result: player won")
    elif computer_choice == "rock" and user_choice == "scissors":
        computer_score += 1
        computer_score_label.config(text="computer: " + str(computer_score))
        results_label.config(fg="red", text="result: computer won")
    elif computer_choice == "paper" and user_choice == "rock":
        computer_score += 1
        computer_score_label.config(text="computer: " + str(computer_score))
        results_label.config(fg="red", text="result: computer won")
    elif computer_choice == "scissors" and user_choice == "paper":
        computer_score += 1
        computer_score_label.config(text="computer: " + str(computer_score))
        results_label.config(fg="red", text="result: computer won")
    user_choice_label.config(fg="black", text="player: " + str(user_choice))
    computer_choice_label.config(fg="black", text="Computer: " + str(computer_choice))


def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text="player:" + str(user_score))
    computer_score_label.config(text="computer: " + str(computer_score))


Label(root, text="Rock,Paper,Scissors", font=("times", 14)).grid(row=0, sticky=N, pady=10, padx=200)
Label(root, text="select one", font=("times", 12)).grid(row=1, sticky=N)
user_score_label = Label(root, text="player: 0", font=("times", 12))
user_score_label.grid(row=4, sticky=W)
computer_score_label = Label(root, text="computer: 0", font=("times", 12))
computer_score_label.grid(row=5, sticky=W)
user_choice_label = Label(root, font=("times", 10))
user_choice_label.grid(row=4, sticky=E, )
computer_choice_label = Label(root, font=("times", 10))
computer_choice_label.grid(row=5, sticky=E)
results_label = Label(root, font=("times", 12))
results_label.grid(row=3, sticky=N)

Button(root, text="rock", width=15, command=lambda: results("rock")).grid(row=4, sticky=N, padx=5, pady=5)
Button(root, text="paper", width=15, command=lambda: results("paper")).grid(row=5, sticky=N, pady=5)
Button(root, text="scissors", width=15, command=lambda: results("scissors")).grid(row=6, sticky=N, padx=5, pady=5)
Button(root, text="reset", width=10, command=reset).grid(row=6, sticky=E)
Label(root).grid(row=5)
root.mainloop()