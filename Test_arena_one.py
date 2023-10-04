# Importing datetime to check refuel method
from datetime import datetime
from datetime import timedelta

# The following is a test for the lifting_partner() method in gym sim project
difference_test = abs(8-1)
print(difference_test)

def test_difference_vars(var1, var2):
    if abs(var1-var2) <= 500:
        return 'Sucess'
    else:
        return 'Fail'

test_var1 = 1300
test_var2 = 2000
test_var3 = 1700

print(test_difference_vars(test_var1, test_var2))
print(test_difference_vars(test_var1, test_var3))
print(test_difference_vars(test_var2, test_var3))

# Testing the time functionality for the refuel method in the gym sim project
# TEST OUT LOWER FUNCTION LOGIC WITH SOMETHING MORE SIMPLE
class PumpControl:
    def __init__(self, val):
        self.val = val
    # Can you not use methods in the __repr__ format?
    def __repr__(self):
        return 'Testing repr'
        #"This is the value for setTime: {set_time}, this is the value for checkTime: {check_time}".format(set_time = self.setTime, check_time = self.checkTime)
    
    def setTime(self):
        now = datetime.now()
        self.timeOff=now + timedelta(minutes=int(self.val))
        return 'pumpOn'

    def checkTime(self):
        if self.timeOff < datetime.now():
            return 'pumpOff'
        else:
            return 'Pump is still on'

# Can i use a method result in __repr__
# Do you have to include self in methods even if there are no attributes
class TestReturns:
    # Do you need to have a __init__ for other methods to work
    #def __init__(self):
       # pass
    
    def test1(self, object):
        if object.setTime == 'pumpOn':
            return 'This works!'
        else:
            return 'Failed'
    
pump_test = PumpControl(2)
print(pump_test)
#print(pump_test.setTime)
#print(pump_test.checkTime)
return_test = TestReturns()
print(return_test.test1(pump_test))

# Test using the returned value of a function/method as an if statement in another function
# FIGURE THIS OUT WITH CLASSES, not sure how it will work with the (self)
def first_return(var):
    if var >= 100:
        return 'Over or equal to 100'
    else:
        return 'Not over or equal to 100'
    
def second_return(returned_val):
    if returned_val == 'Over or equal to 100':
        return 'Success'
    else:
        return 'Fail'
    
print(second_return(first_return(100)))
print(second_return(first_return(20)))

# Testing mutliple options for using one classes attributes in another class
class Lifter:
    def __init__(self, name, age, strength):
        self.name = name
        self.age = age
        self.strength = strength

    def __repr__(self):
        return '{name} is {age} years old, and has a strength of {strength}.'.format(name = self.name, age = self.age, strength = self.strength)
    
    def lift(self):
        # Could you ask for input inside a method? If so, you could add functionality based on the input at the beginning of the method with an if statement (if they have taken a steroid, strength will increase faster)
        # Could figure out how to do the timer and set a swtich for how long the lifter will have increased strenghth w/ each lift after taking the steroid
        # Use returned value of the use method in an if statment to add functionality... would this automatically call the use method?
        if self.strength <= 10:
            self.strength += 2
        elif self.strength > 10:
            self.strenght += 1
        else:
            return 'Something went wrong'
        
class Steroid:
    def __init__(self, type, lifter: Lifter):
        self.type = type
        self.lifter = lifter
    
    def __repr__(self):
        # If you include the use method in this repr, it automatically calls the method and returns the value (the methods functionality is automatically called for future reference)
        return 'This is a {type} steroid, and it belongs to {lifter}.'.format(type = self.type, lifter = self.lifter.name)
    
    def use(self):
        if self.lifter.age >= 18:
            self.lifter.strength += 10
            return 'You have used {type} and your strength has increased by 1.'.format(type = self.type)
        elif self.lifter.age < 18:
            return 'You are too young to be taking steroids, please comee back when you are 18 or older'
        else:
            return 'Something went wrong'
        
lifter_one = Lifter('John', 25, 5)
steroid_one = Steroid('Testosterone', lifter_one)
print(lifter_one)
print(steroid_one)
print(lifter_one.strength)
print(steroid_one.lifter.strength)
print(steroid_one.use())

# Dont need to put the lifter in the init, just each needed method
class Supplement:
    def __init__(self, type):
        self.type = type
    
    def use(self, lifter: Lifter):
        if self.type == 'Protein':
            lifter.strength += 1
            return 'You have used {type} and your strength has increased by 1.'.format(type = self.type)
        elif self.type == 'Creatine':
            lifter.strength += 2
            return 'You have used {type} and your strength has increased by 2.'.format(type = self.type)
        else:
            return 'Something went wrong'

# Testing the use of input() inside methods, as well as calling methods based on input
class Player:
    def __init__(self, name, card1, card2):
        self.name = name
        self.card1 = card1
        self.card2 = card2
        self.hand = [self.card1, self.card2]

    def __repr__(self):
        return '{name} has {card1} and {card2}.'.format(name = self.name, card1 = self.card1, card2 = self.card2)
    
    # Could do an analyze hand method that checks for blackjack, bust, win, push, etc. and then call that method in another method that lets you choose if you want to hit stay
    # Could check this method every time, maybe have a change ace method that changes the value of the ace if it is in the hand
    def check_ace(self):
        if self.card1 or self.card2 == 'Ace':
            ace_choice = input('You have an ace in your hand, would you like it to be 1 or 11? [Please enter 1 or 11]')
            if ace_choice == '1':
                return 'Your ace is now 1'
        else:
            return 'Your hand does not contain an ace'
        
    def test(self):
        if self.check_ace() == '1':
            return 'This works'
        
player_one = Player('John', 'Ace', 'King')
print(player_one)
#print(player_one.check_ace())

# Calls the check_ace method automatically, and then returns the value of the method
#print(player_one.test())


def input_func1():
    print('You have selected 1')
    next_input = input('Now select 3 or 4: ')
    if next_input == '3':
        return 'You have selected 3'

def input_func2():
    return 'You have selected 2'

# Could also do this without a function and just use if statements, and change the returns to prints
def input_func():
    input_test = input('Please select the number 1 or 2: ')
    if input_test == '1':
        return input_func1()
    elif input_test == '2':
        return input_func2()
    # Could use while loop to keep asking for input until the correct input is given
    else:
        return input_func()
    
print(input_func())

# Testing this for the blackjack project
# Options for inheritance dillema: 
# 1. Possibly take away game class and just have the methods in the player and dealer classes, would have to dupicate some methods in both classes
# 2. Could just have the methods in the player class and then have the dealer class inherit from the player class, or vice versa 
# 3. Could do a parent/child class or the other type of inheritance (starts with a c)
# 4. Could take away the game class and just have the checking functions by themselves (not in a class) and call them in the methods of the player and dealer classes

# Testing 4 below: (WORKS)
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chips = 100
    
    def __repr__(self):
        return '{name} has {hand}.'.format(name = self.name, hand = self.hand)
    
    def get_cards(self, card1, card2, card3):
        self.hand.append(card1)
        self.hand.append(card2)
        self.hand.append(card3)
        return self.hand
    
    def get_chips(self, bet_amount):
        if check_for_bust() == 'Bust':
            self.chips -= bet_amount
            return 'You have busted and lost your bet'
        else:
            self.chips += bet_amount
            return 'You have won and gained your bet'

def check_for_bust(player: Player):
    if sum(player.hand) > 21:
        return 'Bust'
    else:
        return 'Not bust'
    
player_1 = Player('John')
player_1.get_cards(3, 10, 10)
print(check_for_bust(player_1))
player_1.hand.pop()
player_1.hand.append(2)
print(check_for_bust(player_1))

# 1 and 2 would work most likely
# Need to figuren out how to automatically call all the checking functions every time a turn is made (could make a function that calls all the checking functions and then call that function in every method that makes a turn)

# How to get the index of a whole word in a string
# Could use a for loop to check each index of the string and then return the index range of the word (after the space)
# Could use if statements to check the first couple letters of the string (to see how long the string is until the suit), and then index to the range of the word if it matches (saved in a variable for each card)... then if that index range variables match, they win the side bet
string = "This is a string" # String would be the card, then there would be another card
string_begin = string[0:4]
if string_begin == 'This':
    suit1 = string[10:16]
    print(suit1)
#elif string_begin == ''
#if statement same as above for the other card
#if suit1 equals other suit, they win the side bet