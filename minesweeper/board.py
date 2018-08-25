import cell
import random as rd


class Board(object):
    def __init__(self, height, width, mines):
        self.height = height
        self.width = width
        self.mines = mines
        minesUsed = 0
        self.board = [[0 for r in range(width)] for c in range(height)]
        for r in range(height):
            for c in range(width):
                if minesUsed < mines:
                    isMine = rd.choice([True, False])
                    self.board[r][c] = cell.Cell(isMine)
                    if isMine:
                        minesUsed = minesUsed+1
                else:
                    self.board[r][c] = cell.Cell()

    def printBoard(self):
        for r in range(self.height):
            cells = []
            for c in range(self.width):
                cells.append(self.board[r][c].printCell())
            print(" ".join(cells))