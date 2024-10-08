from CircleShape import CircleShape
from constant import *
import pygame


class Asteroid(CircleShape):
    def __init__(self, x:int,y:int, radius: int):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position +=  self.velocity * dt