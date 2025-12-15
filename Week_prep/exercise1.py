#Ask the user for a number between 1 and 100

#If the number is a divisible by three, print Fizz

#If the number is a divisible by five, print Buzz.

#If the number is a divisible by both three and five, print FizzBuzz instead.
number = int(input("Please enter a number between 1 and 100: "))    
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)


#Print the following output using one line of code:

print("Hello world\n" * 4)  