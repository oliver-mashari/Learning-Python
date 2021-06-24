# Deck Class
# Instantiate a new deck each time
# Shuffle deck through a method call
# Deal cards from the deck object
import CardClass as card 
import random

class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in card.suits:
            for rank in card.ranks:
                # Create card object 
                created_card = card.Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# Test example 
new_deck = Deck()
print(new_deck.all_cards[-1])
new_deck.shuffle()
print(new_deck.all_cards[0])
my_card = new_deck.deal_one()
print(my_card)