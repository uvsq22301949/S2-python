import tkinter as tk
import random as rd

"""claire.baskevitch@uvsq.fr"""


couleur="blue"
objets=[]

def affiche_cercle(color):

    global objets
    #print(canvas.size)
    x,y=rd.randint(100,500),rd.randint(100,500)
    objets.append(canvas.create_oval(x,y,x+100,y+100,fill=color))
    print(objets)
    

def affichge_carre(color):

    global objets
    x,y=rd.randint(100,500),rd.randint(100,500)
    objets.append(canvas.create_rectangle(x,y,x+100,y+100,fill=color))
    print(objets)


def affiche_croix(color):

    global objets
    x,y=rd.randint(100,500),rd.randint(100,500)
    objets.append(canvas.create_line(x,y,x+100,y+100,fill=color))
    objets.append(canvas.create_line(x+100,y,x,y+100,fill=color))
    print(objets)

def choisir_couleur():
    global couleur
    couleur=input("choisir une couleur parmi: white, black, red, green, blue, cyan, yellow. ")

def Undo():
    global objets
    if len(objets)!=0:
        if canvas.type(objets[-1])=="line":
            for i in range(2):
                canvas.delete(objets[-1])
                objets.pop(-1)
        else:
            canvas.delete(objets[-1])
            objets.pop(-1)

    print (objets)

fenetre_height,fenetre_width= 600,600
root = tk.Tk()
root.title("Mon dessin")


canvas= tk.Canvas(root,height=fenetre_height,width=fenetre_height-50,background="black",borderwidth=50,relief="raised")
boutton_choix_couleur=tk.Button(root,text="Choisir couleur", font=("Helvetica", "30"),command=lambda:choisir_couleur())
boutton_cercle=tk.Button(root,text="cercle", font=("Helvetica", "30"),command=lambda: affiche_cercle(couleur))
boutton_carre=tk.Button(root,text="carré", font=("Helvetica", "30"),command=lambda : affichge_carre(couleur))
boutton_croix=tk.Button(root,text="croix", font=("Helvetica", "30"),command=lambda:affiche_croix(couleur))
boutton_undo=tk.Button(root,text="Undo", font=("Helvetica", "30"),command=lambda:Undo())



canvas.grid(column=1,rowspan=fenetre_height,pady=80)
boutton_choix_couleur.grid(row=0,columnspan=fenetre_width)
boutton_carre.grid(row=1,column=0,pady=80)
boutton_cercle.grid(row=2,column=0)
boutton_croix.grid(row=3,column=0,pady=80)
boutton_undo.grid(row=0,columnspan=1)


root.mainloop()