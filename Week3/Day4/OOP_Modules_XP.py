#Exercise 1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):  # print(c1)
        name = self.currency + "s" if self.amount != 1 else self.currency
        return f"{self.amount} {name}"

    __repr__ = __str__  # repr(c1)

    def __int__(self):  # int(c1)
        return self.amount

    def __add__(self, other):   # c1 + 5 or c1 + c2
        if isinstance(other, int):
            return self.amount + other
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            return self.amount + other.amount
        return NotImplemented

    def __radd__(self, other):   # 5 + c1
        return self.__add__(other)

    def __iadd__(self, other):# c1 += 5 or c1 += c2
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            self.amount += other.amount
        else:
            return NotImplemented
        return self
    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
try:
    print(c1)
    print(int(c1))
    print(repr(c1))
    print(c1 + 5)
    print(c1 + c2)
    print(c1)
    c1 += 5
    print(c1)
    c1 += c2
    print(c1)
    print(c1 + c3)
except TypeError as e:
    print(e)

#Exercise 2
import func as f
f.add_numbers(c3,c4)

#Exercise 3
import string
import random
random_string = ''.join(random.choice(string.ascii_letters) for _ in range(5))
print(random_string)

#Exercise 4
from datetime import datetime
today = datetime.now()
print(today)

#Exercise 5
next_jan_1 = datetime(year=today.year + 1, month=1, day=1)
print(next_jan_1)
time_left = next_jan_1 - today
print(time_left)

#Exercise 6
birthdate = datetime.strptime(input("Enter your birthday in DD/MM/YYYY: "), "%d/%m/%Y")
time_lived = today - birthdate
minutes = int(time_lived.total_seconds() // 60)
print(f"You have lived {minutes:,} minutes.")

#Exercise 7
from faker import Faker
users = []
faker = Faker()

def add_users(number_of_users): # Create a function to add users
    for _ in range(number_of_users):
        user = {
            "name": faker.name(),
            "address": faker.address(),
            "language_code": faker.language_code()
        }
        users.append(user)

add_users(5)
for i, user in enumerate(users, start=1):
    print(f"User {i}:")
    print(f"\tName: {user['name']}")
    print(f"\tAddress: {user['address']}")
    print(f"\tLanguage Code: {user['language_code']}\n")
