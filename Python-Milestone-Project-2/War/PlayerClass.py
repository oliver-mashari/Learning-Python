# Player class

import CardClass as card
import DeckClass as deck

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple card objects
            # If player wins a war
            self.all_cards.extend(new_cards)
        else:
            # For a single card object

            self.all_cards.append(new_cards) 

    def __str__(self):
        return f'{self.name} has {len(self.all_cards)}'

# Example 
# Check adding a player
new_player = Player("Nier")
print(new_player)
# Check adding a single card
new_deck = deck.Deck()
my_card = new_deck.deal_one()
new_player.add_cards(my_card)
print(new_player, f"- Nier has the {new_player.all_cards[0]}")
# Check adding multiple cards
new_player.add_cards([my_card, my_card, my_card])
print(new_player)
# Check remove functionality
new_player.remove_one()
print(new_player)