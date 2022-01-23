import random
from board import BOARD


class Player:

    def __init__(self, name, location=0, balance=1000, assets=[]):
        self.name = name
        self.location = location
        self.balance = balance
        self.assets = assets

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
        self.location + n % len(BOARD)

    def add_asset(self, single_cell):
        """
        Single cell object is added
        :param single_cell: Cell object
        :return:
        """
        self.assets.append(single_cell)

    def calculate_networth(self):
        """
        Initialising balance of player. Calculating the total networth with the no of asset of
        player and remaining balance.
        :return:
        """
        networth = self.balance
        for asset in self.assets:
            networth += asset.get_cell_price()
        return networth








