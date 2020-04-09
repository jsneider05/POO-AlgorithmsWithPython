import random


def ordenamientoBurbuja(lista):
  n = len(lista)

  for i in range(n):                                              # O(n)
    for j in range(0, n - i - 1):                                 # * O(n - i - 1) = O(n)
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
 
  return lista
                                                                  #________________
                                                                  # O(n**2)
                                                                  
if __name__ == "__main__":
    tamanoLista = int(input('De que tamano es la lista? '))

    lista = [random.randint(0, 100) for i in range(tamanoLista)]
    print(lista)

    listaOrdenada = ordenamientoBurbuja(lista)
    print(listaOrdenada)