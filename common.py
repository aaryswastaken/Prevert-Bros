#
# @aaryswastaken
#

# This class defines types

import pygame


PLAYER = 0
GROUND = 1
NPC = 2
STATIC = 3
ENNEMY = 4


class V2(pygame.Vector2):
    """
        Extended version of the vec2
    """

    def inside(self, p1, p2):
        """
            inside: returns true if the point located at self is in the (p1, p2) rectangle

            params:
             - p1, p2: Points
            
            returns:
             - out: bool
        """
        return p1.x <= self.x <= p2.x and p1.y <= self.y <= p2.y

    def abs(self):
        """
            returns a new vector that is the opposite
        """

        return V2(abs(self.x), abs(self.y))

    def revY(self):
        """
            returns a new vector that is the opposite regarding the y coordinate
        """

        return V2(self.x, -self.y)

    def revX(self):
        """
            same as revY but for X
        """

        return V2(-self.x, self.y)

    def onlyX(self):
        """
            returns only (X, 0)
        """

        return V2(self.x, 0)

    def onlyY(self):
        """
            returns only (0, y)
        """

        return V2(0, self.y)

    def clone(self):
        return V2(self.x, self.y)

def drawCross(screen, p1, color="#ff0000", size=100):
    """
        drawCross: draws a cross at a given coordinate

        inputs:
         - screen: Screen, the screen to update
         - p1: Vec2, a point at which you want to draw a cross
         - color: Color (optionnal)
         - size: int (optionnal)
    """

    vx = V2(size, 0)
    vy = V2(0, size)

    pygame.draw.line(screen, color, p1+vx, p1-vx)
    pygame.draw.line(screen, color, p1+vy, p1-vy)

def drawRectangle(screen, p1, p2, color="#ff0000"):
    """
        drawRectabgle: draws a rectangle

        inputs:
         - screen: Screen, the screen tu update
         - p1: Vec2 point A
         - p2: Vec2 point B
         - color: Color (optionnal)
    """

    pygame.draw.rect(screen, color, pygame.Rect(p1, p2-p1), width=1)

def convertCoords(p1, dy=720):
    """
        convertCoords: shifts coordinate from usual base to pygame base

        usual base  (0,0) --->
                      |
                      V
        
        inputs:
         - p1: Vec2, point
         - dy: int, the size of the screen (optionnal)

        returns:
         - out: Vec2
    """

    print(f"dy={dy}, p1={p1}")
    return V2(0, dy) + p1.revY()

def rectFromPoints(p1, p2, corrected=True, dy=720):
    """
        rectFromPoints: assess the strangely built Rectangle constructing method

        inpurs:
         - p1: Vec2 point A
         - p2: Vec2 point B
         - corrected: bool, if convertCoords has already been called
         - dy: int, the value to pass to convertCoords
        
        output:
         - out: Rect, the rectangle
    """
    
    p1 = convertCoords(p1)
    p2 = convertCoords(p2)

    _p1 = V2(max(0, min(p1.x, p2.x)), max(0, min(p1.y, p2.y)))
    _p2 = V2(max(p1.x, p2.x), max(p1.y, p2.y))

    return pygame.Rect(_p1, _p2 - _p1)
