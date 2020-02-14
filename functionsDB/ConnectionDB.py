import psycopg2 as dbapi

def abrirconexion():
    con = dbapi.connect("dbname='d6ufcnrlk9c7lb' user='iqgxcjpyhzimhk' host='ec2-52-203-160-194.compute-1.amazonaws.com' password='b961f23b0f9d5d31b9fa9bc8d9af26e8548ffb7453cfe568b13d9abd62b8d546'")
    cur = con.cursor()
    return cur,con

def cerrarconexion(cur,con):
    con.commit()
    cur.close()
    con.close()