
class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x,y): # 순전파법
        self.x = x
        self.y = y
        out = x * y

        return out

    def backward(self, dout): # 역전파법
        dx = dout * self.y  # 입력 값 * y축에 입력이 되었던 값
        dy = dout * self.x  # 입력 값 * x축에 입력이 되었던 값

        return dx, dy



class AddLayer:
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y

        return out


    def backward(self, dout):
        dx = dout * 1 # 결과값의 하등의 영향을 미치지 않는 액션만을 취함.
        dy = dout * 1

        return  dx, dy


