#Challenge 1 
#Create a dictionary that stores the indices 
# (number of the position) of each letter in a word provided 
# by the user(input()).
def letter_indices(word):
    indices = {}
    for index, letter in enumerate(word):
        if not(letter.isalpha()):
            return "Please enter a valid word containing only letters."
        if letter in indices:
            indices[letter].append(index)
        else:
            indices[letter] = [index]
#Ensure that the indices (values) are stored in lists.
        if not isinstance(indices[letter], list):
            print("Something went wrong.")
    return indices      
word =  input("Enter a word: ")
print(letter_indices(word))

#Challenge 2
#Create a program that prints a list of items that can be 
#purchased with a given amount of money.
def fill_the_basket(items_purchase, wallet):
    basket =[]
    wallet = int(wallet.strip('$').replace(',',''))
    for key, value in items_purchase.items():
        value = int (value.strip('$').replace(',',''))
        if value < wallet:
            wallet -= value
            basket.append(key)
    if basket == []:
        return 'Nothing'
    return basket
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
print(fill_the_basket(items_purchase, wallet)) 
#
items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet = "$100"
print(fill_the_basket(items_purchase, wallet)) 
#
items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet = "$1"
print(fill_the_basket(items_purchase, wallet)) 

#challenge GOLD: Caesar Cypher
method = input("Do you want encrypt 'C' or decrypt 'D'? ").upper()
string = input("Enter text for "+method+": ")
text = cypher_text = ''
if method == "C":
    text = string
    for letter in text:
        cypher_text += chr(ord(letter) + 3)
    print(cypher_text)
elif method == "D":
    cypher_text = string
    for letter in cypher_text:
        text += chr(ord(letter) - 3)
    print(text)

    