# 
# @aaryswastaken, 2024
#

# This file contains the game manager, principal class of the game.
# It is responsible for the management of all the entities, the 
# physics engine and the rendering engine

import pygame

from physics import PhysicsEngine
from renderer import RenderingEngine
from common import V2


class GameManager():
    def __init__(self, debug=False, tfps=60):
        self.debug = debug 
        self.targetFps = tfps

        self.pE = PhysicsEngine()
        self.rE = RenderingEngine(self)

        self.objects = []
        self.inputObjects = []
        self.uuid_counter = 0

        self.clock = None
        self.key = None
        self.rE.init()

        self.dt = 0
        self.stop = False

        self.viewingCoordinates = V2(0, 0)
        self.halfScreen = V2(self.rE.size[0] / 2, self.rE.size[1] / 2)

    def addObject(self, obj, hasInput=False):
        obj.uuid = self.uuid_counter
        self.uuid_counter += 1

        self.objects.append(obj)

        if hasInput:
            self.inputObjects.append(obj)

    def run(self):
        if self.key is None or self.clock is None:
            print("There has been an error, please check logs, err-state: run init")
            return 1
        
        while not self.stop:
            if self.debug:
                print("New frame")
                print(f"{len(self.objects)} objects and {len(self.inputObjects)} input objects")

            self.rE.newFrame()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop = True

            # p1 = self.viewingCoordinates - self.halfScreen
            # p2 = self.viewingCoordinates + self.halfScreen
            p1 = V2(0, 0)
            p2 = self.halfScreen * 2

            keys = self.key.get_pressed()

            if keys[pygame.K_a]:
                print("[!] a is pressed")

            for e in self.inputObjects:
                print(f"Handling input for {e}")
                e.handleInput(keys)

            self.pE.tick(self.objects, self.dt)

            for e in self.objects:
                if e.isInScope(p1, p2):
                    print(f"Object {str(e)} is in scope")
                    self.rE.render(e, debug=self.debug)
            # DEBUG
            # if self.debug:
            #     for i in range(720):
            #         clr = "#ffffff"
            #         if self.objects[0].isInScope(V2(0, i), V2(0, i)):
            #             clr = "#ffff00"
            #         pygame.draw.rect(self.rE.screen, clr, pygame.Rect(V2(0, 720-i), V2(5, 1)))


            self.rE.finaliseFrame()
            
            self.dt = self.clock.tick(self.targetFps) / 1000
