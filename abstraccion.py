
class Lavadora:

  def __init__(self):
    pass

  def lavar(self, temperatura='caliente'):
    self._llenar_tanque_agua(temperatura)
    self._anadir_jabon()
    self._lavar()
    self._centrifurar()


  def _llenar_tanque_agua(self, temperatura):
    print(f'Llenando el tanque de agua {temperatura}')

  def _anadir_jabon(self):
    print(f'Anadiendo jabon')

  def _lavar(self):
    print(f'Lavando')

  def _centrifurar(self):
    print(f'Centrifugando')

if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()