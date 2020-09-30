import  psycopg2

conn = psycopg2.connect(f"dbname='Genes' "
                        f"user='postgres' "
                        f"host='localhost'"
                        f"password='Mcherving18'")

cur = conn.cursor()

# Query_Select
query = "select id,name from dados"
cur.execute(query)
print("Os itens a selecionar são")
resultado = cur.fetchall()
print(resultado)


if(conn):
    cur.close()
    conn.close()
    print("Postgres esta fechado")

