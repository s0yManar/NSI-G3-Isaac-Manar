from p5 import *

class Monstre:
    def __init__(self, x, y, patrol_limit, speed=2):
        self.x = x  # Position horizontale
        self.y = y  # Position verticale
        self.direction = 1  # Direction (1 = droite, -1 = gauche)
        self.speed = speed  # Vitesse de déplacement
        self.patrol_limit = patrol_limit  # Limites de patrouille

    def patrouille(self):
        # Mise à jour de la position
        self.x += self.speed * self.direction

        # Inverser la direction si une limite est atteinte
        if self.x > self.patrol_limit[1] or self.x < self.patrol_limit[0]:
            self.direction = -1*self.direction

    def draw(self):
        # Corps
        fill(0, 200, 200)
        ellipse(self.x, self.y, 60, 40)

        # Yeux
        fill(255)
        ellipse(self.x - 15, self.y - 10, 10, 10)
        ellipse(self.x + 15, self.y - 10, 10, 10)

        # Pupilles
        fill(0)
        ellipse(self.x - 15, self.y - 10, 5, 5)
        ellipse(self.x + 15, self.y - 10, 5, 5)

        # Bouche
        fill(255, 0, 0)
        arc(self.x, self.y + 10, 30, 10, 0, PI)

# Créer une instance de la classe Monster
monstre = Monstre(x=100, y=200, patrol_limit=(50, 750))

def setup():
    size(800, 600)  # Taille de la fenêtre

def draw():
    background(220)

    # Mettre à jour et dessiner le monstre
    monstre.patrouille()
    monstre.draw()

run()