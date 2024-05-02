#
# @aaryswastaken, 2024
#

# This file is in charge of rendering every element to the screen

import pygame

from common import V2


class RenderingEngine:
    def __init__(self, parent, size=(1280, 720), pfactor = 2):
        self.parent = parent

        self.size = size
        self.dy = size[1]

        self.pFactor = pfactor

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

        self.parent.clock = self.clock
        self.parent.key = pygame.key

        self.bg = None
        if self.parent.debug:
            self.bg = pygame.image.load("bg_debug.png")
            self.bg = self.bg.convert()

    def newFrame(self):
        self.screen.fill("black")

    def printBG(self, vpos):
        if self.bg is None:
            self.screen.fill("black")
            return 1
        
        bgSize = self.bg.get_rect()
        
        # Should write this as a shader
        _vpos = vpos
        cnt = 0
       
        while vpos.x < self.size[0]:
            self.screen.blit(self.bg, vpos / self.pFactor)
            vpos += V2(bgSize.w * self.pFactor, 0)


    def render(self, obj, viewingCoords, debug=False):
        # dy is to flip the screen
        print(f"Rendering {str(obj)} from rE")
        obj.render(self.screen, viewingCoords, debug=debug)

    def finaliseFrame(self):
        pygame.display.flip()

