from mock import Mock
from mock import patch
from unittest import TestCase

from tenthou.game import Game


class TestGame(TestCase):

  def test_game_start(self):
    game = Game()
    self.assertNotEquals(None, game.pool)
    self.assertEquals(0, len(game.pool.all()))
    self.assertEquals(0, game.current_player)

  # def test_turn_rolls_pool(self):
  #   game = Game()
  #   game.pool.draw = Mock()
  #   with patch('random.randrange', return_value=1) as mock_random:
  #     game.turn()
  #     self.assertEquals(5, len(game.pool.rolled))
  #     self.assertEquals(0, game.current_player)
  #     self.assertEquals(1, game.pool.draw.call_count)
