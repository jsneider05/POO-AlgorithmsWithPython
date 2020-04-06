# Ley de la suma


#Ejemplo 1

def f1(n):

  for i in range(n):
    print(i)

  for i in range(n):
    print(i)

# O(n) + O(n) = O(n + n) = O(2n) = O(n)
# Crecimiento lineal con respecto a n
# La funcion crece en O(n) 


#Ejemplo 2

def f2(n):

  for i in range(n):
    print(i)

  for i in range(n * n):
    print(i)

# O(n) + O(n * n) = O(n + n^2) = O(n^2)
# Crecimiento cuadratico con respecto a n
# La funcion crece en O(n^2)