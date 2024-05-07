import bauer
import turm
import laufer
import springer
import dame
import konig


class brett:
    def __init__(self):  #8x8 Feld
       self.feld = [[turm.turm(0,0,'s'), springer.springer(0,1,'s'),laufer.laufer(0,2,'s'), dame.dame(0,3,'s'),konig.konig(0,4,'s') , laufer.laufer(0,5,'s'), springer.springer(0,6,'s'),turm.turm(0,7,'s')] ,
                    [bauer.bauer(1,0,'s'), bauer.bauer(1,1,'s'), bauer.bauer(1,2,'s'), bauer.bauer(1,3,'s'), bauer.bauer(1,4,'s'), bauer.bauer(1,5,'s'), bauer.bauer(1,6,'s'), bauer.bauer(1,7,'s')],
                    [None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None],
                    [bauer.bauer(6,0,'w'), bauer.bauer(6,1,'w'), bauer.bauer(6,2,'w'), bauer.bauer(6,3,'w'), bauer.bauer(6,4,'w'), bauer.bauer(6,5,'w'), bauer.bauer(6,6,'w'), bauer.bauer(6,7,'w')],
                    [turm.turm(7,0,'w'), springer.springer(7,1,'w'), laufer.laufer(7,2,'w'),  dame.dame(7,3,'w'), konig.konig(7,4,'w'),  laufer.laufer(7,5,'w'),springer.springer(7,6,'w'), turm.turm(7,7,'w')]
                    ]




    def move(self,fromRow,fromCol,toRow,toCol):
        if(self.feld[fromRow][fromCol] != None and self.feld[fromRow][fromCol].canMove(toRow,toCol,self.feld)):
            self.feld[fromRow][fromCol].move(toRow, toCol)
            self.feld[toRow][toCol] = self.feld[fromRow][fromCol]
            self.feld[fromRow][fromCol] = None


    def set_field(self,row,col,obj):
        self.feld[row][col] = obj


    def reset(self,row_from,col_from,row_to,col_to,cop,piece):
        self.set_field(row_from, col_from, piece)
        self.set_field(row_to, col_to, cop)
        piece.move(row_from,col_from)

    def getMoves(self, fromRow, fromCol):

        if self.feld[fromRow][fromCol] == None:
            return None
        piece = self.feld[fromRow][fromCol]
        farbe = piece.farbe
        possible_destinations = piece.getMoveableFields(self.feld)
        final_destinations = []
        for to_row,to_col in possible_destinations:
            cop = self.feld[to_row][to_col]
            self.move(fromRow,fromCol, to_row,to_col)
            if not self.canBeatKing('w' if farbe == 's' else 's'):
                final_destinations.append((to_row,to_col))
            self.reset(fromRow,fromCol,to_row,to_col,cop,piece)
        return final_destinations

    def getBlackKing(self):
        for i in range(8):
            for k in range(8):
                if self.feld[i][k] != None and self.feld[i][k].print() == '\u265A':
                    return (i,k)
        return (-1,-1)

    def getWhiteKing(self):
        for i in range(8):
            for k in range(8):
                if self.feld[i][k] != None and self.feld[i][k].print() == u'\u2654':
                    return (i,k)
        return (-1,-1)


    def getAllPositionsOfColor_movable(self,farbe,feld):
        positions=[]
        for i in range(8):
            for k in range(8):
                piece = self.feld[i][k]
                if piece != None and piece.farbe == farbe and len(piece.getMoveableFields(feld))>0:
                    positions.append((piece,i,k))
        return positions

    def getAllPositions(self):
        positions=[]
        for i in range(8):
            for k in range(8):
                piece = self.feld[i][k]
                if piece != None:
                    positions.append((piece,i,k))
        return positions

    def getAllPositionsOfColor(self,farbe):
        positions=[]
        for i in range(8):
            for k in range(8):
                piece = self.feld[i][k]
                if piece != None and piece.farbe == farbe:
                    positions.append((piece,i,k))
        return positions


    def getAllMovableFielsOfColor_same(self,farbe):
        positions = self.getAllPositionsOfColor(farbe)
        movable = []
        for _,row,col in positions:
            movable+=self.feld[row][col].getMoveableFields_sameColor(self.feld)
        return movable


    def getAllMovableFielsOfColor(self,farbe):
        #positions = self.getAllPositionsOfColor(farbe)
        movable = []
        for row in range(8):
            for col in range(8):
                current_field = self.feld[row][col]
                if current_field == None or current_field.farbe != farbe:
                    continue
                movable+=current_field.getMoveableFields(self.feld)
        return movable


    def getAllMovableFielsOfColor_with_rowfrom_colfrom(self,farbe):
        #positions = self.getAllPositionsOfColor(farbe)
        movable = []
        for row in range(8):
            for col in range(8):
                current_field = self.feld[row][col]
                if current_field == None or current_field.farbe != farbe:
                    continue
                temp = current_field.getMoveableFields(self.feld)
                for to_r,to_c in temp:
                    movable.append((row,col,to_r,to_c))
        return movable


    def movableFielsSameColorAuswerung(self,farbe):
        auswertung = 0
        for row in range(8):
            for col in range(8):
                current_filed = self.feld[row][col]
                if current_filed == None or current_filed.farbe != farbe:
                    continue
                for row_to in range(8):
                    for col_to in range(8):
                        if current_filed.canMove(row_to,col_to,self.feld):
                            to_field = self.feld[row_to][col_to]
                            if to_field != None:
                                if to_field.farbe == farbe:  # andere Figuren decken
                                    #auswertung += (to_field.wertung ** 2 - to_field.wertung)
                                    auswertung += (to_field.wertung -2)
                                else:
                                    #auswertung += (to_field.wertung ** 2)
                                    auswertung += to_field.wertung
                            else:
                                #auswertung += 4
                                auswertung += 1

        return auswertung




    def getColorOfField(self, row,col):
        if self.feld[row][col] == None:
            return None
        return self.feld[row][col].farbe
    def copy(self, feld):
        ret = []
        for i in range(len(feld)):
            ret.append([])
            for k in range(len(feld[i])):
                ret[i].append(feld[i][k])
                if ret[i][k] != None:
                    ret[i][k].move(i,k)
        return ret

    def setField(self, field):
        self.feld = self.copy(field)

    def print(self):
        chars = ["A","B","C","D","E","F","G","H"]
        print("       1      2      3      4      5      6      7      8")
        print("   ---------------------------------------------------------")
        for row in range(8):
            print(chars[row]+" ",end=" ")
            for col in range(8):
                if(self.feld[row][col] == None):
                    print("|     ",end=" ")


                else:
                    print("|  "+self.feld[row][col].print()+"  ", end = " ")

            print("|\n   ---------------------------------------------------------")


    def to_string(self):
        chars = ["A","B","C","D","E","F","G","H"]
        returning = ""
        returning+=("       1      2      3      4      5      6      7      8\n")
        returning+=("   ---------------------------------------------------------\n")
        for row in range(8):
            returning+=(chars[row]+" ")
            for col in range(8):
                if(self.feld[row][col] == None):
                    returning+=("|      ")


                else:
                    returning +=("|  "+self.feld[row][col].print()+"   ")

            returning+=("|\n   ---------------------------------------------------------\n")
        return returning


    def canBeatKing(self,farbe):
        positions=[]
        if farbe == 'w':
            kingPos = self.getBlackKing()
        else:
            kingPos = self.getWhiteKing()
        for i in range(8):
            for k in range(8):
                piece = self.feld[i][k]
                if piece != None and piece.farbe == farbe and piece.canMove(kingPos[0],kingPos[1],self.feld):
                    return True
        return False




    def fitness(self):
        fit = 0
        for i in range(8):
            for k in range(8):
                piece = self.feld[i][k]
                if piece != None and piece.farbe == 'w':
                    fit+=piece.wertung
                elif piece!= None and piece.farbe == 's':
                    fit-=piece.wertung

        return fit



    def safe(self,farbe):
        andere_farbe = 'w' if farbe == 's' else 's'
        movableFields_andere_farbe = self.getAllMovableFielsOfColor(andere_farbe)   # wenn kein anderer Spieler auf das Feld ziehen kann
        movableFields_farbe_same_color = self.getAllMovableFielsOfColor_same(farbe)  # wenn ein eigener Spieler auf das Feld ziehen kann (schuetzen)
        positions = self.getAllPositions()

        auswertung = 1

        for _,i,k in positions:
            if self.feld[i][k].farbe == farbe:
                safe = True
                max = -1
                for row,col in movableFields_andere_farbe:
                    if i == row and k == col: # anderer Spieler kann auch drauf
                        safe = False
                        if self.feld[row][col].wertung > max:
                            max = self.feld[row][col].wertung
                if safe:
                    auswertung+=self.feld[i][k].wertung
                else:
                    if self.feld[i][k].wertung == 100:
                        return 0
                    for row,col in movableFields_farbe_same_color:
                        if i == row and k == col: # mein Spieler kann auch drauf
                            safe = True
                if safe:
                    if max >= self.feld[i][k].wertung: # bedrohende Figur hat eine größere Wertung oder gleiche
                        auswertung+=self.feld[i][k].wertung
                    #else:
                    #    auswertung+=(max-self.feld[i][k].wertung)
        return auswertung



    def movableFieldsAuswertung(self,farbe):
        movableFields = self.getAllMovableFielsOfColor(farbe)
        auswertung = 0
        for row,col in movableFields:
            if self.feld[row][col] != None:
                #if self.feld[row][col].farbe == farbe:      #andere Figuren decken
                #    auswertung+=(self.feld[row][col].wertung -1)
                #else:
                auswertung+=self.feld[row][col].wertung
            else:
                auswertung+=2
        return auswertung

