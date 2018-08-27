#!/usr/bin/python3
import cell
import board


class GamePlay(object):
    '''
    Game Play initialization
    @arg height (Number of board rows)
    @arg width (Number of board columns)
    @arg mines (number of mines in game)
    '''
    def __init__(self, height, width, mines):
        self.board = board.Board(height, width, mines)
        self.playing = True
        self.msg = ''
    
    '''
    Method controller for game play. it makes all calls to board
    '''
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

    '''
    Call board's print method
    '''
    def printBoard(self):
        self.board.printBoard()

    '''
    Game play status
    return True/False acording to checkBoard
    '''
    def isPlaying(self):
        return self.playing

    '''
    Check if each play is valid and has all the information needed
    return row, column, action
    '''
    def askPlay(self):
        goodPlay = False
        while(not goodPlay):
            try:
                row, columm, action = input("Select a Cell and an Action: ").split()
                goodPlay = True
                return int(row), int(columm), action.upper()
            except ValueError:
                print("Enter all the play.")
