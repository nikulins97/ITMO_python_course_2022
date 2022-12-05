import psycopg2

conn = psycopg2.connect(database='registration', user='postgres', host='localhost', password='qwerty123')
cur = conn.cursor()

cur.execute("CREATE TABLE clients (client_id serial PRIMARY KEY, name varchar, surname varchar, phone varchar);")

conn.commit()

cur.close()
conn.close()
