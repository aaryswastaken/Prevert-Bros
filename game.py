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
from common import V2, STATIC, ENNEMY
from class_sauvegarde import Sauvegardes


class GameManager():
    """
        The overall manager
    """

    def __init__(self, givenTime=360, debug=False, tfps=60):
        self.givenTime = givenTime
        self.debug = debug 
        self.targetFps = tfps

        self.pE = PhysicsEngine()
        self.rE = RenderingEngine(self)

        self.objects = []
        self.players = []
        self.inputObjects = []
        self.uuid_counter = 0

        self.clock = None
        self.time = None
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

        self.cookieCount = 0

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

            # edit mort du joueur
            for p in self.players:
                print("===========position=========")
                print(p.pos)
                if p.pos[1] < 0:
                    self.mort()
                elif p.pos[0] >= 2250:
                    self.victoire()
                    #si ça marche gérer le score puis exit
                for obj in self.objects:
                    if obj.objType == ENNEMY and self.pE.isTouchingEnnemi(p, obj):# mort du player s'il rentre en contact avec l'ennemi
                        self.mort()
                
            # Some debug
            print(f"Updated viewingCoordinates: {self.viewingCoordinates}")

            for e in self.objects: # for every object
                if e.isInScope(p1, p2): # if it has to be drawn
                    print(f"Object {str(e)} is in scope") # debug
                    self.rE.render(e, self.viewingCoordinates, debug=self.debug) # render the object through the rendering engine
                    if e.objType == STATIC:
                        self.getCookie(e)
            
            self.rE.renderCookieCount(self.cookieCount)


            # If debug, do debug thing
            if self.debug:
                pygame.draw.rect(self.rE.screen, "red",
                        pygame.Rect(self.followVec, self.ssize - self.followVec * 2), width=1)
   
                if self.dt != 0:
                    fps = 1/self.dt 
                    dbsf = self.dfont.render(f"FPS: {fps:.1f}", False, "#ff0000")
                    self.rE.screen.blit(dbsf, (100, 5))

            self.soldeRestant = self.givenTime - self.time.get_ticks() / 1000
            self.rE.renderTime(self.soldeRestant)

            # Finalise the frame and show it to the player
            self.rE.finaliseFrame()
            
            # Ticking
            self.dt = self.clock.tick(self.targetFps) / 1000

    def getCookie(self, obj):
        limR = self.players[0].pos[0] + self.players[0].r
        limL = self.players[0].pos[0] - self.players[0].r
        limT = self.players[0].pos[1] + self.players[0].r*2
        limB = self.players[0].pos[1] - self.players[0].r*2
        if limR >= obj.pos[0] and limL <= obj.pos[0] and limT >= obj.pos[1] and limB <= obj.pos[1]:
            #Ajouter 1 au compteur
            self.cookieCount += 1
            #effacer la pièce et l'enlever de la liste des objets
            obj.collected = True
            self.objects.remove(obj)
            pygame.display.flip()

    def mort(self):
        self.players[0].pos = V2(50, 350)

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

    # Cette fonction a été rédigé en grande partie avec Chat GPT
    def victoire(self):
        """
        permet d'afficher la fenêtre de fin
        """
        sauvegarde = Sauvegardes()
        sauvegarde.save(str(self.cookieCount), f"{self.soldeRestant:.0f}")
        
        pygame.init()

        # Définir la taille de la fenêtre
        largeur, hauteur = 800, 600
        fenetre = pygame.display.set_mode((largeur, hauteur))

        image_fond = pygame.image.load('./fin.png')
        #redimensionnement de l'image
        image_fond = pygame.transform.scale(image_fond, (largeur,hauteur))
        
        # Charger une police et définir la taille
        police = pygame.font.Font(None, 60) 


        texte1 = "Félicitations, vous avez gagné !"
        txt_cookiesRecord = f"Record cookies : {str(sauvegarde.cookiesRecord)}"
        txt_soldeRecord = f" Record solde : {str(sauvegarde.soldeRecord)}"
        txt_cookies = f"Cookie : {str(self.cookieCount)}"
        txt_solde = f"Solde: {str(self.soldeRestant)}"
        
        texte1_surface = police.render(texte1, True, (0, 0, 0))  # Texte noir
        txt_cookiesRecord_surface = police.render(txt_cookiesRecord, True, (0, 0, 0))
        txt_soldeRecord_surface = police.render(txt_soldeRecord, True, (0, 0, 0))
        txt_cookies_surface= police.render(txt_cookies, True, (0,0,0))
        txt_solde_surface = police.render(txt_solde, True, (0,0,0))

        # Positionnement du texte
        texte1_rect = texte1_surface.get_rect(center=(largeur/2, hauteur/1.78))
        txt_cookiesRecord_rect = txt_cookiesRecord_surface.get_rect(center=(2.5*largeur/3.7, 450))
        txt_soldeRecord_rect = txt_soldeRecord_surface.get_rect(center=(2.5*largeur/3.7, 500))
        txt_cookies_rect = txt_cookies_surface.get_rect(center=(largeur/5,450))
        txt_solde_rect = txt_solde_surface.get_rect(center = (largeur/5, 500))


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
    
            #Met l'image de fond
            fenetre.blit(image_fond, (0,0))

            if self.soldeRestant >0:
            # Blit le texte sur la fenêtre
                fenetre.blit(texte1_surface, texte1_rect)
                fenetre.blit(txt_cookiesRecord_surface, txt_cookiesRecord_rect)
                fenetre.blit(txt_soldeRecord_surface, txt_soldeRecord_rect)
                fenetre.blit(txt_cookies_surface, txt_cookies_rect)
                fenetre.blit(txt_solde_surface, txt_solde_rect)
            else:#Cas où le solde s'est complétement écoulé
                fenetre.blit(texte2_surface, texte2_rect)
                fenetre.blit(texte3_surface, texte3_rect)
                fenetre.blit(txt_cookiesRecord_surface, txt_cookiesRecord_rect)
                fenetre.blit(txt_soldeRecord_surface, txt_soldeRecord_rect)
            
            # Mettre à jour l'affichage
            pygame.display.flip()
