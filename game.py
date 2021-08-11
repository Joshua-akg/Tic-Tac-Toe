import time
from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # list of 9 elements
        self.currentWinner = None

    def printBoard(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def printBoardNums():
        numberBoard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print('| '+' | '.join(row) + ' |')

    def availableMoves(self):
        moves = []
        for (i,mark) in enumerate(self.board):
            if mark == ' ':
                moves.append(i)
        return moves
        #return [i for i,spot in enumerate(self.board) if spot == ' ']
        
    def playable(self):
        return ' ' in self.board

    def numPlayable(self):
        return self.board.count(' ')

    def makeMove(self, square, letter):
        if self.board[square] == ' ':           #Check if the square is free
            self.board[square] = letter

            if self.winner(square, letter):     #Check if it is a winning move
                self.currentWinner = letter

            return True
        return False

    def winner(self, square, letter):
        #Check the row of the played square
        rowIndex = square // 3 # row index is square div 3
        row = self.board[rowIndex*3 : (rowIndex+1)*3]        
        if all(squares == letter for squares in row): #If there are three in a row
            return True

        #Check the column of the played square
        columnIndex = square % 3 #column index is square mod 3
        column = [self.board[columnIndex + i*3] for i in range(3)]
        if all(squares == letter for squares in column): #If there are three in a column
            return True
        
        #Check the diagonals
        if square%2==0:     #If even
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all(squares == letter for squares in diagonal1): #If there are three in a row
                return True

            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all(squares == letter for squares in diagonal2): #If there are three in a row
                return True

        return False


def play(game, xPlayer, oPlayer, printGame=True):
    if printGame:
        game.printBoardNums()
        print('')
    
    letter = 'X'                    #starting letter
    while game.playable():          #Whilst there are free squares
        if letter == 'O':           #Get the player's move
            square = oPlayer.get_move(game) 
        else:
            square = xPlayer.get_move(game)
                                    #Play the player's move
        if game.makeMove(square, letter):
            if printGame:           #Print the board
                print("\n"+letter+f' has played on square {square}')
                game.printBoard()
                print('')

            if game.currentWinner:
                print(letter + ' has WON!')
                return letter

            letter = 'O' if letter == 'X' else 'X'  #Switch players

    print('It\'s a TIE!')

    # @staticmethod
def printMenu():
    print("Welcome to TIC-TAC-TOE\n")
    print("You may choose to play either against the random computer, or against another human player \n")

    choice = 0

    while (choice != 1) and (choice != 2):
        print("Please choose from the options below: \n(1) Player vs Player \n(2) Player vs Computer\n")

        try:
            # choice = input("Choice: ")
            choice = int(input("Choice: "))

            # print(f"Choice is {choice}")

            if (choice != 1) and (choice != 2):
                raise ValueError
        except:
            print("\nInvalid Choice Entered! Try Again.\n")
            choice = 0

    return choice



if __name__ == "__main__":
    print("")
    choice = printMenu()
    print("")

    if choice == 2:
        oPlayer = ComputerPlayer('O')
    else:
        oPlayer = HumanPlayer('O')

    xPlayer = HumanPlayer('X')

    g = TicTacToe()
    play(g, xPlayer, oPlayer, printGame=True)
            