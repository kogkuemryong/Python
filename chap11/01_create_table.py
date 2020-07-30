
import sqlite3  # 파이썬3에는 SQLite 라이브러리가 기본 탑재
'''
# 1. 커넥션(Connection) 열기
conn = sqlite3.connect('test.db')

# 2. 커서(Cursor) 열기
cursor = conn.cursor()

# 3. 커서를 이용하여 데이터 추가/조회/수정/삭제하기
cursor.execute() #sql문 전달 등 실제로 수행.

# 4. 커서 닫기
cursor.close()

# 5. 커넥션 닫기
conn.close()
'''

# test.db 파일 안에 phonebook 테이블 생성

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("""
    create table phonebook(
    name char(32),
    phone char(32),
    email char(64) primary key)
""")

cursor.close()
conn.close()

