# O que é um dicionário em python? e como criar um dicionário em python?
""" Um {Dicionario} consiste em uma chave e depois emum valor associado.
esse valor pode ser quase qualquer tipo objeto em Python
criamos o dicionário com Chaves {}
"""

dico = {1: "Merlin", 2: "Lancelot", 3: "Perceval"}
print(dico)

# podemos adicionar um elemento em um dicionario ?
""" SIM,Para inserir novos elementos em um dicionario, existem duas formas.
A primeira e passar o valor ao indice de um dicionario e a segunda e utilizando o metodo update(),
passando como parametro a chave e o elemento a ser adicionado
"""

dico[4] = "Rei Arthur"

dico.update({5: "Excalibur"})
print(dico)

# Podemos remover um item de um dicionario?
"""Para remover elementos de um dicionario utilizamos o metodo pop()
seguido do indice do elemento que deve ser removido.
Isso fara com que o elemento seja removido, como podemos ver no codigo abaixo
"""

dico.pop(5)
print(dico)

# Como Retornar o tamanho de um dicionario ?
""" Para retornar o tamanho de um dicionario, podemos utilizar o metodo len()
e passar o dicionario a ser analisado como parametro
"""

print(len(dico))
print(dico)
