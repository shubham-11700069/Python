from tkinter import *
def processOK():
    print("OK is pressed\n ")
def processCancel():
    print("CANCEL is pressed\n")

window=Tk()
window["bg"]="black"
label=Label(window,text="Welcome..",bg="black",fg="white")
label.pack()

OKbt=Button(window,text="ok",bg="green",fg="white",command=processOK)
OKbt.pack()

Cbt=Button(window,text="cancel",bg="green",fg="white",command=processCancel)


Cbt.pack()
window.mainloop()
