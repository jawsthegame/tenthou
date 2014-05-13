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
    self.rolled = [Die(i) for i in range(num_to_roll)]

  def hold(self, i):
    to_hold = [d for d in self.rolled if d.num is i]
    if to_hold:
      self.score += get_score(to_hold)
      self.held += to_hold
      self.rolled = list(set(self.rolled) - set(self.held))

  def all(self):
    def sort(dice):
      return sorted(dice, key=lambda d: d.num)
    # sorted for consistent rendering
    return sort(self.held + self.rolled)

  def draw(self):
    top    = ' '.join(['╭ ━ ━ ━ ━ ╮' for i in range(len(self.all()))])
    bottom = ' '.join(['╰ ━ ━ ━ ━ ╯' for i in range(len(self.all()))])

    row1 = ' '.join(self._draw_row_1())
    row2 = ' '.join(self._draw_row_2())
    row3 = ' '.join(self._draw_row_3())
    held = ' '.join(self._draw_held())
    score = self._draw_score()

    return '\n'.join([top, row1, row2, row3, bottom, held, '', score])

  def _draw_row_1(self):
    for d in self.all():
      if d.value in [2, 3]:       yield '┃ ⬤       ┃'
      elif d.value in [4, 5, 6]:  yield '┃ ⬤     ⬤ ┃'
      else:                       yield '┃         ┃'

  def _draw_row_2(self):
    for d in self.all():
      if d.value in [1, 3, 5]:    yield '┃    ⬤    ┃'
      elif d.value is 6:          yield '┃ ⬤     ⬤ ┃'
      else:                       yield '┃         ┃'

  def _draw_row_3(self):
    for d in self.all():
      if d.value in [2, 3]:       yield '┃       ⬤ ┃'
      elif d.value in [4, 5, 6]:  yield '┃ ⬤     ⬤ ┃'
      else:                       yield '┃         ┃'

  def _draw_held(self):
    held_nums = [d.num for d in self.held]
    for i in range(len(self.all())):
      if i in held_nums:
        yield '  H E L D  '
      else:
        yield '           '

  def _draw_score(self):
    return 'S C O R E:  %d' % self.score
