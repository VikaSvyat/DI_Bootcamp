#Exercise 1
#Create a set called my_fav_numbers and populate it with 
#your favorite numbers.
#Add two new numbers to the set.
#Remove the last number you added to the set.
#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
my_fav_numbers = {5,7,23,2002}
my_fav_numbers.update([4,13])
my_fav_numbers.remove(13)
friend_fav_numbers={1,2,3,4,5}
print(my_fav_numbers|friend_fav_numbers)

#Exercise 2
#Given a tuple of integers, 
#try to add more integers to the tuple.
my_tuple = (10,20,30)
#my_tuple.append(40)
my_tuple = my_tuple + (40,)
print(my_tuple)

#Exercise 3
#Remove "Banana" from the list.
#Remove "Blueberries" from the list.
#Add "Kiwi" to the end of the list.
#Add "Apples" to the beginning of the list.
#Count how many times "Apples" appear in the list.
#Empty the list.
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.append("Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)

#Exercise 4
#Create a list containing the following sequence of mixed types: floats and integers:
#1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
i = 1.5
list_1_5 = []
while i<=5:
    if i//1 == i:
        i = int(i)
    list_1_5.append(i)
    i+=0.5
print(list_1_5)

#Exercise 5 
#Write a for loop to print all numbers from 1 to 20, inclusive.
#Write another for loop that prints every number from 1 to 20 
#where the index is even.
#for i in range (0,20):
    #print(i+1)
for i in range (0,20):
    if (i+1)%2==0:
        print(i+1)
        
#Exercise 6 
#Use an input to ask the user to enter their name.
#Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
#hint: check for the method isdigit()
#if the input is incorrect, keep asking for the correct input until it is correct
#if the input is correct print “thank you” and break the loop
user_name = input("Enter your name: ")
while True:
    if user_name.isdigit() or len(user_name)<=3 :
        user_name = input("Give the correct name: ")
    else:
        break
print(f"Thank you, {user_name}")

#Exercise 7 
#Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
#Store these fruits in a list.
#Ask the user to input the name of any fruit.
#If the fruit is in their list of favorite fruits, print:
#"You chose one of your favorite fruits! Enjoy!"
#If not, print: "You chose a new fruit. I hope you enjoy it!"
fruits =[]                  #list of fruits
text_list = input("input your favorite fruits: ")
i=text_list.find(" ")       #index of first " "
while i != -1:
    fruit = text_list[0:i]  #find fruit before " " 
    if fruit != "":
        fruits.append(fruit)#add fruit
    text_list=text_list[i+1:]
    i=text_list.find(" ")   #index of current " "
if text_list != "":
    fruits.append(text_list)#last fruit - all remain after last " "
                            #if it's not empty
#print(fruits)
fruit_user = input("input the name of any fruit: ")
if fruit_user in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

#Exercise 8
#Write a loop that asks the user to enter pizza toppings one by one.
#Stop the loop when the user types 'quit'.
#For each topping entered, print: "Adding [topping] to your pizza."
#After exiting the loop, print all the toppings and the total cost of the pizza.
#The base price is $10, and each topping adds $2.50.
toppings =[]
active = True
price = 10.0
while active: 
    topping = input("Please enter pizza toppings one by one (enter 'quit' when you are finished): ")
    if topping == 'quit':
        active = False
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza")
        price+=2.5
print(f"Full price {price}$ ")

#Exercise 9
#Ask for the age of each person in a family who wants to buy a movie ticket.
#Calculate the total cost based on the following rules:
#Free for people under 3.
#$10 for people aged 3 to 12.
#$15 for anyone over 12.
#Print the total ticket cost.
#Bonus:
#Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
#Ask for each person’s age.
#Remove anyone who isn’t allowed to watch.
#Print the final list of attendees.
cost = 0
text_age = input("Age of each person who wants to buy a movie ticket: ")
attendees =[]                  #list of ages of attendees
i=text_age.find(" ")       #index of first " "
while i != -1:
    age = text_age[0:i]  #find age before " " 
    if age != "" :
        attendees.append(int(age))#add age
    text_age=text_age[i+1:]
    i=text_age.find(" ")   #index of current " "
if text_age != "":
    attendees.append(int(text_age))#last age - all remain after last " "
                            #if it's not empty 
for age in attendees[:]: #use copy of list because it's a error to remove from curring list 
    if 16<=age<21:
        print(f"isn’t allowed to watch in age {age}")
        attendees.remove(age)
print(f"For that ages of attendees {attendees}")

for age in attendees:
    if 3<=age<12:
        cost+=10 
    elif 12<=age :
        cost+=15 
print(f"the total ticket cost {cost}" )
