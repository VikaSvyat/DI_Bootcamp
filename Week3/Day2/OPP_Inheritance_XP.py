# Exercise 1: Pets
# Step 1: Create the Siamese class

# Step 2: Create a list of cat instances

# Step 3: Create a Pets instance of the list of cat instances

# sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
# sara_pets.walk()
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'

class Siamese (Cat):
   pass

class Bengal(Cat):
    pass

class Chartreux(Cat):
    pass




#Exercise 2: Dogs
# Step 1: Create the Dog Class

# Create a class called Dog with name, age, and weight attributes.
# Implement a bark() method that returns “<dog_name> is barking”.
# Implement a run_speed() method that returns weight / age * 10.
# Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.

class Dog:
    def __init__(self, name, age, weight):
       self.name = name
       self.age = age
       self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        winner = self.run_speed() * self.weight
        if winner > other_dog.run_speed()*other_dog.weight:
            return f"winner {self.name}"
        else:
            return f"winner {other_dog.name}"

if __name__ == "__main__":
    all_cats = [Bengal("Beni", 5), Chartreux("Chati", 3), Siamese("Simy", 15)]
    sara_pets = Pets(all_cats)
    sara_pets.walk()
    
    dog1 = Dog("Viva",5,38)
    dog2 = Dog("Baldr",5,28)

    print(dog1.bark())
    print(dog2.run_speed())
    print(dog1.fight(dog2))


