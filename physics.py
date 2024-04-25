#
# @aaryswastaken, 2024
# 

# This file and its elements are in charge of handling the 
# physics of the game.

from common import V2, PLAYER


class PhysicsEngine:
    def __init__(self, maxPlayerSpeed=200, playerLambda=1.1, g=250):
        self.maxPlayerSpeed = maxPlayerSpeed
        self.playerLambda = playerLambda
        self.g = g

    def tick(self, objects, dt):
        for o in objects:
            if not o.static:
                if o.objType == PLAYER and o.free:
                    o.acc.x = -self.playerLambda * o.vel.x

                o.vel += (o.acc + V2(0, -self.g)) * dt

                self.checkCollisions(o, objects)

                o.pos += o.vel * dt

                if o.objType == PLAYER:
                    if o.vel.x > self.maxPlayerSpeed:
                        o.vel.x = self.maxPlayerSpeed

                    if o.vel.x < -self.maxPlayerSpeed:
                        o.vel.x = -self.maxPlayerSpeed
   
    def checkCollisions(self, obj, objects):
        if not obj.colliding:
            print(f"{obj} not colliding")
            return obj.vel

        # Poor algorithm
        #       +
        #  |    |           p2
        #  | X--+--+      p1  p3
        #  |    |           p4
        #  |    +
        #

        # epsilon = V2(0.01, 0.01)

        s2 = obj.size / 2
        p1 = obj.pos - s2.onlyX()
        p2 = obj.pos + s2.onlyY()
        p3 = obj.pos + s2.onlyX()
        p4 = obj.pos - s2.onlyY()

        for o in objects:
            if o.uuid != obj.uuid:
                print(f"trying {obj} against {o}")
                if obj.vel.x > 0 and o.isInScope(p3, p3):
                    obj.vel.x = 0

                if obj.vel.x < 0 and o.isInScope(p1, p1):
                    obj.vel.x = 0

                if obj.vel.y > 0 and o.isInScope(p2, p2):
                    obj.vel.y = 0
                    obj.pos.y = p2.y

                if obj.vel.y < 0 and o.isInScope(p4, p4):
                    obj.vel.y = 0
                    obj.pos.y = p4.y + 4

