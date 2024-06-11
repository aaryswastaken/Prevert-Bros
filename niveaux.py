#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:54:08 2024

@author: ademin
"""

class Niveaux():
    
    __slots__ = ['x', 'y', 'l', 'h', 'nv1', 'coord']
    
    def __init__(self):
        self.x = [0, 400, 600, 700, 800, 1100, 1450, 1600, 1750, 1900]
        self.y = 0
        self.l = [300, 200, 100, 100, 100, 250, 50, 50, 50, 400]
        self.h = [200, 200, 270, 340, 410, 200, 200, 200, 200, 200]
        self.create_dic()
        
    def create_dic(self):
        self.nv1 = dict()
        if len(self.x) == len(self.l) and len(self.l) == len(self.h):
            for i in range(len(self.x)):
                self.nv1[str(i)] = (self.x[i], self.y, self.l[i], self.h[i])
            self.coord = self.nv1.values()
        else:
            print("The number of levels is not coherent")

class Pieces():
    
    __slots__ = ['x', 'y', 'cookies', 'coord']
    
    def __init__(self):
        self.x = [150, 250, 350, 650, 750, 850, 1150, 1300, 1475, 1625, 1775]
        self.y = [240, 240, 330, 310, 380, 450, 240, 240, 340, 340, 340]
        self.create_dic()
        
    def create_dic(self):
        self.cookies = dict()
        if len(self.x) == len(self.y):
            for i in range(len(self.x)):
                self.cookies[str(i)] = (self.x[i], self.y[i])
            self.coord = self.cookies.values()
        else:
            print("The number of levels is not coherent")