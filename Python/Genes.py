import psycopg2

conn = psycopg2.connect(f"dbname='Genes' user='postgres' "
                            f"host='localhost' password='Mcherving18'")
cur = conn.cursor()

query = "select id from dados"
cur.execute(query)
resultado = cur.fetchall()
print(resultado)

query = "insert into dados (id, name, cromossome) values (7422 , 'VEGFA', 6);"