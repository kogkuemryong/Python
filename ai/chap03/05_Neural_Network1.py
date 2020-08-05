import numpy as np

# 1층에서의 활성화 함수 처리
def sigmoid(x): # 시그모이드 함수 정의
    return 1/ (1 + np.exp(-x))

# 항등 함수의 정의 - 출력단
def identity_function(x):
    return x


# 입력층에서 1층오로의 신호 전달
X = np.array([1.0,0.5]) # x1 , x2
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]]) # 2행 3열
B1 = np.array([0.1,0.2,0.3])

print(W1.shape) # (2, 3)
print(X.shape)  # (2,)
print(B1.shape) # (3,)

A1 = np.dot(X,W1) + B1 # =  A(1) = XW(1) + B(1)
Z1 = sigmoid(A1)
print(A1) # [0.3 0.7 1.1] # 활성화 함수를 거치기 전
print(Z1) # [0.57444252 0.66818777 0.75026011] # 활성화 함수를 거친후, 0 초과 1미만의 값.

# x : 0.3 0.7 1.1 - y : 0.57444252 0.66818777 0.75026011

# 1층에서 2층으로의 신호 전달
W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]]) # 3행 2열
B2 = np.array([0.1,0.2])

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)
print(A2) # [0.51615984 1.21402696]
print(Z2) # [0.62624937 0.7710107 ]

# 2층에서 3층(출력층)으로의 신호 전달
W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1,0.2])

A3 = np.dot(Z2,W3) + B3
print(A3) # [0.31682708 0.69627909]
Y = identity_function(A3)
print(Y) # [0.31682708 0.69627909]







