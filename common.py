#
# @aaryswastaken
#

# This class defines types

import pygame


PLAYER = 0
GROUND = 1
NPC = 2
STATIC = 3


class V2(pygame.Vector2):
    def inside(self, p1, p2):
        return p1.x <= self.x <= p2.x and p1.y <= self.y <= p2.y

    def abs(self):
        return V2(abs(self.x), abs(self.y))

    def revY(self):
        return V2(self.x, -self.y)

    def onlyX(self):
        return V2(self.x, 0)

    def onlyY(self):
        return V2(0, self.y)

def drawCross(screen, p1, color="#ff0000", size=100):
    vx = V2(size, 0)
    vy = V2(0, size)

    pygame.draw.line(screen, color, p1+vx, p1-vx)
    pygame.draw.line(screen, color, p1+vy, p1-vy)

def drawRectangle(screen, p1, p2, color="#ff0000"):
    pygame.draw.rect(screen, color, pygame.Rect(p1, p2-p1), width=1)
