
class Coordenada:

  def __init__(self, x , y):
    self.x = x
    self.y = y

  def distancia(self, otraCoodenada):
    x_diff = (self.x - otraCoodenada.x)**2
    y_diff = (self.y - otraCoodenada.y)**2

    return (x_diff + y_diff)**0.5

if __name__ == "__main__":
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2)) #22.02271554554524
    print(isinstance(coord_2, Coordenada)) #True

    distancia = coord_1.distancia(coord_2)

    print(f'La distancia es: {distancia}' if isinstance(coord_1, Coordenada) and isinstance(coord_2, Coordenada) else f'No son instancias de Coordenada') #22.02271554554524

    print(f'La distancia es: {distancia}' if isinstance(0, Coordenada) and isinstance(coord_2, Coordenada) else f'No son instancias de Coordenada') #No son instancias de Coordenada