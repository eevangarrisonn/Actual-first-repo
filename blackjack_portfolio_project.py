"""This is apparently a needed docstring according to pylint"""
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
    """Player class (expand later)"""
    # Add cash in and cash out functionality, and exchanging between cash and chips
    # If i add checking functions to dealer class then I will need to have a dealer
    # object in the player class intialization^
    # Call check functions
    # Add a turn counter (put in end of the line check function(s) to add 1
    # every time a turn is made, if it is the first turn have a 'ready to play'^
    # input prompt in the deal method, if it is not the first turn then have a 'continue playing'^
    # input prompt in the deal method)... possibly only have the continue playing prompt after^
    # the deck is done (also reset the counter after deck is done if I do that)^
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = []

    # What is the difference between __str__ and __repr__?
    def __repr__(self):
        return f"{self.name} has {self.chips} chips"

    def bet(self, bet_amount):
        """Set the bet (expand later)"""
        self.money -= bet_amount

    # Use random module to generate random card from deck
    def hit(self, card):
        """Hit (expand later)"""
        self.hand.append(card)

    def stand(self):
        pass

    def double_down(self):
        pass

    def split(self):
        pass

    # Add change ace value method here or dealer class?

# Call check functions


class Dealer:
    """Dealer class (expand later)"""
    def __init__(self, name, player: Player):
        self.hand = []
        self.deck = []
        self.name = name
        self.player = player

    # Pop cards out of deck after they are dealt, then when lenght of
    # deck is equal to some number, call the shuffle method^
    def deal(self):
        pass

    def hit(self):
        pass

    # Call deal method at the end
    def shuffle(self):
        pass

    # Checking functions here? Maybe create them and then call them each time in the methods above (if check(x) == True then (y))... create class with these functions that i can call above
    
# Options for inheritance dillema: 
# 1. Possibly take away game class and just have the methods in the player and dealer classes, would have to dupicate some methods in both classes
# 2. Could just have the methods in the player class and then have the dealer class inherit from the player class, or vice versa 
# 3. Could do a parent/child class or the other type of inheritance (starts with a c)
# 4. Could take away the game class and just have the checking functions by themselves (not in a class) and call them in the methods of the player and dealer classes
    
# Applying number 4 below
# Need seperate check for bust with dealer
# Need seperate check for everything with dealer?
# Figure out order of checking functions, which will connect to which, which will be called in which methods, and the end of the line (of checking functions) for every possible outcome, which checks need to go in which methods in both classes,  and how to get back to the beginning of the line (of checking functions) after every turn (call the deal function at end of line?)


def check_for_blackjack():
    pass
    # still need to figure out how to check for ace
    # use if statement to check the player/dealer statement (might need and or or)
    # if it is true, return 'blackjack' and then call the check_for_win function
    # if it is false, pass (can you use pass statement in a function?)


def check_for_bust():
    pass
    # use if statement to check the player hand total, then use another if statement to check the dealer hand total
    # return player/dealer bust depending on the if statement then trigger the deal or another checking method


def check_for_win():
    pass


def check_for_push():
    pass


def check_for_ace():
    pass


def check_for_loss():
    pass

# Test rogue functions for checking functionality with inheritance below... will delete after testing


# Make the deck_cards list a dictionary and a
# Assign values to each card, or just have the Ace be a string and the rest numbers
# Have aces be worth 1 than just add 10 based on input?
# Could also use a dictionary, and have the keys differentiated by suit, and the values be the card values... if I were to do this, then I could add side bet functionality
deck_cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9,
9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 'Ace', 'Ace', 'Ace', 'Ace']
print(len(deck_cards))
# Have to use a loop to shuffle the deck, then pop the cards out of the list after they are dealt, then shuffle again when the deck is close to empty
random.shuffle(deck_cards)
print(deck_cards)

# Use len(deck_cards) to determine when to shuffle the deck
# Use random module to shuffle the deck
# Assign cards taken out of deck to a value so that they can be added back in when the deck is shuffled
# Figure out how to deal with the Ace card, it can be 1 or 11
# Test out inputs inside of methods in test file, and calling methods depending on input as well
# Have a choice method that takes input and calls the appropriate method (hit, stand, double down, split, etc.)

# Need to figuren out how to automatically call all the checking functions every time a turn is made (could make a function that calls all the checking functions and then call that function in every method that makes a turn)
