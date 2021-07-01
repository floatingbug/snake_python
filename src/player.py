import vector, pygame

class Player:
    def __init__(self, screen):
        self.pos = vector.Vector(300, 300)
        self.screen = screen
        self.img_smiley = pygame.image.load('smiley.jpg')

    def draw(self):
        self.screen.blit(img_smiley, (self.pos.x, self.pos.y))
