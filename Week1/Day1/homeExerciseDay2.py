#Part 1 XP
print ("Hello word \n"*4)

print((99**3)*8 )

print(5 < 3)               #False
print(3 == 3)              #True
#print(3 == "3")           #Error
#print(3" > 3)             #Error
print("Hello" == "hello")  #False

computer_brand='Mac'
print(f"I have a {computer_brand} computer.")

name='Victoria'
age=52
shoe_size=36
print(f"My name is {name} and for the last {age-16} years (since I was 16) my shoe size has not changed from {shoe_size}")

a=16
b=5
if a>b:
    print ("Hello word")
    
if (int(input ("Enter integer: "))%2 == 0):
    print ("Odd")
else:
    print("Even")
    
if (input("Lets play game. The winner's name matches mine. Enter your name: ").capitalize()==name):
    print("Wow! When Victoria plays, victory follows")
else:
    print("There will be another attempt after rebirth")
    
if int(input("Enter your height in centimeters: "))>145:
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride")
    

#Part 2 XP Gold
#Exercise 1 : Hello World-I love Python
print ("Hello word \n"*4,"I love python \n"*4)

#Exercise 2 : What is the Season ?
months = {
    'spring':'345',
    'summer':'678',
    'autumn':['9','10','11'],
    'winter':['12','1','2']
}
mnth=input("Enter month number: ")
if not mnth.isdigit() :
    print('out of type')
elif  not(1<=int(mnth)<=12):
    print('out of range')
else:
    for season,month in months.items():
        if mnth in month:
            print (season)
        
#Part 3 XP Ninja
#Exercise 4
#Use python to find out how many characters are in the following text, 
#use a single line of code (beyond the establishment of your my_text variable).
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
my_text += 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ' 
my_text += 'Ut enim ad minim veniam, quis nostrud exercitation ullamco '
my_text += 'laboris nisi ut aliquip ex ea commodo consequat. '
my_text += 'Duis aute irure dolor in reprehenderit in voluptate velit '
my_text += 'esse cillum dolore eu fugiat nulla pariatur. '
my_text += 'Excepteur sint occaecat cupidatat non proident, '
my_text += 'sunt in culpa qui officia deserunt mollit anim id est laborum.'
print(len(my_text))

#Exercise 5
#Keep asking the user to input the longest sentence they can without the character “A”.
#Each time a user successfully sets a new longest sentence, print a congratulations message.
curr_str = input ('Input the longest sentence they can without the character “A”: ')
max_len=len(curr_str)
while 'A' not in curr_str:
    curr_str = input ("Can you input more long? ")
    if len(curr_str)>max_len and 'A' not in curr_str:
        print (f"Winner! Won by {len(curr_str)-max_len} characters")
        max_len=len(curr_str)
else:
    print ("'A' stopes the game")
