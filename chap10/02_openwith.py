'''
with open('test.txt','rt') as flie:
    str = file.read()
    print(str)
    # fire.close() # 이 코드는 필요 x
'''

'''
# 텍스트 파일 일기 / 쓰기
    1. 문자열을 담은 리스트를 파일에 쓰는 writelines() 메서드  
'''

# ex1)
lines = ["we'll find a way we always have - Intersteller\n",
         "I'll find you and I'll kill you - Taken\n",
         "I'll ve back - Terminator2\n"]

with open('movie_quotes.txt','w') as file:
    for line in lines:
        file.write(line) #한줄씩 저장

# ex2)
with open('movie_quotes.txt', 'w') as file:
    file.writelines(lines)


'''
# 텍스트 파일 일기 / 쓰기
    2. 문자열을 담은 리스트를 파일에 쓰는 readline() & readlines() 메서드  
'''
# readine
with open("movie_quotes.txt","r") as file:
    line = file.readline()

    while line != '':
        print(line, end='') # 한 라인상에 연속해서 출력
        line = file.readline()


# ex2)
with open("movie_quotes.txt","r") as file:
    lines = file.readlines()
    line = ''
    for line in lines:
        print(line, end='')




