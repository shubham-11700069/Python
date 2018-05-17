from tkinter import *
import time
import random


class Snake:
    def __init__(self):

        window=Tk()
        self.i,self.j=270,270
        self.k,self.l=280,280
        self.x=30
        window.title("*#*Snake*#*")
        self.canvas=Canvas(window,width=650,height=650)
        self.canvas.pack()
        self.canvas.create_rectangle(10,10,643,643,fill="black")
        self.canvas.create_rectangle(self.i,self.j,self.k,self.l,fill="blue",
                                     tags="snake")
        self.food()
        self.canvas.bind("<Key>",self.move)
        self.canvas.focus_set()

    def move(self,event):
        
        if event.keycode==38 and self.j>10:
            while self.i>10:
                self.j-=10
                self.l-=10
                self.canvas.delete("snake")
                self.canvas.after(self.x)
                self.canvas.create_rectangle(self.i,self.j,self.k,self.l,
                                                 fill="blue",tags="snake")
                self.canvas.update()

        elif event.keycode==37 and self.i>10:
            while self.i>10:
                self.i-=10
                self.k-=10
                self.canvas.delete("snake")
                self.canvas.after(self.x)
                self.canvas.create_rectangle(self.i,self.j,self.k,self.l,
                                                 fill="blue",tags="snake")
                self.canvas.update()

        elif event.keycode==40 and self.l<640:
            while self.l<640:
                self.j+=10
                self.l+=10
                self.canvas.delete("snake")
                self.canvas.after(self.x)
                self.canvas.create_rectangle(self.i,self.j,self.k,self.l,
                                                 fill="blue",tags="snake")
                self.canvas.update()

        elif event.keycode==39 and self.k<640:
            while self.k<640:
                self.i+=10
                self.k+=10
                self.canvas.delete("snake")
                self.canvas.after(self.x)
                self.canvas.create_rectangle(self.i,self.j,self.k,self.l,
                                                 fill="blue",tags="snake")
                self.canvas.update()

        elif event.keysym=="empty":
            print("end")
            self.canvas.update()

        self.canvas.mainloop()


        
    def food(self):
        self.a=random.randrange(10,640,10)
        self.b=random.randrange(10,640,10)
        self.c=self.a+10
        self.d=self.b+10
        self.canvas.create_rectangle(self.a,self.b,self.c,self.d,
                                             fill="red",tags="food")
        
        
Snake()











