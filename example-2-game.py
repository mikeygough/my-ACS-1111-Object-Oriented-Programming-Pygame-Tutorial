# imports
import pygame

pygame.init()

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

# instantiate GameObject
apple = GameObject(100, 100, 'apple.png')
strawberry = GameObject(200, 200, 'strawberry.png')

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
    
    # update display
    pygame.display.flip()