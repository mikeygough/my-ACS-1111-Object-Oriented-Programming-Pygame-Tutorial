# imports
import pygame
from random import randint, sample

pygame.init()
# by default, pygame tries to draw the screen as fast as the system allows
# use clock to get a consistent frame rate
clock = pygame.time.Clock()

# configure screen
screen = pygame.display.set_mode([500, 500])

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        
    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))
        
class Apple(GameObject):
    def __init__(self):
        x = randint(50, 400)
        super(Apple, self).__init__(x, 0, 'apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check y position
        if self.y > 500:
            self.reset()
            
    def reset(self):
        self.x = sample([93, 218, 343], 1)[0]
        self.y = -64
        
class Strawberry(GameObject):
    def __init__(self):
        y = randint(50, 400)
        super(Strawberry, self).__init__(y, 0, 'strawberry.png')
        self.dy = 0
        self.dx = (randint(0, 200) / 100) + 1
        self.reset()
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check y position
        if self.x > 500:
            self.reset()
            
    def reset(self):
        self.y = sample([93, 218, 343], 1)[0]
        self.x = -64

# instantiate GameObject
apple = Apple()
strawberry = Strawberry()

running = True
while running:
    # look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # clear screen
    screen.fill((255, 255, 255))
    
    apple.render(screen)
    strawberry.render(screen)
    apple.move()
    strawberry.move()
    
    # update display
    pygame.display.flip()
    # tick the clock
    clock.tick(60) # next update should be applied in 1/30th of a second