# 071
# my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()
print(type(my_variable))


# 072
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다.
# 영화 제목을 movie_rank 이름의 튜플에 저장하라.(순위 정보는 저장하지 않는다.)
# 순위 영화
# 1   닥터 스트레인지
# 2   스플릿
# 3   럭키

movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

# 073
# 숫자 1 이 저장된 튜플을 생성하라.
tupe = (1,)
print(type(tupe))

# 075
# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다.
# t가 바인딩하는 데이터 타입은 무엇인가?
# t = 1, 2, 3, 4
# 답 : 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만,
#      사용자 편의를 위해 괄호 없이도 동작합니다.


# 076
# 변수 t에는 아래와 같은 값이 저장되어 있다.
# 변수 t가 ('A', 'B', 'C') 튜플을 가리키도록 수정 하라.
t = ('a', 'b', 'c') # 변경 되지 않기 때문에
t = ('A', 'B', 'C') # 기존 튜플 자동 삭제
print(t)


# 077
# 다음 튜플을 리스트로 변환하라. 튜플 -> 리스트 (list)
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
print(data, type(data))


# 078
# 다음 리스트를 튜플로 변경하라. 리스트 -> 튜플 (tuple)
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)
print(data, type(data))


# 079 튜플 언팩킹
# 다음 코드의 실행 결과를 예상하라.
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c) # apple banana cake


# 080 range 함수
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
# (2, 4, 6, 8 ... 98)
data = tuple(range(2,100,2))
print(data)







