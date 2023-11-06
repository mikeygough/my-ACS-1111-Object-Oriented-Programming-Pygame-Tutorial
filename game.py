# imports
import pygame

pygame.init()

# configure screen
screen = pygame.display.set_mode([500, 500])

running = True
while running:
    # look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # clear screen
    screen.fill((255, 255, 255))
    
    # draw circle
    colors = {
        'red': (235, 78, 61),
        'orange': (241, 155, 56),
        'yellow': (248, 206, 70),
        'green': (119, 214, 114),
        'blue': (120, 198, 245),}
    
    position = (250, 250) # x and y coordinates
    r = 75 # circle radius
    
    pygame.draw.circle(screen, colors['red'], (75, 75), r)
    pygame.draw.circle(screen, colors['orange'], (500-75, 75), r)
    pygame.draw.circle(screen, colors['yellow'], position, r)
    pygame.draw.circle(screen, colors['green'], (500-75, 500-75), r)
    pygame.draw.circle(screen, colors['blue'], (75, 500-75), r)
    
    # update display
    pygame.display.flip()
    
'''
some alternative colors:
(255, 255, 0) - Yellow is all Red and Green and no Blue
(0, 255, 255) - Cyan is Green and Blue with no Red
(255, 0, 255) - Fuschia has no Green.

(255, 255, 255) - We get white when all of the values are 255
(0, 0, 0) - We get black when all of the values are 0
(100, 100, 100) - If all of the values are equal we get gray
(250, 141, 7) - A nice shade of orange.
(25, 184, 22) - A nice shade of green.
(20, 121, 199) - A nice shade of green.
'''