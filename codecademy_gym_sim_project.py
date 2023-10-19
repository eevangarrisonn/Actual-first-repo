"""This is a project for the CS path on Codecademy, it is a gym simulator."""
# Research docstrings and how they work, especially __doc__

# The program will be a gym simulator, where you can make friends, find a lifting partner,
# gain muscle/lose weight, and generally just lift... you can also level up your player,^
# and take certain supplements to become stronger^

# Supplement attributes: Ingredients, form, effect
# Supplement methods: Get taken, get analyzed, show effects

# Research how to order, how much that matters (classes and methods)... also research how to use
# classes within other classes... also reseaarch class attributes vs instance attributes^

# Will figure out order of methods later, and their inputs

# ****Will change out numbers to make more sense after logic is
# complete****^

# ***Figure out how to take in functions as input, and specify the directions in depth****

# ***Create dictionarys for all information, change this in methods
# (can these be below the classes or do they have to be above)****^

# ***Read all comments and change****

class Weights:
    """This class will be used to create weights, and will have a method to see how much strength 
    you will gain from lifting them."""
    def __init__(self, type_equipment, weight):
        # Possibly chnage the .type to .type_equipment
        self.type = type_equipment
        self.weight = weight

    def __repr__(self):
        return f'''This type of weight is a {self.type}, that weighs {self.weight}. See how much
        strength you will gain by calling the function below, with your character object as a 
        parameter!'''
        # figure out how users can see all this information, and how to use inputs

    # Make the person param a mandatory object type? (see blackjack project)
    def see_strength_gain(self, person):
        """This is a method that will be used to see how much strength you will gain from lifting, 
        a person object is used as a parameter"""
        # make dictionary for type of weights
        # possibly put in repitition functionality
        # how to avoid so many if/elif statements?
        if self.type == 'bar' and person.strength <= 100:
            return round((self.weight * 3) / 4)
        elif self.type == 'bar' and person.strength > 1000:
            return round((self.weight * 2.5) / 4)
        elif self.type == 'dumbell' and person.strength <= 100:
            return round((self.weight * 2) / 4)
        elif self.type == 'dumbell' and person.strength > 1000:
            return round((self.weight * 1.5) / 4)
        elif self.type == 'medicine ball' and person.strength <= 100:
            return round((self.weight * 1) / 4)
        elif self.type == 'medicine ball' and person.strength > 1000:
            return round((self.weight * 0.5) / 4)
        else:
            return 'That is not a type of weight you can lift here!'
        # possibly put max weight functionality


class Supplements:
    """This class will be used to create supplements, and will have methods to see the price, 
    see the ingredients and see themselves."""
    # Create dictionary with supplement info (prices, types, effects, ingredients... maybe users can access it by typing in a variable (variable would be connected to list index accordingly)
    def __init__(self, ingredients, type_supp, price, effect):
        self.ingredients = ingredients
        self.price = price
        self.effect = effect
        # Possibly change the .type to .type_supp
        self.type = type_supp

    def __repr__(self):
        # Test below
        return f'This supplement is {self.type}, the ingredients are {self.ingredients}, and the price is {self.price}. The effect this will have on you is {self.effect}, how it changes your stats is dependent on your players attributes.'

    def see_price(self, quantity):
        final_price = self.price * quantity
        # Test below
        return f'The final price of this supplement order is {final_price}.'

    def see_ingredients(self):
        if self.type == 'high quality creatine' and self.price > 20:
            return 'The ingredients are'  # + dict entry + something about low/high quality
        elif self.type == 'generic creatine' and self.price <= 20:
            return 'The ingredients are'  # + dict entry + something about low/high quality
        elif self.type == 'high quality pre-workout' and self.price > 20:
            return 'The ingredients are'  # + dict entry + something about low/high quality
        elif self.type == 'generic pre-workout' and self.price <= 20:
            return 'The ingredients are'  # + dict entry + something about low/high quality
        elif self.type == 'high quality muscle builder' and self.type > 20:
            return 'The ingredients are'  # + dict entry + something about low/high quality
        elif self.type == 'generic muscle builder' and self.price <= 20:
            return 'The ingredients are'  # + dict entry + something about low/high quality
        else:
            return 'This is not a type of supplement we offer!'

    def see_effects(self, person):
        pass
        # Think about/correlate to the take_supplement method in the People class
        # Person parameter will be an object from the Person class
        # If statements for the person object/attributes will be dependent on the take_supplements method (talked about above)
        # Just return info according to the above
        # Try to figure out how to connect this method with the take_supplements method below (maybe by using the the returned value as a paraemter like I did in test_arena... this would result in less code)


class People:
    def __init__(self, name, is_friendly=True, level=1):
        self.name = name
        self.friendly = is_friendly
        self.level = level
        self.strength = level * 100
        self.energy = level * 10
        self.money = level * 50
        self.friends = []
        self.liftpartners = []
        self.creatine_list = []
        self.preworkout_list = []
        self.musclebuilder_list = []
        self.supplements_list = []
        # make sure that strength, energy and money dont reset every time there is a level up, if they do, try to figure out/make each of them parameters in __init__
        # make sure supplement names are in seperare list since they have different effects... add high quality list

    def __repr__(self):
        return '{name} has {friends_num} friend(s), and {lift_partners_num} lifting partner(s)! You own a total of {supplement} supplement(s), {creatine} creatine supplements, {preworkout} pre-workout supplements, and {musclebuilder} muscle builder supplements'.format(name=self.name, friends_num=len(self.friends), supplement=len(self.supplements_list), creatine=len(self.creatine_list), preworkout=len(self.preworkout_list), musclebuilder=len(self.musclebuilder_list), lift_partners_num=len(self.liftpartners))
        # add more to this later
        # make if statements for this... especially for the '(s)'

    def meet_friend(self, other_person):
        if self.friendly == True and other_person.friendly == True:
            self.friends.append(other_person)
            other_person.friends.append(self)
            return 'You and {new_friend} are now friends!'.format(new_friend=other_person.name)
        else:
            return 'You and {person} are not compatible.'.format(person=other_person.name)
        # Add no duplicate functionality

    def buy_supplements(self, supplement, quantity):
        if self.money >= supplement.price * quantity and supplement.type == 'creatine':
            self.creatine_list.append(supplement)
            self.supplements_list.append(supplement)
            return 'Purchase of creatine was succesful!'
        elif self.money >= supplement.price * quantity and supplement.type == 'pre-workout':
            self.preworkout_list.append(supplement)
            self.supplements_list.append(supplement)
            return 'Purchase of pre-workout was succesful!'
        elif self.money >= supplement.price * quantity and supplement.type == 'muscle builder':
            self.musclebuilder_list.append(supplement)
            self.supplements_list.append(supplement)
            return 'Purchase of muscle builder was succesful!'
        else:
            return 'You do not have enough money for these supplement(s)'
        # instance/object or dictionary reference... either make second parameter class, or use dict entry instead of supplement.price for second paramater
        # fixed the above, add if statements for different types of supplements and append to their own list
        # add high quality/low quality functionality since they will have different effects

    def take_supplements(self, supplement):
        pass
        # Supplement gets taken by person, changes that persons stats
        # Could store in a dictionary, the keys would be the supplement name and the values would be a number (1, 2, or 3). Calling that value (number) is how the program will know what stats to change
        # If supplement is (x), have x affect on x attribute... taking pre workout adds energy just like the refuel function, but you can call this one anytime, refuel is more of a forced function
        # Depending on the persons current attributes, change the effects (have this be an if statment inside the if statement in the comment above)

    # Need to test this still at bottom of file
    def level_up(self):
        if self.strength >= self.level * 1000:
            self.level += 1
            self.money += self.level * 20
            # Make a max energy level and possibly make this function refill it to max when you level up
            self.energy += 10
            # Test out that the money format works with the above
            return 'You have leveled up to level {level}! You have received {money} dollars, and 10 energy!'.format(level=self.level, money=self.level * 20)
        else:
            # Test out the strenght left format functionality
            return 'You have to gain {strength_left} more strength to level up, keep lifting!'.format(strength_left=(self.level + 1) * 1000 - self.strength)
        # Player will level up every time he gains a certain amount of strength
        # Test stats with this function
        # After a certain amount of strength is gained the level up will happen

    def lift_weights(self):
        pass
        # Player will lift weights at the gym, and gain strength
        # Deplete energy as they lift, add if statement about energy being at 0
        # Include the run out of energy function in this so it checks everytime
        # Include the level up function in this so it checks everytime

    def lifting_partner(self, other_person):
        if abs(self.strength-other_person.strength) <= 500:
            self.liftpartners.append(other_person)
            other_person.liftpartners.append(self)
            # Test below
            return f'You and {other_person} are now lifting partners!'
        else:
            return f'You and {other_person} are not close enough in strength to be lifting partners'
        # Player will be able to see if another player is compatible as a lifting partner
        # Figure out how to make it within a certaain amount of strength (is this done?)
        # Test this
        # Add no duplicate functionality
        # Add friendly functionality, and authomatic calling of meet friends function

    def run_out_of_energy(self):
        # Add an elif/else statement for if they have energy, would just return 'You have energy, you may continue to workout!'
        if self.energy == 0 and len(self.preworkout_list) >= 1:
            self.refuel()  # Ask for input here too?
            return 'You have refueled, you may continue to workout!'
        # elif self.energy == 0 and len(self.preworkout_list) == 0:
            # if self.money >= 20: (buy preworkout) # <-- ask for input on buying pre workout
        else:
            return 'Game over, you have run out of energy, and have no abiltiy to refuel.'
        # Player will have to stop working out and have to refuel
        # Add refuel function to this
        # You must refuel, add input note about needing to get preworkout for this reason
        # Is this function needed/possibly change returns
        # Auto buy lower grade pre workout to continue game, if they have no money, they lose... could you put an input in this to ask if they want higher or lower grade?

    def refuel(self):
        pass
        # Player will sleep/eat so they replenish their energy, and can workout again... energy can also be replenished by taking supplements (Only supps for now)
        # Possibly make it only supplements that can refuel, until I figure out how to use datetime to control the other functions
        # Add functionality to support the different supplement qualitys
        # Add take supplements functionality to this


# TESTING BELOW
# weight_types = ['bar', 'dumbell', 'medicine ball']
test_person_scope = People('Tester')
test = Weights('bar', 300)
print(test.see_strength_gain(test_person_scope))
print(test.__repr__)
test_person_two = People('Tester2')
print(test_person_scope.meet_friend(test_person_two))
# print(test_person_scope.friends)
# print(test_person_two.friends)
print(test_person_scope)
print(test_person_two)
test_supp = Supplements('a, b, c', 'creatine', 30, 'x')
print(test_person_scope.buy_supplements(test_supp, 1))
print(test_person_scope)
test_person_scope.lifting_partner(test_person_two)
test_person_two.lifting_partner(test_person_scope)
print(test_person_scope)
print(test_person_two)

# Order of methods I need to work on: Take supplements, Refuel, Run out of energy, Lift weights
# Things to possibly add: Sleeping for refuel, being able to buy food and eat to refuel, being able to buy a trainer to help you lift/gain strength faster, getting injured (and having injury preventative supps or training)
# Need to test the level up function

# Figure out how to do final newline