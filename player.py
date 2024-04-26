#
# @aaryswastaken, 2024
#

# This file defines a user class

import pygame

from object import Object
from common import V2, drawCross, drawRectangle, PLAYER
from renderer import convertCoords


class Player(Object):
    def __init__(self, move_a=500, jump_v=300):
        super().__init__()

        self.r = 30

        self.objType = PLAYER
        self.size = V2(self.r, self.r)
        self.move_a = move_a
        self.jump_v = jump_v

        self.static = False
        self.colliding = True
        self.free = False

        self.last_space = False

    def handleInput(self, keys, parent):
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

        if keys[pygame.K_SPACE] and parent.pE.isTouchingGround(self, parent.objects):
            if not self.last_space:
                self.vel.y = self.jump_v
                self.last_space = True
        else:
            self.last_space = False

    def isInScope(self, _p1, _p2):
        return self.pos.inside(_p1, _p2)

    def render(self, screen, vC, debug=False):
        absPos = self.pos - vC

        center = convertCoords(absPos)

        pygame.draw.circle(screen, "#0000ff", center, self.r)

        if debug:
            print("debug2")
            drawCross(screen, center)
            drawRectangle(screen, center - self.size, center + self.size)

    def __str__(self):
        return "Player"
