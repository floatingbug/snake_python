import player, pygame

class PlayState:
    def __init__(self, screen):
        self.player = player.Player()
        self.screen = screen
        self.NotQuit = True

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.NotQuit = False

            self.screen.fill((0,0,0))
            self.player.update(event)
            self.player.draw(self.screen)
        
        return self.NotQuit 
