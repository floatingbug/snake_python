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
        return self.notQui 

        def draw(self):
            self.screen.fill((0,0,0))
            
            self.player.draw()

            pygame.display.flip()
