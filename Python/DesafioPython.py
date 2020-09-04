with open("C:/Users/Magic Studio/Downloads/mutation.csv", "r") as mutatation:
    arquivo = mutatation.read()
    print(arquivo)

    dic = {}

    for linha in arquivo:
        print(linha, end="")
    quebra = arquivo.split()
    dic[quebra[0]] = [quebra[1], quebra[2], quebra[3], quebra[4], quebra[5], quebra[6]]
    print(dic)