# 1. Given a list: [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this: 
# {'job': 'Instructor', 'name': 'Elie'} (Note: The order does not matter).
list_ = [("name", "Elie"), ("job", "Instructor")]
new_dict = {}
for i in list_:
    new_dict[i[0]] = i[1]
print(new_dict)         





#2. Given two lists: ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"], return a dictionary that looks like this: 
# {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
list_1 = ["CA", "NJ", "RI"]
list_2 = ["California", "New Jersey", "Rhode Island"]
new_dict = {}
for i in range(len(list_1)):
    new_dict[list_1[i]] = list_2[i]
print(new_dict)
#3. Create a dictionary where the keys are vowels in the alphabet and the values are 0. Your dictionary should look like this: 
# {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).
new_dict = {}
for i in "aeiou":
    new_dict[i] = 0
print(new_dict)
new_dict_1 = {}.fromkeys("aeiou", 0)
print(new_dict_1)
#4. Create a dictionary where the key is the position of the letter in the alphabet, and the value is the letter itself. 
# You should return something like this:
new_dict = {}
for i in range(26):
    new_dict[i+1] = chr(i+65)
print(new_dict)
#5. Given the string "awesome sauce", return a dictionary where the keys are vowels, and the values are the count of each vowel in the string. Your dictionary should look like this: {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}.
list_="awesome sauce"
new_dict = {}
for i in list_:
    new_dict[i] = list_.count(i)
print(new_dict)