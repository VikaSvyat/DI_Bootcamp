# Exercise 4: Family
# Define a Person class with the following attributes:
# first_name
# age
# last_name (string, should be initialized as an empty string)
# Add a method called is_18():
# It should return True if the person is 18 or older, otherwise False.

class Person():
    def __init__(self, first_name, age, last_name =''):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        return self.age >= 18

# Define a Family class with:
# A last_name attribute
# A members list that will store Person objects (should be initialized as an empty list)
class Family():
    def __init__(self, last_name, members = []):
        self.last_name = last_name
        self.members = members

# Add a method called born(first_name, age):
    def born(self, first_name, age):
        new_born = Person (first_name, age) #create a new Person object with the given first name and age.
        new_born.last_name = self.last_name #assign the family’s last name to the person.
        self.members.append(new_born)       #add this new person to the members list.

# Add a method called check_majority(first_name):
    def check_majority(self,first_name):
        for mem in self.members:
            if first_name == mem.first_name:# It should search the members list for a person with that first_name.
                if mem.is_18():               # If the person is over 18, print:
                    print ("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends")

# Add a method called family_presentation():
    def family_presentation(self):
        print (self.last_name,': ') # It should print the family’s last name.
        for mem in self.members:    # Then, it should print each family member’s first name and age.
            print(f"{mem.first_name} {mem.last_name} is {mem.age} years_old")

# Create a family with a last name.
# Add members to the family using the born() method.
# Use check_majority() to see if someone is allowed to go out.
# Display family information with family_presentation().
family1 = Family("Yakobson")
family1.born("Yakov",33)
family1.born("Miri", 28)
family1.family_presentation()
family1.check_majority("Miri")

family2 = Family("Petrov")
family2.born("Serg",13)
family2.born("Miri", 11)
family2.born("Petr",55)
family2.family_presentation()
family2.check_majority("Miri")