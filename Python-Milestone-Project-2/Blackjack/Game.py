import Card as cd 
import Deck as dk 
import Dealer as deal
import Player as play

# Add player to game 
player = play.Player()
# Deposit chips 
player.deposit()
# Add dealer to game
dealer = deal.Dealer()
# Add deck to game ans shuffle deck
deck = dk.Deck()
deck.shuffle()


game_on = True 
# Start game
while game_on:

    player.bet()
    
    # Deal starting hand
    while True:
        player.deal_hand(deck.deal_one())
        dealer.deal_hand(deck.deal_one())
        if len(player.hand) == 2:
            break 
    
    # Show player hands 
    print (f"Player hand: {player.hand[0]}, {player.hand[1]}\n ")
    print (f"Dealer hand: {dealer.hand[0]}, <Card> \n ")
    
    # Check player hand 
    
    
    
    break


    