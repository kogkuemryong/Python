import numpy as np

def init_network():
    network = {}
    network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network['B1'] = np.array([0.1,0.2,0.3])
    network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['B2'] = np.array([0.1,0.2])
    network['W3'] = np.array([[0.1,0.3],[0.2,0.4]])
    network['B3'] = np.array([0.1,0.2])

    return network

# 1층에서의 활성화 함수 처리
def sigmoid(x): # 시그모이드 함수 정의
    return 1/ (1 + np.exp(-x))

# 항등 함수의 정의 - 출력단
def identity_function(x):
    return x

# 데이터 전달
def forward(network, x):
    W1,W2,W3 = network['W1'], network['W2'], network['W3']
    B1,B2,B3 = network['B1'], network['B2'], network['B3']

    a1 = np.dot(x, W1) +B1
    z1 = sigmoid(a1) # 다음 은닉층

    a2 = np.dot(z1, W2) +B2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) +B3
    Y = identity_function(a3)

    return Y

if __name__ == "__main__":
    network = init_network()

    x = np.array([1.0,0.5])
    y = forward(network, x)

    print(y) # [0.31682708 0.69627909]













