import sqlite3
conn = sqlite3.connect('dict1.db')
cursor = conn.cursor()
cursor .execute('''create table dict1(author text,quote text)''')
for i in dict:
    cursor.execute('''insert into dict1(author , quote) values(?,?)''',(i,dict[i]))
records = cursor.execute('''select *  from dict1''')
for i in records:
    print(i)
