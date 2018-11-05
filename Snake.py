from tkinter import *
import time
import random
class snake:
    def __init__(self):
        
        self.window=Tk()
        self.faceA,self.faceB=270,270
        self.tailA,self.tailB=280,280
        self.speed=50
        self.window.title("*#*Snake*#*")
        self.canvas=Canvas(self.window,width=650,height=650)
        self.canvas.pack()
        self.canvas.create_rectangle(10,10,643,643,fill="black")
        self.canvas.create_rectangle(self.faceA,self.faceB,self.tailA,self.tailB,fill="blue",tags="snake")
        self.food()
        self.canvas.bind("<Left>",self.moveL)
        self.canvas.bind("<Right>",self.moveR)
        self.canvas.bind("<Up>",self.moveU)
        self.canvas.bind("<Down>",self.moveD)
        self.canvas.bind("<space>",self.pause)
        self.canvas.focus_set()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def on_closing(self):
        self.window.destroy()
        
    def moveU(self,event):
        ke=event.keycode
        if self.faceB>10:
            while self.faceB>10:
                self.faceB-=10
                self.tailB-=10
                self.canvas.delete("snake")
                self.canvas.after(self.speed)
                self.canvas.create_rectangle(self.faceA,self.faceB,self.tailA,self.tailB,fill="blue",tags="snake")
                self.canvas.update()
                self.hasate()
                if event.keycode is not ke:
                    break
                elif event.keycode is None:
                    self.moveU()
                
    def moveL(self,event):
        ke=event.keycode
        if self.faceA>10:
            while self.faceA>10:
                self.faceA-=10
                self.tailA-=10
                self.canvas.delete("snake")
                self.canvas.after(self.speed)
                self.canvas.create_rectangle(self.faceA,self.faceB,self.tailA,self.tailB,fill="blue",tags="snake")
                self.canvas.update()
                self.hasate()
                if event.keycode is not ke:
                    break
                elif event.keycode is None:
                    self.moveL()
    def moveD(self,event):
        ke=event.keycode

        if self.tailB<640:
            while self.tailB<640:
                self.faceB+=10
                self.tailB+=10
                self.canvas.delete("snake")
                self.canvas.after(self.speed)
                self.canvas.create_rectangle(self.faceA,self.faceB,self.tailA,self.tailB,fill="blue",tags="snake")
                self.canvas.update()
                self.hasate()
                if event.keycode is not ke:
                    break
                elif event.keycode is None:
                    self.moveD()
    def moveR(self,event):
        ke=event.keycode

        if self.tailA<640:
            while self.tailA<640:
                self.faceA+=10
                self.tailA+=10
                self.canvas.delete("snake")
                self.canvas.after(self.speed)
                self.canvas.create_rectangle(self.faceA,self.faceB,self.tailA,self.tailB,fill="blue",tags="snake")
                self.canvas.update()
                self.hasate()
                if event.keycode is not ke:
                    break
                elif event.keycode is None:
                    self.moveR()
    def pause(self,event):

        if event.keycode==32:
            while True:
                self.canvas.crea_rectangle(self.faceA,self.faceB,self.tailA,self.tailB,fill="white",tags="snake")
                self.canvas.update()
       
    
    def food(self):
        self.foodA=random.randrange(10,640,10)
        self.foodB=random.randrange(10,640,10)
        self.foodC=self.foodA+10
        self.foodD=self.foodB+10
        self.canvas.create_rectangle(self.foodA,self.foodB,self.foodC,self.foodD,fill="red",tags="food")

    def hasate(self):
        if((self.foodA==self.faceA and self.foodB==self.faceB) or (self.foodC==self.faceA and self.foodD==self.faceB)
        and (self.foodB==self.faceA and self.foodD==self.faceB) or (self.foodC==self.faceA and self.foodD==self.faceB)):
            self.canvas.delete("food")
            self.food()

snake()








