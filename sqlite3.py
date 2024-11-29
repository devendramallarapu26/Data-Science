import sqlite3
os.chdir('d://TextFile')
conn = sqlite3.connect('gcet1.db')  # creating the database
cursor = conn.cursor()
cursor.execute('''create table test1(col1 int,col2 int,col3 int)''')
cursor.execute('''insert into test1 values(1,2,3)''')
cursor.execute('''insert into test1 values(4,5,6)''')
records = cursor.execute('''select * from test1''')
for record in records:
    print(record)
output:
(4, 5, 6)
(1, 2, 3)
