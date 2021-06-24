# Deck Class
# Instantiate a new deck each time
# Shuffle deck through a method call
# Deal cards from the deck object
import Card as card 
import random

class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in card.suits:
            for rank in card.ranks:
                # Create card object 
                created_card = card.Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        # Shuffle deck
        random.shuffle(self.all_cards)

    # Deal one card
    def deal_one(self):
        # Deal one from top of deck 
        return self.all_cards.pop(0)
