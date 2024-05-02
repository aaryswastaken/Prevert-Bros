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

    def revX(self):
        return V2(-self.x, self.y)

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

def convertCoords(p1, dy=720):
    print(f"dy={dy}, p1={p1}")
    return V2(0, dy) + p1.revY()

def rectFromPoints(p1, p2, corrected=True, dy=720):
    p1 = convertCoords(p1)
    p2 = convertCoords(p2)

    _p1 = V2(max(0, min(p1.x, p2.x)), max(0, min(p1.y, p2.y)))
    _p2 = V2(max(p1.x, p2.x), max(p1.y, p2.y))

    return pygame.Rect(_p1, _p2 - _p1)
