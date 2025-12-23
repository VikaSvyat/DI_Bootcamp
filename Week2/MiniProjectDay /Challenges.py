# Exercise 1
# Write a script that inserts an item at a defined index in a list.
my_list = [1, 2, 3, 4, 5]
index = 2
item = 10       
my_list.insert(index, item)
print(my_list)  

# Exercise   2
# 
string = "Write a script that counts the number of spaces in a string."
spaces = string.count(" ")
print(spaces)

# Exercise 3
#        
string = "Write a script that calculates the number of upper case letters and lower case letters in a string."
upper_case = sum(1 for c in string if c.isupper())
lower_case = sum(1 for c in string if c.islower())
print(f"Upper case letters: {upper_case}, Lower case letters: {lower_case}")    

# Exercise 4
# Write  a function to find the sum of an array without using the built in function:
def my_sum(list):
    total = 0
    for num in list:
        total += num
    return total

print(my_sum([1,5,4,2]))    

# Exercise 5
# Write a function to find the max number in a list 
def find_max(list):
    max_num = list[0]
    for num in list:
        if num > max_num:
            max_num = num
    return max_num  

print(find_max([0,1,3,50]))

# Exercise 6
# Write a function that returns factorial of a number
def factorial(n):
    result = 1
    if n == 0:
        return result
    else:
        for i in range(1, n + 1):
            result *= i
        return result

print(factorial(4))

# Exercise 7
# Write a function that counts an element in a list (without using the count method):
def list_count(list, element):
    count = 0
    for item in list:
        if item == element:
            count += 1
    return count

print(list_count(['a','a','t','o'],'a'))

# Exercise 8
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:
def norm(list):
    sum_of_squares = 0
    for num in list:
        sum_of_squares += num ** 2
    return sum_of_squares ** 0.5

print(norm([1,2,2])) 

# Exercise 9
# Write a function to find if an array is monotonic (sorted either ascending of descending)
def is_mono(list):
    def compare_func(a, b):
        if a == b:
            return '='
        elif a < b:
            return '<'
        else:
            return '>'
        
    for i in range(len(list)-1):
        comp = compare_func(list[i], list[i+1])
        if comp != '=':
            break
    for i in range(len(list)-1):
        if compare_func(list[i], list[i+1]) != comp and compare_func(list[i], list[i+1]) != '=': 
            return False
    return True

print(is_mono([7,6,5,5,2,0]))
print(is_mono([2,3,3,3]))
print(is_mono([1,2,0,4]))

# Exercise 10
# Write a function that prints the longest word in a list.
def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word("Write a function that prints the longest word in a list.".split()))

# Exercise 11
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.
def inr_or_str(mix_list):
    int_list = []
    str_list = []
    for item in mix_list:
        if isinstance(item, int):
            int_list.append(item)
        elif isinstance(item, str):
            str_list.append(item)
    return int_list, str_list

ints, strs = inr_or_str([10, 'afsss', -2, 'b', 3, 'c'])
print("Integers:", ints)
print("Strings:", strs) 

# Exercise 12
# Write a function to check if a string is a palindrome:
def is_palindrome (text):
    for i in range (len(text)//2):
        if text[i] != text [-i-1]:
            return False
    return True
    
print(is_palindrome('radtoooootdar'))
print(is_palindrome('John'))

# Exercise 13
# Write a function that returns the amount of words in a sentence with length > k:
def sum_over_k(sentence, k):
    words = sentence.split()
    count = 0
    for word in words:
        if len(word) > k:
            count += 1
    return count    
print(sum_over_k('Do or do not there is no try', 2))   
print(sum_over_k('Do or do not there is no try', 3))

# Exercise 14
# Write a function that returns the average value in a dictionary (assume the values are numeric):
def dict_avg(dict):
    sum = 0
    for value in dict.values():
        sum += value
    return sum / len(dict)

print(dict_avg({'a': 1,'b':2,'c':8,'d': 1}))


# Exercise 15
# Write a function that returns common divisors of 2 numbers:
def common_div(a, b):   
    divisors = []
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisors.append(i)
    return divisors 

print(common_div(10,20))

# Exercise 16
# Write a function that test if a number is prime:
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(11))

# Exercise 17
# Write a function that prints elements of a list if the index and the value are even:
def weird_print(list):
    result = []
    for i in range(len(list)):
        if i % 2 == 0 and list[i] % 2 == 0:
            result.append(list[i])
    return result
print(weird_print([1,2,2,3,4,5]))

# Exercise 18
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:
def type_count(**kwargs):
    number_of_strings = number_of_ints = number_of_floats = number_of_bools = 0
    types = {}
    for value in kwargs.values():
        if isinstance(value, int) and not type(value) is bool:
            number_of_ints += 1
        elif isinstance(value, str):
            number_of_strings += 1
        elif isinstance(value, float):
            number_of_floats += 1
        elif type(value) is bool:
            number_of_bools += 1
    types['int'] = number_of_ints
    types['str'] = number_of_strings
    types['float'] = number_of_floats
    types['bool'] = number_of_bools
    return types
print(type_count(a=1,b='string',c=1.0,d=True,e=False))
# >>>int: 1, str:1 , float:1, bool:2


# Exercise 19
# Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument 
# for any character and split with that argument.
def like_split(string, sep=' '):
    words = []
    current_word = ''
    for char in string:
        if char == sep:
            if current_word:
                words.append(current_word)
                current_word = ''
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    return words
print(like_split("Write a function that mimics the builtin .split() method for strings."))
print(like_split("Write,function, that, mimics, the builtin, method", sep=','))   


# Exercise 20
# Convert a string into password format.
def to_password(string):
    password = ''
    for char in string:
        password += '*'
    return password

print(to_password(input("Enter your password:")))
# Example:
# input : "mypassword"
# output: "***********"

