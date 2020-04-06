# Recursividad multiple

def fibonacci(n):
  
  if n == 0 or n == 1:
    return 1

  return fibonacci(n - 1) + fibonacci(n - 2)

# O(2**n)
# Crecimiento exponencial con respecto a n
# La funcion crece en O(2**n)

if __name__ == "__main__":
    print(fibonacci(5))