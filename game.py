import os
import random
from PyInquirer import prompt
import cfonts
from termcolor import colored
from pyfiglet import figlet_format

os.system("clear")

def winner(user, computer):
    who_won = None
    if user == 'ROCK':
        if computer == 'SCISSORS':
            who_won = user
        elif computer == 'PAPER':
            who_won = computer
    elif user == 'PAPER':
        if computer == 'ROCK':
            who_won = user
        elif computer == 'SCISSORS':
            who_won = computer
    elif user == 'SCISSORS':
        if computer == 'PAPER':
            who_won = user
        elif computer == 'ROCK':
            who_won = computer
    return who_won


print(colored(figlet_format("Welcome To \n Rock \t Paper \t Scissors", font="big", width=100, justify="center"), "green"))

CHOICES = ["ROCK", "PAPER", "SCISSORS"]
again  = True

while again:
    question = [
        {
            'type': 'list',
            'name': 'user_option',
            'message': 'Choose rock, paper or scissors',
            'choices': ["ROCK", "PAPER", "SCISSORS"]
        }
    ]
    user_choice = prompt(question)

    computer_choice = random.choice(CHOICES)

    if user_choice.get("user_option") == None:
        print("Please use the arrow keys to select an option")

    elif user_choice.get("user_option") in CHOICES:

        print(colored("You threw {}, and the computer threw {}".format(
                user_choice.get("user_option"), computer_choice
                ),  "cyan"))
        print(cfonts.render("{} vs {}".format(user_choice.get("user_option"), computer_choice), "tiny", gradient=["blue", "red"], align="center"))

        if (winner(user_choice.get("user_option"), computer_choice) == user_choice.get("user_option")):
            print(cfonts.render("YOU WON", "chrome", gradient=["blue", "red"], align="center"))
        elif (winner(user_choice.get("user_option"), computer_choice) == computer_choice):
            print(cfonts.render("YOU LOST", "chrome", gradient=["blue", "red"], align="center"))
        else:
            print(cfonts.render("DRAW", "chrome", gradient=["blue", "red"], align="center"))

    again = (input("Play again (y/n): ") in ['y', 'Y', 'yes'])
    

print(colored(figlet_format("Goodbye !", font="big", width=100, justify="center"), "green"))