import time

from player import Player

class Game:

    def __init__(self, game_duration=1200, bank_balance=50000):
        """
        This is going to be used to set the duration of the game. For our use case,
        (hope you remember what is an use case), this is going to be 20 minutes. Hence,
        I set a default time of 1200 seconds which ultimately equates to 20 minutes.
        """
        self.duration = game_duration
        self.bank_balance = bank_balance
        
        
    def set_timer(self):
        """
        We have two values, the start_epoch and the stop epoch. Epoch is a term used to define a
        certain unique point of time in computing.

        Essentially, most computers start computing time from the midnight of 1st of January 1970.
        The epoch time at any point denotes the amount of seconds passed since that point till now.

        time.time() helps you with that. All we are doing is, we are finding out the epoch time at which
        the game should end, hence we are adding 1200 seconds to the start time of the game. After that
        we simply do a while loop and continue it until it reaches stop_epoch's value.
        """

        self.start_epoch = time.time()
        self.stop_epoch = self.start_epoch + self.duration

    def transact(self, player, amount):
        self.bank_balance -= amount
        player.update_balance(amount)

    def pay_rent(self, tenant, landlord):
        rent = 500
        tenant.update_balance(-rent)
        landlord.update_balance(rent)


    def bank_has_enough_balance(self):
        if self.bank_balance < 0:
            return False
        return True

    def declare_winner(self, player1, player2, winner=None):
        """
        At this point, we know the game has ended and has been won by a player. Through this
        function, we find out the final winner of the game!

        :params player1: The player object of the first player
        :params player2: The player object of the second player
        :params winner: If we already know the winner then we do not check the networth, we
            just declare him/her the winner
        """
        if winner:
            return winner, winner.calculate_networth()

        player1_networth = player1.calculate_networth()
        player2_networth = player2.calculate_networth()

        if player1_networth == player2_networth:
            return

        elif player1_networth > player2_networth:
            return player1, player1_networth

        return player2, player2_networth

    
    def display_welcome_message_and_rules(self, player1, player2):
        print(f'Welcome to Monopoly {player1.name} and {player2.name}!')
        print('The rules of the game are as follows: ')
        time.sleep(0.5)
        print('If a player loses all money, the other player automatically wins.')
        time.sleep(0.5)
        print('If a player cannot pay the rent (Rs. 500) for an owned place, they lose.')
        time.sleep(0.5)
        print('If all cities get owned by players, then the player with the highest net worth wins.')
        time.sleep(0.5)
        print('If a player goes bankrupt, then the other player wins.')
        time.sleep(0.5)
        print('By the end of 20 minutes, the player with the highest net worth wins.')
        time.sleep(0.5)
        print('If the central bank balance goes below 0, the player with the highest net worth wins.')
        time.sleep(0.5)

    def start(self, player1, player2):
        
        self.display_welcome_message_and_rules(player1, player2)
        self.set_timer()

    def is_player_bankrupt(self, player):
        """
        Finding out if a player has gone bankrupt or not.
        """
        player_balance = player.get_balance()
        if player_balance <= 0:
            return True
        return False

    def handle_events(self, player):
        """
        These are the events that will be checked on every turn of the player.
        One of them is bankruptcy. Find out other possibilites :)
        """
        cell = player.get_cell()

        if cell.get_cell_name() in ['Motel', 'Jail', 'Club']:
            self.transact(player, -cell.get_cell_price())

        else:
            if cell.is_cell_owned():
                if cell.get_cell_owner() != player:
                    tenant = player
                    landlord = cell.get_cell_owner()
                    self.pay_rent(tenant=tenant, landlord=landlord)
            elif not cell.is_cell_owned() and player.has_enough_balance() is True:
                buy = input("Do you want to buy this cell? ")
                if buy == "yes":
                    self.transact(player, -cell.get_cell_price())
                    player.add_asset(cell)
                    cell.set_owner(player)
                    for asset in player.get_assets():
                        print(asset.name)

        if self.is_player_bankrupt(player) is True:
            return -1

        if not self.bank_has_enough_balance():
            return -1

        # Declare other events that can happen here


if __name__ == '__main__':
    game = Game()

    # Initialize players here (create the player objects) and pass them in game.start()
    player1 = Player(name='Peter')
    player2 = Player(name='Jack')

    game.start(player1=player1, player2=player2)

    winner = None
    
    while time.time() <= game.stop_epoch:
        
        # Player 1's turn
        print(f"It is {player1.get_name()}'s turn!")

        player1_input = input()
        if player1_input == 'roll':
            player1.roll_dice()
            event_outcome = game.handle_events(player1)
            if event_outcome == -1:
                winner, winner_networth = game.declare_winner(player1, player2, winner=player2)
                break

        # Player 2's turn
        print(f"It is {player2.get_name()}'s turn!")
        player2_input = input()
        if player2_input == 'roll':
            player2.roll_dice()
            event_outcome = game.handle_events(player2)
            if event_outcome == -1:
                winner, winner_networth = game.declare_winner(player1, player2, winner=player1)
                break

    if winner:
        print(f'Congratulations {winner.name}! Your networth is Rs.{winner_networth} and you won the game.')

    else:
        winner, winner_networth = game.declare_winner(player1, player2)
        if winner is None:
            print('Its a draw!! Both of your networth is Rs.{player1.calculate_networth()}')
        else:
            print(f'Congratulations {winner.name}! Your networth is Rs.{winner.winner_networth}')
