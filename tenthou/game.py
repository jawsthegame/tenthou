from tenthou.player import Player
from tenthou.pool import NUM_DICE
from tenthou.pool import Pool


class Game(object):

  def __init__(self):
    self.pool = Pool()
    self.players = []
    self.current_player = 0

  def start(self):
    print '\n\nT E N   T H O U S A N D\n'
    self.num_players = int(raw_input('Number of players? '))
    self.players = [Player() for i in range(self.num_players)]

    while True:
      self.turn()

  def turn(self):
    player = self.players[self.current_player]
    roll = 1
    end = False

    while not end:
      self.pool.roll()
      print 'Player %d: Turn %d, Roll %d' % (self.current_player+1, player.turn, roll)
      print self.pool.draw()

      while len(self.pool.held) <= NUM_DICE:
        print
        i = raw_input('Hold (1-5), End turn (0): ')
        if i == '':
          break
        elif int(i) is 0:
          end = True
          break

        self.pool.hold(int(i)-1)
        print [d.num for d in self.pool.held]

      roll += 1
      print '\n-------------------------------------------------------'

    player.turn += 1
