import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor() # cursor : 데이터 베이스와 sql문을 연결해주는 extute함수 제공

cursor.execute("""
delete from phonebook where email =?
""",('hkd@hong.com',)) # .tuple의 자료일 때 하나만 입력하려 (,)를 통해서 가능

cursor.close()
conn.close()

