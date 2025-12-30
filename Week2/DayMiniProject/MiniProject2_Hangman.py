import random
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

stages = [
    "",
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    --------
    """
]
st = 0
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist).lower()
incorrect_letters =[]
alive = True
#print(word)
#to show * instead of each letter in guessed word
lenth_word = len(word)
hide_word = list("*" * lenth_word)
#to add space in case of several words
pos = word.find(" ")
while pos != -1:
    hide_word[pos] = " "
    pos = word.find(" ", pos + 1) 
while alive:
    #for each attempt 
    clear_terminal()
    print("Guess the word  " + "".join(hide_word).upper())
    print(f"Incorrect letters: {incorrect_letters}")
    print(stages[st])
    #if gallow is full:
    if st >= len(stages)-1:
        alive = False
        print("Game is over!(((((((((")
    #in case of guessing all letters:
    elif hide_word.count("*") == 0:
        alive = False
        print("You are winner!!!!!")
    #continue the game:
    else:
        guess_letter= input("Enter guess letter: ").lower()
        pos = word.find(guess_letter)
        #letter not in the word:
        if pos == -1:
            st += 1 
            incorrect_letters.append(guess_letter)
        else:
            #to replace all occurrence
            while pos != -1:
                hide_word[pos] = word[pos]
                pos = word.find(guess_letter, pos + 1)
            
    
    
    
    
    