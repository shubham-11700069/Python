from tkinter import *
snakef=Tk()
canvas=Canvas(snakef,width=500,height=500)
canvas.pack()
j=90
i=90
canvas.create_rectangle(10,10,490,490,fill="black")
canvas.create_rectangle(i+48,j+48,i+72,j+72,outline="red",fill="gray")
canvas.create_oval(i+54,j+54,i+56,j+56,tags="eye",fill="black")
canvas.create_oval(i+64,j+54,i+66,j+56,tags="eye",fill="black")
canvas.create_rectangle(i+59,j+55,i+61,j+63,tags="nose",fill="black")
canvas.create_rectangle(i+54,j+66,i+66,j+68,tags="teeth",fill="white")
canvas.create_line(i+60,j+66,i+60,j+68)
canvas.create_line(i+56,j+66,i+56,j+68)
canvas.create_line(i+58,j+66,i+58,j+68)
canvas.create_line(i+62,j+66,i+62,j+68)
canvas.create_line(i+64,j+66,i+64,j+68)
canvas.create_oval(i+46,j+54,i+48,j+65,fill="black",tags="ears")
canvas.create_oval(i+72,j+54,i+74,j+65,fill="black",tags="ears")


canvas.create_polygon(j+48,i+48,i+48,j-30,i+72,j-45,i+72,j
                      +48,fill="white",outline="red")





