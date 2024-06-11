#
# @aaryswastaken, 2024
#

# This file defines a couple of objects

import pygame
from pygame.key import stop_text_input
from pygame.time import wait

from common import V2, drawCross, rectFromPoints, convertCoords, GROUND, STATIC


class Object:
    """
        This class defines a generic object
    """

    def __init__(self):
        self.uuid = None
        
        self.pos = V2(0,0) # Position vector
        self.vel = V2(0,0) # speed vector
        self.acc = V2(0,0) # acceleration vector

        # size if applicable
        self.size = V2(0,0)

        # That has to change (TODO)
        self.static = True
        self.colliding = True
        self.objType = None

    def isInScope(self, _p1, _p2):
        # This function returns True if the object has to be rendered to the screen
        # using p1 and p2 as two opposites point of the said screen
        return False

    def handleInput(self, keys, parent):
        pass

    def render(self, screen, vC, debug=False):
        pass

    def __str__(self):
        return "Empty object"

class RectGroundPart(Object):
    """
        Defines a ground part that is rectangular
    """

    def __init__(self, pos, size, color, image = ""):
        super().__init__()

        self.size = size.abs()
        self.pos = pos
        
        self.color = color

        self.objType = GROUND
        self.image = image


    def isInScope(self, p1, p2):  
        self.p1 = self.pos + self.size.onlyY()
        self.p2 = self.pos + self.size.onlyX()
        top_pos = -1 if self.p1.y < p1.y else 1 if self.p1.y > p2.y else 0
        bottom_pos = -1 if self.p2.y < p1.y else 1 if self.p2.y > p2.y else 0
        # if we are not both above screen or both below screen, that means we are vertically visible
        verticaly_visible = top_pos * bottom_pos != 1

        left_pos = -1 if self.p1.x < p1.x else 1 if self.p1.x > p2.x else 0
        right_pos = -1 if self.p2.x < p1.x else 1 if self.p2.x > p2.x else 0
        horizontal_visible = left_pos * right_pos != 1

        return verticaly_visible and horizontal_visible

    def render(self, screen, viewingCoordinates, debug=False):
        # render the object to the screen, here a rectangle
        absPos = self.pos - viewingCoordinates

        if (self.image != ""):
            loadedImage = pygame.image.load("./plateforme.png")
            loadedImage = pygame.transform.scale(loadedImage, self.size)
            screen.blit(loadedImage, rectFromPoints(absPos, absPos + self.size))
        else :
            r = screen.fill(self.color, rectFromPoints(absPos, absPos + self.size))
            
        # if debug, we print the boundaries too 
        if debug:
            print("debug")
            drawCross(screen, r.center)
            print(f"CrossA {convertCoords(self.pos)}")
            drawCross(screen, convertCoords(absPos), size=50)
            print(f"CrossB {convertCoords(self.pos + self.size.revY())}")
            drawCross(screen, convertCoords(absPos + self.size), size=50)


    def __str__(self):
        return f"Rectangle: {self.pos}, {self.pos + self.size}"


class Cookie(Object):

    def __init__(self, pos):
        super().__init__()

        self.pos = pos
        self.r = 10
        self.objType = STATIC
        self.size = V2(self.r, self.r)

        self.static = True
        self.colliding = True
        self.free = False
        self.collected = False
        
    def isInScope(self, p1, p2):  
        self.p1 = self.pos + self.size.onlyY()
        self.p2 = self.pos + self.size.onlyX()
        top_pos = -1 if self.p1.y < p1.y else 1 if self.p1.y > p2.y else 0
        bottom_pos = -1 if self.p2.y < p1.y else 1 if self.p2.y > p2.y else 0
        # if we are not both above screen or both below screen, that means we are vertically visible
        verticaly_visible = top_pos * bottom_pos != 1

        left_pos = -1 if self.p1.x < p1.x else 1 if self.p1.x > p2.x else 0
        right_pos = -1 if self.p2.x < p1.x else 1 if self.p2.x > p2.x else 0
        horizontal_visible = left_pos * right_pos != 1

        return verticaly_visible and horizontal_visible

    def render(self, screen, viewingCoordinates, debug = False):
        if not self.collected: #Si la pièce n'a pas été collecté
            #Création de pièces
            absPos = self.pos - viewingCoordinates
            centre = convertCoords(absPos)
            pygame.draw.circle(screen, "#db911a" , centre, self.r)

    def __str__(self):
        return "Cookie"
    
