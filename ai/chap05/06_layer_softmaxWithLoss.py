import numpy as np

def softmax(a):
    max = np.max(a)
    exp_a = np.exp(a-max) # 오버프롤 처리
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

def cross_tropy_error(y,t):
    delta = 1e-7 # log 함수가 0이 되지 않도록 적용
    return -np.sum(t * np.log(y+delta)) # log함수는 0에 가까이 가면 무한대로 간다. 그래서 계산되지 않는 문제점이 생긴다.

class SoftmaxWithLoss:
    def __init__(self):
        self.t = None # 정답 레이블
        self.y = None # softmax의 출력
        self.loss = None # 손실함수


    def forward(self,x,t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_tropy_error(self.y, self.t)

        return self.loss

    def backward(self):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx



