import numpy as np

class Relu:
    def __init__(self):
        self.mask = None # 값을 보관하기 위함

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self,dout):
        dout[self.mask] = 0  # 음수 값을 체크 - 음수 값은 0 (양수는 그 값 그대로 유지)
        dx = dout
        return dx

# 이해를 위한 확인용

if __name__ == "__main__":
    x = np.array([[1.0,-0.5],[-2.0,3.0]])
    print(x)

    mask = (x <= 0) # 배열의 데이터 일때, 비교 연산자를 활용하면 각각의 값을 확인하여 boolean 값을 출력
    print(mask)

    out = x.copy()
    out[mask] = 0 # True 의 값만 0으로 넣어준다.
    print(out)

