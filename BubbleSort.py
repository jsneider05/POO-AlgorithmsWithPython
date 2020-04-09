import random

contador = 0

def ordenamientoBurbuja(lista):
  global contador
  n = len(lista)

  for i in range(n):                                              # O(n)
    contador += 1
    for j in range(0, n - i - 1):                                 # * O(n - i - 1) = O(n)
      contador += 1
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
    print(f'contador: {contador}')

    # Para una lista de 1000 el contador dio un valor de: 500500
    # Este valor porque el range del for interior se fue disminuyendo en i
    # Si esta estrategia no se aplicara el contador daria O(n**2) es decir 1000000