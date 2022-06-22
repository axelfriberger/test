
from tkinter import *
from txt_file import *
#test

class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry = ("1200x800")
        self.root.resizable = (False, False)

        self.canvas = Canvas(self.root, width=1200, height=800, bg="#2C2F33")
        self.canvas.pack()
        
        self.img_a = PhotoImage(file="image_file/A.png").zoom(2).subsample(7)
        self.img_b = PhotoImage(file="image_file/B.png").zoom(2).subsample(7)
        self.img_c = PhotoImage(file="image_file/C.png").zoom(10).subsample(19)
        self.img_d = PhotoImage(file="image_file/D.png").zoom(2).subsample(7)
        self.img_e = PhotoImage(file="image_file/E.png").zoom(2).subsample(7)
        self.img_f = PhotoImage(file="image_file/F.png").zoom(8).subsample(15)
        self.img_g = PhotoImage(file="image_file/G.png").zoom(2).subsample(7)
        self.img_h = PhotoImage(file="image_file/H.png").zoom(2).subsample(7)
        self.img_i = PhotoImage(file="image_file/I.png").zoom(2).subsample(7)
        self.img_j = PhotoImage(file="image_file/J.png").zoom(4).subsample(7)
        self.img_k = PhotoImage(file="image_file/K.png").zoom(2).subsample(7)
        self.img_l = PhotoImage(file="image_file/L.png").zoom(2).subsample(7)
        self.img_m = PhotoImage(file="image_file/M.png").zoom(2).subsample(7)
        self.img_n = PhotoImage(file="image_file/N.png").zoom(2).subsample(7)
        self.img_o = PhotoImage(file="image_file/O.png").zoom(2).subsample(7)
        self.img_p = PhotoImage(file="image_file/P.png").zoom(2).subsample(7)
        self.img_r = PhotoImage(file="image_file/R.png").zoom(2).subsample(7)
        self.img_s = PhotoImage(file="image_file/S.png").zoom(2).subsample(7)
        self.img_t = PhotoImage(file="image_file/T.png").zoom(2).subsample(7)
        self.img_u = PhotoImage(file="image_file/U.png").zoom(2).subsample(7)
        self.img_v = PhotoImage(file="image_file/V.png").zoom(2).subsample(7)
        self.img_x = PhotoImage(file="image_file/X.png").zoom(2).subsample(7)
        self.img_y = PhotoImage(file="image_file/Y.png").zoom(2).subsample(7)
        self.img_z = PhotoImage(file="image_file/Z.png").zoom(4).subsample(7)
        self.img_å = PhotoImage(file="image_file/Å.png").zoom(4).subsample(7)
        self.img_ä = PhotoImage(file="image_file/Ä.png").zoom(2).subsample(7)
        self.img_ö = PhotoImage(file="image_file/Ö.png").zoom(2).subsample(7)
        self.img_blank = PhotoImage(file="image_file/_blank.png").zoom(2).subsample(7)
        self.img_board = PhotoImage(file="image_file/_board.png").zoom(3).subsample(5)

        
        self.letter_value = {
            "a": 1, "b": 3, "c": 8, "d": 1, "e": 1, "f": 3, "g": 2, "h": 3, "i": 1, 
            "j": 7, "k": 3, "l": 2, "m": 3, "n": 1, "o": 2, "p": 4, "r": 1, "s": 1,
            "t": 1, "u": 4, "v": 3, "x": 8, "y": 7, "z": 8, "å": 4, "ä": 4, "ö": 4, "blank":0
            }

        # 1->DL, 2->TL, 3->DW, 4->TW
        self.value_map = [
                [2, 0, 0, 0, 4, 0, 0, 1, 0, 0, 4, 0, 0, 0, 2],
                [0, 1, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 1, 0],
                [0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0],
                [0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0],
                [4, 0, 0, 0, 3, 0, 1, 0, 1, 0, 3, 0, 0, 0, 4],
                [0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0],
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                [1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1],
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                [0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0],
                [4, 0, 0, 0, 3, 0, 1, 0, 1, 0, 3, 0, 0, 0, 4],
                [0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0],
                [0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0],
                [0, 1, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 1, 0],
                [2, 0, 0, 0, 4, 0, 0, 1, 0, 0, 4, 0, 0, 0, 2]
                ]
        
        self.alphabet = [chr(i+97) for i in range(26)]
        self.alphabet.remove("q")
        self.alphabet.remove("w")
        self.alphabet.append("å")
        self.alphabet.append("ä")
        self.alphabet.append("ö")
        self.alphabet.append("blank")

        self.letters_on_board = [["null" for i in range(15)] for i in range(15)]
        self.letters_on_hand = ["null" for i in range(7)]

    def draw_scene(self):
        self.board_widget = Label(self.canvas, image=self.img_board)
        self.a_widget = Label(self.canvas, image=self.img_a)
        self.b_widget = Label(self.canvas, image=self.img_b)
        self.c_widget = Label(self.canvas, image=self.img_c)
        self.d_widget = Label(self.canvas, image=self.img_d)
        self.e_widget = Label(self.canvas, image=self.img_e)
        self.f_widget = Label(self.canvas, image=self.img_f)
        self.g_widget = Label(self.canvas, image=self.img_g)
        self.h_widget = Label(self.canvas, image=self.img_h)
        self.i_widget = Label(self.canvas, image=self.img_i)
        self.j_widget = Label(self.canvas, image=self.img_j)
        self.k_widget = Label(self.canvas, image=self.img_k)
        self.l_widget = Label(self.canvas, image=self.img_l)
        self.m_widget = Label(self.canvas, image=self.img_m)
        self.n_widget = Label(self.canvas, image=self.img_n)
        self.o_widget = Label(self.canvas, image=self.img_o)
        self.p_widget = Label(self.canvas, image=self.img_p)
        self.r_widget = Label(self.canvas, image=self.img_r)
        self.s_widget = Label(self.canvas, image=self.img_s)
        self.t_widget = Label(self.canvas, image=self.img_t)
        self.u_widget = Label(self.canvas, image=self.img_u)
        self.v_widget = Label(self.canvas, image=self.img_v)
        self.x_widget = Label(self.canvas, image=self.img_x)
        self.y_widget = Label(self.canvas, image=self.img_y)
        self.z_widget = Label(self.canvas, image=self.img_z)
        self.å_widget = Label(self.canvas, image=self.img_å)
        self.ä_widget = Label(self.canvas, image=self.img_ä)
        self.ö_widget = Label(self.canvas, image=self.img_ö)
        self.blank_widget = Label(self.canvas, image=self.img_blank)

        
        self.letters = {
            "a":[self.a_widget], "b":[self.b_widget], "c":[self.c_widget], "d":[self.d_widget], 
            "e":[self.e_widget], "f":[self.f_widget], "g":[self.g_widget], "h":[self.h_widget], 
            "i":[self.i_widget], "j":[self.j_widget], "k":[self.k_widget], "l":[self.l_widget], 
            "m":[self.m_widget], "n":[self.n_widget], "o":[self.o_widget], "p":[self.p_widget], 
            "r":[self.r_widget], "s":[self.s_widget], "t":[self.t_widget], "u":[self.u_widget], 
            "v":[self.v_widget], "x":[self.x_widget], "y":[self.y_widget], "z":[self.z_widget], 
            "å":[self.å_widget], "ä":[self.ä_widget], "ö":[self.ö_widget], "blank":[self.blank_widget]}
        
        self.letters_keys = list(self.letters)
        self.letters_values = list(self.letters.values())
        
        def find_index_for_letters(target):
            for lst in self.letters_values:
                if target in lst:
                    return self.letters_values.index(lst)

        self.board_widget.place(x=450, y=40)
        
        def draw_alphabet_background():
            color = "#145000"
            x0 = 30
            y0 = 30
            x1 = 395
            y1 = 215
            r = 30
            self.canvas.create_oval(x0,y0, x0+r, y0+r, fill=color, outline="")
            self.canvas.create_oval(x1-r,y0, x1, y0+r, fill=color, outline="")
            self.canvas.create_oval(x0,y1, x0+r, y1+r, fill=color, outline="")
            self.canvas.create_oval(x1-r,y1, x1, y1+r, fill=color, outline="")
            self.canvas.create_rectangle(x0+r/2, y0, x1-r/2, y1+r, fill=color, outline="")
            self.canvas.create_rectangle(x0, y0+r/2, x1, y1+r/2, fill=color, outline="")
        draw_alphabet_background()


        def draw_hand():
            color_bg = "#145000"
            x0 = 30
            y0 = 300
            x1 = 395
            y1 = 340
            r = 30
            self.canvas.create_oval(x0, y0, x0+r, y0+r, fill=color_bg, outline="")
            self.canvas.create_oval(x1-r, y0, x1, y0+r, fill=color_bg, outline="")
            self.canvas.create_oval(x0, y1, x0+r, y1+r, fill=color_bg, outline="")
            self.canvas.create_oval(x1-r, y1, x1, y1+r, fill=color_bg, outline="")
            self.canvas.create_rectangle(x0+r/2, y0, x1-r/2, y1+r, fill=color_bg, outline="")
            self.canvas.create_rectangle(x0, y0+r/2, x1, y1+r/2, fill=color_bg, outline="")
            
            color_drop = "#767676"
            x2=40
            y2=312.5
            x3=80
            y3=342.5
            r1=10
            for i in range(7):
                self.canvas.create_oval(x2+50*i, y2, (x2+r1)+50*i, y2+r1, fill=color_drop, outline="black", width=2)
                self.canvas.create_oval((x3-r1)+50*i, y2, x3+50*i, y2+r1, fill=color_drop, outline="black", width=2)
                self.canvas.create_oval(x2+50*i, y3, (x2+r1)+50*i, y3+r1, fill=color_drop, outline="black", width=2)
                self.canvas.create_oval((x3-r1)+50*i, y3, x3+50*i, y3+r1, fill=color_drop, outline="black", width=2)
                self.canvas.create_rectangle((x2+r1/2)+50*i, y2, (x3-r1/2)+50*i, y3+r1, fill=color_drop, outline="")
                self.canvas.create_rectangle(x2+50*i, y2+r1/2, x3+50*i, y3+r1/2, fill=color_drop, outline="")
        draw_hand()


        def coord_alphabet(letter):
            if self.alphabet.index(letter) < len(self.alphabet)/4:
                y_coord = 0
            elif self.alphabet.index(letter) < 2*len(self.alphabet)/4:
                y_coord = 1
            elif self.alphabet.index(letter) < 3*len(self.alphabet)/4:
                y_coord = 2
            else:
                y_coord = 3
            
            if self.alphabet.index(letter)<len(self.alphabet)/4:
                x_coord = self.alphabet.index(letter)
            elif self.alphabet.index(letter)<2*len(self.alphabet)/4:
                x_coord = self.alphabet.index(letter)-len(self.alphabet)/4
            elif self.alphabet.index(letter)<3*len(self.alphabet)/4:
                x_coord = self.alphabet.index(letter)-2*len(self.alphabet)/4
            else:
                x_coord = self.alphabet.index(letter)-3*len(self.alphabet)/4
            return 40+50*x_coord, 40+50*y_coord


        def get_coord_for_click(x, y):
            if 40 < x < 340 and 40 < y < 200:
                for i in range(7):
                    for j in range(4):
                        if 40+50*i < x < 80+50*i and 40+50*j < y < 80+50*j:
                            return 40+50*i, 40+50*j

            if 40 < x < 390 and 310 < y < 340:
                for i in range(7):
                    if 40+50*i < x < 80+50*i:
                        return 40+50*i, 310, "h"

            if 450 < x and 40 < y:
                for i in range(15):
                    for j in range(15):
                        if 450+45.6*i < x < 500+45.6*i and 40+46*j < y < 86+46*j:
                            return 450+45.6*i, 40+45.6*j, "b"
            else:
                return

        def draw_alphabet():
            for lst in self.letters_values:
                for widget in lst:
                    widget.place(x=coord_alphabet(self.letters_keys[find_index_for_letters(widget)])[0], y=coord_alphabet(self.letters_keys[find_index_for_letters(widget)])[1])
        draw_alphabet()
        
        def clone(widget):
            parent = widget.nametowidget(widget.winfo_parent())
            cls = widget.__class__
            clone = cls(parent)
            for key in widget.configure():
                clone.configure({key: widget.cget(key)})
            return clone


        def drag_start(event):
            widget = event.widget
            widget.startX = event.x
            widget.startY = event.y
            widget_clone = clone(widget)
            widget_clone.place(x=coord_alphabet(self.letters_keys[find_index_for_letters(widget)])[0], y=coord_alphabet(self.letters_keys[find_index_for_letters(widget)])[1])
            widget.tkraise()
            self.letters[self.letters_keys[find_index_for_letters(widget)]].append(widget_clone)
           

        def drag_motion(event):
            widget = event.widget
            x = widget.winfo_x() - widget.startX + event.x
            y = widget.winfo_y() - widget.startY + event.y
            widget.place(x=x,y=y)


        def snap_to_pos(event):
            widget = event.widget

            x = widget.winfo_x() - widget.startX + event.x + 10
            y = widget.winfo_y() - widget.startY + event.y + 10

            try:
                x_stop = get_coord_for_click(x, y)[0]
                y_stop = get_coord_for_click(x, y)[1]
                area = get_coord_for_click(x, y)[2]
                widget.place(x=x_stop, y=y_stop)

                if area == "h":
                    self.letters_on_hand[round((x_stop-40)/50)] = self.letters_keys[find_index_for_letters(widget)] 

                elif area == "b":
                    self.letters_on_board[round((y_stop-40)/45.6)][round((x_stop-450)/45.6)] = self.letters_keys[find_index_for_letters(widget)] 
                
                bind_widgets()
                
            except:
                widget.place(x=coord_alphabet(self.letters_keys[find_index_for_letters(widget)])[0], y=coord_alphabet(self.letters_keys[find_index_for_letters(widget)])[1])
                bind_widgets()
        
            
        def bind_widgets():
            for lst in self.letters_values:
                for widget in lst:
                    widget.bind("<Button-1>", drag_start)
                    widget.bind("<B1-Motion>", drag_motion)
                    widget.bind("<ButtonRelease-1>", snap_to_pos)
        bind_widgets()


        def word_fits(word, letters3):
            letters_fixed = [letter7 for letter7 in letters3 if letter7 != "null"]
            word2 = [letter5 for letter5 in word] 
            try:
                for letter9 in word:
                    letters_fixed.remove(letter9)
                    word2.remove(letter9)
                if word2 == []:
                    return True
            except:
                return False


        def wordlist(self):
            with open("txt_file/svenska-ord.txt") as f:
                wordlist_unaltered = f.readlines()
            wordlist_altered = []
        
            for word in wordlist_unaltered:
                if len(word) > 15 or "q" in word or "w" in word or len(word) == 1 or " " in word:
                    None
                else:
                    wordlist_altered.append(word.strip())
            return wordlist_altered


        def is_horizontal(coord_x, coord_y):
            if self.letters_on_board[coord_y-1][coord_x] == "null" or self.letters_on_board[coord_y+1][coord_x] == "null":
                return coord_x, coord_y
            else:
                return coord_y, coord_x
        

        def is_on_corner(coord_x, coord_y):
            if self.letters_on_board[coord_y-1][coord_x] != "null" and self.letters_on_board[coord_y][coord_x-1] != "null":
                return True
            if self.letters_on_board[coord_y+1][coord_x] != "null" and self.letters_on_board[coord_y][coord_x+1] != "null":
                return True
            if self.letters_on_board[coord_y-1][coord_x] != "null" and self.letters_on_board[coord_y][coord_x+1] != "null":
                return True
            if self.letters_on_board[coord_y+1][coord_x] != "null" and self.letters_on_board[coord_y][coord_x-1] != "null":
                return True
            else:
                return False


        def find_best_word():
            best_word_value = 0
            best_word = ""
            label_word = Label(self.canvas, text=f"BEST WORD: {best_word}")
            label_value = Label(self.canvas, text=f"NUMBER OF POINTS: {best_word_value}")
            label_word.place(x=200, y=400)
            label_value.place(x=200, y=420)

            for coord_x in range(15):
                for coord_y in range(15):
                    anchor = self.letters_on_board[coord_x][coord_y]
                    if anchor != "null":
                        letters_used = [letter for letter in self.letters_on_hand]
                        letters_used.append(anchor)
                        
                        words_available = [word for word in wordlist(self) if word_fits(word, letters_used)]

                        for word in words_available:
                            if len(word) == 1:
                                words_available.remove(word)
                        
                        try:
                            copy_of_board = self.letters_on_board
                            for word in words_available:
                                letters_in_word = [letter for letter in word] 
                                index_of_letters = [letters_in_word.index(letter)-letters_in_word.index(anchor) for letter in letters_in_word]
                                word_value = [0, 1]
                                
                                if is_on_corner(coord_x, coord_y):
                                    pass

                                for letter in letters_in_word:
                                    letter_value = self.letter_value[letter]
                                    if self.value_map[coord_y][coord_x+index_of_letters[letters_in_word.index(letter)]] == 1:
                                        letter_value *= 2
                                    elif self.value_map[coord_y][coord_x+index_of_letters[letters_in_word.index(letter)]] == 2:
                                        letter_value *= 3
                                    elif self.value_map[coord_y][coord_x+index_of_letters[letters_in_word.index(letter)]] == 3:
                                        word_value[1] = 2
                                    elif self.value_map[coord_y][coord_x+index_of_letters[letters_in_word.index(letter)]] == 4:
                                        word_value[1] = 3
                                    word_value[0] += letter_value


                                word_value[0] *= word_value[1]
                                if word_value[0] >= best_word_value:
                                    best_word_value = word_value[0]
                                    best_word = word     
                        except:
                            pass   
                                                        
            label_word.config(text=f"BEST WORD: {best_word.upper()}")
            label_value.config(text=f"NUMBER OF POINTS: {best_word_value}")

        def draw_buttons():
            def done_button_command():
                self.root.destroy()
            done_button = Button(self.root, text="DONE", command=done_button_command)
            done_button.place(x=40, y=760)


            start_button = Button(self.canvas, text="START", command=find_best_word)
            start_button.place(x=40, y=400)
        draw_buttons()


    

def main():
    app = App()
    app.draw_scene()
    app.root.mainloop()
    

if __name__ == "__main__":
    main()

