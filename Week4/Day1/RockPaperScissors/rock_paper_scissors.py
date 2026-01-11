from game import Game
# get_user_menu_choice() - this should display a simple menu, get the user’s choice (with data validation), and return the choice. No looping should occur here.
# The possibles choices are : Play a new game or Show scores or Quit

def print_results(results): #this should print the results of the games played. 
# It should have a single parameter named results; which will be a dictionary of the results of 
# the games played. It should display these results in a user-friendly way, and thank the user for playing.
    print(f"Thank you for playing with us! Game Results:")
    print(f"You won {results["your_win"]} times")
    print(f"You lost {results["your_loss"]} times")
    print(f"You drew {results["draw"]} times")

def get_user_menu_choice():
    print("\n Menu:")
    print("(g) Play a new game")
    print("(x or q) Show score and exit")
    choice = input("")
    if choice in ('g','G','x','X','q','Q'):
        return choice.lower()
    else:
            raise ValueError ("Enter correct choice: ")

def main ():#the main function. It should take care of 3 things:
    wl = True
    while wl:
        try:   # Displaying the menu repeatedly, until the user types in the value to exit the program: ‘x’ or ‘q’
            if get_user_menu_choice() == 'g': # When the user chooses to play a game:
                # Create a new Game object (see below), and call its play() function, receiving the result of the game that is returned.
                g = Game()
                print(g.play())
            else:   # When the user chooses to exit the program, call the print_results function in order to display a summary of all the games played.
                wl = False
                print_results(Game.results)  
        except ValueError as e:
            print("", e)
main() 

            