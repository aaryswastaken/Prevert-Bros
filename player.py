#
# @aaryswastaken, 2024
#

# This file defines a user class

import pygame

from object import Object
from common import V2, drawCross, drawRectangle, convertCoords, PLAYER


class Player(Object):
    """
        Derives the player object from the bare Object class
    """

    def __init__(self, move_a=500, jump_v=300, image =""):
        super().__init__()

        self.r = 30

        self.objType = PLAYER
        self.size = V2(self.r, self.r)
        self.move_a = move_a # move acceleration
        self.jump_v = jump_v # jump velocity
        self.image = image

        self.static = False
        self.colliding = True
        self.free = False

        self.last_space = False

    def handleInput(self, keys, parent):
        # print("Hello from Player.handleInput")

        # Handles the input for the player
        if keys[pygame.K_RIGHT]:
            print("right")
            self.free = False
            self.acc.x = self.move_a # change acceleration accordingly
        elif keys[pygame.K_LEFT]:
            print("left")
            self.free = False
            self.acc.x = -self.move_a
        else:
            self.free = True
            self.acc.x = 0

        if keys[pygame.K_SPACE] and parent.pE.isTouchingGround(self, parent.objects): 
            # if space is pressed and the physics engine tells us the player is touching grounf
            if not self.last_space:
                self.vel.y = self.jump_v # set the velocity to jump
                self.last_space = True # debounce 
        else:
            self.last_space = False

    def isInScope(self, _p1, _p2):
        # Check if the player is in scope
        return self.pos.inside(_p1, _p2)

    def render(self, screen, vC, debug=False):
        # Render the user to the screen, currently a cute lil circle
        absPos = self.pos - vC
        center = convertCoords(absPos)

        if self.image != "":
            loadedImage = pygame.image.load("./PERSO.png")
            loadedImage = pygame.transform.scale(loadedImage, self.size*3)
            screen.blit(loadedImage, (center.x-self.r, center.y-self.r/0.55))
        else:
            #au cas où on oublie d'ajouter le chemin pour l'image du perso
            
            pygame.draw.circle(screen, "#0000ff", center, self.r)

        if debug:
            print("debug2")
            drawCross(screen, center)
            drawRectangle(screen, center - self.size, center + self.size)

    def __str__(self):
        return "Player"

