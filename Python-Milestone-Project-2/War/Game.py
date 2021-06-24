import CardClass as card 
import DeckClass as deck 
import PlayerClass as player 

# Game setup
# Add Players
player_one = player.Player("one")
player_two = player.Player("two")

# Setup a new deck for the game 
new_deck = deck.Deck()
new_deck.shuffle()

# Split the deck among the players 
for x in range(26):
    # Each player dealt 1 card every loop
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# Confirm player hand size 
print(f"Player {player_one.name} has {player_one} cards")
print(f"Player {player_two.name} has {player_two} cards")

game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f"This is round {round_num}")

    if len(player_one.all_cards) == 0:
        print(f"Player {player_one.name}, out of cards! Player {player_two.name} wins!")
        game_on = False 
        break
    if len(player_two.all_cards) == 0:
        print(f"Player {player_two.name}, out of cards! Player {player_one.name} wins!")
        game_on = False 
        break

    # Start new round 
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war: 
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print('WAR!')
            if len(player_one.all_cards) < 3:
                print("Player {player_one.name} unable to declare war")
                print("Player {player_two.name} wins!")
                game_on = False
                break
            elif len(player_two.all_cards) < 3:
                print("Player {player_two.name} unable to declare war")
                print("Player {player_one.name} wins!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
