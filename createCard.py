#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 10:52:30 2018

@author: jenny
"""

#image
import pygame

class Img():

    def __init__(self, screen, src,w,h,x,y):
        self.screen = screen
        self.src = src

        self.image = pygame.image.load(self.src).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.width = w
        self.rect.height = h
        self.rect.x = x
        self.rect.y = y

        self.x = 0
        self.y = 0
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def store_pos(self):
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        return self.x,self.y
    
    def repos(self):
        self.rect.x = self.x
        self.rect.y = self.y