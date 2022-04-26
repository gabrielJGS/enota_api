class notaLoja:
  def __init__(self, nome, cnpj, endereco, items):
      self.nome = nome
      self.cnpj = cnpj.replace("CNPJ ","")
      self.endereco = endereco
      self.items = items

  def __str__(self):
    return str(self.__class__) + ": " + str(self.__dict__)
