import pygame

class Player:
    def __init__(self):
        self.img_smiley = pygame.image.load("smiley.jpg")
        self.size = width, height = 800, 600

    def update(self, event):
        

    def draw(self, screen):
        screen.blit(self.img_smiley, (400, 300))


