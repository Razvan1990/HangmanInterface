from reader import FileReader
import constants
from tkinter import *
import tkinter
import os
from PIL import Image, ImageTk
from tkinter import messagebox


class HangmanGame:

    def __init__(self):
        self.reader = FileReader(os.getcwd(), "words.txt")
        self.list_words = self.reader.read_file()
        self.word_chosen = self.reader.get_random_word(self.list_words)
        self.file_ico = "hangman.ico"
        self.file_png = "hanged.jpg"
        self.remaining_tries = 5
        self.dict_buttons = {}
        # logic to create list of letters
        self.list_letters = []
        for letter in self.word_chosen[0]:
            self.list_letters.append(letter)
        self.list_letters_final = [letter for letter in self.list_letters if letter != " "]

    def check_winner(self):
        # all letters completed
        if len(self.list_letters_final) == 0:
            messagebox.showinfo(title="WORD DISCOVERED", message="Congratulations, you discovered the word!!")
            correct_word_frame.place(x=90, y=20)
            # here we will put the correct word
            label_correct_word = Label(correct_word_frame, text=self.word_chosen[0], justify="center",
                                       font=("Helvetica", 19, "bold"),
                                       cursor="trek", fg="#4cd283", bg="#e8f0bb")
            label_correct_word.grid(row=0, column=0, padx=40)
            # make all buttons disabled to not continue
            for button in self.dict_buttons:
                self.dict_buttons[button]["state"] = tkinter.DISABLED
            return True
        else:
            return False

    def check_loser(self):
        # no tries left
        if self.remaining_tries == 0:
            messagebox.showinfo(title="YOU ARE HANGED",
                                message="Sorry, you are out of tries and HANGED. Please check the correct answer!!")
            # here we will put the correct word
            correct_word_frame.place(x=90, y=20)
            label_correct_word = Label(correct_word_frame, text=self.word_chosen[0], justify="center",
                                       font=("Helvetica", 19, "bold"),
                                       cursor="trek", fg="#4cd283", bg="#e8f0bb")
            label_correct_word.grid(row=0, column=0, padx=40)
            #put the hanged image
            hanged_image = ImageTk.PhotoImage(Image.open(self.file_png))
            hang_frame = Label(image=hanged_image)
            hang_frame.image = hanged_image
            hang_frame.place(x=650, y=150)
            # make all buttons disabled to not continue
            for button in self.dict_buttons:
                self.dict_buttons[button]["state"] = tkinter.DISABLED
            return True
        else:
            return False


    def replace_letter(self, letter, dict_labels):
        # check if letter is in word
        if letter in self.word_chosen[0]:
            for label in dict_labels:
                # check if we have the word in the label
                if letter in dict_labels[label]:
                    # now we need to  the replacement
                    chosen_label = label
                    # chosen_label["text"].delete(0, END)
                    chosen_label["text"] = letter
                    # make the button state green in this case
                    self.dict_buttons[letter]["bg"] = "#1ed450"
                    self.dict_buttons[letter]["state"] = tkinter.DISABLED
                    '''in order to know when everything is completed we need to make a logic to verify this
                    in this case maybe we can remove for the list the letter and at the last check if we have an emtpy list
                    '''
                    self.list_letters_final = [let for let in self.list_letters_final if let != letter]
                    # check if you won
            if self.check_winner():
                return
        else:
            # in this case we need to update the counter and make the button red
            self.remaining_tries -= 1
            label_tries["text"] = "TRIES LEFT: " + str(self.remaining_tries)
            messagebox.showinfo(title="LETTER NOT PRESENT",
                                message="The {} is not present in the word".format(letter), )
            self.dict_buttons[letter]["bg"] = "#a7133c"
            self.dict_buttons[letter]["state"] = tkinter.DISABLED
            if self.check_loser():
                return

    def create_main_gui(self):
        global correct_word
        global correct_word_frame
        global root
        global label_tries
        # global buttons to add function to them
        global buttonA
        global buttonB
        global buttonC
        global buttonD
        global buttonE
        global buttonF
        global buttonG
        global buttonH
        global buttonI
        global buttonJ
        global buttonK
        global buttonL
        global buttonM
        global buttonN
        global buttonO
        global buttonP
        global buttonR
        global buttonQ
        global buttonS
        global buttonT
        global buttonU
        global buttonV
        global buttonX
        global buttonY
        global buttonW
        global buttonZ

        # get list of words and create label words
        labels = []
        for i in range(0, len(self.word_chosen[0])):
            global_label = f"global_label{i + 1}"
            globals()[global_label] = f"Label_{i + 1}"
            labels.append(globals()[global_label])
        root = Tk()
        root.title("Hangman Game")
        root.iconbitmap(self.file_ico)
        root.geometry("900x700")
        root.resizable(NO, NO)
        root["bg"] = "#8bb6cc"

        # create a first frame in which we put the buttons
        frame_letters = LabelFrame(root, fg="#31322a", bg="#e8f0bb", font=("Helvetica", 25, "bold"), bd=5,
                                   cursor="target", width=550, height=350, labelanchor="n", text="LETTERS",
                                   relief=tkinter.GROOVE)
        frame_letters.place(x=90, y=150)
        word_frame = LabelFrame(root, fg="#31322a", bg="#e8f0bb", font=("Helvetica", 25, "bold"), bd=5,
                                cursor="target", width=800, height=100, labelanchor="n", text="GUESS THE WORD",
                                relief=tkinter.GROOVE)
        word_frame.place(x=60, y=550)
        dictionary_label_letter = {}
        x_initial = 0
        y_initial = 10
        for i in range(0, len(self.word_chosen[0])):
            if self.word_chosen[0][i] == " ":
                x_initial += 40
                dictionary_label_letter.update({labels[i]: self.word_chosen[0][i]})
            else:
                labels[i] = Label(word_frame, text=self.word_chosen[1][i], bd=6, fg="#31322a",
                                  relief=SUNKEN, font=("Georgia", "16", "bold"),
                                  anchor=E, cursor="target",
                                  bg="#e8f0bb")
                x_initial += 40
                labels[i].place(x=x_initial, y=y_initial)
                dictionary_label_letter.update({labels[i]: self.word_chosen[0][i]})

        # create the buttons on the frame
        x_initial = 0
        y_initial = 0
        # todo - buttons need to be global all
        "A"
        buttonA = Button(frame_letters, text=constants.LETTERS[0], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("A", dictionary_label_letter))
        buttonA.place(x=x_initial, y=y_initial)
        x_initial += 70
        "B"
        buttonB = Button(frame_letters, text=constants.LETTERS[1], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("B", dictionary_label_letter))
        buttonB.place(x=x_initial, y=y_initial)
        x_initial += 70
        "C"
        buttonC = Button(frame_letters, text=constants.LETTERS[2], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("C", dictionary_label_letter))
        buttonC.place(x=x_initial, y=y_initial)
        x_initial += 70
        "D"
        buttonD = Button(frame_letters, text=constants.LETTERS[3], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("D", dictionary_label_letter))
        buttonD.place(x=x_initial, y=y_initial)
        x_initial += 70
        "E"
        buttonE = Button(frame_letters, text=constants.LETTERS[4], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("E", dictionary_label_letter))
        buttonE.place(x=x_initial, y=y_initial)
        x_initial += 70
        "F"
        buttonF = Button(frame_letters, text=constants.LETTERS[5], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("F", dictionary_label_letter))
        buttonF.place(x=x_initial, y=y_initial)
        x_initial += 70
        "G"
        buttonG = Button(frame_letters, text=constants.LETTERS[6], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("G", dictionary_label_letter))
        buttonG.place(x=x_initial, y=y_initial)
        x_initial += 70
        "H"
        buttonH = Button(frame_letters, text=constants.LETTERS[7], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("H", dictionary_label_letter))
        buttonH.place(x=x_initial, y=y_initial)
        # reset line and new row
        x_initial = 0
        y_initial += 80
        "I"
        buttonI = Button(frame_letters, text=constants.LETTERS[8], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("I", dictionary_label_letter))
        buttonI.place(x=x_initial, y=y_initial)
        x_initial += 70
        "J"
        buttonJ = Button(frame_letters, text=constants.LETTERS[9], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("J", dictionary_label_letter))
        buttonJ.place(x=x_initial, y=y_initial)
        x_initial += 70
        "K"
        buttonK = Button(frame_letters, text=constants.LETTERS[10], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("K", dictionary_label_letter))
        buttonK.place(x=x_initial, y=y_initial)
        x_initial += 70
        "L"
        buttonL = Button(frame_letters, text=constants.LETTERS[11], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("L", dictionary_label_letter))
        buttonL.place(x=x_initial, y=y_initial)
        x_initial += 70
        "M"
        buttonM = Button(frame_letters, text=constants.LETTERS[12], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("M", dictionary_label_letter))
        buttonM.place(x=x_initial, y=y_initial)
        x_initial += 70
        "N"
        buttonN = Button(frame_letters, text=constants.LETTERS[13], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("N", dictionary_label_letter))
        buttonN.place(x=x_initial, y=y_initial)
        x_initial += 70
        "O"
        buttonO = Button(frame_letters, text=constants.LETTERS[14], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("O", dictionary_label_letter))
        buttonO.place(x=x_initial, y=y_initial)
        x_initial += 70
        "P"
        buttonP = Button(frame_letters, text=constants.LETTERS[15], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("P", dictionary_label_letter))
        buttonP.place(x=x_initial, y=y_initial)
        # reset line and new row
        x_initial = 0
        y_initial += 80
        "R"
        buttonR = Button(frame_letters, text=constants.LETTERS[16], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("R", dictionary_label_letter))
        buttonR.place(x=x_initial, y=y_initial)
        x_initial += 70
        "Q"
        buttonQ = Button(frame_letters, text=constants.LETTERS[17], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("Q", dictionary_label_letter))
        buttonQ.place(x=x_initial, y=y_initial)
        x_initial += 70
        "S"
        buttonS = Button(frame_letters, text=constants.LETTERS[18], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("S", dictionary_label_letter))
        buttonS.place(x=x_initial, y=y_initial)
        x_initial += 70
        "T"
        buttonT = Button(frame_letters, text=constants.LETTERS[19], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("T", dictionary_label_letter))
        buttonT.place(x=x_initial, y=y_initial)
        x_initial += 70
        "U"
        buttonU = Button(frame_letters, text=constants.LETTERS[20], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("U", dictionary_label_letter))
        buttonU.place(x=x_initial, y=y_initial)
        x_initial += 70
        "V"
        buttonV = Button(frame_letters, text=constants.LETTERS[21], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("V", dictionary_label_letter))
        buttonV.place(x=x_initial, y=y_initial)
        x_initial += 70
        "X"
        buttonX = Button(frame_letters, text=constants.LETTERS[22], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("X", dictionary_label_letter))
        buttonX.place(x=x_initial, y=y_initial)
        x_initial += 70
        "Y"
        buttonY = Button(frame_letters, text=constants.LETTERS[23], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("Y", dictionary_label_letter))
        buttonY.place(x=x_initial, y=y_initial)
        # last row
        x_initial = 210
        y_initial += 80
        "W"
        buttonW = Button(frame_letters, text=constants.LETTERS[24], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("W", dictionary_label_letter))
        buttonW.place(x=x_initial, y=y_initial)
        x_initial += 70
        "Z"
        buttonZ = Button(frame_letters, text=constants.LETTERS[25], foreground="#3c313c", bg="#c1cf8b",
                         padx=5, pady=5, font=("Georgia", "9", "bold"),
                         bd=11, command=lambda: self.replace_letter("Z", dictionary_label_letter))
        buttonZ.place(x=x_initial, y=y_initial)
        # make the dictionary of buttons to be used in the function of replacing
        self.dict_buttons.update({"A": buttonA})
        self.dict_buttons.update({"B": buttonB})
        self.dict_buttons.update({"C": buttonC})
        self.dict_buttons.update({"D": buttonD})
        self.dict_buttons.update({"E": buttonE})
        self.dict_buttons.update({"F": buttonF})
        self.dict_buttons.update({"G": buttonG})
        self.dict_buttons.update({"H": buttonH})
        self.dict_buttons.update({"I": buttonI})
        self.dict_buttons.update({"J": buttonJ})
        self.dict_buttons.update({"K": buttonK})
        self.dict_buttons.update({"L": buttonL})
        self.dict_buttons.update({"M": buttonM})
        self.dict_buttons.update({"N": buttonN})
        self.dict_buttons.update({"O": buttonO})
        self.dict_buttons.update({"P": buttonP})
        self.dict_buttons.update({"R": buttonR})
        self.dict_buttons.update({"Q": buttonQ})
        self.dict_buttons.update({"S": buttonS})
        self.dict_buttons.update({"T": buttonT})
        self.dict_buttons.update({"U": buttonU})
        self.dict_buttons.update({"V": buttonV})
        self.dict_buttons.update({"X": buttonX})
        self.dict_buttons.update({"Y": buttonY})
        self.dict_buttons.update({"W": buttonW})
        self.dict_buttons.update({"Z": buttonZ})

        '''frame to remind nr of tries'''

        label_tries = Label(root, text="TRIES LEFT: " + str(self.remaining_tries), justify="center",
                            font=("Helvetica", 19, "bold"),
                            cursor="trek", fg="#2a0510", bg="#e8f0bb")
        label_tries.place(x=680, y=100)
        '''here we will create a labelframe in which we will have a number of labels equal to the number of letters'''

        # this will be added in function to put on screen
        correct_word_frame = LabelFrame(root, fg="#31322a", bg="#e8f0bb", font=("Helvetica", 25, "bold"), bd=5,
                                        cursor="target", width=550, height=100, labelanchor="n", text="CORRECT WORD",
                                        relief=tkinter.GROOVE)

        root.mainloop()

    @staticmethod
    def split_names(list_labels):
        numbers = []
        for label in list_labels:
            numbers.append(int(label.split("_")[1]))
        return numbers

    def create_letter_list(self, correct_word):
        for letter in correct_word:
            self.list_letters.append(letter)
