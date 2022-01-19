import random


class Player:

    def __init__(self, name, roll_dice, location, balance, assets):
        self.name = name
        self.location = location
        self.balance = balance
        self.assets = assets
        self.roll_dice = roll_dice

    def roll_dice(self):
        print("enter 'roll' to roll the die")
        die = input(" ")
        n = random.randint(0, 6)
        print(n)


player1 = Player(name='Peter')
player2 = Player(name='Jack')







