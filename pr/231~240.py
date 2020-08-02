# 231
# 아래 코드를 실행한 결과를 예상하라.
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
# print (result)
# error 지역변수를 함수 밖에서 출력하려 하였기 떄문이다.
# 함수 내부에서 계산한 값을 전달하기 위해서는 return을 사용해야 합니다.


# 232
# 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# make_url("naver")
def make_url(domain):
    return "www."+ domain +".com"

result = make_url("naver")
print(result)

# 233
# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# make_list("abcd")
# ['a', 'b', 'c', 'd']

# 틀림
def make_list(data):
    for i in data:
       for j in i:
           print(j)
make_list("abcd")

# 방법 1
def make_list1(data):
    mylist = []
    for i in data:
        mylist.append(i) # i -> 'a'
    return mylist

result = make_list1("abcd")
print(result)

# 방법 2
def make_list2(data):
    return list(data)

result1=make_list2("abcd")
print(result1)

# 234
# 숫자로 구성된 하나의 리스트를 입력받아,
# 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
# pickup_even([3, 4, 5, 6, 7, 8])

def pickup_even(num):
    result = []
    for i in num:
        if i % 2 == 0 :
            result.append(i)
    return result

result = pickup_even([3, 4, 5, 6, 7, 8])
print(result)

# 235
# 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
# convert_int("1,234,567")

def convert_int(string):
    string = int(string.replace(',',''))
    return string
result = convert_int("1,234,567")
print(result)


# 236
# 아래 코드의 실행 결과를 예측하라.
def 함수(num) :
    return num + 4

a = 함수(10) # 14
b = 함수(a)  # 18
c = 함수(b)  # 22
print(c)    # 22

# 237
# 아래 코드의 실행 결과를 예측하라.
def 함수(num) :
    return num + 4
c = 함수(함수(함수(10))) # 14 , 18, 22
print(c) # 22

# 238
# 아래 코드의 실행 결과를 예측하라.
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10) # 14
c = 함수2(a) # 140
print(c) # 140

# 239
# 아래 코드의 실행 결과를 예측하라.

def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)  # 16
print(c) # 16

# 240
# 아래 코드의 실행 결과를 예측하라.

def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)  #2(12+2) 14 * 2 28

def 함수2(num) :
    num = num + 10 #12
    return 함수1(num)

c = 함수2(2)
print(c) # 28
