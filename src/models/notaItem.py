class notaItem:
  def __init__(self, nome, cod, qtd, unTipo, vlUnit):
      self.nome = nome
      self.cod = cod
      self.qtd = qtd
      self.unTipo = unTipo
      self.vlUnit = vlUnit

  def __str__(self):
    return str(self.__class__) + ": " + str(self.__dict__)

  def format_items(self):
    self.cod = self.cod.replace("(C\u00f3digo: ","").replace(" )","")
    self.qtd = self.qtd.replace("Qtde.:","")
    self.unTipo = self.unTipo.replace("UN: ","")
    self.vlUnit = self.vlUnit.replace("Vl. Unit.:   ","")

