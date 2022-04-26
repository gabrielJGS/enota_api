class itemClass:
  def __init__(self, txtTit, RCod, Rqtd, RUN, RvlUnit):
      self.txtTit = txtTit
      self.RCod = RCod
      self.Rqtd = Rqtd
      self.RUN = RUN
      self.RvlUnit = RvlUnit

  def __init__(self):
    self

  def __str__(self):
    return str(self.__class__) + ": " + str(self.__dict__)

