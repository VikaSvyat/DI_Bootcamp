#Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = {}
for i in range(0,min(len(keys),len(values))):
    dictionary [keys[i]] = values[i]
print(dictionary)

#Exercise 2
# Write a program that calculates the total cost of movie tickets for a family based on their ages.

def calculate_ticket_cost(person):
    total_cost = 0
    for name, age in person.items():
        if age < 3:
            cost = 0
        elif 3 <= age <= 12:
            cost = 10
        else:
            cost = 15
        total_cost += cost
        print(f"{name} (age {age}): ${cost}")
    return total_cost

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# total = calculate_ticket_cost(family)
# print(f"Total ticket cost for the family: ${total}")

#Allow the user to input family members’ names and ages, then calculate the total ticket cost.

def input_family_info():
    family = {}
    while True:
        name = input("Enter family member's name (or 'X' to finish): ")
        if name.lower() == 'x':
            break
        try:
            age = int(input(f"Enter {name}'s age: "))
            family[name] = age
        except ValueError:
            print("Please enter a valid age.")
    return family   
family = input_family_info()
total = calculate_ticket_cost(family)
print(f"Total ticket cost for the family: ${total}")

#Exercise 3


brand ={    
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",     
        "US": "pink, green"
    }
}
brand["number_stores"] = 2
print("Zara's clients are:", brand["type_of_clothes"])
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print(" the last item in international_competitors ",brand["international_competitors"][-1])
print(" the major colors in the US ",brand["major_color"]["US"])
print(' the number of keys in the dictionary', len(brand))
print(' all keys of the dictionary ', brand.keys())
more_on_zara = {
    "creation_date": 2005,
    "number_stores": 5 
}               
brand.update(more_on_zara)  #Merge this dictionary with the original brand dictionary
for key, value in brand.items():
    print(f'{key}: {value}') 
    
#Exercise 4 
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]  

users_sorted = sorted(users)  
dict1 = {}
dict2 = {}
dict3 = {}
for i in range(len(users)):
    dict1[users[i]] = i
    dict2[i] = users[i]
    dict3[users_sorted[i]] = i
print(dict1)
print(dict2)
print(dict3)        
