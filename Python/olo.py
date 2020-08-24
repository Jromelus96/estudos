arq = open("../Txt/abc.txt", "w+")
arq.write("Linha o\n")
arq.write("Linha 1\n")
arq.write("Linha 2\n")
arq.write("Linha 3\n")

# Read
arq.seek(0)
print(arq.read())

# Leo uma linha
arq.seek(0)
print(arq.readline())

# READLINES com For Laco (for) e (in)
arq.seek(0)
for linha in arq.readlines():
    print(linha, end="")

# Jogar minha linha na uma lista
arq.seek(0)
print(arq.readlines())
