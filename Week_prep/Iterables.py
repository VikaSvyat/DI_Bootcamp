#Given a list [1, 2, 3, 4], print out all the values in the list one by one.
list_ = [1, 2, 3, 4]
for i in list_:
    print(i)
#Given a list [1, 2, 3, 4], print out all the values in the list multiplied by 20.
list_ = [1, 2, 3, 4]
for i in list_:
    print(i*20)

#Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter of each name: ["E", "T", "M"].
list_ = ["Elie", "Tim", "Matt"]
new_list = []
for i in list_:
    new_list.append(i[0])
print(new_list)

#Given a list [1, 2, 3, 4, 5, 6], return a new list with all the even values: [2, 4, 6].
list_ = [1, 2, 3, 4, 5, 6]
new_list = []
for i in list_:
    if i % 2 == 0:
        new_list.append(i)
print(new_list)

#Given two lists [1, 2, 3, 4] and [3, 4, 5, 6], return a new list that contains only the values present in both lists: [3, 4].
list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
new_list = []
for i in list_1:
    if i in list_2:
        new_list.append(i)
print(new_list)
#Given a list of words ["Elie", "Tim", "Matt"], return a new list with each word reversed and in lowercase: ["eile", "mit", "ttam"].
list_ = ["Elie", "Tim", "Matt"]
new_list = []
for i in list_:
    new_list.append(i[::-1].lower())
print(new_list)
#Given two strings "first" and "third", return a new list of the letters that are present in both strings: ["i", "r", "t"].
list_1 = "first"
list_2 = "third"
new_list = []
for i in list_1:
    if i in list_2 and i not in new_list:
        new_list.append(i)
print(new_list)     
#For all numbers between 1 and 100, return a list of the numbers that are divisible by 12: [12, 24, 36, 48, 60, 72, 84, 96].
new_list = []
for i in range(1, 101):
    if i % 12 == 0:
        new_list.append(i)
print(new_list)
#Given the string "amazing", return a list with all the vowels removed: ["m", "z", "n", "g"].
list_ = "amazing"
new_list = []
for i in list_:
    if i not in "aeiou":
        new_list.append(i)
print(new_list)
#Generate a list with the following value: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
new_list = []
for i in range(3):
    new_list.append([0, 1, 2])
print(new_list)         
#Generate a list with the following structure:
new_list = []
for i in range(10): 
    new_list.append([j for j in range(10)])
print(new_list)