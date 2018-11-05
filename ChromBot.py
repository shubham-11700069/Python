# -*-   coding: utf-8 -*-
""" 
Crea ted on Sat Sep  1 16:16:58 2018

@auth or: Tony
"""
 
from PIL import ImageGrab, ImageOps
import pyautogui
import time
from  numpy import *
class  Cordinates():
    replaybtn=(342,421)
    dinosaur=(170,425)
      
def restartGame():
    pyautogui.click(Cordinates.replaybtn)
    #pyautogui.keyDown('down')
     
def pressSpace():
    #pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.1)
    #  print("jum p")
    pyautogui.keyUp('space')
    #pyautogui.keyDown('down')
      
def imageGrab():
    box=(Cordinates.dinosaur[0]+x1Inc,Cordinates.dinosaur[1],
         Cordinates.dinosaur[0]+x2Inc,Cordinates.dinosaur[1]+y2Inc)
    image =ImageGrab.grab(box) 
    grayImage =ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    return(a.sum())  
    
    

startTime=time.time()
endTime=time.time()
x1Inc=70 
x2Inc=100 
y2Inc=30
restartGame()
while True:
    if (endTime-startTime%4000==0):
        x1Inc+=(round(6 +0.1*(endTime-startTime)/100))
        x2Inc+=(round(6+ 0.1*(endTime-startTime)/100))
    if(imageGrab()>1148):  
         pressSpace()  
         time.sleep(0.1)
    endTime=time.time() 
exit(0)  
#(170   ,442)