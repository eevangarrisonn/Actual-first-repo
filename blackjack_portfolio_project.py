# This is a text based version of blackjack, the player plays against the dealer
# The classes will be player and dealer
# The player will have the following attributes: name, hand, chips/money
# The dealer will have the following attributes: hand, deck
# The player will have the follwing methods: bet, hit, stand, double down, split
# The dealer will have the following methods: deal, hit

# **NEEDED? May be able to include this in the methods of the player/dealer** 
# The game will have the following attributes: deck, player, dealer
# The game will have the following methods: check for blackjack, check for bust, check for win, check for push 

import random

class Player:
    # Add cash in and cash out functionality, and exchanging between cash and chips
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = []

    # What is the difference between __str__ and __repr__?
    def __repr__(self):
        return f"{self.name} has {self.chips} chips"

    def bet(self, bet_amount):
        self.money -= bet_amount

    # Use random module to generate random card from deck
    def hit(self, card):
        self.hand.append(card)

    def stand(self):
        pass

    def double_down(self):
        pass

    def split(self):
        pass

class Dealer:
    def __init__(self):
        self.hand = []
        self.deck = []

    def deal(self, player: Player):
        pass

    def hit(self):
        pass

    # Checking functions here? Maybe create them and then  call them each time in the methods above (if check(x) == True then x)

# Make the deck_cards list a dictionary and assign values to each card, or just have the Ace be a string and the rest numbers
# Have aces be worth 1 than just add 10 based on input?
# Could also use a dictionary, and have the keys differentiated by suit, and the values be the card values
deck_cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4 ,4 ,4, 5, 5, 5, 5, 6, 6, 6, 6, 7 ,7 ,7 ,7, 8, 8, 8, 8, 9, 9, 9, 9, 10 ,10 ,10 ,10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 'Ace', 'Ace', 'Ace', 'Ace']
print(len(deck_cards))
# Have to use a loop to shuffle the deck, then pop the cards out of the list after they are dealt, then shuffle again when the deck is close to empty
shuffle_deck = random.shuffle(deck_cards)
print(deck_cards)

# Use len(deck_cards) to determine when to shuffle the deck
# Use random module to shuffle the deck
# Assign cards taken out of deck to a value so that they can be added back in when the deck is shuffled
# Figure out how to deal with the Ace card, it can be 1 or 11
# Test out inputs inside of methods in test file, and calling methods depending on input as well
# Have a choice method that takes input and calls the appropriate method (hit, stand, double down, split, etc.)