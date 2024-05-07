class state:
    def __init__(self,feld,moves):
        self.feld = feld
        self.moves = moves
        self.average = 0



    def isqualto(self,state):
        return self.to_string() == state.to_string()


    def contains_move(self,move):
        for i in range(len(self.moves)):
            move_temp,grade = self.moves[i]
            if move_temp[0] == move[0] and move_temp[1] == move[1] and move_temp[2] == move[2] and move_temp[3] == move[3]:
                return (i,grade)
        return -1

    def update(self,move,grade):
        temp = self.remove(move)
        self.moves.append((move,grade+temp))
        self.average += grade


    def remove(self,move):
        for i in self.moves:
            if i[0][0] == move[0] and i[0][1] == move[1] and i[0][2] == move[2] and i[0][3] == move[3]:
                temp = i[1]
                self.moves.remove(i)
                return temp
        return 0


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