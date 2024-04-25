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
        debugFlag = True

    manager = GameManager(debug=debugFlag)

    ec = manager.run()

    if ec != 0:
        print("An error has occured, please check logs")
