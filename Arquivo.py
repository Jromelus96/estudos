# Arquivo
""" modo de abertura : r    Somente leitura
                       W    Escrita (caso o arquivo ja exista ,ele sera apagado
                              e um novo arquivo vazio sera criado)
                       a    Leitura e escrita (adiciona o novo conteudo ao fim do arquivo
                       r+   Leitura e escrita
                       w+   Escrita (o modo w,assim como o w,tambem apagar o conteudo
                              anterior do arquivo)
                       a+   Leitura e escrita (abre arquivo para atualizacao)"""

# Lendo Arquivo
""" read()      :        le arquivo inteiro
    readline(  ):        le uma linha
    readlines() :        le arquivo e amarzena em uma lista """


arquivo = open("arquivo.txt")

linhas = arquivo.readlines()
for linha in linhas:
    print(linha)


# Texto Completo

arquivo = open("arquivo.txt")

texto_completo = arquivo.read()
print(texto_completo)

# Vou cria um Archivo2

arquivo2 = open("arquivo2.txt", "a")

arquivo2.write("Isso e meu novo Archivo")

arquivo2.close()

"""Se o archivo2 for criado com "a" ele vai duplucar o conteudo ao fim do meu archivo"""