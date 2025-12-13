#The program picks a random number between 1-100, 
#and user have 7 attempts to guess it. 
#Get hints if user is too high 📈 or too low 📉!
import random
# def number_guessing_game():
guessed_number = random.randint(1, 100)   # integer between 1 and 100 (inclusive)
max_attempts = 7
attempt_number = 0
i = 0
list_low = [1]
list_high = [100]
print ("You are asked to guess an integer between 1 and 100 in 7 tries.")
input("Press Enter to start the game...")
print ("Please enter only integers, otherwise you will lose your attempt!")
input (" ")
print ('However you can take a hint (a help) at any time by pressing "h" or "H"')
input (" ")
while (i in range (max_attempts) and attempt_number != guessed_number):
    attempt_number =  input (f"Your attempt {i+1}: ")
    if attempt_number in ('h','H'):
        print (f"You know already that guessed integer between {max(list_low)} and {min(list_high)}")
    else:    
        try:
            attempt_number = int (attempt_number)
            if attempt_number == guessed_number:
                print("You are winner!")
            elif attempt_number > guessed_number:
                print("you’re too high 📈")
                list_high.append (attempt_number)
                #print(list_high)
            elif attempt_number < guessed_number:
                print("you’re too too low 📉")
                list_low.append (attempt_number)
                #print(list_low)
        except Exception:
            print ("isn't integer")
        i += 1
print (f"Game over! Guessed_number was {guessed_number}")
