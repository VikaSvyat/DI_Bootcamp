import math

class Pagination():# Define a class called Pagination to represent paginated content.
    def __init__(self, items = [], page_size = 10):# It should optionally accept a list of items and a page size when initialized.
        #if items == []:
        self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.number_of_pages = math.ceil(len(self.items) / self.page_size)
        print(self.number_of_pages)

    def get_visible_items(self):    # This method returns the list of items visible on the current page.
        return self.items[self.current_idx : self.current_idx + self.page_size]

    def go_to_page(self,page_num):#  Goes to the specified page number (1-based indexing).#  If page_num is out of range, raise a ValueError.
        if page_num > self.number_of_pages:
            raise Exception ("ValueError")
        self.current_idx = self.page_size * (page_num -1)
        self.get_visible_items()
        return self
    
    def first_page(self):   #  Navigates to the first page.
        self.go_to_page(1)
        return self

    def last_page(self):    #  Navigates to the last page.
        self.go_to_page(self.number_of_pages)
        return self
    
    def next_page(self):    # Moves one page forward (if not already on the last page).
        current_page = int(self.current_idx / self.page_size) +1
        if current_page < self.number_of_pages:
             self.go_to_page(current_page + 1)
        else:
            print('This the last page')
        return self

    def previous_page(self): # Moves one page backward (if not already on the first page).
        current_page = int(self.current_idx / self.page_size) +1
        if current_page > 2:
            return self.go_to_page(current_page - 1)
        else:
            print('This the first page')
        return self

    def __str__(self):  #This magic method should return a string displaying the items on the current page, each on a new line.
        str_return =""
        for letter in self.get_visible_items():
            str_return  += letter+"\n"
        return str_return

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(str(p))

print(p.get_visible_items())

p.next_page()
print(p.get_visible_items())

p.last_page()
print(p.get_visible_items())

p.go_to_page(7)

p.go_to_page(1)

print(p.current_idx + 1)

print(p.next_page().next_page().next_page().get_visible_items())
print(p.last_page().previous_page().previous_page().next_page().get_visible_items())

