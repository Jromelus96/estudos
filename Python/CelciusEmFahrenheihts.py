def meu_function():
    c = float(input("informe a temperatura °C: "))
    f = ((c * 9) / 5) + 32
    print(" A temperatura de {}°C corresponde a {}°F!".format(c,f))

meu_function()


"""Uma função é um bloco de código que só executa quando chamado.
Você pode passar dados, chamados de parâmetros, para uma função.
Uma função pode retornar dados de acordo.
Em Python, uma função é definida usando a palavra-chave def:
Para chamar uma função, use o nome da função seguido por parênteses:"""


#Argumentos ( A estudar melhor)
"""As informações podem ser passadas para funções como argumentos.
Os argumentos são especificados após o nome da função, entre parênteses. 
Você pode adicionar quantos argumentos quiser, apenas separe-os com uma vírgula.
O exemplo a seguir tem uma função com um argumento (fname). Quando a função é chamada,
 passamos um primeiro nome, que é usado dentro da função para exibir o nome completo:"""