import figur

class springer:

    def __init__(self, row, col, farbe):
        self.row = row
        self.col = col
        self.farbe = farbe
        #self.wertung = 4
        self.wertung = 6
        self.id = 's'
        self.o_notaion = 8

    def canMove(self, otherRow, otherCol, feld):
        if feld[otherRow][otherCol] != None and feld[otherRow][otherCol].farbe == self.farbe:
            return False


        #eins unten, 2 rechsts
        if otherRow - self.row == 1 and otherCol - self.col == 2:
            return True
        #eins unten 2 links
        if otherRow - self.row == 1 and self.col - otherCol == 2:
            return True
        #2 unten, 1 links
        if otherRow - self.row == 2 and self.col - otherCol == 1:
            return True
        #2 unten, 1 rechts
        if otherRow - self.row == 2 and otherCol - self.col == 1:
            return True

            # eins oben, 2 rechsts
        if otherRow - self.row == -1 and otherCol - self.col == 2:
            return True
            # eins oben 2 links
        if otherRow - self.row == -1 and self.col - otherCol == 2:
            return True
            #2 oben, 1 links
        if otherRow - self.row == -2 and self.col - otherCol == 1:
            return True
            #2 oben, 1 rechts
        if otherRow - self.row == -2 and otherCol - self.col == 1:
            return True


    def canMove_sameColor(self, otherRow, otherCol, feld):

        #eins unten, 2 rechsts
        if otherRow - self.row == 1 and otherCol - self.col == 2:
            return True
        #eins unten 2 links
        if otherRow - self.row == 1 and self.col - otherCol == 2:
            return True
        #2 unten, 1 links
        if otherRow - self.row == 2 and self.col - otherCol == 1:
            return True
        #2 unten, 1 rechts
        if otherRow - self.row == 2 and otherCol - self.col == 1:
            return True

            # eins oben, 2 rechsts
        if otherRow - self.row == -1 and otherCol - self.col == 2:
            return True
            # eins oben 2 links
        if otherRow - self.row == -1 and self.col - otherCol == 2:
            return True
            #2 oben, 1 links
        if otherRow - self.row == -2 and self.col - otherCol == 1:
            return True
            #2 oben, 1 rechts
        if otherRow - self.row == -2 and otherCol - self.col == 1:
            return True

    def move(self, newRow, newCol):
        self.row = newRow
        self.col = newCol

    def print(self):
        if self.farbe == 'w':
            return u'\u2658'
        else:
            return'\u265E'

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