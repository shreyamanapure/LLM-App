import sqlite3

connection=sqlite3.connect("students.db")

cursor=connection.cursor()

#creating table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Shreya','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Swayam','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Shruti','Data Science','A',80)''')
cursor.execute('''Insert Into STUDENT values('Somya','Data Science','B',60)''')
cursor.execute('''Insert Into STUDENT values('Simma','Data Science','A',65)''')

## Display ALl the records

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

#close connection
connection.commit()
connection.close()


