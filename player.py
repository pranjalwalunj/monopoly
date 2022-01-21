import random


class Player:

    def __init__(self, name, location=0, balance=1000, assets=[]):
        self.name = name
        self.location = location
        self.balance = balance
        self.assets = assets

    def give_name(self):
        print("enter your name :")
        your_name = input(" ")
        print("{}'s is added successfully".format(your_name))

    def update_balance(self, amount):
        self.balance += amount

    def get_balance(self):
        print("{}'s current balance is {} ".format(self.name, self.balance))
        return self.balance

    def _dice(self):
        print("enter 'roll' to roll the die")
        roll_dice = input(" ")
        n = random.randint(0, 6)
        print(n)


player1 = Player(name=())
player2 = Player(name=())
player1.give_name()
player2.give_name()
player1._dice()
player2._dice()








