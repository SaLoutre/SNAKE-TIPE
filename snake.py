# On importe Tkinter

from tkinter import *
from random import randrange


def dep():
    global x,y,pX,pY
    global Serpent
    global direction
    
    can.delete('all')
    #i=len(Serpent)-1 #i=nbp-1
    #j=0
    #while i > 0:
        #Serpent[i][0]=Serpent[i-1][0]
        #Serpent[i][1]=Serpent[i-1][1]
        #i=i-1
    for k in range(nbp):
        can.create_rectangle(pX, pY, pX+a, pY+b, outline='red', fill='red')
        k=k+1

    if direction  == 'gauche':
        Serpent[0][0]  = Serpent[0][0] - dx
        if Serpent[0][0] < 5:
            direction = 'none'
            col()
            
            
    elif direction  == 'droite':
        Serpent[0][0]  = Serpent[0][0] + dx
        if Serpent[0][0] > 488:
            direction = 'none'
            col()
            
    elif direction  == 'haut':
        Serpent[0][1]  = Serpent[0][1] - dy
        if Serpent[0][1] < 5:
            direction='none'
            col()
            
    elif direction  == 'bas':
        Serpent[0][1]  = Serpent[0][1] + dy
        if Serpent[0][1] > 488:
            direction = 'none'
            col()
            

            
    can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0]+10, Serpent[0][1]+10,outline='blue', fill='white')
    test()
    

    if flag != 0:
        fen.after(60, dep)
 
def newGame():
    global pX,pY
    global flag
    if flag == 0:
        flag = 1
    dep()

def left(event):
    global direction
    direction = 'gauche'
 
def right(event):
    global direction
    direction = 'droite'
 
def up(event):
    global direction
    direction = 'haut'
 
def down(event):
    global direction
    direction = 'bas'

def arret(event):
    global direction
    direction = 'none'
        
def dessine_cercles(self):
        for i in range(nbp):
            x, y = [rd.randint(1, self.size) for j in range(2)]
            diameter = rd.randint(1, 50)
            self.dechet        
      
def test():
    global dechet
    global x,y,pX,pY
    global Serpent
    #o=0
    if Serpent[1][0]>pX-7 and  Serpent[1][0]<pX+7:
      if Serpent[1][1]>pY-7 and Serpent[1][1]<pY+7:
            #On remet une pomme au hasard
            pX = randrange(5, 495)
            pY = randrange(5, 495)
            can.coords(dechet,pX, pY, pX+5, pY+5)
            

def col():
    tex1 = Label(fen, text="Obstacle détecté", bg='red' , fg='white')
    tex1.pack(padx=0, pady=11)
    fen.after(1000, tex1.destroy)#désaffiche le message d'alerte
    
            
nbp=randrange(1, 20)#Nombre de déchets
x = 250 #coordonnée
y = 250 #coordonnée   
dx, dy = 5, 5 #vitesse du serpent

flag = 0
direction = 'none' #mouvement auto
Serpent=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]] #le serpent

pX = randrange(5, 495)
pY = randrange(5, 495)
            
a = randrange(1, 10)
b = randrange(1, 10)
# On cree une fenetre, racine de notre interface
fen = Tk()



# Dans Fenetre nous allons creer un objet type Canvas qui se nomme zone_dessin
# Nous donnons des valeurs aux proprietes "width", "height", "bg", "bd"
can = Canvas(fen, width=500,height=500,bg="black")
can.pack(side=TOP, padx=5, pady=5) #Affiche le Canvas



dechet = can.create_rectangle(pX, pY, pX+a, pY+b, outline='red', fill='red')


b1 = Button(fen, text='Lancer', command=newGame, bg='black' , fg='red')
b1.pack(side=LEFT, padx=5, pady=5)



b2= Button(fen, text='Quitter', command=fen.destroy, bg='red', fg='white')
b2.pack(side=RIGHT, padx=10, pady=10)


fen.bind('<d>', right)
fen.bind('<q>', left)
fen.bind('<z>' , up)
fen.bind('<s>', down)
fen.bind('<a>', arret)
fen.bind('<l>', quit)

# On demarre la boucle Tkinter qui s'interompt quand on ferme la fenetre
fen.mainloop()
