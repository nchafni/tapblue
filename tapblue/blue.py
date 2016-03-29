import pubnub

class BlueBase(object):
  def __init__(
      self,
      channel,
  ) :
      self.channel = channel

class BlueCore(BlueBase):
  def __init__(
      self,
      channel,
  ) : 
    self.channel = channel
  
  def printChannel(self):
    print self.channel

  def printChannel2(self, args):
    print args['channel']

class Blue(BlueCore):
  def __init__(
      self,
      channel,
  ) :
      super(Blue, self).__init__(
          channel = channel,
  )