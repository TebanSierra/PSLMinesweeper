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
        cell = self.board[row][column]
        if action == "U":
            cell.uncover()
            if cell.getCover():
                return True
            elif cell.getMine():
                for i in range(len(self.minesLoc)):
                    pos = self.minesLoc[i].split(',')
                    rowAux = int(pos[0])
                    colAux = int(pos[1])
                    self.board[rowAux][colAux].uncover()
                return False 
            else:
                self.uncoverCell(row, column)
                return True
        elif action == "M":
            cell.mark()
            self.marks.append(str(row) + ',' + str(column))
            return True

    def uncoverCell(self, row, column):
        if row == 0:
            cellD = self.board[row+1][column]
            if column == 0:
                cellR = self.board[row][column+1]
                cellRD = self.board[row+1][column+1]
                if cellR.getNext() == 0 and cellR.getCover() and not cellR.getMine():
                    cellR.uncover()
                    self.uncoverCell(row, column+1)
                elif cellR.getNext() != 0 and cellR.getCover() and not cellR.getMine():
                    cellR.uncover()
                if cellRD.getNext() == 0 and cellRD.getCover() and not cellRD.getMine():
                    cellRD.uncover()
                    self.uncoverCell(row+1, column+1)
                elif cellRD.getNext() != 0 and cellRD.getCover() and not cellRD.getMine():
                    cellRD.uncover()
                if cellD.getNext() == 0 and cellD.getCover() and not cellD.getMine():
                    cellD.uncover()
                    self.uncoverCell(row+1, column)
                elif cellD.getNext() != 0 and cellD.getCover() and not cellD.getMine():
                    cellD.uncover()
            if column == self.width-1:
                cellL = self.board[row][column-1]
                cellLD = self.board[row+1][column-1]
                if cellL.getNext() == 0 and cellL.getCover() and not cellL.getMine():
                    cellL.uncover()
                    self.uncoverCell(row, column-1)
                elif cellL.getNext() != 0 and cellL.getCover() and not cellL.getMine():
                    cellL.uncover()
                if cellLD.getNext() == 0 and cellLD.getCover() and not cellLD.getMine():
                    cellLD.uncover()
                    self.uncoverCell(row+1, column-1)
                elif cellLD.getNext() != 0 and cellLD.getCover() and not cellLD.getMine():
                    cellLD.uncover()
                if cellD.getNext() == 0 and cellD.getCover() and not cellD.getMine():
                    cellD.uncover()
                    self.uncoverCell(row+1, column)
                elif cellD.getNext() != 0 and cellD.getCover() and not cellD.getMine():
                    cellD.uncover()
            else:
                cellR = self.board[row][column+1]
                cellRD = self.board[row+1][column+1]
                cellL = self.board[row][column-1]
                cellLD = self.board[row+1][column-1]
                if cellL.getNext() == 0 and cellL.getCover() and not cellL.getMine():
                    cellL.uncover()
                    self.uncoverCell(row, column-1)
                elif cellL.getNext() != 0 and cellL.getCover() and not cellL.getMine():
                    cellL.uncover()
                if cellLD.getNext() == 0 and cellLD.getCover() and not cellLD.getMine():
                    cellLD.uncover()
                    self.uncoverCell(row+1, column-1)
                elif cellLD.getNext() != 0 and cellLD.getCover() and not cellLD.getMine():
                    cellLD.uncover()
                if cellD.getNext() == 0 and cellD.getCover() and not cellD.getMine():
                    cellD.uncover()
                    self.uncoverCell(row+1, column)
                elif cellD.getNext() != 0 and cellD.getCover() and not cellD.getMine():
                    cellD.uncover()
                if cellRD.getNext() == 0 and cellRD.getCover() and not cellRD.getMine():
                    cellRD.uncover()
                    self.uncoverCell(row+1, column+1)
                elif cellRD.getNext() != 0 and cellRD.getCover() and not cellRD.getMine():
                    cellRD.uncover()
                if cellR.getNext() == 0 and cellR.getCover() and not cellR.getMine():
                    cellR.uncover()
                    self.uncoverCell(row, column+1)
                if cellR.getNext() != 0 and cellR.getCover() and not cellR.getMine():
                    cellR.uncover()


    def printBoard(self):
        for r in range(self.height):
            cells = []
            for c in range(self.width):
                cells.append(self.board[r][c].printCell())
            print(" ".join(cells))