from tkinter import * #import all tkinter

class widgetDemo:
    def __init__(self):
        window=Tk()
        window.title("change Label Demo")

        frame1=Frame(window)
        frame1.pack()
        self.lbl=Label(frame1,text="Programming is fun ")
        self.lbl.pack()

        frame2=Frame(window)
        frame2.pack()
        label=Label(frame2,text="Enter text: ")
        self.msg=StringVar()
        entry=Entry(frame2,textvariable=self.msg)
        btChangeText=Button(frame2,text="Change text ",command=self.processButton)
        self.v1=StringVar()
        rbRed=Radiobutton(frame2,text="Red",bg="red",variable=self.v1,value="R",
                          command=self.processRadiobutton)
        rbYellow=Radiobutton(frame2,text="Yellow",bg="yellow",variable=self.v1,value="Y",
                          command=self.processRadiobutton)
        label.grid(row=1,column=1)
        entry.grid(row=1,column=2)
        btChangeText.grid(row=1,column=3)
        rbRed.grid(row=2,column=1)
        rbYellow.grid(row=2,column=2)

        window.mainloop()

    def processButton(self):
        if self.v1.get()=="R":
            self.lbl["bg"]="red"
        elif self.v1.get()=="Y":
            self.lbl["bg"]="Yellow"

    def processRadiobutton(self):
        self.lbl["text"]=self.msg.get()

widgetDemo()
    
