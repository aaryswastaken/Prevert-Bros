# 
# @aaryswastaken, 2024
#

# This file contains the game manager, principal class of the game.
# It is responsible for the management of all the entities, the 
# physics engine and the rendering engine

from physics import PhysicsEngine
from renderer import RenderingEngine


class GameManager():
    def __init__(self, debug=False):
        self.debug = debug 

        self.pE = PhysicsEngine()
        self.rE = RenderingEngine()

        self.objects = []

    def run(self):
        pass
