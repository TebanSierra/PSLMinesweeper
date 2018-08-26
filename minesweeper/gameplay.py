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
        self.playing = True
    
    def play(self):
        row, columm, action = input("Select a Cell and an Action: ").split()
        rowNum = int(row) 
        colNum = int(columm)
        invalidPlay = True
        while(invalidPlay):
            rowNum = int(row) 
            colNum = int(columm)
            if rowNum < 1 or rowNum > self.board.height or \
                colNum < 1 or colNum > self.board.width:
                print("Play must be a valid cell")
                row, columm, action = input("Select a Cell and an Action: ").split()
            elif not ((action != "U") ^ (action != "M")):
                print("Play must be Uncover (U) or Mark (M)")
                row, columm, action = input("Select a Cell and an Action: ").split()
            else:
                invalidPlay = False
        self.playing = self.board.play(rowNum-1, colNum-1, action)             

    def printBoard(self):
        self.board.printBoard()

    def isPlaying(self):
        return self.playing