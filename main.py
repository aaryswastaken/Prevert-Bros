# 
# @aaryswastaken, 2024
#

# This file is the main entry for the Prevert-Bros project,
# a crude knock-off of the Nintendo game.
# This project and every part of is isn't associated by any
# means to the Nintendo corporation and has been developped
# for entertainement purpose only
import pygame
import sys
from game import GameManager

if __name__ == "__main__":
    debugFlag = False
    if "-d" in sys.argv:
        print("Debugging")
        debugFlag = True

    manager = GameManager(debug=debugFlag)

    ## Debug scene
    from object import RectGroundPart, Cookie
    from player import Player
    from common import V2
    from niveaux import Niveaux, Pieces
    from ennemi import Ennemi
    
    for platform in Niveaux().coord:
        manager.addObject(RectGroundPart(V2(platform[0], platform[1]), V2(platform[2], platform[3]), "#00ff00", "./plateforme.png"))
   
    manager.addObject(RectGroundPart(V2(-5000, 0), V2(5000, -200), "#ff0000"))
    # manager.addObject(RectGroundPart(V2(-500, 0), V2(2000, 200), "#00ff00"))
    # manager.addObject(RectGroundPart(V2(700, 200), V2(300, 50), "#00ffff"))
    # manager.addObject(RectGroundPart(V2(800, 300), V2(200, 200), "#00ffff"))
    player = Player(image="./PERSO.png")
    player.pos = V2(50, 350)
    manager.addObject(player, hasInput=True, isPlayer=True)
    
    for cookie in Pieces().coord:
        manager.addObject(Cookie(V2(cookie[0], cookie[1])))

    ennemi1 = Ennemi("./Vous_voulez_une_boisson.png", 1200, 350, 100)
    manager.addObject(ennemi1, hasInput= False, isPlayer=False)
    ennemi2 = Ennemi("./ya_plus_de_paninis.png", 520, 350, 60)
    manager.addObject(ennemi2, hasInput= False, isPlayer=False)

    ec = manager.run()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    if ec != 0:
        print("An error has occured, please check logs")
