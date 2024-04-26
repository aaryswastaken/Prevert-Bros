#
# @aaryswastaken, 2024
#

# This file defines a couple of objects

import pygame
from pygame.key import stop_text_input
from pygame.time import wait

from common import V2, drawCross, rectFromPoints, convertCoords, GROUND


class Object:
    def __init__(self):
        self.uuid = None
        
        self.pos = V2(0,0)
        self.vel = V2(0,0)
        self.acc = V2(0,0)

        self.size = V2(0,0)

        self.static = True
        self.colliding = True
        self.objType = None

    def isInScope(self, _p1, _p2):
        # This function returns True if the object has to be rendered to the screen
        # using p1 and p2 as two opposites point of the said screen
        return False

    def handleInput(self, keys):
        pass

    def render(self, screen, vC, debug=False):
        pass

    def __str__(self):
        return "Empty object"

class RectGroundPart(Object):
    def __init__(self, pos, size, color):
        super().__init__()

        self.size = size.abs()
        self.pos = pos
        
        self.color = color

        self.objType = GROUND


    def isInScope(self, p1, p2):  # Variables vraiment très mal nommées
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
        absPos = self.pos - viewingCoordinates

        r = screen.fill(self.color, rectFromPoints(absPos, absPos + self.size))

        if debug:
            print("debug")
            drawCross(screen, r.center)
            print(f"CrossA {convertCoords(self.pos)}")
            drawCross(screen, convertCoords(absPos), size=50)
            print(f"CrossB {convertCoords(self.pos + self.size.revY())}")
            drawCross(screen, convertCoords(absPos + self.size), size=50)


    def __str__(self):
        return f"Rectangle: {self.pos}, {self.pos + self.size}"
