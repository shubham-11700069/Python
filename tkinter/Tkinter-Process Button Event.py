from tkinter import *

def processOK():
    print("OK button is clicked")

def processCancel():
    print("Cancel buttton is clicked")

window=Tk()
btOK=Button(window,text="OK",bg="red",command=processOK)
btCancel=Button(window,text="Cancel",bg="yellow",command=processCancel)
btOK.pack()
btCancel.pack()

window.mainloop()
