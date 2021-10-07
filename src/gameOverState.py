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
        self.stateName = 'gameOverState'
        self.highScore = 0
        self.is_new_highscore = False
        self.handleHighscore()

    def handleHighscore(self):
        f = open('highScore.txt', 'r')
        oldHighscore = int(f.read())
        f.close()
        if oldHighscore < self.score:
            f = open('highScore.txt', 'w')
            f.write(str(self.score))
            f.close()
            self.is_new_highscore = True 
        
    #if there is a new Highscore handleHighscore return True else False
    def draw(self):
        if self.is_new_highscore:
            self.txt_score = self.font.render("New Highscore: " + str(self.score), 
            True, (255, 255, 255))
        else:
            f = open('highScore.txt', 'r')
            oldHighscore = f.read()
            f.close()
            self.txt_score = self.font.render("Old Highscore: " + oldHighscore,
            True, (255, 255, 255))
        self.screen.blit(self.txt_score, (200, 200))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notQuit = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notQuit = False
                else:
                    self.nextState = 'playState'
   
        self.screen.fill((0,0,0))
        self.draw()
        pygame.display.flip()
        
        return self.notQuit
