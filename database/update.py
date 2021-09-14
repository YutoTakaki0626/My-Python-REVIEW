import sqlite3

con = sqlite3.connect('sample.db')
cursor = con.cursor()

target_name = input('Whose "age" do you want to update? : ')
new_age = input('Tell me new age : ')

# SQL injection の危険
# update_query = f"UPDATE User SET age={new_age} WHERE name='{target_name}';"
# cursor.executescript(update_query)

update_query = 'UPDATE User SET age=? WHERE name=?'
cursor.executescript(update_query, (new_age, target_name))
cursor.executescript(update_query, (new_age))

con.commit()
