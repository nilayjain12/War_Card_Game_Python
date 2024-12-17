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
