#
# @aaryswastaken, 2024
#

# This file defines a user class

import pygame

from object import Object
from common import V2, drawCross, drawRectangle, PLAYER


class Player(Object):
    def __init__(self, move_a=500):
        super().__init__()

        self.objType = PLAYER
        self.size = V2(30, 30)
        self.move_a = move_a

        self.static = False
        self.colliding = True
        self.free = False

    def handleInput(self, keys):
        print("Hello from Player.handleInput")
        if keys[pygame.K_d]:
            print("right")
            self.free = False
            self.acc.x = self.move_a
        elif keys[pygame.K_a]:
            print("left")
            self.free = False
            self.acc.x = -self.move_a
        else:
            self.free = True
            self.acc.x = 0

    def isInScope(self, _p1, _p2):
        return self.pos.inside(_p1, _p2)

    def render(self, screen, dy=0, debug=False):
        r = self.size.x
        center = V2(r, dy - r) + self.pos.revY()

        pygame.draw.circle(screen, "#0000ff", center, r)

        if debug:
            print("debug2")
            drawCross(screen, center)
            drawRectangle(screen, center - self.size, center + self.size)

    def __str__(self):
        return "Player"
