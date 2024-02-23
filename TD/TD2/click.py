import tkinter as tk

def affichage(event):

    canvas.create_rectangle(event.x,event.y,event.x+1,event.y+1,width=0,fill="red")


root=tk.Tk()


canvas=tk.Canvas(root,height=500,width=500,background="Black")

canvas.bind("<Button-1>",affichage)

canvas.grid()
root.mainloop()