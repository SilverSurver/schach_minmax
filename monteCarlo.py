import random
import state


class monteCarloSimulation:

    def __init__(self,games):
        self.games = games


    def check(self,brett,farbe,row,col):
        return brett.feld[row][col] is not None and brett.feld[row][col].farbe == farbe and \
                len(brett.feld[row][col].getMoveableFields(brett.feld)) > 0

    def doRandomMove(self,brett,farbe,n,m,bretter,tiefe):
        #brett ist nxm, n nach unten, m nach rechts
        wk = brett.getWhiteKing()
        bk = brett.getBlackKing()
        if farbe == 'w' and brett.canBeatKing(farbe):
            #print("white wins")
            return 1000000
        if farbe == 's' and brett.canBeatKing(farbe):
            #print("white loses")
            return -1000000

        if tiefe == 0:
            return brett.fitness()
        positions = brett.getAllPositionsOfColor_movable(farbe, brett.feld)
        if len(positions) == 0:
            return 0
        if len(positions) > 1:
            _, rand_row, rand_col = positions[random.randint(0, len(positions) - 1)]
        else:
            _, rand_row, rand_col = positions[0]
        movable = brett.feld[rand_row][rand_col].getMoveableFields(brett.feld)
        rand_to = movable[random.randint(0, len(movable) - 1)]
        copy = self.copy(brett.feld)
        move = (rand_row, rand_col, rand_to[0], rand_to[1])
        brett.move(rand_row, rand_col, rand_to[0], rand_to[1])
        result = self.doRandomMove(brett, 'w' if farbe == 's' else 's', n,m,bretter,tiefe-1)
        brett.setField(copy)
        temp = self.contains_brett(bretter, brett)
        if temp == -1:
            bretter.append(state.state(self.copy(brett.feld), [(move, result)]))
            return result
        else:
            bretter[temp].update(move, result)
            return bretter[temp].average


    def start(self,brett,farbe,n,m,tiefe):
        bretter = []
        for counter in range(self.games):

            positions = brett.getAllPositionsOfColor_movable(farbe,brett.feld)
            _, rand_row, rand_col = positions[random.randint(0, len(positions) - 1)]
            movable = brett.feld[rand_row][rand_col].getMoveableFields(brett.feld)
            rand_to = movable[random.randint(0, len(movable) -1)]
            copy = self.copy(brett.feld)
            move = (rand_row, rand_col, rand_to[0], rand_to[1])
            brett.move(rand_row, rand_col, rand_to[0], rand_to[1])
            result = self.doRandomMove(brett, 'w' if farbe == 's' else 's', n, m,bretter,tiefe-1)
            brett.setField(copy)
            temp = self.contains_brett(bretter,brett)
            if temp == -1:
                #print("here")
                bretter.append(state.state(self.copy(brett.feld), [(move,result)]))
            else:
                bretter[temp].update(move,result)
            #print(bretter[self.contains_brett(bretter,brett)].moves)
        moves = []
        for i in bretter:
            if i.to_string() == brett.to_string():
                moves = i.moves
        moves.sort(key= lambda a:a[-1],reverse=True)
        print(moves)
        return moves[0][0]





    def copy(self, feld):
        ret = []
        for i in range(len(feld)):
            ret.append([])
            for k in range(len(feld[i])):
                ret[i].append(feld[i][k])
        return ret

    def contains_brett(self,states,brett):
        for i in range(len(states)):
            state_temp = states[i]
            #print(state_temp.to_string())
            if state_temp.to_string() == brett.to_string():
                return i
        return -1

    def remove(self,moves,move):
        for i in moves:
            if i[0][0] == move[0] and i[0][1] == move[1] and i[0][2] == move[2] and i[0][3] == move[3]:
                moves.remove(i)
                return moves


