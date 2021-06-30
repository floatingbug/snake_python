import pygame

class Player:
    def __init__(self):
        self.img_smiley = pygame.image.load("smiley.jpg")
        self.img_smiley = pygame.transform.scale(self.img_smiley, (40, 40))
        self.size = width, height = 800, 600
        self.x = 400
        self.y = 300
        self.moveStep = 10
        self.moveDirection = 'right'
        
    def getMoveDirection(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.moveDirection = 'left' 
            elif event.key == pygame.K_UP:
                self.moveDirection = 'up'
            elif event.key == pygame.K_RIGHT:
                self.moveDirection = 'right'
            elif event.key == pygame.K_DOWN:
                self.moveDirection = 'down'
    
    def update(self):
        if self.moveDirection == 'left':
            self.x -= self.moveStep
        elif self.moveDirection == 'right':
            self.x += self.moveStep
        elif self.moveDirection == 'down':
            self.y += self.moveStep
        elif self.moveDirection == 'up':
            self.y -= self.moveStep

    def draw(self, screen):
        screen.blit(self.img_smiley, (self.x, self.y))

