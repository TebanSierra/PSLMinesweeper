import cell
import random as rd


COVER = 0
UNCOVER = 1
MARK = 2
MINE = 3

class Board(object):
    def __init__(self, height, width, mines):
        self.height = height
        self.width = width
        self.mines = mines
        self.minesLoc = []
        self.marks = []
        self.marksLeft = mines

        minesUsed = 0
        self.board = [[0 for r in range(width)] for c in range(height)]
        for r in range(height):
            for c in range(width):
                if minesUsed < mines:
                    prob = round(rd.uniform(0,1), 2)
                    if prob < 0.2:
                        self.board[r][c] = cell.Cell(True)
                        self.minesLoc.append(str(r) + ',' + str(c))
                        minesUsed = minesUsed+1
                    else:
                        self.board[r][c] = cell.Cell()
                else:
                    self.board[r][c] = cell.Cell()
        for r in range(height):
            for c in range(width):
                if not self.board[r][c].getMine():
                    if r == 0:
                        if c == 0:
                            if self.board[r+1][c].getMine():
                                self.board[r][c].addNext()
                            if self.board[r][c+1].getMine():
                                self.board[r][c].addNext()                        
                            if self.board[r+1][c+1].getMine():
                                self.board[r][c].addNext()
                        elif c == width-1:
                            if self.board[r][c-1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r+1][c-1].getMine():
                                self.board[r][c].addNext()                        
                            if self.board[r+1][c].getMine():
                                self.board[r][c].addNext()
                        else:
                            if self.board[r][c-1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r+1][c-1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r+1][c].getMine():
                                self.board[r][c].addNext()
                            if self.board[r+1][c+1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r][c+1].getMine():
                                self.board[r][c].addNext()
                    elif r == height-1:
                        if c == 0:
                            if self.board[r-1][c].getMine():
                                self.board[r][c].addNext()
                            if self.board[r-1][c-1].getMine():
                                self.board[r][c].addNext()                        
                            if self.board[r][c+1].getMine():
                                self.board[r][c].addNext()
                        elif c == width-1:
                            if self.board[r][c-1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r-1][c-1].getMine():
                                self.board[r][c].addNext()                        
                            if self.board[r-1][c].getMine():
                                self.board[r][c].addNext()
                        else:
                            if self.board[r][c-1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r-1][c-1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r-1][c].getMine():
                                self.board[r][c].addNext()
                            if self.board[r-1][c+1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r][c+1].getMine():
                                self.board[r][c].addNext()
                    else:
                        if c == 0:
                            if self.board[r-1][c].getMine():
                                self.board[r][c].addNext()
                            if self.board[r-1][c+1].getMine():
                                self.board[r][c].addNext()                        
                            if self.board[r][c+1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r+1][c+1].getMine():
                                self.board[r][c].addNext()                        
                            if self.board[r+1][c].getMine():
                                self.board[r][c].addNext()
                        elif c == width-1:
                            if self.board[r][c-1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r-1][c-1].getMine():
                                self.board[r][c].addNext()                        
                            if self.board[r-1][c].getMine():
                                self.board[r][c].addNext()
                            if self.board[r+1][c-1].getMine():
                                self.board[r][c].addNext()                        
                            if self.board[r+1][c].getMine():
                                self.board[r][c].addNext()
                        else:
                            if self.board[r][c-1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r-1][c-1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r-1][c].getMine():
                                self.board[r][c].addNext()
                            if self.board[r-1][c+1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r][c+1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r+1][c+1].getMine():
                                self.board[r][c].addNext()
                            if self.board[r+1][c].getMine():
                                self.board[r][c].addNext()
                            if self.board[r+1][c-1].getMine():
                                self.board[r][c].addNext()
    def play(self, row, column, action):
        if action == "U":
            self.board[row][column].uncover()
            if self.board[row][column].getCover():
                return True
            if self.board[row][column].getMine():
                for i in range(len(self.minesLoc)):
                    pos = self.minesLoc[i].split(',')
                    rowAux = int(pos[0])
                    colAux = int(pos[1])
                    self.board[rowAux][colAux].uncover()
                return False
            else:
                self.checkCell(row, column)
                return True
        elif action == "M":
            self.board[row][column].mark()
            self.marks.append(str(row) + ',' + str(column))
            return True

    def checkCell(self, row, column):
        pass

    def printBoard(self):
        for r in range(self.height):
            cells = []
            for c in range(self.width):
                cells.append(self.board[r][c].printCell())
            print(" ".join(cells))