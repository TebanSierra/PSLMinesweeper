#!/usr/bin/python3
import cell
import board
import color as color


COVER = 0
MINE = 1
UNCOVER = 2
MARK = 3

class GamePlay(object):
    def __init__(self, height, width, mines):
        self.board = board.Board(height, width, mines)
    
    def play(self):
        row, columm, action = input("Select a Cell and an Action: ").split()
        invalidPlay = True
        while(invalidPlay):
            if not ((action != "U") ^ (action != "M")):
                print("Play must be Uncover (U) or Mark (M)")
                row, columm, action = input("Select a Cell and an Action: ").split()
            else:
                invalidPlay = False
             

    def printBoard(self):
        self.board.printBoard()

    def isPlaying(self):
        return True