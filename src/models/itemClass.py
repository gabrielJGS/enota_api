class itemClass:
  def __init__(self, nome, cod, qtd, un_tipo, vl_unit):
      self.nome = nome
      self.cod = cod
      self.qtd = qtd
      self.un_tipo = un_tipo
      self.vl_unit = vl_unit

  def __init__(self):
    self

  def __str__(self):
    return str(self.__class__) + ": " + str(self.__dict__)

