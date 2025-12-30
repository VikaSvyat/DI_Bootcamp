# Exercise 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        
# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    # ... code to find and return the oldest cat ...
    max_age = cat1.age
    oldest_cat = cat1
    if cat2.age > max_age:
        max_age = cat2.age
        oldest_cat = cat2   
    elif cat3.age > max_age:
        max_age = cat3.age
        oldest_cat = cat3
    return oldest_cat

cat1 = Cat("Whisky", 15)
cat2 = Cat("Barsik", 15)
cat3 = Cat("Ryzhyi", 21)
# Step 3: Print the oldest cat's details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old")
#Exercise 2 
# Create a class called Dog.
class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height
# Create a bark() method that prints “<dog_name> goes woof!”.
    def bark(self):
        print (f"{self.name} goes woof!")
# Create a jump() method that prints “<dog_name> jumps <x> cm 
# high!”, where x is height * 2.
    def jump(self):
        print (f"{self.name} jumps {self.height * 2} cm high!")
def find_bigger_dog(Dog1, Dog2):
    if Dog1.height >= Dog2.height:
        return Dog1
    else:
        return Dog2
        
# Step 2: Create Dog Objects
davids_dog = Dog ("Sharick", 90) 
sarahs_dog = Dog ("Bobick", 20)
# Step 3: Print Dog Details and Call Methods
print (f'''We have {davids_dog.name} who {davids_dog.height} cm
            and {sarahs_dog.name} with {sarahs_dog.height} cm ''')
# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.
davids_dog.bark()
sarahs_dog.bark()
davids_dog.jump()
sarahs_dog.jump()

# Step 4: Compare Dog Sizes
bigger_dog = find_bigger_dog (davids_dog, sarahs_dog)
print (f"The biggerest dog is {bigger_dog.name}")

#Exercise 3 
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line) 
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

# Add a method sort_animals():

# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.

 #Exercise 4
 class Zoo:
    def __init__(self, zoo_name, animals = []):
        Zoo.name = zoo_name
        Zoo.animals = animals

    def add_animal(self, *new_animals):
        for new_animal in list(new_animals):
            if new_animal not in self.animals:
                self.animals.append (new_animal)
        return True

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove (animal_sold)
            return True
        else:
            return False

    def sort_animals(self):
        sorted_animals = {}
        for animal in sorted(self.animals):
            first_letter = animal[0]
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = []
            sorted_animals[first_letter].append(animal)
        return sorted_animals
  
    def get_groups(self):
        print(self.sort_animals() )
        return True

# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")
# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe","Baboon","Bear")
# brooklyn_safari.add_animal()
# brooklyn_safari.add_animal()
# brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
# brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()

# Exercise XP
# Create a class called Phone. This class takes a parameter called phone_number. 
# When instantiating an object create an attribute called call_history which value is an empty list.
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []  
        self.messages = []
# Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. 
# The method should print a string stating who called who, and add this string to the phone’s call_history.
    def call(self, other_phone):
        call_record = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_record)
        self.call_history.append(call_record)   

# Add a method called show_call_history. This method should print the call_history. 
    def show_call_history(self):
        for record in self.call_history:
            print(record)

# Add another attribute called messages to your __init__() method which value is an empty list.

# Create a method called send_message which is similar to the call method. Each message should be saved 
# as a dictionary with the following keys:
# to : the number of another Phone object
# from : your phone number (also a Phone object)
# content
    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}")
# Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)
    def show_outgoing_messages(self):
        for message in self.messages:
            if message["from"] == self.phone_number:
                print(f"To: {message['to']}, wrote: {message['content']}")

    def show_incoming_messages(self):
        for message in self.messages:
            if message["to"] == self.phone_number:
                print(f"From: {message['from']}, received: {message['content']}")

    def show_messages_from(self, other_phone):
        for message in self.messages:
            if message["from"] == other_phone.phone_number and message["to"] == self.phone_number:
                print(f"From: {message['from']}, received: {message['content']}")

# Create two Phone objects.
phone1 = Phone("050-11111")
phone2 = Phone("053-22222")  
# Make  call between the two phones.
phone1.call(phone2)
phone2.call(phone1)
phone2.call(phone1)
phone1.call(phone2)
# Show call history for both phones.
phone1.show_call_history()
phone2.show_call_history()
# Send messages between the two phones.
phone1.send_message(phone2, "Message 1 from Phone 1")
phone1.send_message(phone2, "Message 2 from Phone 1")
phone2.send_message(phone1, "Message 1 from Phone 2")
phone2.send_message(phone1, "Message 2 from Phone 2")
# Show outgoing messages for phone1 and incoming messages for phone2.
phone1.show_outgoing_messages()
# Show incoming messages for phone2 and outgoing messages for phone1.
phone2.show_incoming_messages()
# Show messages received by phone1 from phone2 and messages received by phone2 from phone1.
phone1.show_messages_from(phone2)   
phone2.show_messages_from(phone1)
    





