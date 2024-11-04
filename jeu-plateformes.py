from p5 import *

def setup():
    size(800,600)
    background(255)
    global plat
    plat = Plateforme(0,67,456,30)

def draw():
    global plat
    plat.couleur(123,43,78)
    plat.dessiner()
    plat.briques(20,30)

class Plateforme:
    def __init__(self,x,y,longueur,largeur):
        self.x = x
        self.y = y
        self.longueur = longueur
        self.largeur = largeur

    def dessiner(self) :
        rect(self.x,self.y,self.longueur,self.largeur)

    def briques(self,hauteur_brique,longueur_brique):
        for x in range(self.y,self.y+self.largeur,hauteur_brique):
            o = (x//hauteur_brique%2)*(longueur_brique//2)
            for y in range(self.x+o,self.x + self.longueur,longueur_brique):
                rect(y,x,longueur_brique,hauteur_brique)
            
        
    def couleur(self,r,g,b):
        fill(r,g,b)


run()