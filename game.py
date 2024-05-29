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
    """
        The overall manager
    """

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

        self.followDx = 220
        self.followDy = 180
        self.followIncrement = 2
        self.followVec = V2(self.followDx, self.followDy)

        if debug:
            pygame.font.init()
            self.dfont = pygame.font.SysFont("Jetbrains Mono", 30)

    def addObject(self, obj, hasInput=False, isPlayer=False):
        """
            addObject: references a new object

            inputs:
             - obj: object
             - hasInput: bool, if it has inpurts (ie. playable character)
             - isPlayer: bool, if it's the player

        """

        obj.uuid = self.uuid_counter
        self.uuid_counter += 1

        self.objects.append(obj)

        if hasInput:
            self.inputObjects.append(obj)

        if isPlayer:
            self.players.append(obj)

    def run(self):
        """
            run: Main loop of the game
        """

        if self.key is None or self.clock is None:
            print("There has been an error, please check logs, err-state: run init")
            return 1
        
        # While the game didn't end
        while not self.stop:
            if self.debug:
                print("New frame")
                print(f"{len(self.objects)} objects and {len(self.inputObjects)} input objects")

            self.rE.newFrame() # Initalise a new frame by the rendering engine
            self.rE.printBG(self.viewingCoordinates) # Add the background

            # Empties the event buffer
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop = True

            # Small definitions, self explainatory
            p1 = self.viewingCoordinates
            p2 = self.viewingCoordinates + self.ssize

            keys = self.key.get_pressed() # Fetching pressed keys

            if keys[pygame.K_a]:
                print("[!] a is pressed") # debug

            # Looping through objects that where referenced using the hasInput flag
            for e in self.inputObjects:
                print(f"Handling input for {e}")
                e.handleInput(keys, self) # Handle eventual inputs

            # Tick the physics engine
            self.pE.tick(self.objects, self.dt)

            # Check if the view has moved
            self.checkOutOfBounds()

            # Some debug
            print(f"Updated viewingCoordinates: {self.viewingCoordinates}")

            for e in self.objects: # for every object
                if e.isInScope(p1, p2): # if it has to be drawn 
                    print(f"Object {str(e)} is in scope") # debug
                    self.rE.render(e, self.viewingCoordinates, debug=self.debug) # render the object through the rendering engine


            # If debug, do debug thing
            if self.debug:
                pygame.draw.rect(self.rE.screen, "red",
                        pygame.Rect(self.followVec, self.ssize - self.followVec * 2), width=1)
   
                if self.dt != 0:
                    fps = 1/self.dt 
                    dbsf = self.dfont.render(f"FPS: {fps:.1f}", False, "#ff0000")
                    self.rE.screen.blit(dbsf, (5, 5))

            
            # Finalise the frame and show it to the player
            self.rE.finaliseFrame()
            
            # Ticking
            self.dt = self.clock.tick(self.targetFps) / 1000

    def checkOutOfBounds(self):
        """
            Check if the player is our of the bonds and the viewing position needs to 
                be updated
        """


        # Relative position
        uPos = self.players[0].pos - self.viewingCoordinates
        
        # right
        while uPos.x > self.ssize.x - self.followDx:
            self.viewingCoordinates.x += self.followIncrement
            uPos = self.players[0].pos - self.viewingCoordinates

        if self.debug:
            print("did right")

        # left
        while uPos.x < self.followDx:
            self.viewingCoordinates.x -= self.followIncrement
            uPos = self.players[0].pos - self.viewingCoordinates

        if self.debug:
            print("did left")

        # top
        while uPos.y > self.ssize.y - self.followDy:
            self.viewingCoordinates.y += self.followIncrement
            uPos = self.players[0].pos - self.viewingCoordinates
        
        if self.debug:
            print("did top")

        # bottom
        while uPos.y < self.followDy:
            self.viewingCoordinates.y -= self.followIncrement
            uPos = self.players[0].pos - self.viewingCoordinates
    
        if self.debug:
            print("did bottom")
