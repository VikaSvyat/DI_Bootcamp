# Exercise 1: Formula
# Write a program that calculates and prints a value according 
# to this given formula: Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# Ask the user for a comma-separated string of numbers, use each number 
# from the user as D in the formula and return all the results
import math
C = 50
H = 30
d_list = input("enter a comma-separated string of numbers: ").split(",")
print(d_list)
for D in d_list:
    Q = round(math.sqrt((2 * C * int(D))/H))
    print (Q)
    
# Exercise 2 : List of integers
#too long task, see it in 
#https://octopus.developers.institute/courses/collection/124/course/501/section/1294/chapter/233#
import random
integer_list = []
list_gr_50 = []
list_ls_10 = []
list_sqr = []
unique_numbers = []
min_ = max_ = avr_ = 0 
range_ = random.randint(50, 50)
print(f"Random range: {range_}")
for i in range(1,range_+1):
    integer_input = random.randint(-100, 100) 
    integer_list.append(integer_input)
print(integer_list) 
integer_list.sort(reverse=True)
print(integer_list) 
print(f"Sum = {sum(integer_list)}")
print(f"First in reverse_ordered list = {integer_list[0]}")
print(f"Last in reverse_ordered list = {integer_list[range_-1]}")

#Counting entrance of each element
counts = {}
for int_ in integer_list:
    counts[int_] = counts.get(int_, 0) + 1
#print(counts)

for int_ in integer_list:
    if int_ > 50:
        list_gr_50.append(int_)
    elif int_ < 10:
        list_ls_10.append(int_)
    list_sqr.append(int_**2)
    avr_ += int_
    if int_ > max_:
        max_ = int_
    elif int_ < min_:
        min_ = int_
    if counts[int_] == 1:
        unique_numbers.append(int_)
avr_ = avr_ / range_
print(f"Greater then 50: {list_gr_50}")
print(f"Less then 10: {list_ls_10}")
print(f"List of squares: {list_sqr}")
print(f"Min value: {min_}")
print(f"Max value: {max_}")
print(f"Average value: {avr_}")
print(f"Unique list: {unique_numbers}, totaly {len(unique_numbers)}")

# Exercise 4 : Frequency Of The Words
# Write a program that prints the frequency of the words from the input.
text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
words = text.split(" ")

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)



