import tkinter as tk


coord=[]

def affichage(event):

    canvas.create_rectangle(event.x,event.y,event.x+1,event.y+1,width=0,fill="red")

def affichage_2(event):

    if event.x<250 :
        canvas.create_oval(event.x-50,event.y-50,event.x+50,event.y+50,fill="blue")
    else:
        canvas.create_oval(event.x-50,event.y-50,event.x+50,event.y+50,fill="red")

def affichage_3(event):

    global coord
    
    coord.append(event.x)
    coord.append(event.y)

    if len(coord)>2:
        if (coord[0]<250 and coord[2]<250 ) or (coord[0]>=250 and coord[2]>=250):
            canvas.create_line(coord[0],coord[1],coord[2],coord[3],fill='blue')
        
        else:
            canvas.create_line(coord[0],coord[1],coord[2],coord[3],fill='red')
    
        for i in range(len(coord)):
            coord.pop()
        
root=tk.Tk()

canvas=tk.Canvas(root,height=500,width=500,background="Black")
canvas.create_line(250,0,250,500,fill="white")
#canvas.bind("<Button-1>",affichage)
#canvas.bind("<Button-1>",affichage_2)
canvas.bind("<Button-1>",affichage_3)
canvas.grid()
root.mainloop()