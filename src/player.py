import vector, pygame

class Player:
    def __init__(self, screen):
        self.pos = vector.Vector(400, 280)
        self.size = vector.Vector(40, 40)
        self.screen = screen
        self.img_smiley = pygame.image.load('smiley.jpg')
        self.img_smiley = pygame.transform.scale(self.img_smiley, (self.size.x, self.size.y))
        self.direction = 'left'
        self.tailLength = 5
        self.tail = [vector.Vector(400, 280)]*self.tailLength
        self.score = 0
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.currScore = self.font.render("score: "+str(self.score), True, (255, 255, 255))
      
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
        for i in range(self.tailLength):
            if self.pos.x == self.tail[i].x and self.pos.y == self.tail[i].y:
                return True 
        return False

    def eatApple(self, applePos):
        if applePos.x == self.pos.x and applePos.y == self.pos.y:
            self.tail.append(vector.Vector(self.pos.x, self.pos.y))
            self.tailLength += 1
            self.score += 1
            self.currScore = self.font.render("score: "+str(self.score), True, (255, 255, 255))

    def update(self, applePos):
        del self.tail[self.tailLength-1]

        if self.direction == 'left':
            self.pos.x -= self.size.x
            self.tail.insert(0, vector.Vector(self.pos.x+self.size.x, self.pos.y))
        elif self.direction == 'right':
            self.pos.x += self.size.x
            self.tail.insert(0, vector.Vector(self.pos.x-self.size.x, self.pos.y))
        elif self.direction == 'up':
            self.pos.y -= self.size.y
            self.tail.insert(0, vector.Vector(self.pos.x, self.pos.y+self.size.y))
        else:
            self.pos.y += self.size.y
            self.tail.insert(0, vector.Vector(self.pos.x, self.pos.y-self.size.y))
       
        if self.checkGameOver():
            return True  
        self.eatApple(applePos)
        

    def draw(self):
        self.screen.blit(self.img_smiley, (self.pos.x, self.pos.y))
        self.screen.blit(self.currScore, (600, 30))
        for i in range(self.tailLength):
            self.screen.blit(self.img_smiley, (self.tail[i].x, self.tail[i].y))








