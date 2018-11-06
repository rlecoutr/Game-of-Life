from tkinter import *
from numpy import random as rd

#Variables
        
height = 600 #Hauteur du damier
width = 800 #Largeur du damier

c = 10 #taille des cellules

vitesse=10 #Vitesse de l'animation

flag=0
nbrAdjacent = {} #Nombre de cellules vivantes autour de chaque cellule
etatCellule = {} #Valeur 0 ou 1 si cellule morte ou vivante
i=0

# Fonctions

def click_gauche(event): #Mettre à la main une cellule à 1
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='red', outline='red')
    etatCellule[x,y]=2

def change_vit(event): #Changer la vitesse
    global vitesse
    vitesse = int(eval(entree.get()))

def go():
    "démarrage de l'animation"
    global flag
    if flag == 0:
        flag = 1
        play()
        
def stop():
    "arrêt de l'animation"
    global flag    
    flag = 0
    
def play(): #Compte le nombre de cellule autour de chacune
    global flag, vitesse
    v = 0
    while v!= width/c:
        w = 0
        while w!= height/c:
            x=v*c
            y=w*c
            
            # les coins
            if x==0 and y==0: #coin en haut à gauche
                compt_feu=0
                if etatCellule[x, y+c]==2:
                    compt_feu+=1
                if etatCellule[x+c, y]==2:
                    compt_feu+=1
                if etatCellule[x+c, y+c]==2:
                    compt_feu+=1
                nbrAdjacent[x, y]=compt_feu
            elif x==0 and y==int(height-c): #coin en bas à gauche
                compt_feu=0
                if etatCellule[x, y-c]==2:
                    compt_feu+=1
                if etatCellule[x+c, y-c]==2:
                    compt_feu+=1
                if etatCellule[x+c, y]==2:
                    compt_feu+=1
                nbrAdjacent[x, y]=compt_feu
            elif x==int(width-c) and y==0: #coin en haut à droite
                compt_feu=0
                if etatCellule[x-c, y]==2:
                    compt_feu+=1
                if etatCellule[x-c, y+c]==2:
                    compt_feu+=1
                if etatCellule[x, y+c]==2:
                    compt_feu+=1
                nbrAdjacent[x, y]=compt_feu
            elif x==int(width-c) and y==int(height-c): #coin en bas à droite
                compt_feu=0
                if etatCellule[x-c, y-c]==2:
                    compt_feu+=1
                if etatCellule[x-c, y]==2:
                    compt_feu+=1
                if etatCellule[x, y-c]==2:
                    compt_feu+=1
                nbrAdjacent[x, y]=compt_feu
                
            # les bords du tableau (sans les coins)    
            elif x==0 and 0<y<int(height-c): # bord de gauche
                compt_feu=0
                if etatCellule[x, y-c]==2:
                    compt_feu+=1
                if etatCellule[x, y+c]==2:
                    compt_feu+=1
                if etatCellule[x+c, y-c]==2:
                    compt_feu+=1
                if etatCellule[x+c, y]==2:
                    compt_feu+=1
                if etatCellule[x+c, y+c]==2:
                    compt_feu+=1
                nbrAdjacent[x, y]=compt_feu
            elif x==int(width-c) and 0<y<int(height-c): # bord de droite
                compt_feu=0
                if etatCellule[x-c, y-c]==2:
                    compt_feu+=1
                if etatCellule[x-c, y]==2:
                    compt_feu+=1
                if etatCellule[x-c, y+c]==2:
                    compt_feu+=1
                if etatCellule[x, y-c]==2:
                    compt_feu+=1
                if etatCellule[x, y+c]==2:
                    compt_feu+=1
                nbrAdjacent[x, y]=compt_feu
            elif 0<x<int(width-c) and y==0: # bord du haut
                compt_feu=0
                if etatCellule[x-c, y]==2:
                    compt_feu+=1
                if etatCellule[x-c, y+c]==2:
                    compt_feu+=1
                if etatCellule[x, y+c]==2:
                    compt_feu+=1
                if etatCellule[x+c, y]==2:
                    compt_feu+=1
                if etatCellule[x+c, y+c]==2:
                    compt_feu+=1
                nbrAdjacent[x, y]=compt_feu
            elif 0<x<int(width-c) and y==int(height-c): # bord du bas
                compt_feu=0
                if etatCellule[x-c, y-c]==2:
                    compt_feu+=1
                if etatCellule[x-c, y]==2:
                    compt_feu+=1
                if etatCellule[x, y-c]==2:
                    compt_feu+=1
                if etatCellule[x+c, y-c]==2:
                    compt_feu+=1
                if etatCellule[x+c, y]==2:
                    compt_feu+=1
                nbrAdjacent[x, y]=compt_feu

            #cas généraux
            else:
                compt_feu=0
                if etatCellule[x-c, y-c]==2:
                    compt_feu+=1
                if etatCellule[x-c, y]==2:
                    compt_feu+=1
                if etatCellule[x-c, y+c]==2:
                    compt_feu+=1
                if etatCellule[x, y-c]==2:
                    compt_feu+=1
                if etatCellule[x, y+c]==2:
                    compt_feu+=1
                if etatCellule[x+c, y-c]==2:
                    compt_feu+=1
                if etatCellule[x+c, y]==2:
                    compt_feu+=1
                if etatCellule[x+c, y+c]==2:
                    compt_feu+=1
                nbrAdjacent[x, y]=compt_feu
                
            w+=1
        v+=1
    redessiner()
    if flag >0: 
        fen1.after(vitesse,play)

        

def redessiner(): #Redessine le tableau à partir de nbrAdjacent
    can1.delete(ALL)
    t=0
    while t!= width/c:
        u=0
        while u!= height/c: #Règles définissant l'apparition ou non de cases noires
            x=t*c
            y=u*c
            if nbrAdjacent[x,y]>=1 and etatCellule[x,y]==1:
                etatCellule[x,y]=2
                can1.create_rectangle(x, y, x+c, y+c, fill='red', outline='red')
            elif etatCellule[x,y]==2:
                etatCellule[x,y]==3
                can1.create_rectangle(x, y, x+c, y+c, fill='black')
            elif etatCellule[x,y]==1:
                etatCellule[x,y]=1
                can1.create_rectangle(x, y, x+c, y+c, fill='lightgreen', outline='lightgreen')
            u+=1
        t+=1

def debut():
    i = 0
    while i!= width/c: #Initialisation du tableau
        j=0
        while j!= height/c:
            x=i*c
            y=j*c
            a = rd.randint(1,100)
            if (a<=30):
                etatCellule[x,y]=0
            else:
                etatCellule[x,y]=1
            j+=1
        i+=1

#Main

fen1 = Tk()

fen1.title("Auto-Evolution. Oui.")

can1 = Canvas(fen1, width =width, height =height, bg ='white')
can1.bind("<Button-1>", click_gauche)
can1.pack(side =TOP, padx =5, pady =5)

debut()

b1 = Button(fen1, text ='Départ', command =go)
b2 = Button(fen1, text ='Arrêt', command =stop)
b3 = Button(fen1, text ='Relancer', command =debut)
b1.pack(side =LEFT, padx =3, pady =3)
b2.pack(side =LEFT, padx =3, pady =3)
b3.pack(side =LEFT, padx =3, pady =3)

entree = Entry(fen1)
entree.bind("<Return>", change_vit)
entree.pack(side =RIGHT)
chaine = Label(fen1)
chaine.configure(text = "Vitesse de l'animation :")
chaine.pack(side =RIGHT)

go()
stop()

fen1.mainloop()
