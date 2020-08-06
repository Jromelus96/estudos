# Lacos de Repeticao

"""- Estrutura de repeticao
   - Iteradores   ( iterar == repetir)
   - Repetem um trecho do codigo
     - Enquanto uma condicao avaliada for verdaderira
     - Durante uma pre-determinada condicao """

# Lacos While

x = 1

while x < 10:
    print(x)
    x = x + 2

# Laco For (Para)

lista1 = [1, 2, 3]
lista2 = ["Welcome", "Junior", "!"]
lista3 = [15, "Junho 1996", 18,99, True ]

for i in  lista1:
    print(i)
for i in lista2:
    print(i)
for i in lista3:
    print(i)

""" Alem dissoeu posso combinar o comando For com a funcao Range
    Funcao Range : ela retorno uma lista """

for i in range (10, 20, 2):
    print(i)