# Ley de la multiplicacion


#Ejemplo 1

def f(n):

  for i in range(n):
    for j in range(n):
      print(i, j)

# O(n) * O(n) = O(n * n) = O(n^2)
# Crecimiento cuadratico con respecto a n
# La funcion crece en O(n^2)

if __name__ == "__main__":
    f(5)