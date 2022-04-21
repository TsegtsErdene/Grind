import psycopg2 as pg

conn = None
curr = None
try:
    conn = pg.connect(host = "20.228.173.229" , dbname = "trade" , user = "postgres", password = 123 , port = 5432)

    cur = conn.cursor()
    insert_script = 'INSERT INTO positions (id,ticket,double,prec) VALUES (%s ,%s, %s, %s);'
    insert_value = (26,2153,0,23.1524)
    # cur.execute(insert_script,insert_value)
    cur.execute("SELECT * FROM positions")
    val = cur.fetchone()
    for rec in val:
        print(rec)
    conn.close()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()