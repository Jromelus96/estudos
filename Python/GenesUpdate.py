import  psycopg2

conn = psycopg2.connect(f"dbname='Genes' "
                        f"user='postgres' "
                        f"host='localhost'"
                        f"password='Mcherving18'")

cur = conn.cursor()

query = "select * from dados"
cur.execute(query)
resultado = cur.fetchall()
print(resultado)


# QUERY_UPDATE
query_update = "update dados set id = '33817' where id = '348';"
cur.execute(query_update)
conn.commit()