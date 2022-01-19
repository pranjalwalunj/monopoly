import random


class Player:

    def __init__(self, name, location=0, balance=1000, assets=[]):
        self.name = name
        self.location = location
        self.balance = balance
        self.assets = assets

    def _dice(self):
        print("enter 'roll' to roll the die")
        roll_dice = input(" ")
        n = random.randint(0, 6)
        print(n)


player1 = Player(name='Peter')
player2 = Player(name='Jack')
player1._dice()
player2._dice()








