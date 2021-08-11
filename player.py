import math
import time
import random

class Player: 
    def __init__(self, letter):
        #Letter will be either x or o
        self.letter = letter

    def get_move(self, game):
        pass

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        print("Computer is Thinking...")
        time.sleep(0.8)
        square = random.choice(game.availableMoves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid = False
        value = None
        while not valid:    #loop until a valid move is entered
            square = input(self.letter + '\'s turn. Enter a square from 0-8: ')
            try:
                value = int(square)
                if value not in game.availableMoves():
                    raise ValueError
                valid = True
            except ValueError:
                print('Invalid move. Try again.\n')

        return value
