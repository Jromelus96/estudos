# Python Lambda

"""Uma funcao lambda e uma pequena funcao anonima.
Uma funcao lambda pode receber qualquer numero de argumentos, mas so pode ter uma expressao."""

"""Syntaxe
lambda arguments : expression"""

# adicione 500  ao argumento a retornou o resultado:

lamb = lambda a : a + 500
print(lamb(5))

# Multiplique o argumento lamb pelo argumento b e c retorne o resultado:

lamb = lambda a, b : a * b
print(lamb(5, 6))

# Resuma os argumentos a, bec e retorne o resultado:

lamb = lambda a, b, c : a + b + c
print(lamb(5, 6, 9))

# Por que usar funções Lambda?
"""O poder do lambda é melhor mostrado quando você os usa como uma função anônima em outra função.
Suponha que você tenha uma definição de função que leva um argumento,
e esse argumento será multiplicado por um número desconhecido:"""

def myfunc(n):
  return lambda a : a * n

# Use esta definição de função para criar uma função que sempre duplica o número que você envia:

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(5))

# Ou use a mesma definição de função para criar uma função dupla e uma função tripla,mesmo programa:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(5))
print(mytripler(5))