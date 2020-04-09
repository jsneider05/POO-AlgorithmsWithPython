import random

contador = 0

def busquedaLineal(lista, objetivo):
  global contador

  match = False                                                                           # O(1)
  
  for elemento in lista:                                                                  # O(n)
    contador += 1                                                                         # O(1)
    if elemento == objetivo:                                                              # O(1)
      match = True                                                                        # O(1)      
      break                                                                               # O(1)
  
  return match                                                                            # O(1)
                                                                                          #______
                                                                                          # O(n)

if __name__ == "__main__":
    tamanoLista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamanoLista)]

    encontrado = busquedaLineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'El algoritmo realizo {contador} pasos')
    