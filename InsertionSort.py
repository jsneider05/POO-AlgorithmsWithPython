import random


def ordenamientoPorInsercion(lista):
  
  for indice in range(1, len(lista)):
    valorActual = lista[indice]
    posicionActual = indice

    while posicionActual > 0 and lista[posicionActual - 1] > valorActual:
      lista[posicionActual] = lista[posicionActual - 1]
      posicionActual -= 1

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