# Exercise 1: Bank Account
# Create a class called BankAccount that contains the following attributes and methods:
# balance - (an attribute)
# __init__ : initialize the attribute
# deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the int is not positive.
# withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception if not positive
# Add the following attributes to the BankAccount class:
# username, password, authenticated (False by default)
class AnyAccount():
    def __init__(self,username, password, balance = 0):
        self.balance = balance
        self.username = username
        self.password = password

class BankAccount():
    def __init__(self,username, password, balance = 0, authenticated = False):
        self.balance = balance
        self.username = username
        self.password = password
 # Edit withdraw and deposit to only work if authenticated is set to True, if someone tries an action without being 
# authenticated raise an Exception   
    def deposit (self,amount):
        if self.authenticated:
            if amount >0:
                self.balance += amount
                return self.balance
            else:
                raise Exception (f"{amount} not positive")
        else:
            raise Exception (f"User is not authenticated")
    
    def withdraw (self,amount):
        if self.authenticated:
            if amount >0:
                self.balance -= amount
                return self.balance
            else:
                raise Exception (f"{amount} not positive")
        else:
            raise Exception (f"User is not authenticated")
# Create a method called authenticate. This method should accept 2 strings : a username and a password. 
# If the username and password match the attributes username and password the method should set 
# the authenticated boolean to True.
    def authenticate (self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        else:
            return False

# Create a MinimumBalanceAccount that inherits from BankAccount.
# Extend the __init__ method and accept a parameter called minimum_balance with a default value of 0.
# Override the withdraw method so it only allows the user to withdraw money if the balance remains higher than the minimum_balance, raise an Exception if not.
class MinimumBalanceAccount (BankAccount):
    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw (self,amount):
        if amount >0 and self.balance - amount >= self.minimum_balance:
            self.balance -= amount
            return self.balance
        else:
            raise Exception (f"{amount} not positive or the balance remains less than the {self.minimum_balance}")

# Part IV: BONUS Create an ATM class
class ATM_class():
    def __init__(self, account_list, try_limit):
        self.account_list = account_list
        self.try_limit = try_limit
        if not all(isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list): 
            # Validates that account_list contains a list of BankAccount or MinimumBalanceAccount instances.
            raise Exception ("account_list not contains a list of BankAccount or MinimumBalanceAccount")
        try:
            if int(try_limit) <= 0:   # Validates that try_limit is a positive number
                print("Invalid, now try limit = 2")
                self.try_limit = 2
            else:
                self.try_limit = int(try_limit)
        except ValueError:
            print("Invalid, now try limit = 2")
            self.try_limit = 2
        
        self.current_tries = 0
        
        self.show_main_menu()

# ask for the users username and password and call the log_in method with the username and password 
    def log_in(self, username, password):
        for account in self.account_list:   # Checks the username and the password against all accounts in account_list.
            if account.authenticate(username, password):    # If there is a match 
                print("Login successful")
                self.show_account_menu(account)
                return
        # If there is no match with any existing accounts, increment the current tries by 1
        self.current_tries += 1
        print("Login and password don't match your accounts")
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached")
            exit()

# Call the method # show_main_menu:
# This method will start a while loop to display a menu letting a user select:
    def show_main_menu(self):
        while True:
            choice = input("\n1. Log in to your Account \n2. Exit\nChoose an option: ")
            if choice == "1":   # Accepts a username and a password.
                username = input("Username: ")
                password = input("Password: ")
                self.log_in(username, password) # Continue asking the user for a username and a password, until the limit is reached 
            elif choice == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid option")
        
# The method will start a loop giving the user the option to deposit, withdraw or exit.
    def show_account_menu(self, account):
        while True:
            try:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Exit")
                choice = input(f"Current balance {account.balance}. Choose an option: ")
                if choice == "1":
                        amount = int(input("Amount to deposit: "))
                        print("Balance:", account.deposit(amount))
                elif choice == "2":
                    amount = int(input("Amount to withdraw: "))
                    print("Balance:", account.withdraw(amount))
                elif choice == "3":
                    print("Logging out")
                    account.authenticated = False
                    break
                else:
                    print("Entry correct value")
            except ValueError:
                print("Entry correct value")

acc1 = BankAccount( "anna", "1234", 1000)
acc2 = MinimumBalanceAccount( "clara", "4321", 500, minimum_balance=200)
acc3 = AnyAccount ("dan",'333')
acc3 = BankAccount ("dan",'333')

atm = ATM_class([acc1, acc2, acc3], try_limit=input("Enter your try limit: "))