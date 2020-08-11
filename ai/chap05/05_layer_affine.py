import numpy as np

class Affine:
    def __init__(self, W , b, dw):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b
        return out


    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)

        return dx

if __name__ == "__main__":
    x_dot_W = np.array([[0,0,0],[10,10,10]]) # 2행 3열
    B = np.array([1,2,3])

    print(x_dot_W + B) # 2행 3열(matrix data) +  B(일차원 배열)

    dY = np.array([[1,2,3],[11,12,13]])
    dB = np.sum (dY, axis = 0)

    print(dB)


