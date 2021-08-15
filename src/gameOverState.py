import pygame
from os import path

class GameOverState:
    def __init__(self, screen, score):
        self.score = score
        self.notQuit = True
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.txt_score = self.font.render("SCORE: " + str(self.score) + " ", True, (255, 255, 255))
        self.screen = screen
        self.nextState = ''
        self.highScore = 0
        self.dirname = path.dirname(__file__)
        with open(path.join(self.dirname, "highScore.txt"), 'w') as f:
            try:
                highScore = int(f.read())
            except:
                highScore = 0

    def draw(self):
        self.screen.blit(self.txt_score, (200, 200))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notQuit = False
        
        self.screen.fill((0,0,0))
        self.draw()
        pygame.display.flip()
        
        return self.notQuit
