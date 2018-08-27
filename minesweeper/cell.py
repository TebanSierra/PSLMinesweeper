

class Cell(object):
    '''
    Cell construction
    @arg isMine (Use to determine if the cell is a Mine or not, 
                 by default is false)
    '''
    def __init__(self, isMine=False):
        self.isCover = True
        self.isMine = isMine
        self.isMarked = False
        if isMine:
            self.minesNext = -1
        else:
            self.minesNext = 0

    '''
    Change cell status to uncover
    '''
    def uncover(self):
        self.isCover = False

    '''
    Make a cell be marked
    '''
    def mark(self):
        self.isMarked = True
    
    '''
    Getter for mine attribute
    return True/False
    '''
    def getMine(self):
        return self.isMine

    '''
    Getter for cover attribute
    return True/False
    '''
    def getCover(self):
        return self.isCover

    '''
    Increment by one to mines next to cell
    '''
    def addNext(self):
        self.minesNext = self.minesNext + 1
    
    '''
    Getter for number of mines next
    retunr int
    '''  
    def getNext(self):
        return self.minesNext
        
    '''
    Cell printing based on conditions and cell state
    '''
    def printCell(self):
        if self.isCover and not self.isMarked:
            return(".")
        elif not self.isCover and not self.isMine:
            if self.minesNext == 0:
                return("_")
            else:
                return(str(self.minesNext))
        elif self.isCover and self.isMarked:
            return("P")
        elif not self.isCover and self.isMine:
            return("*")
    
    '''
    Check if cell does not contain neighbour mines, cover status and mine status
    '''
    def checkEmpty(self):
        return self.getNext() == 0 and self.getCover() and not self.getMine()
    
    '''
    Check if cell contains neighbour mines, cover status and mine status
    '''
    def hasNeighbours(self):
        return self.getNext() != 0 and self.getCover() and not self.getMine()