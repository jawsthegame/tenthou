from random import randrange

class Die(object):

  def __init__(self, num, **kwargs):
    self.num = num
    self.value = kwargs.get('value', randrange(1, 6))
