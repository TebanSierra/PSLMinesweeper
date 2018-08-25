import color as color


class Cell(object):
    def __init__(self, isMine=False):
        self.isCover = True
        self.isMine = isMine
        self.isMarked = False
        #self.minesNext = 0

    def uncover(self):
        self.isCover = False

    def mark(self):
        self.isMarked = True

    def printCell(self):
        if self.isCover and not self.isMarked:
            return(".")
        elif self.isCover and not self.isMarked:
            return("_")
        elif self.isCover and self.isMarked:
            return("P")
        elif not self.isCover and self.isMine:
            return("*")