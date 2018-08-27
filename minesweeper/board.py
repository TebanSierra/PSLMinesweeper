import cell
import random as rd


'''
Board Class

Used to storage and control each cell of the game
'''
class Board(object):
    '''
    Board constructor
    @arg height (number of rows)
    @arg width (number of columns)
    @arg mines (number of mines)
    '''
    def __init__(self, height, width, mines):
        self.height = height
        self.width = width
        self.mines = mines
        self.minesLoc = []
        self.marks = []
        self.totalCells = width*height
        self.uncovered = 0

        # Mines locations generation
        minesUsed = 0
        while(minesUsed < mines):
            rdR = rd.randint(0, height-1)
            rdC = rd.randint(0, width-1)
            mineLoc = str(rdR) + ',' + str(rdC)
            if mineLoc not in self.minesLoc:
                self.minesLoc.append(mineLoc)
                minesUsed = minesUsed + 1
        
        # Board filling
        self.board = [[cell.Cell() for r in range(width)] for c in range(height)]
        for i in range(len(self.minesLoc)):
            pos = self.minesLoc[i].split(',')
            row = int(pos[0])
            col = int(pos[1])
            self.board[row][col] = cell.Cell(True)

        self.seekMines()

    """
    Board controller, each play is processed here
    """
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
                self.uncovered += 1
                self.uncoverCell(row, column)
                return True
        elif action == "M":
            if cell.getCover():
                cell.mark()
                self.marks.append(str(row) + ',' + str(column))
            else:
                print("You cannot mark an uncovered cell.")    
            return True

    '''
    Method use to uncover the appropiate cells after each play.
    return nothing
    '''
    def uncoverCell(self, row, column):
        # cellU stands for cell Up
        # cellUR stands for cell Upper Right
        # cellR stands for cell Right
        # cellLR stands for cell Lower Right
        # cellD stands for cell Down
        # cellLL stands for cell Lower Left
        # cellL stands for cell Left
        # cellUL stands for cell Upper Left
        if self.board[row][column].getNext() == 0:
            if row == 0:
                cellD = self.board[row+1][column]
                if column == 0:
                    cellR = self.board[row][column+1]
                    cellLR = self.board[row+1][column+1]
                    if cellR.checkEmpty():
                        cellR.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row, column+1)
                    elif cellR.hasNeighbours():
                        cellR.uncover()
                        self.uncovered += 1
                    if cellLR.checkEmpty():
                        cellLR.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column+1)
                    elif cellLR.hasNeighbours():
                        cellLR.uncover()
                        self.uncovered += 1
                    if cellD.checkEmpty():
                        cellD.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column)
                    elif cellD.hasNeighbours():
                        cellD.uncover()
                        self.uncovered += 1
                elif column == self.width-1:
                    cellL = self.board[row][column-1]
                    cellLL = self.board[row+1][column-1]
                    if cellL.checkEmpty():
                        cellL.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row, column-1)
                    elif cellL.hasNeighbours():
                        cellL.uncover()
                        self.uncovered += 1
                    if cellLL.checkEmpty():
                        cellLL.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column-1)
                    elif cellLL.hasNeighbours():
                        cellLL.uncover()
                        self.uncovered += 1
                    if cellD.checkEmpty():
                        cellD.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column)
                    elif cellD.hasNeighbours():
                        cellD.uncover()
                        self.uncovered += 1
                else:
                    cellR = self.board[row][column+1]
                    cellLR = self.board[row+1][column+1]
                    cellL = self.board[row][column-1]
                    cellLL = self.board[row+1][column-1]
                    if cellL.checkEmpty():
                        cellL.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row, column-1)
                    elif cellL.hasNeighbours():
                        cellL.uncover()
                        self.uncovered += 1
                    if cellLL.checkEmpty():
                        cellLL.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column-1)
                    elif cellLL.hasNeighbours():
                        cellLL.uncover()
                        self.uncovered += 1
                    if cellD.checkEmpty():
                        cellD.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column)
                    elif cellD.hasNeighbours():
                        cellD.uncover()
                        self.uncovered += 1
                    if cellLR.checkEmpty():
                        cellLR.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column+1)
                    elif cellLR.hasNeighbours():
                        cellLR.uncover()
                        self.uncovered += 1
                    if cellR.checkEmpty():
                        cellR.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row, column+1)
                    if cellR.hasNeighbours():
                        cellR.uncover()
                        self.uncovered += 1
            elif row == self.height-1:
                cellU = self.board[row-1][column]
                if column == 0:
                    cellR = self.board[row][column+1]
                    cellUR = self.board[row-1][column+1]
                    if cellR.checkEmpty():
                        cellR.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row, column+1)
                    elif cellR.hasNeighbours():
                        cellR.uncover()
                        self.uncovered += 1
                    if cellUR.checkEmpty():
                        cellUR.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row-1, column+1)
                    elif cellUR.hasNeighbours():
                        cellUR.uncover()
                        self.uncovered += 1
                    if cellU.checkEmpty():
                        cellU.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row-1, column)
                    elif cellU.hasNeighbours():
                        cellU.uncover()
                        self.uncovered += 1
                elif column == self.width-1:
                    cellL = self.board[row][column-1]
                    cellUL = self.board[row-1][column-1]
                    if cellL.checkEmpty():
                        cellL.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row, column-1)
                    elif cellL.hasNeighbours():
                        cellL.uncover()
                        self.uncovered += 1
                    if cellUL.checkEmpty():
                        cellUL.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row-1, column-1)
                    elif cellUL.hasNeighbours():
                        cellUL.uncover()
                        self.uncovered += 1
                    if cellU.checkEmpty():
                        cellU.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column)
                    elif cellU.hasNeighbours():
                        cellU.uncover()
                        self.uncovered += 1
                else:
                    cellR = self.board[row][column+1]
                    cellUR = self.board[row-1][column+1]
                    cellL = self.board[row][column-1]
                    cellUL = self.board[row-1][column-1]
                    if cellL.checkEmpty():
                        cellL.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row, column-1)
                    elif cellL.hasNeighbours():
                        cellL.uncover()
                        self.uncovered += 1
                    if cellUL.checkEmpty():
                        cellUL.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row-1, column-1)
                    elif cellUL.hasNeighbours():
                        cellUL.uncover()
                        self.uncovered += 1
                    if cellU.checkEmpty():
                        cellU.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row-1, column)
                    elif cellU.hasNeighbours():
                        cellU.uncover()
                        self.uncovered += 1
                    if cellUR.checkEmpty():
                        cellUR.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row-1, column+1)
                    elif cellUR.hasNeighbours():
                        cellUR.uncover()
                        self.uncovered += 1
                    if cellR.checkEmpty():
                        cellR.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row, column+1)
                    if cellR.hasNeighbours():
                        cellR.uncover()
                        self.uncovered += 1
            else:
                cellU = self.board[row-1][column]
                cellD = self.board[row+1][column]
                if column == 0:
                    cellR = self.board[row][column+1]
                    cellUR = self.board[row-1][column+1]
                    cellLR = self.board[row+1][column+1]
                    if cellR.checkEmpty():
                        cellR.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row, column+1)
                    elif cellR.hasNeighbours():
                        cellR.uncover()
                        self.uncovered += 1
                    if cellUR.checkEmpty():
                        cellUR.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row-1, column+1)
                    elif cellUR.hasNeighbours():
                        cellUR.uncover()
                        self.uncovered += 1
                    if cellU.checkEmpty():
                        cellU.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column)
                    elif cellU.hasNeighbours():
                        cellU.uncover()
                        self.uncovered += 1
                    if cellLR.checkEmpty():
                        cellLR.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column+1)
                    elif cellLR.hasNeighbours():
                        cellLR.uncover()
                        self.uncovered += 1
                    if cellD.checkEmpty():
                        cellD.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column)
                    elif cellD.hasNeighbours():
                        cellD.uncover()
                        self.uncovered += 1
                elif column == self.width-1:
                    cellL = self.board[row][column-1]
                    cellUL = self.board[row-1][column-1]
                    cellLL = self.board[row+1][column-1]
                    if cellL.checkEmpty():
                        cellL.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row, column-1)
                    elif cellL.hasNeighbours():
                        cellL.uncover()
                        self.uncovered += 1
                    if cellUL.checkEmpty():
                        cellUL.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column-1)
                    elif cellUL.hasNeighbours():
                        cellUL.uncover()
                        self.uncovered += 1
                    if cellU.checkEmpty():
                        cellU.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column)
                    elif cellU.hasNeighbours():
                        cellU.uncover()
                        self.uncovered += 1
                    if cellD.checkEmpty():
                        cellD.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column)
                    elif cellD.hasNeighbours():
                        cellD.uncover()
                        self.uncovered += 1
                    if cellLL.checkEmpty():
                        cellLL.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column-1)
                    elif cellLL.hasNeighbours():
                        cellLL.uncover()
                        self.uncovered += 1
                else:
                    cellR = self.board[row][column+1]
                    cellUR = self.board[row-1][column+1]
                    cellL = self.board[row][column-1]
                    cellUL = self.board[row-1][column-1]
                    cellLR = self.board[row+1][column+1]
                    cellLL = self.board[row+1][column-1]
                    if cellU.checkEmpty():
                        cellU.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row-1, column)
                    elif cellU.hasNeighbours():
                        cellU.uncover()
                        self.uncovered += 1
                    if cellUR.checkEmpty():
                        cellUR.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row-1, column+1)
                    elif cellUR.hasNeighbours():
                        cellUR.uncover()
                        self.uncovered += 1
                    if cellR.checkEmpty():
                        cellR.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row, column+1)
                    elif cellR.hasNeighbours():
                        cellR.uncover()
                        self.uncovered += 1
                    if cellLR.checkEmpty():
                        cellLR.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column+1)
                    elif cellLR.hasNeighbours():
                        cellLR.uncover()
                        self.uncovered += 1
                    if cellD.checkEmpty():
                        cellD.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column)
                    elif cellD.hasNeighbours():
                        cellD.uncover()
                        self.uncovered += 1
                    if cellLL.checkEmpty():
                        cellLL.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row+1, column-1)
                    elif cellLL.hasNeighbours():
                        cellLL.uncover()
                        self.uncovered += 1
                    if cellL.checkEmpty():
                        cellL.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row, column-1)
                    elif cellL.hasNeighbours():
                        cellL.uncover()
                        self.uncovered += 1
                    if cellUL.checkEmpty():
                        cellUL.uncover()
                        self.uncovered += 1
                        self.uncoverCell(row-1, column-1)
                    elif cellUL.hasNeighbours():
                        cellUL.uncover()
                        self.uncovered += 1
    
    '''
    Method used to assing number of mines next to a cell
    return nothing
    '''
    def seekMines(self):
        height = self.height
        width = self.width
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

    '''
    Method use to check board state in case of win
    return True/False, message
    '''
    def checkBoard(self):
        if len(self.minesLoc) == len(self.marks):
            if self.totalCells-len(self.minesLoc) == self.uncovered:
                return False, "You Win!"
        for i in range(len(self.minesLoc)):
            pos = self.minesLoc[i].split(',')
            row = int(pos[0])
            col = int(pos[1])
            if not self.board[row][col].getCover():
                return False, "Game Over. You Lose!"
        return True, ''

    '''
    Method use to print board content according to conditions
    return nothing
    '''
    def printBoard(self):
        for r in range(self.height):
            cells = []
            for c in range(self.width):
                cells.append(self.board[r][c].printCell())
            print(" ".join(cells))