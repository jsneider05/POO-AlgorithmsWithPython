import random

contador = 0

def ordenamientoPorInsercion(lista):
  global contador
  for indice in range(1, len(lista)):
    valorActual = lista[indice]
    posicionActual = indice
    contador += 1

    while posicionActual > 0 and lista[posicionActual - 1] > valorActual:
      lista[posicionActual] = lista[posicionActual - 1]
      posicionActual -= 1
      contador += 1

    lista[posicionActual] = valorActual
  
  return lista
                                                                  #________________
                                                                  # O(n**2)
                                                                  
if __name__ == "__main__":
    tamanoLista = int(input('De que tamano es la lista? '))

    lista = [random.randint(0, 100) for i in range(tamanoLista)]
    print(lista)

    listaOrdenada = ordenamientoPorInsercion(lista)
    print(listaOrdenada)
    print(f'contador: {contador}')

    # Para una lista de 1000 el contador dio un valor de: 255000