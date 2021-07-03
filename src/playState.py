import pygame, time, player

class PlayState:
    def __init__(self, screen):
        self.screen = screen
        self.notQuit = True
        self.player = player.Player(self.screen)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notQuit = False
            self.player.getMoveDirection(event)

        self.screen.fill((0,0,0))

        self.player.update()
        self.player.draw()

        pygame.display.flip()
        
        time.sleep(0.2)
        return self.notQuit
