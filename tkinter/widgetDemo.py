from tkinter import *
class widgetDemo():
    def __init__(self):
        window=Tk()
        window.title("Widget's Demo")

        frame1=Frame(window)
        frame1.pack()
        self.v1=IntVar()
        cbtBold=Checkbutton(frame1,text="Bold",variable=self.v1,command=self.processCheckbutton)
        self.v2=IntVar()
        rbRed=Radiobutton(frame1,text="Red",bg="red",variable=self.v2,value=1,
                          command=self.processRadiobutton)
        rbYellow=Radiobutton(frame1,text="Yellow",bg="yellow",variable=self.v2,value=2,
                          command=self.processRadiobutton)
        cbtBold.grid(row=1,column=1)
        rbgreen=Radiobutton(frame1,text="Green",bg="green",variable=self.v2,value=3,
                          command=self.processRadiobutton)
        rbRed.grid(row=2,column=2)
        rbYellow.grid(row=2,column=3)
        rbgreen.grid(row=2,column=4)
        #add a label ,an entry, a button, and a message to frame1

        frame2=Frame(window)
        frame2.pack()
        label=Label(frame2,text="Enter your name: ")
        self.name=StringVar()
        entryName=Entry(frame2,textvariable=self.name)
        btGetName=Button(frame2,text="Get Name",command=self.processButton)
        message=Message(frame2,text="It is widgets demo")
        label.grid(row=1,column=1)
        entryName.grid(row=1,column=2)
        btGetName.grid(row=2,column=2)
        message.grid(row=3,column=1)

        window.mainloop()

    def processCheckbutton(self):
        print("check button is "+("checked" if self.v1.get()==1 else "Unchecked"))
        
    def processRadiobutton(self):
        print("aah")

        
    def processButton(self):
        print("Your name is " +self.name.get())

widgetDemo() #create GUI
