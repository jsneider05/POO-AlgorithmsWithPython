def f(x):

  response = 0          # 1 operation

  for i in range(1000):
    response += 1       # 1000 operations

  for i in range(x):
    response += x       # x operations

  for i in range(x):
    for j in range(x):
      response += 1
      response += 1     # 2x^2 operations

  return response       # 1 operation

                        # _______________
                        # 1002 + x + 2x^2 operations