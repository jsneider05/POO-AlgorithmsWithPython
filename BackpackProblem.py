

def morral(tamano, pesos, valores, n):
  if n == 0 or tamano == 0:
    return 0

  if pesos[n - 1] > tamano:
    return morral(tamano, pesos, valores, n - 1)

  return max(valores[n - 1] + morral(tamano - pesos[n - 1], pesos, valores, n - 1), 
            morral(tamano, pesos, valores, n - 1))


def morral1(tamano, pesos, valores, n):
  if n == 0 or tamano == 0:
    return 0

  if pesos[n - 1] > tamano:
    return morral(tamano, pesos, valores, n - 1)

  agrego = valores[n - 1]
  tamanoMorralActual = tamano - pesos[n - 1]
  opcion1Lotoma = agrego + morral(tamanoMorralActual, pesos, valores, n - 1)
  opcion2noLotoma = morral(tamano, pesos, valores, n - 1)
  maximo = max(opcion1Lotoma, opcion2noLotoma)
  return maximo


if __name__ == "__main__":
  valores = [60, 100, 120]
  pesos = [10, 20, 30]
  tamano = 50
  n = len(valores)
  print(f'Valores: {valores}, Pesos: {pesos}')
  resultado = morral(tamano, pesos, valores, n)
  print(resultado)