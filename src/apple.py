import pygame, vector

class Apple:
    def __input__(self, screen):
        self.screen = screen
        self.pos = vector.Vector(200, 200)
        self.img_apple = pygame.image.load('apple.png', (self.pos.x, self.pos.y))

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.img_apple, (self.pos.x, self.pos.y))
