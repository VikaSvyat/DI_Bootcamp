from collections import deque
# Represents a citizen of the city, it has the following attributes: id_number (str), name (str), age (int), priority (bool) 
# and blood_type (str). Its blood type can be “A”, “B”, “AB” or “O”.    
class Family:
    def __init__(self, name):
        self.name = name
        self.members = set()

    def add_member(self, person):
        self.members.add(person)
        person.family = self

    def show_family(self):
        return f"In {self.name}: {[member.name for member in self.members]}"
    
class Human:
    VALID_BLOOD_TYPES = ("A", "B", "AB", "O")
    def __init__(self, id_number, name, age, priority, blood_type):
        if blood_type not in self.VALID_BLOOD_TYPES:
            raise ValueError(f"blood_type must be one of {self.VALID_BLOOD_TYPES}")
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
    # Create an attribute family for the Human class.
    # Initialized as empty, family is a list of all the humans that are living in the same house with this human.
    # Add a method add_family_member(self, person) that adds the person to this human’s family and this human to the person’s family.   
        self.family = None  # will add to the family later

    def add_family_member(self, person):
        # If there is no family yet, create one
        if self.family is None:
            family_name = f"{self.name.lower()}_family"
            self.family = Family(family_name)
            self.family.add_member(self)
        # add new member to the person's family
        self.family.add_member(person)
    
    
# Represents a queue of humans waiting for their vaccine.
# It has the following attribute : humans, the list containing the humans that are waiting. It is initialized empty.
class Queue():
# This class is useful to manage who will get vaccinated in priority. It has the following methods:
    def __init__(self):
        self.persons =  deque()

    def add_person(self, person) : #Adds a human to the queue, if he is older than 60 years old or a priority person, put him at the beginning of the list (at index 0) before every other.
        if person.age >= 60 or person.priority == True:
            self.persons.appendleft (person)
        else:
            self.persons.append (person)

    def __str__(self):
        return ",".join(member.name for member in self.persons)
    
    def find_in_queue(self, person) : #Returns the index of a human in the queue.
        return self.persons.index (person)
    
    def swap(self, person1, person2): #Swaps person1 with person2.
        if person1 in self.persons and person2 in self.persons:
            i1 = self.persons.index (person1)
            i2 = self.persons.index (person2)
            self.persons[i1] = person2
            self.persons[i2] = person1
        else:
            print(f"{person1.name} or {person2.name} not in queue")

# Every human returned by get_next and get_next_blood_type is removed from the list.
# Those functions return None if the list is empty (ie. no one in the list).
    def get_next(self) : #Returns the next human waiting in the queue. The next human should be the one located at the index 0 in the list.
        if self.persons.maxlen == 0:
            return None        
        else:
            return self.persons.popleft()
    
    def get_next_blood_type(self, blood_type) : #Returns the first human with this specific blood type.
        if self.persons.maxlen == 0:
            return None        
        else:
            for i, person in enumerate(self.persons):
                if person.blood_type == blood_type:
                    self.persons.remove(person)
                    return person
            return None

    def sort_by_age(self) : #Sorts the queue
                            # first the priority people
                            # then, the older people
                            # then the younger people
        n=len(list(self.persons))
        print('n=',n)
        for i in range(n):
            # Find the 'first' element according to rules
            first = i
            for j in range(i + 1, n):
                a = self.persons[j]
                b = self.persons[first]
                if a.priority and not b.priority:
                    first = j
                elif a.priority == b.priority and a.age > b.age:
                    first = j
            if first != i:
                self.swap (a,b)


# Part 2
# Human
alice = Human("1", "Alice", 30, False, "AB")
bob   = Human("2", "Bob", 35, True, "O")
dan   = Human('3', "Dan", 17, False, "A")   

alice.add_family_member(alice)    # creating alice_family
alice.add_family_member(bob)
alice.add_family_member(dan)

# print(alice.family.name)
print(alice.family.show_family())

# print([member.name for member in alice.family.members])

# print(bob.family is alice.family)


anna = Human("1", "Anna", 65, False, "A")
boris = Human("2", "Boris", 35, True, "O")
carl = Human("3", "Carl", 10, False, "B")

anna.add_family_member(anna)    # creating anna_family
anna.add_family_member(boris)
anna.add_family_member(carl)
print(anna.family.show_family())

# Queue
# Add the rearrange_queue(self) method to the Queue class, so that there won’t be two members of the same family one after the other in the line.

queue = Queue()
queue.add_person(alice)
queue.add_person(bob)
queue.add_person(anna)
queue.add_person(carl)
queue.add_person(boris)
queue.add_person(dan)
print(queue.find_in_queue(alice))

# print([member for member in queue()])
print(queue)
queue.sort_by_age()
print('after sorting ',queue)
print(queue.get_next().name)
queue.swap(bob,carl)
queue.get_next_blood_type("AB")
print(queue)
