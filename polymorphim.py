
class Persona:

  def __init__(self, nombre):
    self.nombre = nombre

  def avanza(self):
    print(f'La perona camina')

class Ciclista(Persona):

  def __init__(self, nombre):
    super().__init__(nombre)

  def avanza(self):
    print('El ciclista se desplaza en la bicicleta')

def main():
  persona = Persona('Joan')
  persona.avanza()

  ciclista = Ciclista('Angie')
  ciclista.avanza()

if __name__ == "__main__":
    main()