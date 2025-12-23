#Exercise 1 
def display_message():
    print("I am repeating about functions in Python")

display_message()

#Exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}")
    
favorite_book("The Catcher in the Rye")

#Exercise 3
def describe_city(city, country='Unknown'):
    print(f"{city} is in {country}")
    
describe_city("Reykjavik", "Iceland") 
describe_city("Paris")

#Exercise 4 
import random
def guess (number):
    if not number.isdigit() or int(number)<0 or int(number)>100:
        print("Value not accepted")
    else:
        guessed_number = random.randint(1, 100) 
        if guessed_number == int(number):
            print("Success!")
        else:
            print(f"Fail! Your number: {number}, Random number: {guessed_number}")
            
guess(input("Guess the number in (1,100) = "))

#Exercise 5 
def make_shirt(size = "L", text = "I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")
    
make_shirt()
make_shirt("M")
make_shirt("S","I'm tied")
make_shirt(size="small", text="Hello!")

#Exercise 6 
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names):
    for name in magician_names:
        print(name)
    
def make_great(magician_names):
   for i in range(len(magician_names)):
        magician_names[i] += " the Great "
        
make_great(magician_names) 
show_magicians(magician_names)
    
#Exercise 7
def get_random_temp(season): 
    if season.lower() == 'summer':
        return round(random.uniform(10, 40),2)
    elif season.lower() == 'autumn':
        return round(random.uniform(0, 25),2)
    elif season.lower() == 'winter':
        return round(random.uniform(-10, 10),2)
    elif season.lower() == 'spring':
        return round(random.uniform(0, 25),2)
    else:
        return 'Unknown season'

def main():
    temp = get_random_temp(input("Enter season: "))
    if temp == 'Unknown season':
        print ('Unknown season')
    else:
        print (f"The temperature right now is {temp} degrees Celsius")
        if temp < 0: 
            print("Brrr, that’s freezing! Wear some extra layers today.")
        elif 0 <= temp < 16: 
            print("Quite chilly! Don’t forget your coat.")
        elif 16 <= temp < 23: 
            print("Nice weather.")
        elif 23 <= temp < 32: 
            print("A bit warm, stay hydrated.")
        elif 32 <= temp <= 40: 
            print("It’s really hot! Stay cool")
    
main()   
    
    
    
    
    
    
    
    
    
    