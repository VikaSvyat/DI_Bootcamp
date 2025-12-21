#Exercise 1: Concatenate lists
#Write code that concatenates two lists together without using the + sign.
list_1 = [1,2,3,4]
list_2 = [5,6,7]
for i in list_2:
    list_1.append(i)
print(list_1)

#Exercise 2: Range of numbers
#Create a loop that goes from 1500 to 2500 and prints 
#all multiples of 5 and 7.
list_5_7 =[]
for i in range(1500,2500):
    if i%5==0 and i%7==0 :
        list_5_7.append(i)
print(list_5_7)        

#Exercise 3: Check the index
#Ask a user for their name, if their name is in the names list 
#print out the index of the first occurence of the name.

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name = input("Enter your name: ")
if name in names:
    print (names.index(name))

#Exercise 4: Greatest Number
#Ask the user for 3 numbers and print the greatest number.  
number_max = 0
for i in range(1,4):
    number = input ("Input the "+str(i)+" number: ")
    if int(number)> number_max:
        number_max=int(number)
print("Maximum: ",number_max)        
        
#Exercise 5: The Alphabet
#Create a string of all the letters in the alphabet
#Loop over each letter and print a message that contains 
#the letter and whether its a vowel or a consonant.
alphabet = []
for i in range(26):
    alphabet.append(chr(65+i))
    if alphabet[i] in "AEIOUY":
        print(f"{alphabet[i]} - vowel")
    else:
        print(f"{alphabet[i]} - consonant")
        
#Exercise 6: Words and letters
#Ask a user for 7 words, store them in a list named words.
#Ask the user for a single character, store it in a variable called letter.
#Loop through the words list and print the index of the first appearence 
#of the letter variable in each word of the list.
#If the letter doesn’t exist in one of the words, 
#print a friendly message with the word and the letter.

words =[]
for i in range(6):
    words.append(input(f"Enter word {i+1}: "))
letter=input("Enter a single character: ")
for word in words:
    index = word.find(letter)
    if index != -1:
        print(f"in word '{word}' letter '{letter}' at {index} position")
    else:
        print(f"in word '{word}' letter '{letter}' not found")
        
#Exercise 7: Min, Max, Sum
#Create a list of numbers from one to one million and then use 
#min() and max() to make sure your list actually starts at one and 
#ends at one million. Use the sum() function to see how quickly 
#Python can add a million numbers.
sum = 0
numbers=[]
for i in range (1,1000001):
    numbers.append(i)
print(min(numbers),max(numbers))

for i in range (0,1000000):
    sum+=numbers[i]
print(sum)
            
#Exercise 8 : List and Tuple
#Write a program which accepts a sequence of comma-separated numbers. 
#Generate a list and a tuple which contain every number.
values = input("Please enter some comma-separated numbers: ")
list_values = values.split(",")
print(list_values)
tuple_values=tuple(list_values)
print(tuple_values)

# Exercise 9 : Random number
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

import random
guessed_number = random.randint(1, 10)   # integer between 1 and 10 (inclusive)
attempt_number = 0
action = True
while action:
    number=int(input("input a number from 1 to 9 or 0 to 'quit': "))
    if number==0:
        action=False
        print (f"{attempt_number} attempts haven't hepl you")
    elif number == guessed_number:
        print(f"Winner! It took only {attempt_number} attempts")
        action=False
    attempt_number+=1 











    
    
    
    
    
    
    
    
    
    












        
        
        
        
        
    






