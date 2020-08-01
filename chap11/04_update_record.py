import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor() # cursor : 데이터 베이스와 sql문을 연결해주는 extute함수 제공

cursor.execute("""
update phonebook set phone=?, email=? where name = ?
""", ('010-7777-7777','hongkd@hong.com','홍깅동'))

cursor.close()
conn.close()
