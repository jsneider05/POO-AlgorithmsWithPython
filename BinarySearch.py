import random

contador = 0

def busquedaBinaria(lista, objetivo, indiceInicial, indiceFinal):
  global contador
  contador += 1
  print(f'>>>Buscando {objetivo} entre {lista[indiceInicial]} y {lista[indiceFinal]}')

  if indiceInicial > indiceFinal or objetivo > lista[indiceFinal]:
    return False

  indiceMedio = (indiceInicial + indiceFinal) // 2

  if objetivo == lista[indiceMedio]:
    return True
  elif objetivo < lista[indiceMedio]:
    return busquedaBinaria(lista, objetivo, indiceInicial, indiceMedio - 1)
  else:
    return busquedaBinaria(lista, objetivo, indiceMedio + 1, indiceFinal)



if __name__ == "__main__":
    tamanoLista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamanoLista)])
    print(lista)

    encontrado = busquedaBinaria(lista, objetivo, 0, len(lista) - 1)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'El algoritmo realizo {contador} pasos')