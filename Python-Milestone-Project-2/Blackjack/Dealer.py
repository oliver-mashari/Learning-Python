import Player 

class Dealer():

    def __init__(self):
        self.hand = [] 
        self.value = 0
        self.aces = 0 
    
    def deal_hand(self, new_card):
        self.hand.append(new_card)
