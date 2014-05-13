class Die(object):

  def __init__(self, **kwargs):
    self.value = kwargs.get('value', None)

  def roll(self):
    pass
