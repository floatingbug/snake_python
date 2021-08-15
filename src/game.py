import pygame, vector, playState, gameOverState

class Game:
    def __init__(self):
        pygame.init()
        self.size = vector.Vector(800, 600)
        self.screen = pygame.display.set_mode((self.size.x, self.size.y))
        self.running = True
        self.currState = playState.PlayState(self.screen)

    def start(self):
        while self.running:
            self.running = self.currState.update()
            if self.currState.nextState == 'gameOverState':
                self.currState = gameOverState.GameOverState(self.screen, self.currState.score) 
