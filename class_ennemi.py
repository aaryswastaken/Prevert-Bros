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
        self.distance = 30
        self.objType = NPC
        self.size = V2(self.r, self.r)
        Object.vel = V2(15,15) #valeur aléatoire à voir, j'ai pas tout compris ce que ça donnait
        
        self.static = False
        self.colliding = True

        #les 2 suivants j'ai pas trop compris à quoi ils correspondaient mais j'ai laissé au cas où
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

        if debug:
            print("debug2")
            drawCross(screen, center)
            drawRectangle(screen, center - self.size, center + self.size)

    def deplacement(self):
        """
        permet le déplacement automatique de l'ennemi
        """
        #TANT QUE JEU NEST PAS TERMINE JE SAIS PAS TROP QUOI DIRE
            self.pos[0] += self.vel * self.distance
            self.after(500, self.pos[0] -= self.vel* self.distance)
        
        

    def __str__(self):
        return "Ennemi"

