import sqlite3

con = sqlite3.connect('sample.db')
cursor = con.cursor()

for row in cursor.execute('select * from User'):
    print(row)

# .fetchall():現在のcursor以下全てをタプルのリストで返す
cursor.execute('select * from User')
print(cursor.fetchall())

# .fetchone():現在のcursorのレコードをタプルで返す
cursor.execute('select * from User')
print(cursor.fetchone())
