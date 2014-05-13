from unittest import TestCase

from tenthou import scoring
from tenthou.die import Die

class TestScoring(TestCase):

  def test_simple_score(self):
    score = scoring.get_score([
      Die(0, value=1),
      Die(1, value=2),
      Die(2, value=5),
      Die(3, value=1),
      Die(4, value=4)])
    self.assertEquals(250, score)

  def test_bust(self):
    score = scoring.get_score([
      Die(0, value=2),
      Die(1, value=2),
      Die(2, value=6),
      Die(3, value=3),
      Die(4, value=4)])
    self.assertEquals(0, score)

  def test_three_of_a_kind_ones(self):
    score = scoring.get_score([
      Die(0, value=1),
      Die(1, value=2),
      Die(2, value=6),
      Die(3, value=1),
      Die(4, value=1)])
    self.assertEquals(1000, score)

  def test_three_of_a_kind_twos(self):
    score = scoring.get_score([
      Die(0, value=2),
      Die(1, value=2),
      Die(2, value=6),
      Die(3, value=3),
      Die(4, value=2)])
    self.assertEquals(200, score)

  def test_three_of_a_kind_threes(self):
    score = scoring.get_score([
      Die(0,value=3),
      Die(1,value=3),
      Die(2,value=6),
      Die(3,value=3),
      Die(4,value=2)])
    self.assertEquals(300, score)

  def test_three_of_a_kind_fours(self):
    score = scoring.get_score([
      Die(0, value=2),
      Die(1, value=2),
      Die(2, value=4),
      Die(3, value=4),
      Die(4, value=4)])
    self.assertEquals(400, score)

  def test_three_of_a_kind_fives(self):
    score = scoring.get_score([
      Die(0, value=5),
      Die(1, value=5),
      Die(2, value=5),
      Die(3, value=3),
      Die(4, value=2)])
    self.assertEquals(500, score)

  def test_three_of_a_kind_sixes(self):
    score = scoring.get_score([
      Die(0, value=2),
      Die(1, value=6),
      Die(2, value=6),
      Die(3, value=6),
      Die(4, value=2)])
    self.assertEquals(600, score)

  def test_three_of_a_kind_ones_with_fourth(self):
    score = scoring.get_score([
      Die(0, value=1),
      Die(1, value=4),
      Die(2, value=1),
      Die(3, value=1),
      Die(4, value=1)])
    self.assertEquals(1100, score)

  def test_three_of_a_kind_fives_with_fourth(self):
    score = scoring.get_score([
      Die(0, value=5),
      Die(1, value=5),
      Die(2, value=5),
      Die(3, value=3),
      Die(4, value=5)])
    self.assertEquals(550, score)
