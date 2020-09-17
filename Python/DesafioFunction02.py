import psycopg2
#
# def funcao(x,y):
#     soma = x + y
#     return soma
# print(funcao(2, 3))
#
#
# def adicionar(x):
#     soma = x + 1
#     return soma
# print(adicionar(0))
#
# def converter():
#     m = int(input("entra o tempo em minute: "))
#     s = m * 60
#     return s
# print(converter())


conn = psycopg2.connect(f"dbname='Mercado' user='postgres' "
                            f"host='localhost' password='Mcherving18'")
cur = conn.cursor()

query = "select * from categoria"
cur.execute(query)
resultado = cur.fetchall()
print(resultado)

query = "insert into categoria (id, descricao, status) values (8 , 'Peixe', 6);"
cur.execute(query)
conn.commit()
