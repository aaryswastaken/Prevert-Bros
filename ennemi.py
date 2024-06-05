import pygame

from object import Object
from common import V2, drawCross, drawRectangle, convertCoords, PLAYER

class Ennemi(Object):
    """
    Créer des NPC, issus de la classe Objet
    """
    
    def __init__(self, chemin_image):
        super().__init__()
        
        self.r = 15

        self.chemin_image = pygame.image.load(chemin_image).convert()
        self.objType = NPC
        self.size = V2(self.r, self.r)
        Object.vel = V2(15,15) #valeur aléatoire à voir, j'ai pas tout compris ce que ça donnait
        
        self.static = False
        self.colliding = True
        
        self.free = False 
        self.last_space = False

    def isInScope(self, _p1, _p2):
        """
        Regarde si l'ennemi est bien dans l'écran
        """
        return self.pos.inside(_p1, _p2)

    def render(self, screen, vC, debug=False): 
        absPos = self.pos - vC

        screen.blit(self.chemin_image, absPos)


    def deplacement_droite(self,dt):
        """
        permet le déplacement vers la droite de l'ennemi
        """
        self.pos[0] += self.vel * dt
    
    def deplacement_gauche(self, dt):
        """
        permet le déplacement vers la gauche de l'ennemi
        """
        self.pos[0] -= self.vel* dt
        

    def __str__(self):
        return "Ennemi"

