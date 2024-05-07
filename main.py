import brett
import com
import gui
import tkinter as tk
#from PyQt6.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

import monteCarlo

counter = 0
chars = ["A", "B", "C", "D", "E", "F", "G", "H"]
ints = ["1","2","3","4","5","6","7","8",]


def check(feld,input):
    if len(input) != 2:
        return -1
    from_row = -1
    from_col = -1
    for i in range(len(chars)):
        if input[0].upper() == chars[i]:
            from_row = i
    for i in range(len(chars)):
        if input[1] == ints[i]:
            from_col = i
    if from_row == -1 or from_col == -1:
        return -1
    from_col = int(input[1]) -1
    if from_col < 0 or from_col > 8:
        return -1
    if feld.feld[from_row][from_col] == None:
        print("select a valid field")
        return -1
    if feld.getColorOfField(from_row,from_col) == 'w':
        print("select your stones!")
        return -1

    return (from_row,from_col)


def check_dest(input,possibleDest):
    if len(input) != 2:
        return -1
    to_row = to_col= -1
    for i in range(len(chars)):
        if input[0].upper() == chars[i]:
            to_row = i
    for i in range(len(chars)):
        if input[1] == ints[i]:
            to_col = i

    if to_row == -1 or to_col == -1:
        return -1
    to_col = int(input[1]) -1
    if to_col < 0 or to_col > 8:
        return -1
    if not possibleDest.__contains__((to_row,to_col)):
        print("select a valid destination")
        return -1

    return (to_row, to_col)

def print_dest(possible_dest):
    for row,col in possible_dest:
        print((chars[row],col+1) , end = " ")
    print()


if __name__ == '__main__':
    #toDo: schau ob koenig im Schach steht, wenn ja ist NUR der Zug raus aus dem Schach moeglich
    #toDo: idee fuer Grafik: wenn schwarz dran ist und auf weiss geklickt wird, reagiere nicht. Analog zu schwarz
    feld = brett.brett()
    feld_copy = feld.copy(feld.feld)
    computer = com.computer()
    #computer = monteCarlo.monteCarloSimulation(100000)

    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    #app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    #window = QWidget()
    #window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    #app.exec()

    root = tk.Tk()
    schach_gui = gui.SchachGUI(root)
    root.mainloop()

    while(True):

        feld.print()


        if counter % 2 == 0:
            #schwarz ist dran


            start = input("from: ")
            if start == 'z':
                feld.setField(feld_copy)
                continue
            temp = check(feld,start)
            if temp == -1:
                print("wrong input format")
                continue
            from_row,from_col = temp
            possible_dest = feld.getMoves(from_row, from_col)
            print_dest(possible_dest)
            dest = input("to ")
            temp = check_dest(dest,possible_dest)
            if temp == -1:
                print("wrong input format")
                continue
            to_row,to_col = temp
            feld_copy = feld.copy(feld.feld)
            feld.move(from_row,from_col,to_row, to_col)
            if feld.canBeatKing("w"):
                print("schach, nicht möglich!")
                feld.setField(feld_copy)
                continue
            counter += 1
        else:
            #weiss ist dran
            _,temp = computer.start(feld, 'w' , 100)
            #temp = computer.start(feld,'w',len(feld.feld),len(feld.feld),2)
            (fr_row,fr_col),(t_row,t_col) = temp
            #fr_row,fr_col,t_row,t_col = temp
            print("from: "+str(chars[fr_row])+str(fr_col+1))
            print("from: "+str(chars[t_row])+str(t_col+1))
            feld.move(fr_row , fr_col , t_row , t_col)
            counter += 1
            # if feld.getColorOfField(int(start[0]), int(start[1])) == 's':
            #     print("turn of white")
            #     continue


        # print(feld.getMoves(int(start[0]), int(start[1])))
        # dest = input("to ")
        # feld.move(int(start[0]),int(start[1]),int(dest[0]),int(dest[1]))
        # counter+=1
