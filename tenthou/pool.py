# coding=utf-8

import sys

from tenthou.die import Die
from tenthou.scoring import get_score


NUM_DICE = 5

class Pool(object):

  def __init__(self):
    self.rolled = []
    self.held = []
    self.score = 0

  def roll(self):
    num_to_roll = NUM_DICE - len(self.held)
    self.rolled = [Die() for i in range(num_to_roll)]

  def hold(self, indexes):
    to_hold = [self.rolled[i] for i in indexes]
    self.score += get_score(to_hold)
    self.held += to_hold
    self.rolled = list(set(self.rolled) - set(self.held))

  def draw(self):
    top    = ' '.join(['╭ ━ ━ ━ ━ ╮' for i in range(len(self.rolled + self.held))])
    bottom = ' '.join(['╰ ━ ━ ━ ━ ╯' for i in range(len(self.rolled + self.held))])

    row1 = ' '.join(self._draw_row_1())
    row2 = ' '.join(self._draw_row_2())
    row3 = ' '.join(self._draw_row_3())

    return '\n'.join([top, row1, row2, row3, bottom])

  def _draw_row_1(self):
    for d in self.rolled:
      if d.value in [2, 3]:       yield '┃ ⬤       ┃'
      elif d.value in [4, 5, 6]:  yield '┃ ⬤     ⬤ ┃'
      else:                       yield '┃         ┃'

  def _draw_row_2(self):
    for d in self.rolled:
      if d.value in [3, 5]:       yield '┃    ⬤    ┃'
      elif d.value is 6:          yield '┃ ⬤     ⬤ ┃'
      else:                       yield '┃         ┃'

  def _draw_row_3(self):
    for d in self.rolled:
      if d.value in [2, 3]:       yield '┃       ⬤ ┃'
      elif d.value in [4, 5, 6]:  yield '┃ ⬤     ⬤ ┃'
      else:                       yield '┃         ┃'
