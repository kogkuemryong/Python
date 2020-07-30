import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 삽입 코드에는 ?를 넣어서 보안성을 높인다.
cursor.execute("""
insert into phonebook values(?,?,?)   
""",('홍깅동','010-5555-5555','hkd@hong.com'))

id = cursor.lastrowid # 마지막 레코드의 id 값을 가짐
print(id)

cursor.execute("""
insert into phonebook values(?,?,?)   
""",('이순신','010-6666-6666','lss@hlee.com'))

id = cursor.lastrowid # 마지막 레코드의 id 값을 가짐
print(id)

conn.commit() # dml 명령어를 수행하고 나서는 commit 해줘야 한다.

cursor.close()
conn.close()

