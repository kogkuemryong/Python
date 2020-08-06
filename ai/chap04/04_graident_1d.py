import numpy as np
import matplotlib.pyplot as plt # 시각화 관련 패키지

# 미분의 나쁜 구현 예(문제점 2가지)
def numerical_diff(f, x):
    h = 10e-50 # 1번째 문제점) 0에 최대한 가깝게 구현.
               # But python의 경우 np.float32(1e-50)는 0.0으로 처리(반올림 오차)
    return (f(x+h)-f(x)) / h # 2번째 문제점) (1e-50)보다 크게 하면 h에 의한 오차 발생.

# 문제점 행결 수지 미분의 예
def numerical_diff(f,x):
    h = 1e-4 # 0.0001
    return (f(x+h) -f(x-h))/2*h # x를 중심으로 그 전후의 차분을 계산한다. : 중심차분 혹은 중앙차분
                                # 오차는 존재하지만 접선의 기울기를 그리는 것과 같은 효과를 낼 수 있다.

def function_1(x):
    return 0.01 * x ** 2 +0.1 * x

x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
# plt.show()

print(numerical_diff(function_1,5))
# 1.9999999999908982e-09
print(numerical_diff(function_1,10))
# 2.999999999986347e-09


# 편미분의 예
# - f(x0,x1) = x0**2 + x1**2
def function_2(x):
    return x[0]**2 + x[1]**2
    # 또는 return np.sum(x ** 2)

# x0 = 3, x1 = 4 일때, x0에 편미분
def function_tmp1(x0):
    return x0 * x0 + 4.0 ** 2.0

# x0 = 3, x1 = 4 일때, x1에 편미분
def function_tmp2(x1):
    return 3 * 2 + x1 * x1

print(numerical_diff(function_tmp1,3))
# 수치미분값(편미분) : 6.000000000003781e-08

print(numerical_diff(function_tmp2,4))
# 수치미분값(편미분) : 7.999999999999119e-08
