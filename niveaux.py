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
        self.h = [200, 200, 270, 340, 411, 200, 200, 200, 200, 200]
        self.create_dic()
        
    def create_dic(self):
        self.nv1 = dict()
        if len(self.x) == len(self.l) and len(self.l) == len(self.h):
            for i in range(len(self.x)):
                self.nv1[str(i)] = (self.x[i], self.y, self.l[i], self.h[i])
            self.coord = self.nv1.values()
        else:
            print("The number of levels is not coherent")
