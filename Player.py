# Apple
from GameObject import GameObject
from constants import LANES
from random import randint, choice

class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'player.png')
    self.dx = 0
    self.dy = 0
    self.pos_x = 1
    self.pos_y = 1
    self.reset()

  def left(self):
    if self.pos_x > 0:
      self.pos_x -= 1
    self.update_dx_dy()

  def right(self):
    if self.pos_x < len(LANES) - 1:
      self.pos_x += 1
    self.update_dx_dy()

  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
    self.update_dx_dy()

  def down(self):
    if self.pos_y < len(LANES) - 1:
      self.pos_y += 1
    self.update_dx_dy()

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = LANES[self.pos_x]
    self.y = LANES[self.pos_y]
    self.dx = self.x
    self.dy = self.y
  
  def update_dx_dy(self):
    self.dx = LANES[self.pos_x]
    self.dy = LANES[self.pos_y]