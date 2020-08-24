
bebidas = "/Users/Excalibugator/PycharmProjects/estudos/Bebidas.txt"

arquivo = open(bebidas, "r")

dic = {}
for linha in arquivo:
    print(linha)
    quebra = linha.strip("\t")
    dic[quebra[0]] = [quebra[1], quebra[2]]
    print(dic)