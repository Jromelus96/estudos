# Estruturas Condicionais
"""Comando Condicinal If :
                           - Realiza testes condicinais
                           - Executa um bloco SE uma determinada
                             condicao for atendida
                           - Avalia se condicao e True ou False."""

x = 5
y = 5000

if x > y:
    print("x e maior que y")

# Indentacao
"""         - Python blocos sao definidos pelo espacamento
             da linha
            - Pode ser com (4) espasos ou tabulacoes (Tecla : TAB)
"""

# Estruturas condicionais Commando Else
"""
Comando Else,e executado caso a condicao do comande If nao seja atendida
"""

x = 1
y = 9

if x > y:
        print("x maior que y")
else:
    print("x nao e maior que y")

# estruturas condicionais Comando Elif
""" Comando Elif e executado caso a condicao do comando if nao seja etendida tambem 
"""

person = "Herving"

if person == "Junior":
    print("Welcom, Junior")
elif person == "Herving":
    print("welcom,Herving")
else:
    print("welcome, qual e o seu nome?")