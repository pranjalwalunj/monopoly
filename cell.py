class Cell:
    def __init__(self, name, price, owner):
        self.name = name
        self.price = price
        self.owner == None

    def get_cell_owner(self):
        if self.owner == None:
            print("you are on unowned cell")

