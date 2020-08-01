import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor() # cursor : 데이터 베이스와 sql문을 연결해주는 extute함수 제공

cursor.execute("select * from phonebook") # 실행

rows = cursor.fetchall()  # 데이터를 가져옴(꺼내오기)

for row in rows:
    print("name:{0}, phone:{1}, email:{2}".format(row[0],row[1],row[2]))

cursor.close()
conn.close()





