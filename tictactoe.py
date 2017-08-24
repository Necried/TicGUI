from random import *
import time

# Credit to inventwithpython.com for AI algorithm

def initial():
    '''initialize starting board state'''
    for i in keys:
        board[i] = " " #Empty space represents an empty box

## Create a dictionary representation of a tic-tac-toe board
row = range(3)
column = range(3)
board = {}
keys = []
for i in row:
    for j in column:
        keys += [(i,j)]

initial()

class Player:
    def __init__(self,piece,turn):
        '''Makes a piece on the tic tac toe board unique to a player'''
        self.piece = piece
        self.turn = turn
        
    def get_piece(self):
        return self.piece

    def get_turn(self):
        return self.turn

    def win(self,board):
        '''Checks if the player wins the board state'''
        for i in range(3):
            rows = []
            columns = []
            for j in range(3):
                rows.append(board[(i,j)])
                columns.append(board[(j,i)])
            if rows.count(self.piece) == 3 or columns.count(self.piece) == 3:
                return True
        if board[(0,0)]== self.piece and board[(1,1)]== self.piece \
        and board[(2,2)]== self.piece:
            return True
        if board[(0,2)]== self.piece and board[(1,1)]== self.piece \
        and board[(2,0)]== self.piece:
            return True
        return False

    def place(self,n,board):
        '''Takes an input of tuple n and places an X or O to the
       corresponding n-square on the board'''
        # return false if n is an illegal move
        if n not in legalmoves(board):
            return False
        board[n] = self.piece
        return n

    def myTurn(self,board):
        '''Returns true if its the player's turn to move'''
        boardstate = []
        for i in board.values():
            boardstate.append(i)
        if self.turn == 0:
            if boardstate.count('X') == boardstate.count('O'):
                return True
        elif self.turn == 1:
            if boardstate.count('X') > boardstate.count('O'):
                return True
        return False
            
def make_move(computer,human):
    '''Top-down algorithm for the computer to select and place a move'''
    ## ADDED RETURN TUPLE VALUE OF COORD
    
    if computer.myTurn(board) == False:
        return False #Prevent computer from moving out of turn
    
    for i in legalmoves(board):
        computer.place(i,board)
        # If placing a move wins, proceed to do so
        if computer.win(board) == True:
            return i
        board[i] = ' '
        
    for i in legalmoves(board):
        # Stop a win by the player
        human.place(i,board)
        if human.win(board) == True:
            board[i] = ' '
            return computer.place(i,board)
        board[i] = ' '
        
    # Take a corner if it is available
    corners = [i for i in legalmoves(board) if i == (0,0) or i == (0,2) or
               i == (2,0) or i == (2,2)]
    if corners != []:
        i = choice(corners)
        return computer.place(i,board)
    
    # Take the centre if it is available
    if board[(1,1)] == ' ':
        return computer.place((1,1),board)
    
    # Take the sides
    sides = [i for i in legalmoves(board)]
    i = choice(sides)
    return computer.place(i,board)

def legalmoves(board):
    '''Returns a list of available tuple moves on the current board state'''
    moves = [i for i in board if board[i] == ' ']
    return sorted(moves)

