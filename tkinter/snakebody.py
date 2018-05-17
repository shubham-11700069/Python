from tkinter import *
canvas=Canvas(Tk())
canvas.pack()
canvas.create_polygon(195,80,80,80,60,111,195,111,fill="white",outline="black")

canvas.create_arc(180,80,210,110,start=270,extent=180)
