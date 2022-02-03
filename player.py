import random
from board import BOARD


class Player:

    def __init__(self, name, location=0, balance=5000, assets=[]):
        self.name = name
        self.location = location
        self.balance = balance
        self.assets = assets

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def update_balance(self, amount):
        self.balance += amount

    def get_balance(self):
        print("{}'s current balance is {} ".format(self.name, self.balance))
        return self.balance

    def get_cell(self):
        return BOARD[self.location]

    def has_enough_balance(self):
        if self.get_balance() >= self.location:
            print("You can buy this cell.")
            return True
        return False

    def roll_dice(self):
        n = random.randint(1, 7)
        print(n)
        self.location = (self.location + n) % len(BOARD)

        cell = self.get_cell()
        print(cell.get_cell_name(), cell.get_cell_price())


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








