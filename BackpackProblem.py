

def morral(tamano, pesos, valores, n):
  if n == 0 or tamano == 0:
    return 0

  if pesos[n - 1] > tamano:
    return morral(tamano, pesos, valores, n - 1)

  return max(valores[n - 1] + morral(tamano - pesos[n - 1], pesos, valores, n - 1), 
            morral(tamano, pesos, valores, n - 1))


if __name__ == "__main__":
  valores = [50, 100, 210]
  pesos = [10, 25, 35]
  tamano = 35
  n = len(valores)
  print(f'Valores: {valores}, Pesos: {pesos}')
  resultado = morral(tamano, pesos, valores, n)
  print(resultado)