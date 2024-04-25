#
# @aaryswastaken, 2024
#

# This file is in charge of rendering every element to the screen

import pygame


class RenderingEngine:
    def __init__(self, parent, size=(1280, 720)):
        self.parent = parent

        self.size = size
        self.dy = size[1]

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

        self.parent.clock = self.clock
        self.parent.key = pygame.key

    def newFrame(self):
        self.screen.fill("black")

    def render(self, obj, debug=False):
        # dy is to flip the screen
        print(f"Rendering {str(obj)} from rE")
        obj.render(self.screen, dy=self.dy, debug=debug)

    def finaliseFrame(self):
        pygame.display.flip()
