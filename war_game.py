# Importing libraries
import random

# Global variable for cards rank loopup
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# Global variable for suits of the cards
suits = ('Hearts', 'Diamond', 'Spades', 'Clubs')

# Global variable for ranks
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#----------------------------------------------#
# CARD class
class Card():

    # Initialize method
    def __init__(self, suit:str, rank:str):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    # To print a card, we create a string method
    def __str__(self):
        return self.rank + " of " + self.suit
    
#----------------------------------------------#
# DECK class
class Deck():
    
    # Initialize method
    def __init__(self):
        self.all_cards = []     # list of all the card objects

        # Create all the card objects using the Card class
        for suit in suits:
            for rank in ranks:
                card = Card(suit=suit, rank=rank)
                self.all_cards.append(card)
    
    # Method to shuffle a deck
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
    
    # Deal a card - Taking one card from the deck
    def deal_once_card(self):
        return self.all_cards.pop()     # Returning last card from the list of cards
    
#----------------------------------------------#
# PLAYER Class
class Player():
    
    # Initialization method
    def __init__(self, name):
        self.name = name        # Identified by name
        self.all_cards = []     # Initially a list of empty card that will be filled

    # Method to remove cards from a player
    def remove_one_card(self):
        return self.all_cards.pop(0)

    # Method to add the card/cards to a player
    def add_cards(self, new_cards):
        # Check if list of new_cards is a list or a single card
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    # String method to print the player
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

#----------------------------------------------#
# GAME Class - GAME SETUP
player_one = Player("P1")
player_two = Player("P2")

new_deck = Deck()
new_deck.shuffle_deck()

# Split the decks to both players
for _ in range(26):
    player_one.all_cards.append(new_deck.deal_once_card())
    player_two.all_cards.append(new_deck.deal_once_card())

# This will help to check if the game is over or not
game_on = True

# This is the current round number that will be displayed
round_number = 0

# Setting up the while loop until the game is on
while game_on:

    # Increasing the round number
    round_number += 1
    print(f"Round {round_number}")

    # Check to see who wins if there are no cards in either player
    if len(player_one.all_cards) == 0:
        print("Player One, is out of cards!\n")
        print("Player Two Wins!!!")
        game_on = False
        break
    elif len(player_two.all_cards) == 0:
        print("Player Two, is out of cards!\n")
        print("Player One Wins!!!")
        game_on = False
        break
    
    # Starting the round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one_card())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one_card())

    war = True
    while war:
        # Check if p1 has greater card than p2
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            war = False
            
        # Check if p1 has smaller card than p2
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            war = False
            
        # Check if p1 has equally similar card than p2
        else:
            print("--WAR--")

            # Check if enough cards are there or not for both players
            if len(player_one.all_cards) < 18:
                print("Player One - Not Enough Cards!\n")
                print("Player Two Wins!!!")
                game_on = False
                break
            elif len(player_two.all_cards) < 18:
                print("Player Two - Not Enough Cards!\n")
                print("Player One Wins!!!")
                game_on = False
                break
            else:
                for num in range(20):
                    player_one_cards.append(player_one.remove_one_card())
                    player_two_cards.append(player_two.remove_one_card())
#----------------------------------------------#
