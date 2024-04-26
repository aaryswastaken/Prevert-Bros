# 
# @aaryswastaken, 2024
#

# This file contains the game manager, principal class of the game.
# It is responsible for the management of all the entities, the 
# physics engine and the rendering engine

import pygame

from object import RectGroundPart
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
        self.players = []
        self.inputObjects = []
        self.uuid_counter = 0

        self.clock = None
        self.key = None
        self.rE.init()

        self.dt = 0
        self.stop = False

        self.viewingCoordinates = V2(0, 0)
        self.ssize = V2(self.rE.size[0], self.rE.size[1])
        self.halfScreen = self.ssize / 2

        self.followDx = 120
        self.followDy = 80
        self.followIncrement = 2
        self.followVec = V2(self.followDx, self.followDy)

        if debug:
            pygame.font.init()
            self.dfont = pygame.font.SysFont("Jetbrains Mono", 30)

    def addObject(self, obj, hasInput=False, isPlayer=False):
        obj.uuid = self.uuid_counter
        self.uuid_counter += 1

        self.objects.append(obj)

        if hasInput:
            self.inputObjects.append(obj)

        if isPlayer:
            self.players.append(obj)

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

            p1 = self.viewingCoordinates
            p2 = self.viewingCoordinates + self.halfScreen * 2

            keys = self.key.get_pressed()

            if keys[pygame.K_a]:
                print("[!] a is pressed")

            for e in self.inputObjects:
                print(f"Handling input for {e}")
                e.handleInput(keys, self)

            self.pE.tick(self.objects, self.dt)

            self.checkOutOfBounds()

            print(f"Updated viewingCoordinates: {self.viewingCoordinates}")

            for e in self.objects:
                if e.isInScope(p1, p2):
                    print(f"Object {str(e)} is in scope")
                    self.rE.render(e, self.viewingCoordinates, debug=self.debug)

            if self.debug:
                pygame.draw.rect(self.rE.screen, "red",
                        pygame.Rect(self.followVec, self.ssize - self.followVec * 2), width=1)
   
                if self.dt != 0:
                    fps = 1/self.dt 
                    dbsf = self.dfont.render(f"FPS: {fps:.1f}", False, "#ff0000")
                    self.rE.screen.blit(dbsf, (5, 5))

            # DEBUG
            # if self.debug:
            #     for i in range(720):
            #         clr = "#ffffff"
            #         if self.objects[0].isInScope(V2(0, i), V2(0, i)):
            #             clr = "#ffff00"
            #         pygame.draw.rect(self.rE.screen, clr, pygame.Rect(V2(0, 720-i), V2(5, 1)))


            self.rE.finaliseFrame()
            
            self.dt = self.clock.tick(self.targetFps) / 1000

    def checkOutOfBounds(self):
        uPos = self.players[0].pos - self.viewingCoordinates
        
        # right
        while uPos.x > self.ssize.x - self.followDx:
            self.viewingCoordinates.x += self.followIncrement
            uPos = self.players[0].pos - self.viewingCoordinates
        print("did right")

        # left
        while uPos.x < self.followDx:
            self.viewingCoordinates.x -= self.followIncrement
            uPos = self.players[0].pos - self.viewingCoordinates
        print("did left")

        # top
        while uPos.y > self.ssize.y - self.followDy:
            self.viewingCoordinates.y += self.followIncrement
            uPos = self.players[0].pos - self.viewingCoordinates
        print("did top")

        # bottom
        while uPos.y < self.followDy:
            self.viewingCoordinates.y -= self.followIncrement
            uPos = self.players[0].pos - self.viewingCoordinates
        print("did bottom")
