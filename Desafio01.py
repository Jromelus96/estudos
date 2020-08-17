tabela_precos = "/Users/Excalibugator/PycharmProjects/estudos/Tabela_Preco.txt"

arquivo = open(tabela_precos, "r")

dic = {}

for linha in arquivo:
    print(linha)
    quebra = linha.strip().split("\t")
    dic[quebra[0]] = [quebra[1], quebra[2]]
print(dic)