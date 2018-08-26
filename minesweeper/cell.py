import color as color


COVER = 0
UNCOVER = 1
MARK = 2
MINE = 3

class Cell(object):
    def __init__(self, isMine=False):
        self.isCover = True
        self.isMine = isMine
        self.isMarked = False
        if isMine:
            self.minesNext = -1
        else:
            self.minesNext = 0

    def uncover(self):
        self.isCover = False

    def mark(self):
        self.isMarked = True
    
    def getMine(self):
        return self.isMine

    def getCover(self):
        return self.isCover

    def addNext(self):
        self.minesNext = self.minesNext + 1
    
    def getNext(self):
        return self.minesNext

    def getState(self):
        state = {'Cover': self.isCover, 'Mine': self.isMine, 'Mark': self.isMarked}
        return state
        
    def printCell(self):
        if self.isCover and not self.isMarked:
            return(".")
        elif not self.isCover and not self.isMarked and not self.isMine:
            if self.minesNext == 0:
                return("_")
            else:
                return(str(self.minesNext))
        elif self.isCover and self.isMarked:
            return("P")
        elif not self.isCover and self.isMine:
            return("*")