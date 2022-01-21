class Cell:
    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.owner = None

    def get_cell_owner(self):
        return self.owner

    def get_cell_name(self):
        return self.name

    def get_cell_price(self):
        return self.price

    def is_cell_owned(self):
        if self.owner is None:
            print('This cell is not owned by anyone.')
            return None
        print(f'This cell is owned by {self.owner.name}')
        return self.owner
