import time

def factorial(n):
  respuesta = 1

  while n > 1:
    respuesta *= n
    n -= 1

  return respuesta

def factorialRecursivo(n):
  if n == 1:
    return 1

  return n * factorialRecursivo(n - 1)

if __name__ == "__main__":
    n = 999

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorialRecursivo(n)
    final = time.time()
    print(final - comienzo)