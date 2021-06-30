import pygame, playState, time
pygame.init()

class Game:
    def __init__(self):
        self.size = self.width, self.height = 800, 600
        self.running = True
        self.screen = pygame.display.set_mode(self.size)
        self.currTime = 0
        self.currState = playState.PlayState(self.screen)

    def start(self):
        while self.running:
            self.running = self.currState.update()
        
            time.sleep(.2)
