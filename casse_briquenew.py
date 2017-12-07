# Imports
from tkinter import *
from math import *
from random import *
import time
import winsound
from msvcrt import getch

def CouleurAleatoire() :
    palette=['orangered','cyan','yellowgreen','green','red','blue','orange','yellow','dark green','white','mediumvioletred','pink','aquamarine','bisque','blueviolet','cadetblue','burlywood','coral','cornflowerblue','tomato','moccasin','darkmagenta','whitesmoke','springgreen','slateblue','skyblue','salmon','royalblue','rosybrown','plum','palegreen','palegoldenrod','orchid','papayawhip']
    # nb aléatoire de 0 à 34
    c=int(random()*34)
    couleur=palette[c]
    return couleur

class Bordure:
    def __init__(bord,canvas,dimension=[1000,1000],couleur='brown'):
        bord.canvas = canvas
        bord.dimension = dimension
        bord.epaisseur = 3
        x0 = 2
        y0 = 2
        x1 = dimension[0]+2
        y1 = dimension[1]+2
        dx = bord.epaisseur
        dy = bord.epaisseur
        bord.id = tableau.create_polygon([x0,y0,x1,y0,x1,y1,x1-dx,y1,x1-dx,y0+dy,x0+dx,y0+dy,x0+dx,y1,x0,y1],fill='sienna')
    def PositionBalle(bord, balle):
        global dxBalle, dyBalle
        # Bordure du haut ?
        if balle.position[1] < 2+balle.rayon:
            dyBalle=-dyBalle
        # Bordure de gauche ?
        if balle.position[0] <= 2+balle.rayon:
            dxBalle=-dxBalle
        # Bordure de droite ?
        if balle.position[0] >= bord.dimension[0]-balle.rayon:
            dxBalle=-dxBalle

class Plateforme:
    def __init__(plte, canvas,dimension=[50,10],position=[525,675],couleur='sienna'):
        plte.canvas=canvas
        plte.dimension=dimension
        plte.position=position
        plte.couleur=couleur
        # Crée l'objet graphique
        dx=plte.dimension[0]/2
        dy=plte.dimension[1]/2
        x=plte.position[0]
        y=plte.position[1]
        plte.id = tableau.create_polygon([x-dx,y-dy,x-dx,y+dy,x+dx,y+dy,x+dx,y-dy,x-dx,y-dy],fill='sienna')
    def deplacer(plte, x, y):
        # La plateforme est-elle trop à gauche ?
        if x<0:
            x=0
        # La plateforme est-elle trop à droite ?
        if x>bordure.dimension[0]:
            x=bordure.dimension[0]
        # Modifie la position de la plateforme
        plte.position = [x, y]
        dx=plte.dimension[0]/2
        dy=plte.dimension[1]/2
        plte.canvas.coords(plte.id, x-dx,y-dy,x-dx,y+dy,x+dx,y+dy,x+dx,y-dy,x-dx,y-dy)
    def PositionBalle(brique, balle):
        global dyBalle
        # Quand la balle va vers le haut, la plateforme est transparente
        if dyBalle<0 :
            return
        # Calcul de la distance entre la balle et la plateforme
        dx = abs(plateforme.position[0] - balle.position[0]) - plateforme.dimension[0]/2 - balle.rayon
        dy = abs(plateforme.position[1] - balle.position[1]) - plateforme.dimension[1]/2 - balle.rayon
        if dx<=0 and dy<=0:
            dyBalle=-dyBalle

        
class Balle:
    def __init__(balle, canvas):
        balle.canvas = canvas
        balle.rayon = 5
        balle.position = [0, 0]
        x=balle.position[0]
        y=balle.position[1]
        balle.id = balle.canvas.create_oval(x-balle.rayon, y-balle.rayon, x+balle.rayon, y+balle.rayon, fill='grey')
    def deplacer(balle, x, y):
        balle.position=[x,y]
        balle.canvas.coords(balle.id, x-balle.rayon, y-balle.rayon, x+balle.rayon, y+balle.rayon)


class Brique():
    def __init__(b,canvas,position=[0,0],dimension=[40,20],couleur=-1):
        # Mémorise les caractéristiques de l'objet
        b.canvas=canvas
        b.position=position
        b.dimension=dimension
        if couleur == -1:
            couleur = CouleurAleatoire()
        b.couleur=couleur
        b.visible=True
        # Crée l'objet graphique
        dx=b.dimension[0]/2
        dy=b.dimension[1]/2
        x=b.position[0]
        y=b.position[1]
        b.id=tableau.create_polygon([x-dx,y-dy,x-dx,y+dy,x+dx,y+dy,x+dx,y-dy,x-dx,y-dy],fill=b.couleur)
    def Afficher(brique, bOui):
        if bOui:
            tableau.itemconfigure(brique.id, state=NORMAL)
        else:
            tableau.itemconfigure(brique.id, state=HIDDEN)
        brique.visible=bOui
    def PositionBalle(brique, balle):
        global tableau, dyBalle
        if not brique.visible:
            return
        dx = abs(brique.position[0] - balle.position[0])
        dy = abs(brique.position[1] - balle.position[1])
        if dx<=brique.dimension[0]+balle.rayon and dy<=brique.dimension[1]+balle.rayon:
            brique.Afficher(False)
            dyBalle=-dyBalle
        

# Définition des variables
dxBalle=4
dyBalle=-4
timer=20
briques=[]
bToucheEntree = False

def InitialisationJeu(bReafficherBriques):
    global dxBalle, dyBalle
    dxBalle=4
    dyBalle=-4
    balle.deplacer(plateforme.position[0], plateforme.position[1]-plateforme.dimension[1]/2-balle.rayon)
    if bReafficherBriques:
        for b in briques: 
            b.Afficher(True)

# Création d'une fonction qui permet de déplacer la plateforme
def Clavier(event):
    global canvas, plateforme
    global bToucheEntree
    touche = event.keysym
    #print(touche)

    if touche == 'Return':
        bToucheEntree = True
  
    # déplacement vers la droite
    if touche == 'Right':
        DeltaX = 20
    # déplacement vers la gauche
    elif touche == 'Left':
        DeltaX =- 20
    else:
        return

    # on déplace la plateforme à sa nouvelle position
    plateforme.deplacer(plateforme.position[0]+DeltaX, plateforme.position[1])


def Tic():
    global dxBalle, dyBalle, briques, plateforme

    # Déplace la balle
    balle.deplacer(balle.position[0]+dxBalle, balle.position[1]+dyBalle)

    # Détection de l'impact sur un objet
    bordure.PositionBalle(balle)
    plateforme.PositionBalle(balle)
    for b in briques: 
        b.PositionBalle(balle)

    # Perdu ?
    if balle.position[1] > bordure.dimension[1]:
        Message("Perdu !")
        InitialisationJeu(True)

    # On relance le timer
    fenetre.after(timer, Tic)

    # Mise à jour du dessin
    tableau.update()

def Message(msg):
    global bToucheEntree
    # Affiche le message
    id = tableau.create_text(bordure.dimension[0]/2, bordure.dimension[1]/2, text=msg+"\nAppuyer sur Entrée", font=('Helvetica', 36, 'bold'), justify=CENTER)
    # Attend l'appui sur la touche Entrée
    bToucheEntree = False
    while not bToucheEntree:
        tableau.update()
    # Efface le message
    tableau.delete(id)

# Initialisation de la zone de dessin
fenetre=Tk(className='Casse brique')
tableau=Canvas(fenetre,width=800,height=710)

# On crée la bordure
bordure=Bordure(tableau, [800,710])

# On crée les briques
dimension_brique = [41, 20]
espacement_brique = 5
nx_brique = int((bordure.dimension[0]-bordure.epaisseur*2-espacement_brique)/(dimension_brique[0]+espacement_brique))
x0_brique = 33
y0_brique = 50
dx_brique = espacement_brique+dimension_brique[0]
dy_brique = espacement_brique+dimension_brique[1]
for ix in range(nx_brique):
    for iy in range(6):
        briques=briques+[Brique(tableau, [x0_brique+ix*dx_brique,y0_brique+iy*dy_brique], dimension_brique)]
tableau.pack()

# On crée la plateforme
plateforme=Plateforme(tableau)
    
# On crée la balle
balle=Balle(tableau)
tableau.pack()

# Attache les évènement clavier à la plateforme
fenetre.bind('<Key>', Clavier)

# Initialise le jeu
InitialisationJeu(True)

Message("Pour démarrer le jeu :")

# Lance le timer qui va gérer l'animation
fenetre.after(timer, Tic)

# Rentre dans la boucle principale de gestion des évènements
mainloop()
