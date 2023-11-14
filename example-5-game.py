# imports
import pygame
from random import randint, choice

pygame.init()
# by default, pygame tries to draw the screen as fast as the system allows
# use clock to get a consistent frame rate
clock = pygame.time.Clock()

# configure screen
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
# configure position values
lanes = [93, 218, 343]


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
        x = choice(lanes)
        super().__init__(x, 0, "apple.png")
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.direction = "down"
        self.reset()

    def move(self):
        if self.direction == "down":
            self.x += self.dx
            self.y += self.dy
            # check y position
            if self.y > 500:
                self.reset()
        else:
            self.x -= self.dx
            self.y -= self.dy
            # check y position
            if self.y < -64:
                self.reset()

    def reset(self):
        self.x = choice(lanes)
        self.direction = choice(["up", "down"])
        if self.direction == "down":
            self.y = -64
        else:
            self.y = screen_height


class Strawberry(GameObject):
    def __init__(self):
        y = choice(lanes)
        super().__init__(y, 0, "strawberry.png")
        self.dy = 0
        self.dx = (randint(0, 200) / 100) + 1
        self.direction = "right"
        self.reset()

    def move(self):
        if self.direction == "right":
            self.x += self.dx
            self.y += self.dy
            # check x position
            if self.x > 500:
                self.reset()
        else:
            self.x -= self.dx
            self.y -= self.dy
            # check y position
            if self.x < -64:
                self.reset()

    def reset(self):
        self.y = choice(lanes)
        self.direction = choice(["left", "right"])
        if self.direction == "right":
            self.x = -64
        else:
            self.x = screen_width


class Bomb(GameObject):
    def __init__(self):
        super().__init__(0, 0, "bomb.png")
        self.dx = 0
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 500 or self.x < -64 or self.y > 500 or self.y < -64:
            self.reset()

    def reset(self):
        direction = randint(1, 4)
        if direction == 1:  # left
            self.x = -64
            self.y = choice(lanes)
            self.dx = (randint(0, 200) / 100) + 1
            self.dy = 0
        elif direction == 2:  # right
            self.x = 500
            self.y = choice(lanes)
            self.dx = ((randint(0, 200) / 100) + 1) * -1
            self.dy = 0
        elif direction == 3:  # down
            self.x = choice(lanes)
            self.y = -64
            self.dx = 0
            self.dy = (randint(0, 200) / 100) + 1
        else:
            self.x = choice(lanes)
            self.y = 500
            self.dx = 0
            self.dy = ((randint(0, 200) / 100) + 1) * -1


class Player(GameObject):
    def __init__(self):
        super().__init__(0, 0, "player.png")
        self.dx = 0
        self.dy = 0
        self.pos_x = 1
        self.pos_y = 1
        self.reset()

    def left(self):
        """Move the character left without cross barrier"""
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

    def right(self):
        """Move the character right without cross barrier"""
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    def up(self):
        """Move the character up without cross barrier"""
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()

    def down(self):
        """Move the character down without cross barrier"""
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    def reset(self):
        """Move the player to the center of the screen,
        this is the starting position."""
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y

    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]


# instantiate GameObject
apple = Apple()
strawberry = Strawberry()
bomb = Bomb()
player = Player()

# make a group
all_sprites = pygame.sprite.Group()
# add sprites
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)

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

    # move and render sprites
    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    # # draw apple
    # apple.render(screen)
    # apple.move()

    # # draw strawberry
    # strawberry.render(screen)
    # strawberry.move()

    # # draw player
    # player.render(screen)
    # player.move()

    # update display
    pygame.display.flip()
    # tick the clock
    clock.tick(120)  # next update should be applied in 1/30th of a second
