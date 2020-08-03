import numpy as np
import matplotlib.pyplot as plt

# 배열 생성
# - 1차원 배열(Vector) 정의
arr = np.array([1,2,3])
print(arr) # [1 2 3]
print(type(arr)) # <class 'numpy.ndarray'>

# - 2차원 배열(Matrix) 정의
arr2 = np.array([[1,2,3],[4,5,6]]) # 2행 3열
print(arr2)
print(type(arr2)) # <class 'numpy.ndarray'>
print("arr2.shape:{0}".format(arr2.shape)) # (2, 3)

# - 3차원 배열(Array) 정의
 # 2면 2행 3열
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3)
print("arr3.shape:{0}".format(arr3.shape)) # (2, 2, 3)

# 배열 생성 및 초기화
# zeros((행, 열)): 0으로 채우는 함수.
arr_zeros = np.zeros((3,4))
print(arr_zeros)

# ones((행, 열)): 1로 채우는 함수
arr_ones = np.ones((2,2)) # 2행 2열
print(arr_ones)

# full((행, 열), 값): 값으로 채우는 함수
arr_full = np.full((3, 4), 7)
print(arr_full)

# eye(N): (N,N)의 단위 행렬 생성
arr_eye = np.eye(5)
print(arr_eye)

# empty((행, 열)): 초기화 없이 기존 메모리 값이 들어감.
arr_empty = np.empty((3,3))
print(arr_empty)

# _like(배열) 지정한 배열과 동일한 shape의 행렬을 만듦.
# 종류: np.zeros_like(), np.ones_like(), np.full_like(), np.empty_like()
arr_sample = np.array([[1,2,3],[4,5,6]])
arr_like = np.ones_like(arr_sample)
print(arr_like)

# 배열 데이터 생성 함수
# - np.linspace(시작, 종료, 개수): 개수에 맞게끔 시작과 종료 사이에 균등하게 분배.
arr_linspace = np.linspace(1,10,5)
print(arr_linspace) # [ 1. 3.25 5.5 7.75 10.  ]

plt.plot(arr_linspace, 'o') # 그래프를 그려주는 함수 마커를 원('o')으로
#plt.show()                  # 만든 그래프를 보여줌.

# np.arange(시작, 종료, 스텝): 시작과 종료 사이에 스텝 간격으로 생성.
arr_arange = np.arange(1,20,2)
print(arr_arange)

plt.plot(arr_arange, 'v')
#plt.show()


# list vs ndarray(1차원 배열(Vector))
x1 = [1,2,3]
y1 = [4,5,6]
print(x1+y1) # [1, 2, 3, 4, 5, 6]

x2 = np.array([1,2,3])
y2 = np.array([4,5,6])
print(x2+y2) # [5 7 9]

print(type(x1)) # <class 'list'>
print(type(x2)) # <class 'numpy.ndarray'>

print(x2[2]) # 요소의 참조: 3
x2[2] = 10   # 요소의 수정
print(x2)    # [ 1  2 10]

# 연속된 정수 벡터의 생성
print(np.arange(10)) # [0 1 2 3 4 5 6 7 8 9]
print(np.arange(5,10)) # [5 6 7 8 9]

x = np.array([10,11,12])
for i in np.arange(1,4):
    print(i)
    print(i+x)

# ndarray형의 주의점
a = np.array([1,1])
b = a  # 주소값 복사

print('a = '+ str(a)) # [1 1]
print('b = '+ str(b)) # [1 1]

b[0] = 100
print('a = '+ str(a)) # [100 1]
print('b = '+ str(b)) # [100 1]

###########################
a = np.array([1,1])
b = a.copy()

print('a = '+ str(a)) # [1 1]
print('b = '+ str(b)) # [1 1]

b[0] = 100
print('a = '+ str(a)) # [1 1]
print('b = '+ str(b)) # [100 1]

# 행렬(2차원)
x = np.array([[1,2,3],[4,5,6]]) # 2행 3열
print(x)
print(type(x))
print(x.shape) # (2, 3) - 튜플
w, h = x.shape
print(w) # 2
print(h) # 3
print(x[1,2]) # 6
x[1,2] = 10 # 요소의 수정
print(x)

# 행렬의 크기 변경
a = np.arange(10)
print(a)
a_arange = a.reshape(2,5)
print(a_arange)
"""
[[0 1 2 3 4]
 [5 6 7 8 9]]
"""
print(type(a_arange)) # <class 'numpy.ndarray'>
print(a_arange.shape) # (2, 5)

# 행렬(numpy.ndarray)의 사칙 연산
# - 덧셈
x = np.array([[4,4,4],[8,8,8]])
y = np.array([[1,1,1],[2,2,2]])
print(x+y)
"""
[[ 5  5  5]
 [10 10 10]]
"""

# - 스칼라 x 행렬
x = np.array([[4,4,4],[8,8,8]])
scar_arr = 10 * x
print(scar_arr)
"""
[[40 40 40]
 [80 80 80]]
"""

# - 산술함술 : np.exp(x) - 지수 함수 , np.sqrt() - 루트 씌운 값, np.log() - 로그 함수 , np.round() - 반올림,
#                         np.mean() - 평균, np.std() - 표준편차, np.max() - 최대 , mp.min() - 최소
print(np.exp(x)) # 지수 함수 : y = e(x제곱)

"""
[[  54.59815003   54.59815003   54.59815003]
 [2980.95798704 2980.95798704 2980.95798704]]
"""

# 행렬 * 행렬
a = np.array([[1,2],[3,4]])
b = np.array([[1,1],[2,2]])
print(a * b)

"""
[[1 2]
 [6 8]]
"""

# 내적의 곱
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[7],[7],[7]])
print(x.dot(y))

""" (2x1) 
[[ 42] (1*7)+(2*7)+(3*7)
 [105]] (4*7)+(5*7)+(6*7)
"""

x = np.array([[1,2,3],[4,5,6]])
y = np.array([[7,2],[7,2],[7,2]])
print(x.dot(y))

""" (2x2)
[[ 42  12]  (1*7)+(2*7)+(3*7) (1*2)+(2*2)+(3*2)
 [105  30]] (4*7)+(5*7)+(6*7) (4*2)+(5*2)+(6*2)

"""


# 원소 접근
data = np.array([[51,55],[14,19],[0,4]])
print(data)
print(data.shape) # (3, 2)
print(data[0][1]) # 55 행렬의 인덱스로 접근

for row in data:
    print(row)
"""
[51 55]
[14 19]
[0 4]
"""

y = data.flatten() # data를 1차원 배열로 변환(평탄화)
print(y) # [51 55 14 19  0  4] // ( 3 , 2 ) -> 1차원 배열

# 슬라이싱
x = np.arange(10)
print(x[:5]) # [0 1 2 3 4]
print(x[5:]) # [5 6 7 8 9]
print(x[3:8]) # [3 4 5 6 7]
print(x[3:8:2]) # [3 5 7]
print(x[::-1]) # [9 8 7 6 5 4 3 2 1 0]

y = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 3행 3열
print(y[:2,1:2])  # (0,1),(1,1)
"""
[[2]
 [5]]
"""

# 조건을 만족하는 데이터 수정
# - bool 배열 사용
x = np.array([1,1,2,3,4,5,8,15]) # list -> array
print(x > 3) # array 와 비교 연산사를 사용하면 boolean 값이 출력 [False False False False  True  True  True  True]

y = x[x > 3] # true인 데이터만 선택된다.
print(y) # [ 4  5  8 15]

x[x > 3] = 555 # 조건이 일치하면 555 담겨진다.
print(x) #  [  1   1   2   3 555 555 555 555]

# - Numpy에서 np.sum 한수의 axis 이해
arr = np.arange(0,4*2*4) # start = 0, end = 31
print(len(arr)) # 32(0~31)

v = arr.reshape([4,2,4]) # 차원의 변경(depth(z축), row(x축), colum(y축)) - (4면, 2행, 4열)
print(v)
"""
[[[ 0  1  2  3]
  [ 4  5  6  7]]

 [[ 8  9 10 11]
  [12 13 14 15]]

 [[16 17 18 19]
  [20 21 22 23]]

 [[24 25 26 27]
  [28 29 30 31]]]
"""

print(v.shape) # (4, 2, 4) : 4 면 2행 4열

print(v.ndim) # v의 차원 : 3차원

print(v.sum()) # 496 : 모든 요소의 합 : (0 ~ 31) 까지 더한 값

print(v.sum(axis=0))  # axis=0 : row 축(단위)로 계산 / 면단 위로
"""
[[48 52 56 60] (0+8+16+24) (1+9+17+25) (2+10+18+26) (3+11+19+27)
 [64 68 72 76]] (4+12+20+28) (5+13+21+29) (6+14+22+30) (7+15+23+31)
"""

print(v.sum(axis=1)) # axis=1 : colum 축(단위)로 계산 / 행 당위
"""
[[ 4  6  8 10] (0+4) (1+5) (2+6) (3+7)
 [20 22 24 26] (8+12) (9+13) (10+14) (11+15)
 [36 38 40 42] (16+20) (17+21) (18+22) (19+23)
 [52 54 56 58]] (24+28) (25+29) (26+30) (27+31)
"""

print(v.sum(axis=2)) # axis=2 : depth 축(단위)로 계산 / 열 단위
"""
[[  6  22] (0+1+2+3) (4+5+6+7)
 [ 38  54] (8+9+10+11) (12+13+14+15)
 [ 70  86] (16+17+18+19) (20+21+22+23)
 [102 118]] (24+25+26+27) (28+29+30+31) 
"""























