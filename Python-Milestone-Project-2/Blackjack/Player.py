# Player Class
# Will have a hand 
import Card as card
import Deck as deck

class Player():

    def __init__(self):
        self.hand = [] 
        self.value = 0
        self.aces = 0 
        self.chips = 0

    def deposit(self):
        self.chips = int(input("How many chips are you playing with today?: "))
        print(f"Avaliable chips - {self.chips}")

    def bet(self):
        place_bet = False
        while place_bet is False:
            bet = int(input("Amount bet on this hand?: "))
            if bet > self.chips:
                print("Bet exceeds avaliable chips")
            else:
                print(f"Bet placed - {bet}")
                break
    
    def deal_hand(self, new_card):
        self.hand.append(new_card)
        self.value += new_card.value

    def __str__(self):
        return f"{self.hand}"

        
