with open("C:/Users/Magic Studio/Downloads/mutation.csv", "r") as mutatation:
    arquivo = mutatation.readlines()[1:]
    print(arquivo)

    dic = {}

    for linha in arquivo:
        print(linha, end="")
        dados = linha.rstrip().split("\t")
        dic[dados[0]]=dados[1:]
    #quebra = arquivo.split()
    #dic[quebra[0]] = [quebra[1], quebra[2], quebra[3], quebra[4], quebra[5], quebra[3]]
    print(dic)