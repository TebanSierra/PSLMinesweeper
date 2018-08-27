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
        self.msg = ''
    
    def play(self):
        row, column, action = self.askPlay()
        invalidPlay = True
        while(invalidPlay):
            if row < 1 or row > self.board.height or \
                column < 1 or column > self.board.width:
                print("Play must be a valid cell")
                row, column, action = self.askPlay()
            elif not ((action != "U") ^ (action != "M")):
                print("Play must be Uncover (U) or Mark (M)")
                row, column, action = self.askPlay()
            else:
                invalidPlay = False
        self.board.play(row-1, column-1, action)
        self.playing, self.msg = self.board.checkBoard()

        return self.msg           

    def printBoard(self):
        self.board.printBoard()

    def isPlaying(self):
        return self.playing

    def askPlay(self):
        goodPlay = False
        while(not goodPlay):
            try:
                row, columm, action = input("Select a Cell and an Action: ").split()
                goodPlay = True
                return int(row), int(columm), action.upper()
            except ValueError:
                print("Enter all the play.")
