import random


def ordenamientoPorMezcla(lista):
  if len(lista) > 1:
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    print(izquierda, '*' * 5, derecha)

    # LLamada recursiva en cada mitad
    ordenamientoPorMezcla(izquierda)
    ordenamientoPorMezcla(derecha)

    # Iteradores para recorrer las dos sublistas
    i = 0
    j = 0
    # Iterador para la lista principal
    k = 0
    
    while i < len(izquierda) and j < len(derecha):
      if izquierda[i] < derecha[j]:
        lista[k] = izquierda[i]
        i += 1
      else:
        lista[k] = derecha[j]
        j += 1

      k += 1

    while i < len(izquierda):
      lista[k] = izquierda[i]
      i += 1
      k += 1

    while k < len(derecha):
      lista[k] = derecha[j]
      j += 1
      k += 1

    print(f'izquierda {izquierda}, derecha {derecha}')
    print(lista)
    print('-' * 50)

  return lista
                                                                  #________________
                                                                  # O(n**2)
                                                                  
if __name__ == "__main__":
    tamanoLista = int(input('De que tamano es la lista? '))

    lista = [random.randint(0, 100) for i in range(tamanoLista)]
    print(lista)
    print('-' * 20)

    listaOrdenada = ordenamientoPorMezcla(lista)
    print(listaOrdenada)