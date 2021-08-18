import pygame
import random

# Worm Player Class

class Worm:
    def __init__(self, surface):
        self.surface = surface
        self.x = surface.get_width() / 2
        self.y = surface.get_height() / 2
        self.length = 1
        self.grow_to = 50
        self.vx = 0
        self.vy = -1
        self.body = []
        self.crashed = False
        self.color = 255, 255, 0

    # eat mechanism
    def eat(self):
        self.grow_to += 25
    
    # Handle keyboard events
    def event(self, event):
        if event.key == pygame.K_UP:
            self.vx = 0
            self.vy = -1
        elif event.key == pygame.K_DOWN:
            self.vx = 0
            self.vy = 1
        elif event.key == pygame.K_LEFT:
            self.vx = -1
            self.vy = 0
        elif event.key == pygame.K_RIGHT:
            self.vx = 1
            self.vy = 0

    # Moving the worm
    def move(self):
        self.x += self.vx
        self.y += self.vy

        if (self.x, self.y) in self.body:
            self.crashed = True
        
        self.body.insert(0, (self.x, self.y))

        if (self.grow_to > self.length):
            self.length += 1

        if len(self.body) > self.length:
            self.body.pop()