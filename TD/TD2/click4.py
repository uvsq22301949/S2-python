import tkinter as tk


coord=[]
plein=[0,0]


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
        
def affichage_4(event):

    global plein
    global rectangle
    print (plein)
    if plein[1]==10:
        root.destroy()
    else:

        if plein[0]==0:
            rectangle=canvas.create_rectangle(50,50,450,450,fill="green")      
            plein[0]=1
            
        else:
            canvas.delete(rectangle)
            plein[0]=0

        plein[1]+=1

root=tk.Tk()

canvas=tk.Canvas(root,height=500,width=500,background="Black")
#canvas.create_line(250,0,250,500,fill="white")
canvas.create_line(450,450,450,50,fill='green')
canvas.create_line(50,50,450,50,fill='green')
canvas.create_line(50,450,450,450,fill='green')
canvas.create_line(50,50,50,450,fill='green')
#canvas.create_rectangle(50,50,450,450,fill="green")


#canvas.bind("<Button-1>",affichage)
#canvas.bind("<Button-1>",affichage_2)
#canvas.bind("<Button-1>",affichage_3)
canvas.bind("<Button-1>",affichage_4)
canvas.grid()
root.mainloop()