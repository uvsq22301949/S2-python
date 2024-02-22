import tkinter as tk


root=tk.Tk()
canvas=tk.Canvas(root,height=500,width=500,background="black")
r=0
liste_color=["blue", "green", "black", "yellow", "magenta", "red"]
i=0
while r<250:
    canvas.create_oval(1+r,1+r,500-r,500-r,fill=liste_color[i%6])
    r+=40
    i+=1

canvas.grid()
root.mainloop()