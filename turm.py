import figur

class turm:

    def __init__(self, row, col, farbe):
        self.row = row
        self.col = col
        self.farbe = farbe
        #self.wertung = 5
        self.wertung = 8
        self.id = 't'
        self.o_notaion = 14

    def canMove(self, otherRow,otherCol, feld):
        if(self.row == otherRow and self.col == otherCol):
            return False

        if self.row != otherRow and self.col != otherCol:
            return False
        if self.row == otherRow:
            if self.col < otherCol:
                for i in range(self.col+1,otherCol):
                    if feld[self.row][i] != None:
                        return False
            else:
                for i in range(otherCol+1,self.col):
                    if feld[self.row][i] != None:
                        return False

        else:
            if self.col == otherCol:
                if self.row < otherRow:
                    for i in range(self.row+1,otherRow):
                        if feld[i][self.col] != None:
                            return False
                else:
                    for i in range(otherRow+1,self.row):
                        if feld[i][self.col] != None:
                            return False

        if feld[otherRow][otherCol] == None or (feld[self.row][self.col].farbe != feld[otherRow][otherCol].farbe):
            return True
        return False


    def canMove_sameColor(self, otherRow,otherCol, feld):
        if(self.row == otherRow and self.col == otherCol):
            return False

        if self.row != otherRow and self.col != otherCol:
            return False
        if self.row == otherRow:
            if self.col < otherCol:
                for i in range(self.col+1,otherCol):
                    if feld[self.row][i] != None:
                        return False
            else:
                for i in range(otherCol+1,self.col):
                    if feld[self.row][i] != None:
                        return False

        else:
            if self.col == otherCol:
                if self.row < otherRow:
                    for i in range(self.row+1,otherRow):
                        if feld[i][self.col] != None:
                            return False
                else:
                    for i in range(otherRow+1,self.row):
                        if feld[i][self.col] != None:
                            return False
        return True

    def move(self, newRow, newCol):
        self.row = newRow
        self.col = newCol

    def print(self):
        if self.farbe == 'w':
            return u'\u2656'
        else:
            return '\u265C'

    def getMoveableFields(self, feld):
        list = []
        for i in range(8):
            for k in range(8):
               # print(str(i) + " "+str(k))
                if(self.canMove(i,k,feld)):
                    list.append((i,k))

        return list

    def getMoveableFields_sameColor(self, feld):
        list = []
        for i in range(8):
            for k in range(8):
               # print(str(i) + " "+str(k))
                if(self.canMove_sameColor(i,k,feld)):
                    if feld[i][k]!= None and feld[i][k].id =='k' and feld[i][k].farbe == self.farbe:
                        continue
                    list.append((i,k))
        return list

    def getMoveableFields_filter(self, feld):
        list = []
        for i in range(8):
            for k in range(8):
               # print(str(i) + " "+str(k))
                if(self.canMove(i,k,feld) and feld[i][k] != None):
                    list.append((i,k))
        return list