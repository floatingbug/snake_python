import pygame, vector, random

class Apple:
    def __init__(self, screen):
        self.screen = screen
        self.pos = vector.Vector(200, 200)
        self.img_apple = pygame.image.load('apple.png')
        self.img_apple = pygame.transform.scale(self.img_apple, (40, 40))

    def update(self, pos):
        if pos.x == self.pos.x and pos.y == self.pos.y:
            self.pos.x = int(random.random()*19)*40
            self.pos.y = int(random.random()*14)*40

    def draw(self):
        self.screen.blit(self.img_apple, (self.pos.x, self.pos.y))
