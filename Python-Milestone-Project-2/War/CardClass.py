# Card 
# Needs Suit, Rank, Value 
import random
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six',
            'Seven', 'Eight', 'Nine', 'Ten',
            'Jack', 'Queen', 'King', 'Ace')
# Ace is treated as high
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 
            'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 
            'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# Example 
# two_hearts = Card(suit='Hearts', rank='Seven')
# print(two_hearts)

# print(values[two_hearts.rank])