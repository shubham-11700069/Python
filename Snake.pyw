from tkinter import *
import time
import random
import keyboard
import sys
from cx_Freeze import setup, Executable

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    

class snake:
    def __init__(self):
        
        self.window=Tk()
        self.i,self.j=270,270
        self.k,self.l=280,280
        self.x=50
        self.window.title("*#*Snake*#*")
        self.canvas=Canvas(self.window,width=650,height=650)
        self.canvas.pack()
        self.canvas.create_rectangle(10,10,643,643,fill="black")
        self.canvas.create_rectangle(self.i,self.j,self.k,self.l,fill="blue",tags="snake")
        self.food()
        self.canvas.bind("<Left>",self.moveL)
        self.canvas.bind("<Right>",self.moveR)
        self.canvas.bind("<Up>",self.moveU)
        self.canvas.bind("<Down>",self.moveD)
        self.canvas.bind("<space>",self.pause)
        self.canvas.focus_set()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)


       
    def on_closing(self):
        self.window.destroy()
    def moveU(self,event):
        ke=event.keycode
        if self.j>10:
            while self.j>10:
                self.j-=10
                self.l-=10
                self.canvas.delete("snake")
                self.canvas.after(self.x)
                self.canvas.create_rectangle(self.i,self.j,self.k,self.l,fill="blue",tags="snake")
                self.canvas.update()
                if event.keycode is not ke:
                    break
                elif event.keycode is None:
                    self.moveU()
                
    def moveL(self,event):
        ke=event.keycode
        if self.i>10:
            while self.i>10:
                self.i-=10
                self.k-=10
                self.canvas.delete("snake")
                self.canvas.after(self.x)
                self.canvas.create_rectangle(self.i,self.j,self.k,self.l,fill="blue",tags="snake")
                self.canvas.update()
                if event.keycode is not ke:
                    break
                elif event.keycode is None:
                    self.moveL()
    def moveD(self,event):
        ke=event.keycode

        if self.l<640:
            while self.l<640:
                self.j+=10
                self.l+=10
                self.canvas.delete("snake")
                self.canvas.after(self.x)
                self.canvas.create_rectangle(self.i,self.j,self.k,self.l,fill="blue",tags="snake")
                self.canvas.update()
                if event.keycode is not ke:
                    break
                elif event.keycode is None:
                    self.moveD()
    def moveR(self,event):
        ke=event.keycode

        if self.k<640:
            while self.k<640:
                self.i+=10
                self.k+=10
                self.canvas.delete("snake")
                self.canvas.after(self.x)
                self.canvas.create_rectangle(self.i,self.j,self.k,self.l,fill="blue",tags="snake")
                self.canvas.update()
                if event.keycode is not ke:
                    break
                elif event.keycode is None:
                    self.moveR()
    def pause(self,event):

        if event.keycode==32:
            while True:
                self.canvas.crea_rectangle(self.i,self.j,self.k,self.l,fill="white",tags="snake")
                self.canvas.update()
       
    
    def food(self):
        self.a=random.randrange(10,640,10)
        self.b=random.randrange(10,640,10)
        self.c=self.a+10
        self.d=self.b+10
        self.canvas.create_rectangle(self.a,self.b,self.c,self.d,fill="red",tags="food")
    

snake()









