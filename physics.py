#
# @aaryswastaken, 2024
# 

# This file and its elements are in charge of handling the 
# physics of the game.

from common import V2, PLAYER


class PhysicsEngine:
    """
        Main class for the physics engine
    """

    def __init__(self, maxPlayerSpeed=200, playerLambda=1.1, g=550):
        self.maxPlayerSpeed = maxPlayerSpeed
        self.playerLambda = playerLambda # adhesion to the ground
        self.g = g

    def tick(self, objects, dt):
        for o in objects:
            if not o.static:
                if o.objType == PLAYER and o.free:
                    o.acc.x = -self.playerLambda * o.vel.x # friction with the ground

                o.vel += (o.acc + V2(0, -self.g)) * dt # compute velocity

                self.checkCollisions(o, objects) # check for eventual collisions with the other objects

                o.pos += o.vel * dt # update the position

                if o.objType == PLAYER: # if it's a player
                    # cap its limit speeds
                    if o.vel.x > self.maxPlayerSpeed:
                        o.vel.x = self.maxPlayerSpeed

                    if o.vel.x < -self.maxPlayerSpeed:
                        o.vel.x = -self.maxPlayerSpeed
                elif o.objType == ENNEMY:
                    o.check_intervalle()
   
    def checkCollisions(self, obj, objects):
        """
            check for collisions from an object to the other objects, update obj's velocity if needed
        """

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

        #
        # In this trash algorithm, we use the power of the isInScope function to handle collisions
        # simply by calculating (p1 ... p4)'s collisions with each colliding objects
        #

        s2 = obj.size
        p1 = obj.pos - s2.onlyX()
        p2 = obj.pos + s2.onlyY()
        p3 = obj.pos + s2.onlyX()
        p4 = obj.pos - s2.onlyY()

        for o in objects:
            if o.uuid != obj.uuid:
                print(f"trying {obj} against {o}")
                if obj.vel.x > 0 and o.isInScope(p3, p3): # if we're going right and the right collides,
                    obj.vel.x = 0 # sets its velocity back
                    p = self.findTouching(o, obj.pos, p3) # set its position back
                    obj.pos.x = p.x - obj.size.x

                if obj.vel.x < 0 and o.isInScope(p1, p1):
                    obj.vel.x = 0
                    p = self.findTouching(o, obj.pos, p1)
                    obj.pos.x = p.x + obj.size.x

                if obj.vel.y > 0 and o.isInScope(p2, p2):
                    obj.vel.y = 0
                    p = self.findTouching(o, obj.pos, p2)
                    obj.pos.y = p.y - obj.size.y

                if obj.vel.y < 0 and o.isInScope(p4, p4):
                    obj.vel.y = 0
                    p = self.findTouching(o, obj.pos, p4)
                    obj.pos.y = p.y + obj.size.y


    def findTouching(self, collider, p1, p2, steps=100):
        # Same, harnessing the power of the isInScope method, we can approximate the collision point
        # between two objects. For that, it'll divide the p1p2 vector into n [steps] steps and check for
        # collision for each of them 

        for i in range(steps):
            p = p1 + (p2 - p1) * (i / steps)
            # print(f"---\n{p1}")
            # print(f"{i}, {p}")
            # print(f"{p2}")

            if collider.isInScope(p, p):
                return p

        return p2

    def isTouchingGround(self, player, objects):
        # Check if the player is touching ground, once again using isInScope
        for o in objects:
            if o.uuid != player.uuid:
                if o.isInScope(player.pos - player.size.onlyY(), \
                        player.pos - player.size.onlyY()):
                    return True

        return False

    def isTouchingCookie(self, player, cookie):
        # Vérifie sir le joueur touche le cookie
        if cookie.uuid != player.uuid:
            if cookie.isInScope(player.pos - player.size.onlyY(), \
                        player.pos - player.size.onlyY()):
                    return True
        return False

     def isTouchingEnnemi(self, player, ennemi):
        # Vérifie si le joueur touche un ennemi
        if ennemi.uuid != player.uuid:
            if ennemi.isInScope(player.pos - player.size.onlyY(), \
                        player.pos - player.size.onlyY()):
                    return True
        return False
