import tkinter as tk
import random as rd

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)



def draw_pixel(i, j, color):
    canvas.create_rectangle(i,j,i+1,j+1,width=0,fill=color)

def ecran_aleatoire():
    for i in range (256):
        for j in range(256):
            draw_pixel(i,j,get_color(rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)))


def degrader_gris():
    for i in range(256):
        for j in range(256):
            draw_pixel(i,j,get_color(i,i,i))

def degrader_2D():
    for i in range(256):
        for j in range(256):
            draw_pixel(i,j,get_color(i,0,j))

def degrader_2D_v2():
    for i in range(256):
        for j in range(256):
            draw_pixel(i,j,get_color(i,j,255-i))


root = tk.Tk()
root.title("_")
canvas=tk.Canvas(root,height=256,width=256,background="black",borderwidth=10,relief="raised")
button_aleatoire= tk.Button(root,text="Aléatoire",command=lambda:ecran_aleatoire())
button_degrader_gris=tk.Button(root,text="Dégradé gris",command=lambda:degrader_gris())
button_2D=tk.Button(root,text="Dégradé 2D",command=lambda:degrader_2D())
button_2D_v2=tk.Button(root,text="Dégradé 2D v2",command=lambda:degrader_2D_v2())

#command=lambda:draw_pixel(256/2,256/2,get_color(rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)))

canvas.grid(column=1,rowspan=4)
button_aleatoire.grid(column=0,row=0)
button_degrader_gris.grid(column=0,row=1)
button_2D.grid(column=0,row=2)
button_2D_v2.grid(column=0,row=3)
root.mainloop()