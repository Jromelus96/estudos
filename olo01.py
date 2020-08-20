abc = "/Users/Excalibugator/PycharmProjects/estudos/abc.txt"
abc = open(abc, "r")

dic = {}

for linha in abc:
    print(linha, end="")
    quebra = linha.strip().rstrip()
    dic[quebra[0]] = [quebra[1], quebra[2], quebra[3]]
    print(dic, end="")

