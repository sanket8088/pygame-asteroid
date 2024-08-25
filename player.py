from CircleShape import CircleShape
from constant import *
import pygame

class Player(CircleShape):
    def __init__(self, x:int,y:int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius/1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, PLAYER_COLOR,self.triangle(), 2)
    
    def rotate(self, dt, key):
        if key == "a":
            self.rotation-= 300 * dt
        elif key == "d":
            self.rotation+= 300 * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Rotation
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # 'A' or Left Arrow
            self.rotate(dt, "a")
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # 'D' or Right Arrow
            self.rotate(dt, "d")

        # Movement
        if keys[pygame.K_w] or keys[pygame.K_UP]:  # 'W' or Up Arrow
            self.move(dt, "w")
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:  # 'S' or Down Arrow
            self.move(dt, "s")

        
    def move(self, dt, key):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if key == "w":
            self.position += forward * PLAYER_SPEED * dt
        elif key == "s":
            self.position -= forward * PLAYER_SPEED * dt
    

