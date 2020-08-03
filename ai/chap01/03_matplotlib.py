import matplotlib.pyplot as plt  # plot 함수 제공
import numpy as np

# 단순한 그래프 그리기
# 데이터 준비
x = np.arange(0,6,0.1) # start 0 ~ last 5 , step = 0.1 (0.1~5.9)
y1 = np.sin(x) # 사인함수 를 이용하여 0.1단위로 계산해서 y1에 저장
y2 = np.cos(x) # 코사인함수 를 이용하여 0.1단위로 계산해서 y2에 저장

# 그래프 그리기
plt.plot(x, y1, label = "sin")
plt.plot(x, y2, linestyle = "--", label = "cos") # cos 함수는 점선으로 그리기
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름
plt.title("sin & cos") # 제목
plt.legend() # 범례
plt.show() # 출력

np.random.seed(1234) # 난수를 고정(생성되어지는 random 값 고정해서 반환)
x = np.arange(10)
y = np.random.rand(10) # random 한 값을 생성. (but, seed를 이용하면 random한 값이 고정)

plt.plot(x,y) # 꺽은선 그래프를 등록 / 10개의 난수를 plot 함수를 이용하여 꺽은석 그래프로 피드백.
plt.show() # 그래프 그리기


# 3차 함수 f(x) = (x-2) x (x+2)
def f(x):
    return (x-2) * x * (x+2) # 3차 함수 정의

print(f(0)) # 0
print(f(2)) # 0
print(f(-2)) # 0

# x값에 대해 ndarray  배열이며 각각에 대한 f를 한꺼번에 ndarray로 돌려줍니다.
print(f(np.array([1,2,3]))) # [-3  0 15]
print(type(f(np.array([1,2,3])))) # <class 'numpy.ndarray'>

#  그래프를 그리는 x의 범위를 -3 ~ 3까지로 하고 , 간격 0.5

x = np.arange(-3,3.5,0.5)
plt.plot(x,f(x))
plt.show()

# 그래프를 장식
def f2(x, w):
    return (x-w) * x * (x+2) # 함수를 정의

# x를 정의
x = np.linspace(-3,3,100) # x를 100 분할하기

# 차트 묘사
plt.plot(x, f2(x,2), color = "black")
plt.plot(x, f2(x,1), color = "blue")
plt.legend(loc="upper left") # 범례의 위치도 정해줄 수 있다.
plt.ylim(-15,15) # y축 범위
plt.title("f2(x, w) 함수")
plt.xlabel("x축")
plt.ylabel("y축")
plt.grid(True) # 그리드(눈금)
plt.show()

# 그래프를 여러 개 보여주기
plt.figure(figsize=(10,3)) # 전체 영역의 크기를 지정
plt.subplots_adjust(wspace=0.5, hspace=0.5) # 그래프의 간격을 지정

for i in range(6):  # 0 ~ 5
    plt.subplot(2, 3, i+1) # 그래프 위치를 지정 # 2행 3열
    plt.title(i+1)
    plt.plot(x,f2(x,i))
    plt.ylim(-20,20)
    plt.grid(True)

plt.show()

# 이미지 표시하기
from matplotlib.image import imread

img = imread('image/2.png') # 이미지 읽어오기

plt.imshow(img)
plt.show()

























