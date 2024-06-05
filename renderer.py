#
# @aaryswastaken, 2024
#

# This file is in charge of rendering every element to the screen

import pygame

from common import V2


class RenderingEngine:
    """
        The rendering engine is written so that we can later replace it with a cutom opengl renderer
    """

    def __init__(self, parent, size=(1280, 720), pfactor = 2):
        self.parent = parent

        self.size = size
        self.dy = size[1]

        self.pFactor = pfactor # parallax factor for the background
        
        self.font = None
        

    def init(self): 
        # initialise the renderer

        pygame.init() # open a window
        self.screen = pygame.display.set_mode(self.size) # set it to the right side
        self.time = pygame.time
        self.clock = pygame.time.Clock() # define the world clock

        self.parent.time = self.time
        self.parent.clock = self.clock # set the clock back to the GameManager
        self.parent.key = pygame.key # same for keys

        self.font = pygame.font.SysFont("Jetbrains Mono", 50)

        self.bg = None
        if self.parent.debug:
            # if debug, we use the bg_debug.png as a background
            self.bg = pygame.image.load("bg_debug.png")
            self.bg = self.bg.convert()

    def newFrame(self):
        # Initialise a new Frame (sets everything back black)

        self.screen.fill("black")

    def renderTime(self, time, targetTime):
        # Render the remaining time 

        time = self.font.render(f"{targetTime - time:.0f}", False, "#ffffff")
        self.screen.blit(time, (5, 5))

    def printBG(self, vpos):
        # Print the background, vpos is the viewing position defined as the bottom left corner of the viewing sight

        if self.bg is None:
            self.screen.fill("black")
            return 1
        
        bgSize = self.bg.get_rect()
        
        # Should write this as a shader
        _vpos = vpos
        cnt = 0
       
        # TODO: Because not working. Background need to self replicate to make a long one
        while vpos.x < self.size[0]:
            self.screen.blit(self.bg, vpos / self.pFactor)
            vpos += V2(bgSize.w * self.pFactor, 0)


    def render(self, obj, viewingCoords, debug=False):
        # dy is to flip the screen
        print(f"Rendering {str(obj)} from rE")
        obj.render(self.screen, viewingCoords, debug=debug)

    def finaliseFrame(self):
        # End the frame by showing the player the screen 
        
        pygame.display.flip()

