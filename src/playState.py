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
            
            self.player.getMoveDirection(event)
        
        self.player.update()
        self.screen.fill((0,0,0))
        self.player.draw(self.screen)
        pygame.display.flip() 
            
        return self.NotQuit 
