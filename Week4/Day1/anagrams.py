import os
os.system('clear')


from anagram_checker import AnagramChecker

class ValidationError (Exception):
    def __init__(self, message):
        super().__init__(f"{message}") # Call the base class constructor

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.
def validation (word):
    if " " in word.strip():
          raise ValidationError ("More than one word")
    elif not word.strip().isalpha():
          raise ValidationError ("Only alphabetic characters are allowed")
    else:
        return True

# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
def show_menu():
        while True:
            try:
                print("\n1. Input a word")
                print("2. Exit")
                choice = input()
                if choice == "2" or choice == 'Exit'.lower():
                    break   
                else:
                    validation(choice)
                    # Once your code has decided that the user’s input is valid, it should find out All possible anagrams to the user’s word.
                    ac = AnagramChecker()
                    # Create an AnagramChecker instance and apply it to the steps created above.
                    ac.is_valid_word(choice)
                    print(f'''YOUR WORD :{choice.upper()}\nthis is a valid English word - {ac.is_valid_word(choice)}.
Anagrams for your word: {", ".join(ac.get_anagrams(choice))}''')
                    break
            except ValidationError as e:
                print(f"{e}. Entry correct value")
show_menu()