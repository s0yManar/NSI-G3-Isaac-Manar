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

class Plateforme:
    def __init__(self,x,y,longueur,largeur):
        self.x = x
        self.y = y
        self.longueur = longueur
        self.largeur = largeur

    def dessiner(self) :
        round(10)
        rect(self.x,self.y,self.longueur,self.largeur)
        

    def couleur(self,r,g,b):
        fill(r,g,b)

run()