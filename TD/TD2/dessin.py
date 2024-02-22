import tkinter as tk
import random as rd

def affiche_cercle():

    #print(canvas.size)
    x,y=rd.randint(100,500),rd.randint(100,500)
    canvas.create_oval(x,y,x+100,y+100,fill="blue")

def affichge_carre():
    x,y=rd.randint(100,500),rd.randint(100,500)
    canvas.create_rectangle(x,y,x+100,y+100,fill="red")

def affiche_croix():
    x,y=rd.randint(100,500),rd.randint(100,500)
    canvas.create_line(x,y,x+100,y+100,fill="yellow")
    canvas.create_line(x+100,y,x,y+100,fill="yellow")

def choisir_couleur():
    couleur=input("couleur parmi: white, black, red, green, blue, cyan, yellow. ")
    

fenetre_height,fenetre_width= 600,600
root = tk.Tk()
root.title("Mon dessin")


canvas= tk.Canvas(root,height=fenetre_height,width=fenetre_height-50,background="black",borderwidth=50,relief="raised")
boutton_choix_couleur=tk.Button(root,text="Choisir couleur", font=("Helvetica", "30"),command=lambda:choisir_couleur())
boutton_cercle=tk.Button(root,text="cercle", font=("Helvetica", "30"),command=lambda: affiche_cercle())
boutton_carre=tk.Button(root,text="carré", font=("Helvetica", "30"),command=lambda : affichge_carre())
boutton_croix=tk.Button(root,text="croix", font=("Helvetica", "30"),command=lambda:affiche_croix())




canvas.grid(column=1,rowspan=fenetre_height,pady=80)
boutton_choix_couleur.grid(row=0,columnspan=fenetre_width)
boutton_carre.grid(row=1,column=0,pady=80)
boutton_cercle.grid(row=2,column=0)
boutton_croix.grid(row=3,column=0,pady=80)
root.mainloop()