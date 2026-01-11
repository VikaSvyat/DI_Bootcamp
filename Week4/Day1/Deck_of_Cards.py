# The Deck of cards class should NOT inherit from a Card class.
import random
import os
os.system('clear')

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and 
# a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
class Card:
    suits = {"Hearts": "♥",
        "Diamonds": "♦",
        "Clubs": "♣",
        "Spades": "♠"}
    values = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
    def __init__(self, suit, value):
        if value in Card.values:
            self.value = value
        else:
            raise ValueError ("incorrect Value")
        if suit in Card.suits:
            self.suit = suit
        else:
            raise ValueError ("incorrect Suit")
    def is_card(self):
        return f"{Card.suits[self.suit]}{self.value}"   
    def __str__(self):
        return self.is_card()  
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards 
# and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. 
# After a card is dealt, it should be removed from the deck.
class Deck:
    def __init__(self):
        self.cards = [Card(suit, value)
                      for suit in Card.suits
                      for value in Card.values
        ]

    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle (self.cards)

    def deal(self):
        return self.cards.pop()
    
    def __str__(self):
        print_line = ""
        for cc in self.cards:
            print_line += " "+cc.is_card()
        return f"{print_line} - {len(self.cards)} cards in the deck"
        # return ", ".join (self.cards.is_card())
    
d = Deck()
d.shuffle()

print(d.deal())
print(d.deal().is_card())

print (d)