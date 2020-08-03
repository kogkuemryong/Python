import numpy as np

def AND(x1, x2):
    x = np.array([x1,x2]) # 배열형으로 형변환 해서 x에 담다아줌
    w = np.array([0.5,0.5])
    b = -0.7

    tmp = np.sum(w * x) + b # b(bias : 편향/절편)
    if tmp <=0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    result = AND(0,0)
    print(result) # 0
    result = AND(0,1)
    print(result) # 0
    result = AND(1,0)
    print(result) # 0
    result = AND(1,1)
    print(result) # 1
