import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, radius:int):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        pass

    def update(self, screen):
        pass

    
    def collide(self, other):
        if isinstance(other, CircleShape):
            print(other)
            distance = self.position.distance_to(other.position)
            if distance < self.radius + other.radius:
                return True