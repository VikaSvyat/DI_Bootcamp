import random
import os
os.system('clear')

class Game:
    results = { #this dictionary will need to be created and populated in some other part of 
                # our code, and passed in to the print_results function at the right time.
         "your_win":0,
         "your_loss":0,
         "draw":0
        }
    def __init__(self):
        pass
    
    def get_user_item(self):    # Ask the user to select an item (rock/paper/scissors). 
        #Keep asking until the user has selected one of the items – use data validation and looping. 
        # Return the item at the end of the function.
        while True:
            choice = input("Select (r)ock / (p)aper / (s)cissors: ")
            if choice.lower() not in ('r','p','s'):
                print("Select valid choice ")
            else:
                return choice.lower()

    def get_computer_item(self) :   # Select rock/paper/scissors at random for the computer. 
        return random.choice(('r','p','s'))

    def get_game_result(self, user_item, computer_item): # Determine the result of the game.
# Parameters:
# user_item – the user’s chosen item (rock/paper/scissors)
# computer_item – the computer’s chosen (random) item (rock/paper/scissors)
# Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.
        if user_item == computer_item:
            Game.results["draw"] += 1
            return "draw"
        elif (user_item == 'r' and computer_item == 's') or (user_item == 'p' and computer_item == 'r') or (user_item == 's' and computer_item == 'p'):
            Game.results["your_win"] += 1
            return "win"
        else:
            Game.results["your_loss"] += 1
            return "loss"
    def play(self): # – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
                    # Get the user’s item (rock/paper/scissors) and remember it
                    # Get a random item for the computer (rock/paper/scissors) and remember it
                    # Determine the results of the game by comparing the user’s item and the computer’s item
                    # Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”
        dict = {
            "r" : "rock",
            "p" : "paper",
            "s" : "scissors"
        }
        your_choice = self.get_user_item()
        comp_choice = self.get_computer_item()
        return f"You chose {dict[your_choice]} - Computer chose {dict[comp_choice]} = Result {self.get_game_result(your_choice, comp_choice)}"

