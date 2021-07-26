import pygame

class GameOverState:
    def __init__(self, screen):
        self.notQuit = True
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font_score = self.font.render("SCORE", True, (255, 255, 255))
        self.img_tryAgain = self.font.render("Try Again", True, (255, 255, 255))
        self.tryAgain_rect = self.img_tryAgain.get_rect()
        self.screen = screen
        self.nextState = ''

    def draw(self):
        self.screen.blit(self.font_score, (200, 200))
        pygame.draw.rect(self.img_tryAgain, (255, 255, 255), self.tryAgain_rect, 1)

    def update(self):
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                self.notQuit = False
            if self.tryAgain_rect.collidepoint(x, y):
                self.img_tryAgain = self.font.render("sldfj", True, (255,255,255))
        
        self.screen.fill((0,0,0))
        self.draw()
        pygame.display.flip()
        
        return self.notQuit
