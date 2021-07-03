import vector, pygame

class Player:
    def __init__(self, screen):
        self.pos = vector.Vector(400, 280)
        self.size = vector.Vector(40, 40)
        self.screen = screen
        self.img_smiley = pygame.image.load('smiley.jpg')
        self.img_smiley = pygame.transform.scale(self.img_smiley, (self.size.x, self.size.y))
        self.direction = 'right'

    def getMoveDirection(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.direction = 'left'
            elif event.key == pygame.K_RIGHT:
                self.direction = 'right'
            elif event.key == pygame.K_UP:
                self.direction = 'up'
            elif event.key == pygame.K_DOWN:
                self.direction = 'down'

    def checkGameOver(self):
        if self.pos.x < 0:
            self.pos.x = 760
        elif self.pos.x > 760:
            self.pos.x = 0
        elif self.pos.y < 0:
            self.pos.y = 560
        elif self.pos.y > 560:
            self.pos.y = 0

    def update(self):
        if self.direction == 'left':
            self.pos.x -= self.size.x
        elif self.direction == 'right':
            self.pos.x += self.size.x
        elif self.direction == 'up':
            self.pos.y -= self.size.y
        else:
            self.pos.y += self.size.y
        
        self.checkGameOver()

    def draw(self):
        self.screen.blit(self.img_smiley, (self.pos.x, self.pos.y))
