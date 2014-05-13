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

  def test_rolled_dice_should_have_values(self):
    self.pool.roll()
    for die in self.pool.rolled:
      self.assertTrue(die.value >= 1 and die.value <=6)

  def test_hold_dice(self):
    self.pool.roll()
    die1 = self.pool.rolled[1]
    die3 = self.pool.rolled[3]

    self.pool.hold(1)
    self.pool.hold(3)
    self.assertEquals(3, len(self.pool.rolled))
    self.assertEquals(2, len(self.pool.held))
    self.assertNotIn(die1, self.pool.rolled)
    self.assertNotIn(die3, self.pool.rolled)
    self.assertIn(die1, self.pool.held)
    self.assertIn(die3, self.pool.held)

  def test_holding_should_score_dice(self):
    self.pool.rolled = [Die(i) for i in range(5)]
    self.pool.rolled[0].value = 3
    self.pool.rolled[1].value = 2
    self.pool.rolled[2].value = 1
    self.pool.rolled[3].value = 5
    self.pool.rolled[4].value = 5

    self.pool.hold(2)
    self.pool.hold(4)
    self.assertEquals(150, self.pool.score)

  def test_roll_with_held_dice(self):
    self.pool.roll()
    self.pool.hold(1)
    self.pool.hold(3)
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
    self.pool.rolled = [Die(0, value=1), Die(1, value=3), Die(2, value=4),
                        Die(3, value=5), Die(4, value=6)]
    self.pool.hold(0)
    self.pool.hold(3)
    rendering = self.pool.draw()
    self.assertEquals(rendering,
      '╭ ━ ━ ━ ━ ╮ ╭ ━ ━ ━ ━ ╮ ╭ ━ ━ ━ ━ ╮ ╭ ━ ━ ━ ━ ╮ ╭ ━ ━ ━ ━ ╮\n' + \
      '┃         ┃ ┃ ⬤       ┃ ┃ ⬤     ⬤ ┃ ┃ ⬤     ⬤ ┃ ┃ ⬤     ⬤ ┃\n' + \
      '┃    ⬤    ┃ ┃    ⬤    ┃ ┃         ┃ ┃    ⬤    ┃ ┃ ⬤     ⬤ ┃\n' + \
      '┃         ┃ ┃       ⬤ ┃ ┃ ⬤     ⬤ ┃ ┃ ⬤     ⬤ ┃ ┃ ⬤     ⬤ ┃\n' + \
      '╰ ━ ━ ━ ━ ╯ ╰ ━ ━ ━ ━ ╯ ╰ ━ ━ ━ ━ ╯ ╰ ━ ━ ━ ━ ╯ ╰ ━ ━ ━ ━ ╯\n' + \
      '  H E L D                             H E L D              \n\n' + \
      'S C O R E:  150')
