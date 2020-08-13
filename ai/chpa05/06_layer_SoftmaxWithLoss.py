import numpy as np

def softmax(a):
    max = np.max(a)
    exp_a = np.exp(a-max) # 오버플로 처리
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

def cross_entropy_error(y,t):
    delta = 1e-7
    return -np.sum(t * np.log(y+delta))


class SoftmaxWithLoss:
    def __init__(self):
        self.t = None    # 정답레이블(One-Hot Encoding)
        self.y = None    # softmax의 출력
        self.loss = None # 손실함수

    def forward(self,x,t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)

        return self.loss


    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx

