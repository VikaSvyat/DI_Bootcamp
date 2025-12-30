# Step 1: Create the Farm Class
# Step 2: Implement the __init__ Method
# Step 3: Create a method called add_animal.
# It should take two parameters: animal_type and count (with a default value of 1). 
# Count is the quantity of the animal that will be added to the animal dictionary.
# The dictionary will look like this:
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    # def add_animal(self, animal_type, count=1):
    #     if animal_type in self.animals:
    #         self.animals[animal_type] += count
    #     else:
    #         self.animals[animal_type] = count

#upgrade the add_animal Method
# use **kwargs for passing multiple animals
    def add_animal(self, **kwargs):
        for animal_type, count in kwargs.items():
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

#Create a method called get_info.
# It should return a string that displays the farm’s name, the animals and their counts, and the “E-I-E-I-0!” phrase.
# Use string formatting to align the animal names and counts into columns.
    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal}\t : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info
#Add a method called get_animal_types to the Farm class.
# This method should return a sorted list of all animal types (keys from the animals dictionary).
    def get_animal_types(self):
        return sorted(self.animals.keys())  
#Add a method called get_short_info to the Farm class.
# This method should return a string like “McDonald’s farm has cows, goats and sheeps.”.
    def get_short_info(self):
        animal_types = self.get_animal_types()
        for animal in animal_types:
            if self.animals[animal] > 1:
                animal_types[animal_types.index(animal)] = animal + 's'
        if not animal_types:
            return f"{self.name}'s farm has no animals."
        elif len(animal_types) == 1:
            return f"{self.name}'s farm has {animal_types[0]}."
        else:
            str = ", ".join(animal_types[:-1]) + f" and {animal_types[-1]}"
            return f"{self.name}'s farm has {str}."

macdonald = Farm("McDonald")
# macdonald.add_animal('cow', 5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 1)
macdonald.add_animal(cow=5, sheep=2, goat=12)
print(macdonald.get_info())
print(macdonald.get_short_info())
