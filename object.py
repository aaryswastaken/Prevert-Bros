#
# @aaryswastaken, 2024
#

# This file defines a couple of objects

import pygame
from pygame.time import wait

from common import V2, drawCross, GROUND


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

    def render(self, screen, dy=0, debug=False):
        pass

    def __str__(self):
        return "Empty object"

class RectGroundPart(Object):
    def __init__(self, p1, p2, color):
        super().__init__()

        # TODO: refactor p1 and p2 with pos and size
        self.p1 = p1
        self.p2 = p2
        self.size = (self.p1 - self.p2).abs()
        self.color = color

        self.objType = GROUND

        self.pos = (p1 + p2) / 2

    def isInScope(self, p1, p2):  # Variables vraiment très mal nommées
        top_pos = -1 if self.p1.y < p1.y else 1 if self.p1.y > p2.y else 0
        bottom_pos = -1 if self.p2.y < p1.y else 1 if self.p2.y > p2.y else 0
        # if we are not both above screen or both below screen, that means we are vertically visible
        verticaly_visible = top_pos * bottom_pos != 1

        left_pos = -1 if self.p1.x < p1.x else 1 if self.p1.x > p2.x else 0
        right_pos = -1 if self.p2.x < p1.x else 1 if self.p2.x > p2.x else 0
        horizontal_visible = left_pos * right_pos != 1

        return verticaly_visible and horizontal_visible

    def render(self, screen, dy=0, debug=False):
        r = screen.fill(self.color, pygame.Rect(V2(0, dy - self.size.y) + self.p1.revY(), self.size))

        if debug:
            print("debug")
            drawCross(screen, r.center)


    def __str__(self):
        return f"Rectangle: {self.p1}, {self.p2}"
