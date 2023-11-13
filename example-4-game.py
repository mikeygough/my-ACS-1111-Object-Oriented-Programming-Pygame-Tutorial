# imports
import pygame
from random import randint, sample

pygame.init()
# by default, pygame tries to draw the screen as fast as the system allows
# use clock to get a consistent frame rate
clock = pygame.time.Clock()

# configure screen
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        
    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))
        
class Apple(GameObject):
    def __init__(self):
        x = sample([93, 218, 343], 1)[0]
        super().__init__(x, 0, 'apple.png')
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
        y = sample([93, 218, 343], 1)[0]
        super().__init__(y, 0, 'strawberry.png')
        self.dy = 0
        self.dx = (randint(0, 200) / 100) + 1
        self.reset()
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check x position
        if self.x > 500:
            self.reset()
            
    def reset(self):
        self.y = sample([93, 218, 343], 1)[0]
        self.x = -64

class Player(GameObject):
    def __init__(self):
        super().__init__(0, 0, 'player.png')
        self.dx = 0
        self.dy = 0
        self.reset()
        
    def left(self):
        if (self.x - 100) > 0:
            self.dx -= 100
        else:
            self.dx = 0
    
    def right(self):
        if (self.x + 100) < screen_width - 58:
            self.dx += 100
        else:
            self.dx = screen_width - 58
        
    def up(self):
        if (self.y - 100) > 0:
            self.dy -= 100
        else:
            self.dy = 0
    
    def down(self):
        if (self.y + 100) < screen_height - 64:
            self.dy += 100
        else:
            self.dy = screen_height - 64
    
    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25
    
    def reset(self):
        """ Move the player to the center of the screen, 
            this is the starting position. """
        self.x = 250 - 32
        self.y = 250 - 32
        

# instantiate GameObject
apple = Apple()
strawberry = Strawberry()
player = Player()

running = True
while running:
    # look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()
    
    # clear screen
    screen.fill((255, 255, 255))
    
    # draw apple
    apple.render(screen)
    apple.move()
    
    # draw strawberry
    strawberry.render(screen)
    strawberry.move()
    
    # draw player
    player.render(screen)
    player.move()
    # print(player.x)
    # print(player.y)
    
    # update display
    pygame.display.flip()
    # tick the clock
    clock.tick(60) # next update should be applied in 1/30th of a second