import pymysql

conn=pymysql.connect(
host= 'localhost',
database= 'test',
user= 'root',
password= '',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor
)

cursor=conn.cursor()
sql_query=""" CREATE TABLE movies(
id integer PRIMARY KEY,
Name text NOT NULL,
Actor text NOT NULL,
Actress text NOT NULL,
Year text NOT NULL,
Director text NOT NULL,
)"""
cursor.execute(sql_query)
conn.close()