import sqlite3
conn = sqlite3.connect("cms.db")
print("Database Created Successfully")


cur = conn.cursor()
# cur.execute("create table login (id integer primary key , username text not null, pass text not null)")
# print("Login Table Created")

cur.execute("insert into login (id,username,pass) values (1258,'Devesh','1234')")
print("Entry added")
conn.close()