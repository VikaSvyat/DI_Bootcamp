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