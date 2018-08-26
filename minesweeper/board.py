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
        self.totalCells = width*height
        self.uncoOrMark = 0

        minesUsed = 0
        while(minesUsed < mines):
            rdR = rd.randint(0, height-1)
            rdC = rd.randint(0, width-1)
            mineLoc = str(rdR) + ',' + str(rdC)
            if mineLoc not in self.minesLoc:
                self.minesLoc.append(mineLoc)
                minesUsed = minesUsed + 1
        
        self.board = [[cell.Cell() for r in range(width)] for c in range(height)]
        for i in range(len(self.minesLoc)):
            pos = self.minesLoc[i].split(',')
            row = int(pos[0])
            col = int(pos[1])
            self.board[row][col] = cell.Cell(True)
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
            if not cell.getCover():
                return True, ''
            elif cell.getMine():
                for i in range(len(self.minesLoc)):
                    pos = self.minesLoc[i].split(',')
                    rowAux = int(pos[0])
                    colAux = int(pos[1])
                    self.board[rowAux][colAux].uncover()
                return(False, "Game Over") 
            else:
                self.uncoOrMark = self.uncoOrMark + 1
                self.uncoverCell(row, column)
                return True, ''
        elif action == "M":
            cell.mark()
            self.uncoOrMark = self.uncoOrMark + 1
            self.marks.append(str(row) + ',' + str(column))
            return True, ''

    def uncoverCell(self, row, column):
        if self.board[row][column].getNext() == 0:
            if row == 0:
                cellD = self.board[row+1][column]
                if column == 0:
                    cellR = self.board[row][column+1]
                    cellLR = self.board[row+1][column+1]
                    if cellR.getNext() == 0 and cellR.getCover() and not cellR.getMine():
                        cellR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row, column+1)
                    elif cellR.getNext() != 0 and cellR.getCover() and not cellR.getMine():
                        cellR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellLR.getNext() == 0 and cellLR.getCover() and not cellLR.getMine():
                        cellLR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column+1)
                    elif cellLR.getNext() != 0 and cellLR.getCover() and not cellLR.getMine():
                        cellLR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellD.getNext() == 0 and cellD.getCover() and not cellD.getMine():
                        cellD.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column)
                    elif cellD.getNext() != 0 and cellD.getCover() and not cellD.getMine():
                        cellD.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                elif column == self.width-1:
                    cellL = self.board[row][column-1]
                    cellLL = self.board[row+1][column-1]
                    if cellL.getNext() == 0 and cellL.getCover() and not cellL.getMine():
                        cellL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row, column-1)
                    elif cellL.getNext() != 0 and cellL.getCover() and not cellL.getMine():
                        cellL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellLL.getNext() == 0 and cellLL.getCover() and not cellLL.getMine():
                        cellLL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column-1)
                    elif cellLL.getNext() != 0 and cellLL.getCover() and not cellLL.getMine():
                        cellLL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellD.getNext() == 0 and cellD.getCover() and not cellD.getMine():
                        cellD.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column)
                    elif cellD.getNext() != 0 and cellD.getCover() and not cellD.getMine():
                        cellD.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                else:
                    cellR = self.board[row][column+1]
                    cellLR = self.board[row+1][column+1]
                    cellL = self.board[row][column-1]
                    cellLL = self.board[row+1][column-1]
                    if cellL.getNext() == 0 and cellL.getCover() and not cellL.getMine():
                        cellL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row, column-1)
                    elif cellL.getNext() != 0 and cellL.getCover() and not cellL.getMine():
                        cellL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellLL.getNext() == 0 and cellLL.getCover() and not cellLL.getMine():
                        cellLL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column-1)
                    elif cellLL.getNext() != 0 and cellLL.getCover() and not cellLL.getMine():
                        cellLL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellD.getNext() == 0 and cellD.getCover() and not cellD.getMine():
                        cellD.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column)
                    elif cellD.getNext() != 0 and cellD.getCover() and not cellD.getMine():
                        cellD.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellLR.getNext() == 0 and cellLR.getCover() and not cellLR.getMine():
                        cellLR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column+1)
                    elif cellLR.getNext() != 0 and cellLR.getCover() and not cellLR.getMine():
                        cellLR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellR.getNext() == 0 and cellR.getCover() and not cellR.getMine():
                        cellR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row, column+1)
                    if cellR.getNext() != 0 and cellR.getCover() and not cellR.getMine():
                        cellR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
            elif row == self.height-1:
                cellU = self.board[row-1][column]
                if column == 0:
                    cellR = self.board[row][column+1]
                    cellUR = self.board[row-1][column+1]
                    if cellR.getNext() == 0 and cellR.getCover() and not cellR.getMine():
                        cellR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row, column+1)
                    elif cellR.getNext() != 0 and cellR.getCover() and not cellR.getMine():
                        cellR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellUR.getNext() == 0 and cellUR.getCover() and not cellUR.getMine():
                        cellUR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row-1, column+1)
                    elif cellUR.getNext() != 0 and cellUR.getCover() and not cellUR.getMine():
                        cellUR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellU.getNext() == 0 and cellU.getCover() and not cellU.getMine():
                        cellU.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row-1, column)
                    elif cellU.getNext() != 0 and cellU.getCover() and not cellU.getMine():
                        cellU.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                elif column == self.width-1:
                    cellL = self.board[row][column-1]
                    cellUL = self.board[row-1][column-1]
                    if cellL.getNext() == 0 and cellL.getCover() and not cellL.getMine():
                        cellL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row, column-1)
                    elif cellL.getNext() != 0 and cellL.getCover() and not cellL.getMine():
                        cellL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellUL.getNext() == 0 and cellUL.getCover() and not cellUL.getMine():
                        cellUL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row-1, column-1)
                    elif cellUL.getNext() != 0 and cellUL.getCover() and not cellUL.getMine():
                        cellUL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellU.getNext() == 0 and cellU.getCover() and not cellU.getMine():
                        cellU.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column)
                    elif cellU.getNext() != 0 and cellU.getCover() and not cellU.getMine():
                        cellU.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                else:
                    cellR = self.board[row][column+1]
                    cellUR = self.board[row-1][column+1]
                    cellL = self.board[row][column-1]
                    cellUL = self.board[row-1][column-1]
                    if cellL.getNext() == 0 and cellL.getCover() and not cellL.getMine():
                        cellL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row, column-1)
                    elif cellL.getNext() != 0 and cellL.getCover() and not cellL.getMine():
                        cellL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellUL.getNext() == 0 and cellUL.getCover() and not cellUL.getMine():
                        cellUL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row-1, column-1)
                    elif cellUL.getNext() != 0 and cellUL.getCover() and not cellUL.getMine():
                        cellUL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellU.getNext() == 0 and cellU.getCover() and not cellU.getMine():
                        cellU.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row-1, column)
                    elif cellU.getNext() != 0 and cellU.getCover() and not cellU.getMine():
                        cellU.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellUR.getNext() == 0 and cellUR.getCover() and not cellUR.getMine():
                        cellUR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row-1, column+1)
                    elif cellUR.getNext() != 0 and cellUR.getCover() and not cellUR.getMine():
                        cellUR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellR.getNext() == 0 and cellR.getCover() and not cellR.getMine():
                        cellR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row, column+1)
                    if cellR.getNext() != 0 and cellR.getCover() and not cellR.getMine():
                        cellR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
            else:
                cellU = self.board[row-1][column]
                cellD = self.board[row+1][column]
                if column == 0:
                    cellR = self.board[row][column+1]
                    cellUR = self.board[row-1][column+1]
                    cellLR = self.board[row+1][column+1]
                    if cellR.getNext() == 0 and cellR.getCover() and not cellR.getMine():
                        cellR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row, column+1)
                    elif cellR.getNext() != 0 and cellR.getCover() and not cellR.getMine():
                        cellR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellUR.getNext() == 0 and cellUR.getCover() and not cellUR.getMine():
                        cellUR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row-1, column+1)
                    elif cellUR.getNext() != 0 and cellUR.getCover() and not cellUR.getMine():
                        cellUR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellU.getNext() == 0 and cellU.getCover() and not cellU.getMine():
                        cellU.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column)
                    elif cellU.getNext() != 0 and cellU.getCover() and not cellU.getMine():
                        cellU.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellLR.getNext() == 0 and cellLR.getCover() and not cellLR.getMine():
                        cellLR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column+1)
                    elif cellLR.getNext() != 0 and cellLR.getCover() and not cellLR.getMine():
                        cellLR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellD.getNext() == 0 and cellD.getCover() and not cellD.getMine():
                        cellD.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column)
                    elif cellD.getNext() != 0 and cellD.getCover() and not cellD.getMine():
                        cellD.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                elif column == self.width-1:
                    cellL = self.board[row][column-1]
                    cellUL = self.board[row-1][column-1]
                    if cellL.getNext() == 0 and cellL.getCover() and not cellL.getMine():
                        cellL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row, column-1)
                    elif cellL.getNext() != 0 and cellL.getCover() and not cellL.getMine():
                        cellL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellUL.getNext() == 0 and cellUL.getCover() and not cellUL.getMine():
                        cellUL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column-1)
                    elif cellUL.getNext() != 0 and cellUL.getCover() and not cellUL.getMine():
                        cellUL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellU.getNext() == 0 and cellU.getCover() and not cellU.getMine():
                        cellU.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column)
                    elif cellU.getNext() != 0 and cellU.getCover() and not cellU.getMine():
                        cellU.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                else:
                    cellR = self.board[row][column+1]
                    cellUR = self.board[row-1][column+1]
                    cellL = self.board[row][column-1]
                    cellUL = self.board[row-1][column-1]
                    cellLR = self.board[row+1][column+1]
                    cellLL = self.board[row+1][column-1]
                    if cellU.getNext() == 0 and cellU.getCover() and not cellU.getMine():
                        cellU.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row-1, column)
                    elif cellU.getNext() != 0 and cellU.getCover() and not cellU.getMine():
                        cellU.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellUR.getNext() == 0 and cellUR.getCover() and not cellUR.getMine():
                        cellUR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row-1, column+1)
                    elif cellUR.getNext() != 0 and cellUR.getCover() and not cellUR.getMine():
                        cellUR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellR.getNext() == 0 and cellR.getCover() and not cellR.getMine():
                        cellR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row, column+1)
                    elif cellR.getNext() != 0 and cellR.getCover() and not cellR.getMine():
                        cellR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellLR.getNext() == 0 and cellLR.getCover() and not cellLR.getMine():
                        cellLR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column+1)
                    elif cellLR.getNext() != 0 and cellLR.getCover() and not cellLR.getMine():
                        cellLR.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellD.getNext() == 0 and cellD.getCover() and not cellD.getMine():
                        cellD.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column)
                    elif cellD.getNext() != 0 and cellD.getCover() and not cellD.getMine():
                        cellD.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellLL.getNext() == 0 and cellLL.getCover() and not cellLL.getMine():
                        cellLL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row+1, column-1)
                    elif cellLL.getNext() != 0 and cellLL.getCover() and not cellLL.getMine():
                        cellLL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellL.getNext() == 0 and cellL.getCover() and not cellL.getMine():
                        cellL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row, column-1)
                    elif cellL.getNext() != 0 and cellL.getCover() and not cellL.getMine():
                        cellL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    if cellUL.getNext() == 0 and cellUL.getCover() and not cellUL.getMine():
                        cellUL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                        self.uncoverCell(row-1, column-1)
                    elif cellUL.getNext() != 0 and cellUL.getCover() and not cellUL.getMine():
                        cellUL.uncover()
                        self.uncoOrMark = self.uncoOrMark + 1
                    
    def checkBoard(self):
        if len(self.minesLoc) == len(self.marks):
            if self.totalCells == self.uncoOrMark:
                return False

    def printBoard(self):
        for r in range(self.height):
            cells = []
            for c in range(self.width):
                cells.append(self.board[r][c].printCell())
            print(" ".join(cells))