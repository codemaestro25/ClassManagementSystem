import pymysql

def connection():
    conn = pymysql.connect(host = 'localhost', user='root', password='12345678', db='cms')
    if(conn):
        print("Database Connected ")
    return conn

def getDetails(table):
    # making db connection
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select * from details")
    results = cursor.fetchall()
#     loop for displaying the data
    for data in results:
        table.insert('', 'end', values=(data))
    conn.commit()
    conn.close()

