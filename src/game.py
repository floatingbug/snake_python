import pygame, sys, time, playState
pygame.init()

class Game:
    def __init__(self):
        self.size = self.width, self.height = 800, 600
        self.running = True
        self.screen = pygame.display.set_mode(self.size)
        self.delta = 0
        self.currTime = 0
        self.currState = playState.PlayState(self.screen)

    def start(self):
        while self.running:
            self.currTime = time.time()
            self.delta = (time.time() - self.currTime) * 1000 
            
            self.running = self.currState.update()
            pygame.display.flip()

