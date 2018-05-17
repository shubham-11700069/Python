from tkinter import *

class CanvasDemo():
    def __init__(self):
        window=Tk()
        window.title("Canvas Demo")

        self.canvas=Canvas(window,width=500,height=500,
                           bg="white")
        self.canvas.pack()

        frame=Frame(window)
        frame.pack()
        btRec=Button(frame,text="Rectangle",bg="gray",
                     command=self.displayRect)
        '''btCircle=Button(frame,text="Circle",bg="gray",
                        command=self.displayCir)'''
        btOval=Button(frame,text="Oval",bg="gray",
                      command=self.displayOval)
        btArc=Button(frame,text="Arc",bg="orange",
                     command=self.displayArc)
        btPolygon=Button(frame,text="Polygon",bg="gray",
                         command=self.displayPolygon)
        btLine=Button(frame,text="line",bg="yellow",
                      command=self.displayLine)
        btString=Button(frame,text="text",
                        command=self.displayString)
        btClear=Button(frame,text="Clear",bg="black",fg="white",
                       command=self.clear)
        btRec.grid(row=1,column=1)
        #btCircle.grid(row=1,column=2)
        btOval.grid(row=1,column=3)
        btArc.grid(row=1,column=4)
        btPolygon.grid(row=1,column=5)
        btLine.grid(row=1,column=6)
        btString.grid(row=1,column=7)
        btClear.grid(row=3,column=3)
        
        window.mainloop()

    '''def displayTriangle(self):
        self.canvas.create_triangle(40,10,460,200,width=5,fill="gray")
    '''
    def displayRect(self):
        self.canvas.create_rectangle(40,200,460,320,tags="rect",width=10
                                     )#display rectangle

    '''def displayCir(self):
        self.canvas.create_circle(10,10,190,90,fill="red",tags="circle")
'''
    def displayOval(self):
        self.canvas.create_oval(200,10,380,90,fill="orange",tags="oval")

    def displayArc(self):
        self.canvas.create_arc(390,10,470,90,start=0,extent=90,width=5,
                               fill="black",tags="arc")

    def displayPolygon(self):
        self.canvas.create_polygon(40,10,460,200,60,50,
                                   tags="polygon")

    def displayLine(self):
        self.canvas.create_line(10,10,190,90,fill="red",
                                tags="line")
        self.canvas.create_line(10,90,190,10,width=9,
                                arrow="last",fill="blue",tags="line")

    def displayString(self):
        self.canvas.create_text(250,250,text="Welcome",font="Times 60 bold underline italic",
                                fill="red",tags="string")

    def clear(self):
        self.canvas.delete("rect","oval","arc","circle","string","line",
                           "polygon")
CanvasDemo()












                     
