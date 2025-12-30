# Create a class called Phone. This class takes a parameter called phone_number. 
# When instantiating an object create an attribute called call_history which value is an empty list.
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []  
        self.messages = []
# Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. 
# The method should print a string stating who called who, and add this string to the phone’s call_history.
    def call(self, other_phone):
        call_record = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_record)
        self.call_history.append(call_record)   

# Add a method called show_call_history. This method should print the call_history. 
    def show_call_history(self):
        for record in self.call_history:
            print(record)

# Add another attribute called messages to your __init__() method which value is an empty list.

# Create a method called send_message which is similar to the call method. Each message should be saved 
# as a dictionary with the following keys:
# to : the number of another Phone object
# from : your phone number (also a Phone object)
# content
    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}")
# Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)
    def show_outgoing_messages(self):
        for message in self.messages:
            if message["from"] == self.phone_number:
                print(f"To: {message['to']}, wrote: {message['content']}")

    def show_incoming_messages(self):
        for message in self.messages:
            if message["to"] == self.phone_number:
                print(f"From: {message['from']}, received: {message['content']}")

    def show_messages_from(self, other_phone):
        for message in self.messages:
            if message["from"] == other_phone.phone_number and message["to"] == self.phone_number:
                print(f"From: {message['from']}, received: {message['content']}")

# Create two Phone objects.
phone1 = Phone("050-11111")
phone2 = Phone("053-22222")  
# Make  call between the two phones.
phone1.call(phone2)
phone2.call(phone1)
phone2.call(phone1)
phone1.call(phone2)
# Show call history for both phones.
phone1.show_call_history()
phone2.show_call_history()
# Send messages between the two phones.
phone1.send_message(phone2, "Message 1 from Phone 1")
phone1.send_message(phone2, "Message 2 from Phone 1")
phone2.send_message(phone1, "Message 1 from Phone 2")
phone2.send_message(phone1, "Message 2 from Phone 2")
# Show outgoing messages for phone1 and incoming messages for phone2.
phone1.show_outgoing_messages()
# Show incoming messages for phone2 and outgoing messages for phone1.
phone2.show_incoming_messages()
# Show messages received by phone1 from phone2 and messages received by phone2 from phone1.
phone1.show_messages_from(phone2)   
phone2.show_messages_from(phone1)
    


