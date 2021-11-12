import pygame
from random import randint, choice
from GameObject import GameObject
from constants import lanes

# ----------------------------------------------
# Fruit

class Fruit():
  def __init__(self):
    super(Fruit, self).__init__(0, 0, 'images/strawberry.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x > 500:
      self.reset()

  def reset(self):
    self.x = -64
    self.y = choice(lanes)
