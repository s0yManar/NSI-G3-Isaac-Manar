from p5 import *

class Clef :
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        
    def dessiner(self) :
        no_stroke()
        fill(self.r, self.g, self.b)
        ellipse(400,300,50,50)
        rect(423,290,95,20)
        rect(460,290,20,30)
        rect(490,290,20,30)
        fill(255)
        ellipse(400,300,30,30)



def setup():
    size(800,600)
    background(255)
    global cle
    cle = Clef(243,187,39)

def draw() : 
    global cle 
    background(255)
    cle.dessiner()

run()