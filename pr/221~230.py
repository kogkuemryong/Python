#221
#입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
def print_reverse(string):
    print(string[::-1])

print_reverse("python")

# 222
# 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
def print_score(score):
    print(sum(score)/len(score))

print_score([1,2,3])

# 223
# 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# print_even ([1, 3, 2, 10, 12, 11, 15])

def print_even(score):
    for i in score:
        if i % 2 ==0:
            print(i)
print_even([1, 3, 2, 10, 12, 11, 15])



# 224
# 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})

def print_keys(data):
    print(dict(data).keys())

print_keys({"이름":"김말똥", "나이":30, "성별":0})

def print_key1(data):
    for i in data.keys():
        print(i)

print_key1({"이름":"김말똥", "나이":30, "성별":0})

def print_key2(dic):
    keys = dic.keys()
    for i in keys:
        print(i)
print_key2({"이름":"김말똥", "나이":30, "성별":0})


# 225
# my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.

def print_value_by_key(dic,key):
    print(dic[key])

print_value_by_key(my_dict,"10/26")


def print_value_by_key1(dic,key):
    print(dic[key])

print_value_by_key1(my_dict,"10/27")


# 226
# 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
# print_5xn("아이엠어보이유알어걸")
def print_5xn(string):
    num = int(len(string)/5)
    for x in range(num + 1):
        print(string[x * 5: x * 5 +5])
print_5xn("아이엠어보이유알어걸")

def print_5xn1(data):
    times = len(data)/5 # 2.0
    times = int(times)  # 2
    print(times)

    for i in range(times):
        print(data[5*i:5*i+5]) # [0:5] , [5:10]

def print_5xn1(data):
    times = len(data)/5 # 2.0
    times = int(times+0.9)  # 2
    print(times)

    for i in range(times):
        print(data[5*i:5*i+5]) # [0:5] , [5:10]
print_5xn1("아이엠")


# 227
# 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된
# 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
# printmxn("아이엠어보이유알어걸", 3)

def print_mxn(string, num):
    times = len(string)/num
    times = int(times+0.9)

    for i in range(times):
        print(string[num*i:num*i+num])

print_mxn("아이엠어보이유알어걸",3)

import math
a = math.ceil(2.1)
print(a) #3 올림 처리 해준다.

def print_mxn1(data, num):
    time = len(data)/num
    time = math.ceil(time)

    for i in range(time):
        print(data[i*num: (i+1)*num]) # num = 3 , i = 0  / 0:3, 3:6
print_mxn1("아이엠어보이유알어걸",3)


# 228
# 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라.
# 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# calc_monthly_salary(12000000)

def calc_monthly_salary(data):
    pay = int(data/12)
    print(pay)

calc_monthly_salary(12000000)


# 229
# 아래 코드의 실행 결과를 예측하라.
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)
my_print(a=100, b=200)
# 왼쪽 : 100 , 오른쪽 : 200

# 230
# 아래 코드의 실행 결과를 예측하라.
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)
my_print(b=100, a=200)

# 왼쪽 : 200
# 오른쪽 : 100
