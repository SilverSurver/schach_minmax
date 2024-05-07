class computer:
    def __init__(self):
        pass



    def getValue(self , brett , farbe):
        counter = 0
        for i in range(len(brett)):
            for k in range(len(brett[i])):
                if brett[i][k] == None:
                    continue
                #print(brett[i][k].col)
                if brett[i][k].farbe == farbe:
                    counter+=brett[i][k].wertung
        return counter



    def bestMoveFarbe(self, feld , farbe , tiefe , moves , allMoves): # tiefe muss ungerade sein
        if tiefe == 0:
            #print(moves)
            moves.append(self.getValue(feld.feld, farbe) - self.getValue(feld.feld , 'w' if farbe == 's' else 's'))
            return allMoves
        brett = feld.feld
        for i in range(len(brett)):
            for k in range(len(brett[i])):
                figur = brett[i][k]
                if figur == None:
                    continue
                if figur.farbe == farbe:
                    possibleMoves = figur.getMoveableFields(brett)
                    for move in possibleMoves:
                        feld.move(i,k,move[0] , move[1])
                        moves.append(move)
                        return self.bestMoveAndereFarbe(feld, 's' if farbe == 'w' else 'w' , tiefe-1 , moves , allMoves)


    def bestMoveAndereFarbe(self, feld , farbe , tiefe , moves , allMoves):
        brett = feld.feld
        for i in range(len(brett)):
            for k in range(len(brett[i])):
                figur = brett[i][k]
                if figur == None:
                    continue
                if figur.farbe == farbe:
                    possibleMoves = figur.getMoveableFields(brett)
                    for move in possibleMoves:
                        feld.move(i, k, move[0], move[1])
                        moves.append(move)
                        return self.bestMoveFarbe(feld, 's' if farbe == 'w' else 'w' , tiefe-1, moves , allMoves)



    def simulation(self, feld, farbe, tiefe , moves):

        for i in range(len(feld.feld)):
            for k in range(len(feld.feld[i])):
                figur = feld.feld[i][k]
                if figur == None:
                    continue
                if figur.farbe == farbe:
                    #print(figur.getMoveableFields(feld.feld))
                    possibleMoves = figur.getMoveableFields(feld.feld)
                    #print(f"at {i} , {k}: {possibleMoves}")
                    #print(f"row: {figur.row} , col : {figur.col}")
                    for move in possibleMoves:
                        brettTemp = self.copy(feld.feld)
                        feld.move(i,k,move[0] , move[1])
                        moves.append([((i,k),move)])
                        #print(moves)
                        self.bestMoveAndereFarbe(feld, 'w' if farbe == 's' else 's' , tiefe-1 , moves[-1] , moves)
                        feld.setField(brettTemp)
        return moves

    def start(self, feld, farbe, tiefe):
        #brett = self.copy(feld.feld)
        moves = []
        temp = self.simulation(feld, farbe, tiefe , moves)
        #feld.setField(brett)
        moves.sort(key = lambda x:x[-1] , reverse= True)
        return (moves[0][0][0] , moves[0][0][1])



    def copy(self, feld):
        ret = []
        for i in range(len(feld)):
            ret.append([])
            for k in range(len(feld[i])):
                ret[i].append(feld[i][k])
        return ret

