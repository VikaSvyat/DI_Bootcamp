fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#Change the second fruit ("banana") to "blueberry".
fruits[1] = "blueberry"
print(fruits)

numbers = [3, 4]
print(numbers.pop(0))  
print(numbers)  

#1. Add "fig" to the end of the fruits
fruits.append("fig")
#2. Insert "grape" at the beginning of the list
fruits.insert(0,"grape")
#3. Remove "cherry" from the list using using the specific method for it
fruits.pop(3)
#4. Remove the last element from the list using the specific method for it
fruits.pop()
#5. Create another list of berries and combine it with the fruits list into a list called "combined_list"
combined_list= fruits.copy()
combined_list.extend(fruits)
#6. Sort the combined_list
combined_list.sort()
print(combined_list)
#7. Slice the last three elements of the combined list
print(combined_list[-3:])