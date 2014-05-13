# coding=utf-8

from unittest import TestCase

from tenthou.pool import Die
from tenthou.pool import Pool


class TestPool(TestCase):

  def setUp(self):
    super(TestPool, self).setUp()
    self.pool = Pool()

  def test_init_creates_rolled_and_held(self):
    self.assertEquals(0, len(self.pool.rolled))
    self.assertEquals(0, len(self.pool.held))

  def test_roll_all_dice_when_none_held(self):
    self.pool.roll()
    self.assertEquals(5, len(self.pool.rolled))
    self.assertEquals(0, len(self.pool.held))

  def test_hold_dice(self):
    self.pool.roll()
    die1 = self.pool.rolled[1]
    die3 = self.pool.rolled[3]

    self.pool.hold([1, 3])
    self.assertEquals(3, len(self.pool.rolled))
    self.assertEquals(2, len(self.pool.held))
    self.assertNotIn(die1, self.pool.rolled)
    self.assertNotIn(die3, self.pool.rolled)
    self.assertIn(die1, self.pool.held)
    self.assertIn(die3, self.pool.held)

  def test_holding_should_score_dice(self):
    self.pool.rolled = [Die() for i in range(5)]
    self.pool.rolled[0].value = 3
    self.pool.rolled[1].value = 2
    self.pool.rolled[2].value = 1
    self.pool.rolled[3].value = 5
    self.pool.rolled[4].value = 5

    self.pool.hold([2, 4])
    self.assertEquals(150, self.pool.score)

  def test_roll_with_held_dice(self):
    self.pool.roll()
    self.pool.hold([1, 3])
    die1 = self.pool.rolled[0]
    die2 = self.pool.rolled[1]
    die3 = self.pool.rolled[2]

    self.pool.roll()
    self.assertEquals(3, len(self.pool.rolled))
    self.assertEquals(2, len(self.pool.held))
    self.assertNotIn(die1, self.pool.rolled)
    self.assertNotIn(die2, self.pool.rolled)
    self.assertNotIn(die3, self.pool.rolled)

  def test_draw_a_pool(self):
    self.pool.rolled = [Die(value=2), Die(value=3), Die(value=4), Die(value=5), Die(value=6)]
    rendering = self.pool.draw()
    self.assertEquals(rendering,
      '╭ ━ ━ ━ ━ ╮ ╭ ━ ━ ━ ━ ╮ ╭ ━ ━ ━ ━ ╮ ╭ ━ ━ ━ ━ ╮ ╭ ━ ━ ━ ━ ╮\n' + \
      '┃ ⬤       ┃ ┃ ⬤       ┃ ┃ ⬤     ⬤ ┃ ┃ ⬤     ⬤ ┃ ┃ ⬤     ⬤ ┃\n' + \
      '┃         ┃ ┃    ⬤    ┃ ┃         ┃ ┃    ⬤    ┃ ┃ ⬤     ⬤ ┃\n' + \
      '┃       ⬤ ┃ ┃       ⬤ ┃ ┃ ⬤     ⬤ ┃ ┃ ⬤     ⬤ ┃ ┃ ⬤     ⬤ ┃\n' + \
      '╰ ━ ━ ━ ━ ╯ ╰ ━ ━ ━ ━ ╯ ╰ ━ ━ ━ ━ ╯ ╰ ━ ━ ━ ━ ╯ ╰ ━ ━ ━ ━ ╯')
