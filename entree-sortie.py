from p5 import *

class Entree :
    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY

    def dessiner(self):
        fill(200,70,125)
        stroke(3)
        rect(self.posX,self.posY,58,80)
        fill(0)
        ellipse(self.posX+54,self.posY+45,12,8)

def setup():
    global porte, porte1
    size(800,600)
    background(255)
    porte = Entree(250,200)
    porte1 = Entree(190,34)

def draw():
    global porte, porte1
    porte.dessiner()
    porte1.dessiner()


run()