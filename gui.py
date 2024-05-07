import tkinter as tk
import brett
import com

class SchachGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Schach")
        self.counter = 1
        self.erstelle_schachbrett()
        self.erstelle_figuren()
        self.last_labeles = []
        self.possible_dest= None
        self.my_figures = ["♜", "♞", "♝", "♛", "♚", "♟"]
        self.from_row = -1
        self.from_col = -1
        self.computer = com.computer()
        self.geschalgene_figuren_wertung = 0
        self.tiefe = 3
        self.schranke = 110

        self.feld = brett.brett()
        self.feld_copy = self.feld.copy(self.feld.feld)
        self.computer = com.computer()
        self.lookup_table = self.create_lookup_table()
        self.lookup_position_to_label = self.create_look_up_other_dir()
        print(self.lookup_table)

        # Variable zur Speicherung der ausgewählten Figur
        self.ausgewaehlt = None

    def get_key_by_value(self,value):
        for key,(row,col) in self.lookup_table.items():
            if row == value[0] and col == value[1]:
                return key
        return None

    def create_lookup_table(self):
        dict = {}
        index = 0
        for label in self.figuren_labels:
            dict[label] = ((index) // 8, (index) %8)
            index+=1
        return dict

    def create_look_up_other_dir(self):
        dict = {}
        for key,value in self.lookup_table.items():
            dict[value] = key
        return dict
    def erstelle_schachbrett(self):
        self.schachbrett = tk.Frame(self.root)
        self.schachbrett.pack()

        farben = ["white", "gray"]
        for i in range(8):
            for j in range(8):
                farbe = farben[(i + j) % 2]
                feld = tk.Frame(self.schachbrett, width=50, height=50, bg=farbe)
                feld.grid(row=i, column=j)
               # feld.bind("<Button-1>", self.feld_geklickt)

    def erstelle_figuren(self):
        self.figuren_labels = []
        figuren = [
            "♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜",
            "♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟",
            "    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ",
            "    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ",
            "    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ",
            "    ", "    ", "    ", "    ", "    ", "    ", "    ", "    ",
            "♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙",
            "♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"
        ]
        for index, figur in enumerate(figuren):
            row = index//8
            col = index % 8
            #label = tk.Label(self.schachbrett, text=figur, font=("Arial", 24))
            label = tk.Label(self.schachbrett, text=figur, font=("Arial", 24),bg="white" if (row +col ) % 2 == 0 else "gray")
            label.grid(row=row, column=col)
            label.bind("<Button-1>", self.figur_geklickt)
            self.figuren_labels.append(label)


# todo: nachdem blau markieren: bei self.ausgewahlt: checken ob valide angeklickt worden ist: wenn ja -> move durchführen und unmarkieren! + ich kann nur meine anklicken! (liste von meinen Figuren führen und falls Liste.contains(angeklickt[text]))
    def figur_geklickt(self, event):
        label = event.widget
        figur = label["text"]
        # Wenn bereits eine Figur ausgewählt wurde, ändere die Position
        if self.possible_dest != None:
            for dest in self.possible_dest + self.last_labeles:
                key_label = self.get_key_by_value(dest)
                key_label.config(bg="white" if (dest[0] + dest[1]) % 2 == 0 else "gray")
        self.last_labeles = []
        if self.ausgewaehlt and label != self.last_label and self.possible_dest != None and self.possible_dest.__contains__(self.lookup_table.get(label)) and not self.my_figures.__contains__(label["text"]):
            label["text"] = self.ausgewaehlt["text"]
            self.ausgewaehlt["text"] = "    "
            self.ausgewaehlt = None
            row,col = self.lookup_table[label]
            if self.feld.feld[row][col] != None:
                self.geschalgene_figuren_wertung += self.feld.feld[row][col].o_notaion
                print(self.geschalgene_figuren_wertung)
                if self.geschalgene_figuren_wertung > self.counter * self.schranke:
                    print("here")
                    self.tiefe+=1
                    self.counter+=1
            self.feld.move(self.from_row,self.from_col,row,col)
            self.root.update()
            _,temp = self.computer.start(self.feld, 'w' , self.tiefe)
            (fr_row,fr_col),(t_row,t_col) = temp
            if self.feld.feld[t_row][t_col] != None:
                self.geschalgene_figuren_wertung += self.feld.feld[row][col].o_notaion
                print(self.geschalgene_figuren_wertung)
                if self.geschalgene_figuren_wertung > self.counter * self.schranke:
                    print("here")
                    self.tiefe+=1
                    self.counter+=1
            self.feld.move(fr_row , fr_col , t_row , t_col)
            from_label = self.lookup_position_to_label[(fr_row,fr_col)]
            to_label = self.lookup_position_to_label[(t_row,t_col)]
            to_label["text"] = from_label["text"]
            from_label["text"] = "    "
            from_label.config(bg="blue")
            to_label.config(bg="blue")
            self.last_labeles.append((fr_row,fr_col))
            self.last_labeles.append((t_row,t_col))
            #self.possible_dest = None
        elif self.ausgewaehlt == None or self.my_figures.__contains__(label["text"]):
            if label["text"] != "    ":
                    self.last_label = label
                    self.ausgewaehlt = label
                    row,col = self.lookup_table.get(label)
                    self.from_row,self.from_col = row,col
                    self.possible_dest = self.feld.getMoves(row,col)
                    for dest in self.possible_dest:
                        key_label = self.get_key_by_value(dest)
                        key_label.config(bg = "blue")






