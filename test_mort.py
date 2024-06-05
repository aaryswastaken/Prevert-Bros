#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:32:12 2024

@author: zfeuilloy
"""
"""Programmer la mort du personnage = fin du niveau/arret de la partie
2 types de mort : chute & collision avec ennemi
"""

# p1 => hauteur de la plateforme  et  p2 => largeur de la plateforme

def chute(self, personnage, plateforme):
    """Quand il n'y a pas de plateforme : si y_perso < 0 : mort
    """
    pltfrm = False
    # tant quil y a une plateforme en dessous du perso
    if (self.x_centre-self.p2/2) < self.x_perso < (self.x_centre+self.p2/2) : 
        pltfrm = True
    # Quand il y a un espace entre 2 plateformes
    if not pltfrm :
        # si le perso passe en dessous du niveau du sol
        if self.y_perso < 0 :
            return gameover
    
def collision_ennemi (self, personnage, ennemi):
    if self.x_max_perso == self.x_min_ennemi or self.x_min_perso == self.x_max_ennemi or self.y_min_perso == self.y_max_ennemi or self.y_max_perso == self.y_min_ennemi : 
        return gameover

def gameover (self, personnage):
    """ on se fait réapparaitre au debut du niveau ==> pos_perso = (x_perso, y_perso) = (x_perso_init,y_perso_init) """
    self.pos_perso = self.pos_perso_init