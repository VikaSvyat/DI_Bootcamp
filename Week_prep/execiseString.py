text = "Python is Fun!"
i=0
t=''
#1. Convert the entire string to uppercase
print (text.upper())
#2. Make the first letter upper case
print(text.capitalize())
#3. Make the first letter of each word upper case
print(text.title())
#4. Find the index of "F". What happens if you use lower case in the method?
print(text.find("F"))
print(text.lower().find("F"))
#5. Find a substring
print(text.find("is"))

#1. Asks the user to input a sentence.
text = input("Please, input a sentence: ")
#2. Checks if the sentence is made up of only alphabetic characters. 
if (text.isalpha()):
    print ('just alpha')
#If not, print how many non-alphabetic characters are in the sentence.
else:
    for t in text:
        if (not t.isalpha()):
            i+=1
    print (i)
#3. Determines if the sentence ends with an exclamation mark (!).
if text.endswith('!'):
    print('ends with !')
#4. Finds out if the sentence contains any whitespace characters and 
#prints a message accordingly.
if any (t.isspace() for t in text):
    print("there is a space")
else:
    print('no space')
    


