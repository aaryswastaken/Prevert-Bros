# 
# @aaryswastaken, 2024
#

# This file is the main entry for the Prevert-Bros project,
# a crude knock-off of the Nintendo game.
# This project and every part of is isn't associated by any
# means to the Nintendo corporation and has been developped
# for entertainement purpose only

import sys
from game import GameManager

if __name__ == "__main__":
    debugFlag = False
    if "-d" in sys.argv:
        print("Debugging")
        debugFlag = True

    manager = GameManager(debug=debugFlag)

    ## Debug scene
    from object import RectGroundPart
    from player import Player
    from common import V2
    manager.addObject(RectGroundPart(V2(0, 0), V2(1000, 200), "#00ff00"))
    player = Player()
    player.pos = V2(50, 250)
    manager.addObject(player, hasInput=True)

    ec = manager.run()

    if ec != 0:
        print("An error has occured, please check logs")
