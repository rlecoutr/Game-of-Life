from tkinter import *

def click_gauche(event): #Mettre à la main une cellule à 1
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can.create_rectangle(x, y, x+c, y+c, fill='black')
    etatCellule[x,y]=1

def change_vit(event): #Changer la vitesse
    global vitesse
    vitesse = int(eval(entree.get()))
    print(vitesse)

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

def LeFameux():
    etatCellule[0,80]=1
    etatCellule[0,100]=1
    etatCellule[20,80]=1
    etatCellule[20,100]=1
    etatCellule[200,80]=1
    etatCellule[200,100]=1
    etatCellule[200,120]=1
    etatCellule[220,60]=1
    etatCellule[220,140]=1
    etatCellule[240,40]=1
    etatCellule[240,160]=1
    etatCellule[260,40]=1
    etatCellule[260,160]=1
    etatCellule[280,100]=1
    etatCellule[300,60]=1
    etatCellule[300,140]=1
    etatCellule[320,80]=1
    etatCellule[320,100]=1
    etatCellule[320,120]=1
    etatCellule[340,100]=1
    etatCellule[400,80]=1
    etatCellule[400,60]=1
    etatCellule[400,40]=1
    etatCellule[420,80]=1
    etatCellule[420,60]=1
    etatCellule[420,40]=1
    etatCellule[440,20]=1
    etatCellule[440,100]=1
    etatCellule[480,20]=1
    etatCellule[480,0]=1
    etatCellule[480,100]=1
    etatCellule[480,120]=1
    etatCellule[680,60]=1
    etatCellule[680,40]=1
    etatCellule[700,60]=1
    etatCellule[700,40]=1
    
def play(): #Compte le nombre de cellule autour de chacune
    global flag, vitesse
    i = 0
    while i!= width/c:
        j = 0
        while j!= height/c:
            x=i*c
            y=j*c
            
            #Coins
            if x==0 and y==0: #coin en haut à gauche
                compt_viv=0
                if etatCellule[x, y+c]==1:
                    compt_viv+=1
                if etatCellule[x+c, y]==1:
                    compt_viv+=1
                if etatCellule[x+c, y+c]==1:
                    compt_viv+=1
                nbrAdjacent[x, y]=compt_viv
            elif x==0 and y==int(height-c): #coin en bas à gauche
                compt_viv=0
                if etatCellule[x, y-c]==1:
                    compt_viv+=1
                if etatCellule[x+c, y-c]==1:
                    compt_viv+=1
                if etatCellule[x+c, y]==1:
                    compt_viv+=1
                nbrAdjacent[x, y]=compt_viv
            elif x==int(width-c) and y==0: #coin en haut à droite
                compt_viv=0
                if etatCellule[x-c, y]==1:
                    compt_viv+=1
                if etatCellule[x-c, y+c]==1:
                    compt_viv+=1
                if etatCellule[x, y+c]==1:
                    compt_viv+=1
                nbrAdjacent[x, y]=compt_viv
            elif x==int(width-c) and y==int(height-c): #coin en bas à droite
                compt_viv=0
                if etatCellule[x-c, y-c]==1:
                    compt_viv+=1
                if etatCellule[x-c, y]==1:
                    compt_viv+=1
                if etatCellule[x, y-c]==1:
                    compt_viv+=1
                nbrAdjacent[x, y]=compt_viv
                
            # Bords du damier    
            elif x==0 and 0<y<int(height-c): # bord de gauche
                compt_viv=0
                if etatCellule[x, y-c]==1:
                    compt_viv+=1
                if etatCellule[x, y+c]==1:
                    compt_viv+=1
                if etatCellule[x+c, y-c]==1:
                    compt_viv+=1
                if etatCellule[x+c, y]==1:
                    compt_viv+=1
                if etatCellule[x+c, y+c]==1:
                    compt_viv+=1
                nbrAdjacent[x, y]=compt_viv
            elif x==int(width-c) and 0<y<int(height-c): # bord de droite
                compt_viv=0
                if etatCellule[x-c, y-c]==1:
                    compt_viv+=1
                if etatCellule[x-c, y]==1:
                    compt_viv+=1
                if etatCellule[x-c, y+c]==1:
                    compt_viv+=1
                if etatCellule[x, y-c]==1:
                    compt_viv+=1
                if etatCellule[x, y+c]==1:
                    compt_viv+=1
                nbrAdjacent[x, y]=compt_viv
            elif 0<x<int(width-c) and y==0: # bord du haut
                compt_viv=0
                if etatCellule[x-c, y]==1:
                    compt_viv+=1
                if etatCellule[x-c, y+c]==1:
                    compt_viv+=1
                if etatCellule[x, y+c]==1:
                    compt_viv+=1
                if etatCellule[x+c, y]==1:
                    compt_viv+=1
                if etatCellule[x+c, y+c]==1:
                    compt_viv+=1
                nbrAdjacent[x, y]=compt_viv
            elif 0<x<int(width-c) and y==int(height-c): # bord du bas
                compt_viv=0
                if etatCellule[x-c, y-c]==1:
                    compt_viv+=1
                if etatCellule[x-c, y]==1:
                    compt_viv+=1
                if etatCellule[x, y-c]==1:
                    compt_viv+=1
                if etatCellule[x+c, y-c]==1:
                    compt_viv+=1
                if etatCellule[x+c, y]==1:
                    compt_viv+=1
                nbrAdjacent[x, y]=compt_viv

            #Cases normales
            else:
                compt_viv=0
                if etatCellule[x-c, y-c]==1:
                    compt_viv+=1
                if etatCellule[x-c, y]==1:
                    compt_viv+=1
                if etatCellule[x-c, y+c]==1:
                    compt_viv+=1
                if etatCellule[x, y-c]==1:
                    compt_viv+=1
                if etatCellule[x, y+c]==1:
                    compt_viv+=1
                if etatCellule[x+c, y-c]==1:
                    compt_viv+=1
                if etatCellule[x+c, y]==1:
                    compt_viv+=1
                if etatCellule[x+c, y+c]==1:
                    compt_viv+=1
                nbrAdjacent[x, y]=compt_viv
                
            j+=1
        i+=1
    redessiner()
    if flag >0: 
        fen.after(vitesse,play)

        

def redessiner(): #Redessine le tableau à partir de nbrAdjacent
    can.delete(ALL)
    i=0
    
    global nbrViv
    global chaineNbrViv
    nbrViv = 0
    
    while i!= width/c:
        j=0
        while j!= height/c: #Règles définissant l'apparition ou non de cases noires
            x=i*c
            y=j*c
            if nbrAdjacent[x,y]==3:
                etatCellule[x,y]=1
                can.create_rectangle(x, y, x+c, y+c, fill='black')
                nbrViv += 1
            elif nbrAdjacent[x,y]==2:
                if etatCellule[x,y]==1:
                    can.create_rectangle(x, y, x+c, y+c, fill='black')
                    nbrViv += 1
            elif nbrAdjacent[x,y]<2 or nbrAdjacent[x,y]>3:
                etatCellule[x,y]=0
            j+=1
        i+=1

    chaineNbrViv.configure(text = "Nombre de cellules vivantes : "+str(nbrViv))
#Variables
        
height = 560 #Hauteur du damier
width = 720 #Largeur du damier

c = 20 #taille des cellules

vitesse=50 #Vitesse de l'animation

nbrViv = 0 #Nombre de cellules vivants au total

flag=0
nbrAdjacent = {} #Nombre de cellules vivantes autour de chaque cellule
etatCellule = {} #Valeur 0 ou 1 si cellule morte ou vivante
i=0
while i!= width/c: #Initialisation du tableau en tout mort
    j=0
    while j!= height/c:
        x=i*c
        y=j*c
        etatCellule[x,y]=0
        j+=1
    i+=1

#Main
    
fen = Tk()

fen.title("Auto-Evolution. Oui.")

can = Canvas(fen, width =width, height =height, bg ='white')
can.bind("<Button-1>", click_gauche)
can.pack(side =TOP, padx =5, pady =5)

b1 = Button(fen, text ='Départ', command =go)
b2 = Button(fen, text ='Arrêt', command =stop)
b3 = Button(fen, text ='Configuration notable', command =LeFameux)
b1.pack(side=LEFT, padx =3, pady =3)
b2.pack(side=LEFT, padx =3, pady =3)
b3.pack(side=LEFT, padx =3, pady =3)

chaineNbrViv = Label(fen)
chaineNbrViv.configure(text = "Nombre de cellules vivantes : 0")
chaineNbrViv.pack(side=RIGHT, padx = 20)

entree = Entry(fen)
entree.bind("<Return>", change_vit)
entree.pack(side=RIGHT)
chaine = Label(fen)
chaine.configure(text = "Vitesse (durée d'un tour) :")
chaine.pack(side=RIGHT, padx = 30)

fen.mainloop()
