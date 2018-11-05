from tkinter import *

class ProcessButtonEvent:
    def __init__(self):
        self.window=Tk()
        self.window.title("Hungman")
        frame=Canvas(self.window, width=500, height=500)
        frame.pack()
        self.n=StringVar()
        entry=Entry(frame, textvariable=self.n)
        entry.grid(row=2,column=3)
        bt=Button(frame,text="go",command=self.afterbt)
        bt.grid(row=3,column=3)
        self.window.mainloop()
    def afterbt(self):
        text=Text(self.window)
        text.pack()
        text.insert(END,self.n.get())
        
ProcessButtonEvent()
