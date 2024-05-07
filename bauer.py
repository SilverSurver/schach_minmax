import figur
import konig

class bauer:
    def __init__(self, row,col,farbe):
        self.row = row
        self.col = col
        self.farbe = farbe
        self.k = konig.konig(row,col,farbe)
        #self.wertung = 3
        self.wertung = 4
        self.id = 'b'
        self.o_notaion = 2


    def canMove(self, otherRow,otherCol, feld):
        if(otherRow < 0 or otherRow > 7 or otherCol <0 or otherCol > 7):
            return False

        if self.farbe == 's':
            if self.col == otherCol and self.row+1 == otherRow and feld[otherRow][otherCol] == None:
                return True
            if self.col+1 == otherCol and self.row+1 == otherRow and feld[otherRow][otherCol] != None and feld[otherRow][otherCol].farbe != self.farbe:
                return True
            if self.col-1 == otherCol and self.row+1 == otherRow and feld[otherRow][otherCol] != None and feld[otherRow][otherCol].farbe != self.farbe:
                return True
            if self.col == otherCol and self.row +2 == otherRow and self.row == 1 and feld[otherRow][otherCol] == None:
                return True

        if self.farbe == 'w':
            if self.col == otherCol and self.row-1 == otherRow and feld[otherRow][otherCol] == None:
                return True
            if self.col-1 == otherCol and self.row-1 == otherRow and feld[otherRow][otherCol] != None and feld[otherRow][otherCol].farbe != self.farbe:
                return True
            if self.col+1 == otherCol and self.row-1 == otherRow and feld[otherRow][otherCol] != None and feld[otherRow][otherCol].farbe != self.farbe:
                return True
            if self.col == otherCol and self.row -2 == otherRow and self.row == 6 and feld[otherRow][otherCol] == None:
                return True

        return False

    def canMove_sameColor(self, otherRow,otherCol, feld):
        if(otherRow < 0 or otherRow > 7 or otherCol <0 or otherCol > 7):
            return False

        if self.farbe == 's':
            if self.col == otherCol and self.row+1 == otherRow and feld[otherRow][otherCol] == None:
                return True
            if self.col+1 == otherCol and self.row+1 == otherRow and feld[otherRow][otherCol] != None:
                return True
            if self.col-1 == otherCol and self.row+1 == otherRow and feld[otherRow][otherCol] != None:
                return True
            if self.col == otherCol and self.row +2 == otherRow and self.row == 1 and feld[otherRow][otherCol] == None:
                return True

        if self.farbe == 'w':
            if self.col == otherCol and self.row-1 == otherRow and feld[otherRow][otherCol] == None:
                return True
            if self.col-1 == otherCol and self.row-1 == otherRow and feld[otherRow][otherCol] != None:
                return True
            if self.col+1 == otherCol and self.row-1 == otherRow and feld[otherRow][otherCol] != None:
                return True
            if self.col == otherCol and self.row -2 == otherRow and self.row == 6 and feld[otherRow][otherCol] == None:
                return True

        return False

    def move(self, newRow, newCol):
        self.row = newRow
        self.col = newCol

    def print(self):
        if self.farbe == 'w':
            return u'\u2659'
        else:
            return'\u265F'

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

