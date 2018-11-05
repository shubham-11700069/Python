# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 12:11:33 2018

@author: Tony
"""

from tkinter import *

class Snakeface():
        
    def __init__(self,x1,y1,x2,y2,length,width):
        self.canvas=canvas
        self.faceX1=x1
        self.faceY1=y1
        self.width=width
        self.length=length
        self.faceX2=x2
        self.faceY2=y2
        pass
        #self.canvas.create_polygon(master=coordinates, *args, **kwargs, outline="blue",fill='white',width=2)

    def faceL(self):
        self.smileX=self.faceX1+self.width
        self.smileY=self.faceY2-(self.faceY2-self.faceY1)/2
        self.canvas.create_polygon((self.faceX1,self.faceY1),(self.smileX,self.smileY),(self.faceX1,self.faceY2),
                                   (self.faceX1,self.faceY1),(self.faceX1+self.length,self.faceY1),
                                   (self.faceX1+self.length,self.faceY2),(self.faceX2,self.faceY2),
                                   outline="black",width=2,fill="blue",tag='face')
        
    def faceR(self):
        self.smileX=self.faceX2-self.width
        self.smileY=self.faceY2-(self.faceY2-self.faceY1)/2
        self.canvas.create_polygon((self.faceX2-self.length,self.faceY2),(self.smileX,self.smileY),
                                   (self.faceX2-self.length,self.faceY1),(self.faceX2-self.length,self.faceY2),
                                   (self.faceX1,self.faceY2),
                                   (self.faceX1,self.faceY1),(self.faceX2-self.length,self.faceY1),
                                   outline="black",width=2,fill="blue",tag='face')
    
    def faceD(self):
        self.smileX=self.faceY2-self.width/2
        self.smileY=self.faceY2-self.width/2
        self.canvas.create_polygon((self.faceX1,self.faceY2),(self.smileX,self.smileY),
                                   (self.faceX2+self.length,self.faceY2),(self.faceX1,self.faceY2),
                                   (self.faceX1,self.faceY1),
                                   (self.faceX2+self.length,self.faceY1),(self.faceX2+self.length,self.faceY2),
                                   outline="black",width=2,fill="blue",tag='face')
    
    def faceU(self):
        self.smile=self.faceY1+self.width/2
        self.canvas.create_polygon((self.faceX1,self.faceY1),(self.smileX,self.smileY),
                                   (self.faceX2+self.length,self.faceY1),(self.faceX1,self.faceY1),
                                   (self.faceX2,self.faceY2),
                                   (self.faceX2+self.length,self.faceY2),(self.faceX2+self.length,self.faceY1),
                                   outline="black",width=2,fill="blue",tag='face')
    

window=Tk()
canvas=Canvas(window,width=650,height=650)
canvas.pack()
s=Snakeface(270,270,270,290,50,10)

#s.createL(270,270,270,290,20)

s.faceR()

#s.createD(270,270,270,290,20)
window.mainloop()

'''
class GUI(Canvas):
    
    def __init__(self,coordinates,*args,**kwargs):
        Canvas.__init__(self, master=coordinates, *args, **kwargs)

polygon = GUI(root)
polygon.create_polygon([150,75,225,0,300,75,225,150],     outline='gray', 
            fill='gray', width=2)

polygon.pack()

                                   

'''