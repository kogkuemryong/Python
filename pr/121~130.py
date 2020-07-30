# 121
# 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
#answer = input('입력(영문) : ')
#if answer.islower()==True:
#    print(answer.upper())
#elif answer.isupper()==True:
#    print(answer.lower())

# 122
# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
# 점수	 학점
# 81~100 A
# 61~80	 B
# 41~60	 C
# 21~40	 D
# 0~20	 E
#score = input("점수를 입력해주세요 :")
#score = int(score) # 입력 받는 값을 숫잘 바꿔야 하기 때문에 int()!!!!
#if 81 <= score <= 100:
#    print("grade is A")
#elif 61 <= score <= 80:
#    print("grade is B")
#elif 41 <= score <= 60:
#    print("grade is C")
#elif 21 <= score <=40:
#    print("grade is D")
#else:
#    print("grade is E")

# 124
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
#num1 = input("숫자를 입력해주세요 : ")
#num2 = input("숫자를 입력해주세요 : ")
#num3 = input("숫자를 입력해주세요 : ")
#num1 = int(num1)
#num2 = int(num2)
#num3 = int(num3)
#if num1 > num2 and num1 >  num3:
#    print(num1)
#elif num2 > num1 and num2 > num3:
#    print(num2)
#elif num3 > num1 and num3 > num2:
#    print(num3)

# 125
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다.
# 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
# 번호	통신사
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음
#phone = input("전화번호를 입력하세요 : ")
#if phone[:3] == "011":
#    com = "SKT"
#elif phone[:3] == "016":
#    com = "KT"
#elif phone[:3] == "019":
#    com = "LGU"
#elif phone[:3] == "010":
#    com = "알수없음"
#print(f"당심은 {com} 사용자 입니다.")

# 126
# 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.
#       0	    1	    2	    3	    4	    5	    6	    7	    8	    9
# 01	강북구	강북구	강북구	도봉구	도봉구	도봉구	노원구	노원구	노원구	노원구
# 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라
'''
pax = input("우편번호를 입력하세요 (5자리) : ")
if pax[:3] in ["010"]:
    com ="강동구"
elif pax[:3] in ["011","012"]:
    com = "강북구"
elif pax[:3] in ["013","014","015"]:
    com = "도봉구"
elif pax[:3] in ["016","017","018","019"]:
    com = "노원구"
print(f"당신은 {com}으로 보내시는군요.")
'''

# 127
# 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다.
# 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
'''

num = input("주민등록 번호를 입력하세요 : ")
# 방법 1
backnum = num.split("-")[1]
if numback[0] == "1" or  numback[0] == "3":
    print("남자")
else:
    print("여자")

# 방법 2 
if num[7:8:] in["1","3"]:
    com = "남자"
elif num[7:8] in["2","4"]:
    com = "여자"
print(f"당신의 성별은 {com} 입니다.")
'''

# 128
# 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
# 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
# 지역코드	출생지
# 00 ~ 08	서울
# 09 ~ 12	부산

'''
num = input("주민번호를 입력해주세요 : ")

# 방법 1 
if num[8:10] in ["00","01","02","03","04","05","06","07","08"]:
    com = "서울"
elif num[8:10] in ["09","10","11","12"]:
    com = "부산"
print(f"당신이 사는 곳은 {com} 입니다.")


# 방법 2
backnum = num.split("-")[1] # 나눈 것에서 index 1 = 뒷자리
if 0 <= int(backnum[1:3]) <=8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")
'''


# 130
# 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다.
# 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.
# Key Name	    Description
# opening_price	최근 24시간 내 시작 거래금액
# closing_price	최근 24시간 내 마지막 거래금액
# min_price	    최근 24시간 내 최저 거래금액
# max_price   	최근 24시간 내 최고 거래금액




