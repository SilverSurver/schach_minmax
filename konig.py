import math

import figur

class konig:

    def __init__(self, row, col, farbe):
        self.row = row
        self.col = col
        self.farbe = farbe
        #self.wertung = 7
        self.wertung = 13
        self.id = 'k'
        self.o_notaion = 8

    def canMove(self, otherRow, otherCol, feld):
        if feld[otherRow][otherCol] != None and feld[otherRow][otherCol].farbe == self.farbe:
            return False

        if abs(otherRow - self.row) <= 1 and abs(otherCol - self.col) <= 1:

            return True

        return False

    def move(self, newRow, newCol):
        self.row = newRow
        self.col = newCol

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col



    def canMove_sameColor(self, otherRow, otherCol, feld):

        if abs(otherRow - self.row) <= 1 and abs(otherCol - self.col) <= 1:
            return True

        return False


    def print(self):
        if self.farbe == 'w':
            return u'\u2654'
        else:
            return '\u265A'

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
                if(self.canMove(i,k,feld)):
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