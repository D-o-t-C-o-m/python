import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomCPU(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.availible_moves())

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        cal = None
        while not valid_square:
            square = input(self.letter + '\'s turn, Input move 0-8:')
            try:
                val = int(square)
                if val not in game.availible_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid Square, Try again')

        return val

