import math
import random


class computer:
    def evaluateField(self, farbe, brett):
        #return 0
        andereFarbe = 'w' if farbe == 's' else 's'
        evaluation = evaluation_farbe = evaluation_andere_farbe = 0
        #positions = brett.getAllPositions()
        movable_fields = []
        feld = brett.feld


        # counter_meine = 0
        # counter_andere = 0
        #
        # for row_f in range(8):
        #     for col_f in range(8):
        #         piece = feld[row_f][col_f]
        #         if piece == None:
        #             continue
        #         if piece.farbe == farbe:
        #             counter_meine += piece.wertung
        #             for row_t in range(8):
        #                 for col_t in range(8):
        #                     if not piece.canMove(row_t,col_t,feld):
        #                         continue
        #                     other_piece = feld[row_t][col_t]
        #                     if other_piece == None or other_piece.farbe == farbe:
        #                         counter_meine += 1
        #                     else:
        #                         counter_meine += other_piece.wertung
        #                         counter_andere -= other_piece.wertung
        #         else:
        #             counter_andere += piece.wertung
        #             for row_t in range(8):
        #                 for col_t in range(8):
        #                     if not piece.canMove_sameColor(row_t,col_t,feld):
        #                         continue
        #                     other_piece = feld[row_t][col_t]
        #                     if other_piece == None or other_piece.farbe != farbe:
        #                         counter_andere += 1
        #                     else:
        #                         counter_andere += other_piece.wertung
        #                         counter_meine -= other_piece.wertung
        #
        # return counter_meine - counter_andere


        for i in range(8):
            for j in range(8):
                piece = feld[i][j]
                if piece == None:
                    continue
                if piece.farbe == farbe:
                    evaluation_farbe +=  piece.wertung**3
                    #evaluation_farbe += piece.wertung
                else:
                    evaluation_andere_farbe += piece.wertung**3
                    #evaluation_andere_farbe += piece.wertung


        evaluation_farbe *= brett.movableFielsSameColorAuswerung(farbe)
        evaluation_andere_farbe *= brett.movableFielsSameColorAuswerung('w' if farbe == 's' else 's')

        return evaluation_farbe - evaluation_andere_farbe


        # for i in range(len(feld)):
        #     for k in range(len(feld[i])):
        #         piece = feld[i][k]
        #         if piece == None:
        #             continue
        #         #movable = piece.getMoveableFields(feld)
        #         weight = 0
        #         for j in range(8):
        #             for q in range(8):
        #                 temp = feld[j][q]
        #                 if temp == None:
        #                     continue
        #                 weight += temp.wertung
        #             if piece.farbe == farbe:
        #                 evaluation += weight * piece.wertung
        #             else:
        #                 evaluation-=weight * piece.wertung
        #return evaluation


    def minmax(self,brett,farbe,tiefe,alpha,beta,maximizing):
        if tiefe == 0:
            return self.evaluateField(farbe, brett),None
        if maximizing:
            v = -math.inf
            move = None
            possible_moves = brett.getAllMovableFielsOfColor_with_rowfrom_colfrom('w')
            for row_from,col_from,row_to,col_to in possible_moves:
                cop = brett.feld[row_to][col_to]
                piece = brett.feld[row_from][col_from]
                brett.move(row_from, col_from, row_to, col_to)
                if brett.canBeatKing('w' if farbe == 's' else 's'):
                    brett.reset(row_from, col_from, row_to, col_to, cop, piece)
                    continue
                temp = self.minmax(brett, farbe, tiefe - 1, alpha, beta,False)
                brett.reset(row_from, col_from, row_to, col_to, cop, piece)
                if temp[0] > v:
                    v = temp[0]
                    move = ((row_from, col_from), (row_to, col_to))
                if v > alpha:
                    alpha = v
                if alpha >= beta:
                    return v, move
            return v, move
        else:
            v = math.inf
            move = None
            possible_moves = brett.getAllMovableFielsOfColor_with_rowfrom_colfrom('s')
            for row_from,col_from,row_to,col_to in possible_moves:
                cop = brett.feld[row_to][col_to]
                piece = brett.feld[row_from][col_from]
                brett.move(row_from, col_from, row_to, col_to)
                if brett.canBeatKing(farbe):
                    brett.reset(row_from, col_from, row_to, col_to, cop, piece)
                    continue
                temp = self.minmax(brett, farbe, tiefe - 1, alpha, beta,True)
                brett.reset(row_from, col_from, row_to, col_to, cop, piece)
                if temp[0] < v:
                    v = temp[0]
                    move = ((row_from, col_from), (row_to, col_to))
                if v < beta:
                    beta = v
                if beta <= alpha:
                    return v, move
            return v, move


    def maximize(self, brett, farbe, tiefe, alpha,beta):
        if tiefe == 0:
            return self.evaluateField(farbe, brett),None

        v = -math.inf
        move = None
        for row_from in range(8):
            for col_from in range(8):
                piece = brett.feld[row_from][col_from]
                if piece == None or piece.farbe != farbe:
                    continue
                for row_to in range(8):
                    for col_to in range(8):
                        if not piece.canMove(row_to,col_to,brett.feld):
                            continue
                        cop = brett.feld[row_to][col_to]
                        piece = brett.feld[row_from][col_from]
                        brett.move(row_from, col_from, row_to, col_to)
                        if brett.canBeatKing('w' if farbe == 's' else 's'):
                            brett.reset(row_from, col_from, row_to, col_to, cop, piece)
                            continue
                        temp = self.minimize(brett, farbe, tiefe - 1,alpha,beta)
                        brett.reset(row_from, col_from, row_to, col_to, cop,piece)
                        if temp[0] > v:
                            v = temp[0]
                            move = ((row_from,col_from),(row_to,col_to))
                        if v > alpha:
                            alpha = v
                        if alpha >= beta:
                            return v,move
        return v,move

    def minimize(self, brett, farbe, tiefe, alpha,beta):
        if tiefe == 0:
            return self.evaluateField(farbe, brett),None
        v = math.inf
        move = None
        for row_from in range(8):
            for col_from in range(8):
                piece = brett.feld[row_from][col_from]
                if piece == None or piece.farbe == farbe:
                    continue
                for row_to in range(8):
                    for col_to in range(8):
                        if not piece.canMove(row_to,col_to,brett.feld):
                            continue
                        cop = brett.feld[row_to][col_to]
                        brett.move(row_from, col_from, row_to, col_to)
                        if brett.canBeatKing(farbe):
                            brett.reset(row_from, col_from, row_to, col_to, cop, piece)
                            continue
                        temp = self.maximize(brett, farbe, tiefe - 1, alpha, beta)
                        brett.reset(row_from, col_from, row_to, col_to, cop,piece)
                        if temp[0] < v:
                            v = temp[0]
                            move = ((row_from, col_from), (row_to, col_to))
                        if v < beta:
                            beta = v
                        if beta <= alpha:
                            return v,move
        return v,move

    def start(self, brett, farbe, tiefe):
        #return self.minmax(brett,farbe,tiefe,-math.inf,math.inf,True)
        return self.minmax(brett,farbe,tiefe,-math.inf,math.inf,True)

    def copy(self, feld):
        ret = []
        for i in range(len(feld)):
            ret.append([])
            for k in range(len(feld[i])):
                ret[i].append(feld[i][k])
        return ret

    def getValue(self, brett, farbe):
        counter = 0
        for i in range(len(brett)):
            for k in range(len(brett[i])):
                if brett[i][k] == None:
                    continue
                # print(brett[i][k].col)
                if brett[i][k].farbe == farbe:
                    counter += brett[i][k].wertung
        return counter



