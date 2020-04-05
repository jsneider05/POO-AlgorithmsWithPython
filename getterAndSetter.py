
class CasillaVotacion:

  def __init__(self, identificador, regionesPais):
    self._identificador = identificador
    self._regionesPais = regionesPais
    self._region = None

  @property
  def region(self):
    return self._region

  @region.setter
  def region(self, region):
    if region in self._regionesPais:
      print('setting')
      self._region = region
    else:
      raise ValueError(f'La region {region} no es valida dentro de las regiones permitidas {self._regionesPais}')


casilla = CasillaVotacion(123, ['Medellin', 'Cucuta'])
print(f'{casilla.region}')
casilla.region = 'Medellin'
print(f'{casilla.region}')
casilla.region = 'Bogota'
print(f'{casilla.region}')