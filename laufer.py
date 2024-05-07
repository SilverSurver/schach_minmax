import figur

class laufer:

    def __init__(self, row, col, farbe):
        self.row = row
        self.col = col
        self.farbe = farbe
        #self.wertung = 4
        self.wertung = 6
        self.id = 'l'
        self.o_notaion = 13

    def canMove(self, otherRow,otherCol, feld):
        if(otherRow < 0 or otherRow > 7 or otherCol <0 or otherCol > 7):
            return False


        if feld[otherRow][otherCol] != None and feld[otherRow][otherCol].farbe == self.farbe:
            return False


        if abs(otherRow-self.row) != abs(otherCol-self.col):
            return False

        betrag = abs(otherRow-self.row)
        # fromRow > toRow and fromCol > toCol
        if self.row > otherRow and self.col > otherCol:
            for i in range(1 , betrag):
                if feld[self.row - i][self.col -i] != None:
                    return False
        # fromRow < toRow and fromCol < toCol
        if self.row < otherRow and self.col < otherCol:
            for i in range(1 , betrag):
                if feld[self.row + i][self.col +i] != None:
                    return False
        # fromRow > toRow and fromCol < toCol
        if self.row > otherRow and self.col < otherCol:
            for i in range(1 , betrag):
                if feld[self.row - i][self.col +i] != None:
                    return False
        # fromRow < toRow and fromCol > toCol
        if self.row < otherRow and self.col > otherCol:
            for i in range(1 , betrag):
                if feld[self.row + i][self.col -i] != None:
                    return False
        return True


    def canMove_sameColor(self, otherRow,otherCol, feld):
        if(otherRow < 0 or otherRow > 7 or otherCol <0 or otherCol > 7):
            return False

        if abs(otherRow-self.row) != abs(otherCol-self.col):
            return False

        betrag = abs(otherRow-self.row)
        # fromRow > toRow and fromCol > toCol
        if self.row > otherRow and self.col > otherCol:
            for i in range(1 , betrag):
                if feld[self.row - i][self.col -i] != None:
                    return False
        # fromRow < toRow and fromCol < toCol
        if self.row < otherRow and self.col < otherCol:
            for i in range(1 , betrag):
                if feld[self.row + i][self.col +i] != None:
                    return False
        # fromRow > toRow and fromCol < toCol
        if self.row > otherRow and self.col < otherCol:
            for i in range(1 , betrag):
                if feld[self.row - i][self.col +i] != None:
                    return False
        # fromRow < toRow and fromCol > toCol
        if self.row < otherRow and self.col > otherCol:
            for i in range(1 , betrag):
                if feld[self.row + i][self.col -i] != None:
                    return False
        return True

    def move(self, newRow, newCol):
        self.row = newRow
        self.col = newCol


    def print(self):
        if self.farbe == 'w':
            return u'\u2657'
        else:
            return'\u265D'

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
                    if feld[i][k]!= None and feld[i][k].id == 'k' and feld[i][k].farbe == self.farbe:
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