# file에 write하기

# 연결통로 생성
file = open('test.txt','wt') # opne(file, mode)
                 # file이 없으면 file을 생성하고, 연결통로를 생성해준다.
                 # stream은 단방향성의 성질을 가지고 있기 때문에 어떤 특성으로 사용할지 지정해줘 한다.
file.write("hello")
file.close()

file = open('test.txt','rt')
str = file.read()
print(str)
file.close()


