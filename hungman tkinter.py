import tkinter
import tkinter.messagebox
import random

#fruit category
easyWords = ['apple', 'orange', 'mango', 'peach', 'guava']
#space category
mediumWords = ['atmosphere', 'jupiter', 'quasar', 'satellite', 'asteroid']
#science category
hardWords = ['biochemical', 'hemoglobin', 'emulsify', 'reactant', 'dynamo']

def setting():

    wordChoice = ''

    difficulty = input('''Welcome to hangman, select your difficulty.
Type, easy, medium, or hard to begin:''')

    if difficulty == 'easy':

        wordChoice = easyWords.random
        print('You have selected easy mode, start guessing your letters now in the game window. The category is: fruit')

    if difficulty == 'medium':

        wordChoice = mediumWords.random
        print('You have selected medium mode, start guessing your letters now in the game window. The category is: space')

    if difficulty == 'hard':

        wordChoice = hardWords.random
        print('You have selected hard mode, start guessing your letters now in the game window. The category is: science')

def game():

    missGuess = 0
    guesses = ''

    for char in wordChoice:
        label3.print(char),

        if char in guesses:
            print(char),

        else:
            label3.print("_"),
            missGuess += 1

        if missGuess == 1:
            label1.print('head')
        if missGuess == 2:
            label1.print('torso')
        if missGuess == 3:
            label1.print('left arm')
        if missGuess == 4:
            label1.print('right arm')
        if missGuess == 5:
            label1.print('left leg')
        if missGuess == 6:
            label1.print('right leg'),

class MyGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()

        #create needed frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.center_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #create top frame labels
        self.label1 = tkinter.Label(self.top_frame, text='Hangman parts:')
        self.label2 = tkinter.Label(self.top_frame, text=' ')
        #center frame labels
        self.label3 = tkinter.Label(self.center_frame, text=' ')
        #bottom frame labels
        self.label4 = tkinter.Label(self.bottom_frame, text='Guess a letter:')
        self.entry1 = tkinter.Entry(self.bottom_frame, width=5)
        self.button1 = tkinter.Button(self.bottom_frame, text='Guess', command=game) #calls the game method
        self.button2 = tkinter.Button(self.bottom_frame, text='Exit',  command=self.main_window.destroy)

        #pack top frame labels
        self.label1.pack(side='left')
        self.label2.pack(side='right')
        #pack center frame
        self.label3.pack(side='top')
        #bottom frame
        self.label4.pack(side='left')
        self.entry1.pack(side='left')
        self.button1.pack(side='left')
        self.button2.pack(side='left')

        self.main_window.mainloop()
MyGUI()
