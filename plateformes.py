from p5 import *

class Plateforme:
    def __init__(self,x,y,longueur,largeur,hauteur_brique,longueur_brique):
        self.x = x
        self.y = y
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur_brique = hauteur_brique
        self.longueur_brique = longueur_brique

    def dessiner(self) :
        rect(self.x,self.y,self.longueur,self.largeur)

    def briques(self):
        for x in range(self.y,self.y+self.largeur,self.hauteur_brique):
            o = (x//self.hauteur_brique%2)*(self.longueur_brique//2)
            for y in range(self.x+o,self.x + self.longueur,self.longueur_brique):
                rect(y,x,self.longueur_brique,self.hauteur_brique)
            
        
    def couleur(self,r,g,b):
        fill(r,g,b)


def setup():
    size(800,600)
    background(255)
    global plat, plat2
    plat = Plateforme(0,67,456,30,20,30)
    plat2 = Plateforme(600,300,200,45,10,15)

def draw():
    global plat, plat2
    plat.couleur(123,43,78)
    plat.dessiner()
    plat.briques()
    plat2.couleur(147,60,20)
    plat2.dessiner()
    plat2.briques()


run()