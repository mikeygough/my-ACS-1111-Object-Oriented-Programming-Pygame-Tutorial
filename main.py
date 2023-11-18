# external imports
import pygame
from random import randint, choice

# class imports
from Apple import Apple
from Bomb import Bomb
from GameObject import GameObject
from Player import Player
from ScoreBoard import ScoreBoard
from Strawberry import Strawberry

# constant imports
from constants import *

# game --
pygame.init()
pygame.font.init()

# configure screen size
screen = pygame.display.set_mode([WIDTH, HEIGHT])


def main():
    # make all-sprites group
    all_sprites = pygame.sprite.Group()
    # make fruits group
    fruit_sprites = pygame.sprite.Group()

    # make fruit instances
    apple = Apple()
    strawberry = Strawberry()

    # add to fruits group
    fruit_sprites.add(apple)
    fruit_sprites.add(strawberry)

    # make player
    player = Player()

    # make bomb
    bomb = Bomb()
    
    # make scoreboard
    score = ScoreBoard(30, 30, 0)
    
    # add score to all_sprites group
    all_sprites.add(score)

    # add sprites to group
    all_sprites.add(player)
    all_sprites.add(apple)
    all_sprites.add(strawberry)
    all_sprites.add(bomb)

    # get clock
    clock = pygame.time.Clock()

    # game loop
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

        # Clear screen
        screen.fill((255, 255, 255))

        # Move and render Sprites
        for entity in all_sprites:
            entity.move()
            entity.render(screen)
            if entity != player:
                pass

        # Check Colisions
        fruit = pygame.sprite.spritecollideany(player, fruit_sprites)

        if fruit:
            score.update(100)
            fruit.reset()

        # Check collision player and bomb
        if pygame.sprite.collide_rect(player, bomb):
            running = False

        # Update the window
        pygame.display.flip()

        # tick the clock!
        clock.tick(60)


if __name__ == "__main__":
    main()
