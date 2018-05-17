from tkinter import *
window=Tk()
window.title("Welcome")

canvas=Canvas(window,width=500,height=500)
canvas.create_rectangle(10,10,490,490,fill="black")
canvas.pack()
def enter(i,j):
    canvas.delete("text")
    canvas.create_text(j,i,text="Welcome",font="Times 60 bold italic underline",fill="red",tags="text")

i=50
enter(i,250)
p=(input("enter choice: "))
if p=="y":
    enter(i+20,250)





