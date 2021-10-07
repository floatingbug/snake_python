import pygame, time, player, apple

class PlayState:
    def __init__(self, screen):
        self.screen = screen
        self.notQuit = True
        self.player = player.Player(self.screen)
        self.apple = apple.Apple(self.screen)
        self.nextState = ''
        self.score = 0
        self.stateName = 'playState'

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notQuit = False
            self.player.getMoveDirection(event)

        self.screen.fill((0,0,0))

        #if game over switch state
        self.score = self.player.score
        if self.player.update(self.apple.pos):
            self.nextState = 'gameOverState'
        self.apple.update(self.player.pos)
        self.apple.draw()
        self.player.draw()

        pygame.display.flip()
        
        time.sleep(0.2)
        return self.notQuit
