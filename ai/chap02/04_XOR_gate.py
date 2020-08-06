# XOR gate : 다층 퍼셉트론
# - 다층 퍼셉트론의 동작 설명
#   1. 0층의 두 뉴런이 입력 신호를 받아 1층의 뉴런으로 신호를 보낸다.
#   2. 1층의 뉴런이 2층의 뉴런으로 신호를 보내고, 2층의 뉴런은
#      이 입력신호를 바탕으로 y를 출력한다.
#   3. 단층 퍼셉트론으로는 표현하지 못한 것을 층을 하나 늘려 구현
#      할 수 있었다.
#       - 퍼셉트론은 층을 쌓아(깊게하여) 더 다양한 것을 표현할 수 있다.

import numpy as np

# AND gate
def AND(x1, x2):
    x = np.array([x1,x2]) # 배열형으로 형변환 해서 x에 담다아줌
    w = np.array([0.5,0.5])
    b = -0.7

    tmp = np.sum(w * x) + b # b(bias : 편향/절편)
    if tmp <=0:
        return 0
    else:
        return 1
# NAND gate
def NAND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7 # bias

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
# OR gate
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y  = AND(s1,s2)

    return y

if __name__ == "__main__":
    print(XOR(0,0)) # 0
    print(XOR(0,1)) # 1
    print(XOR(1,0)) # 1
    print(XOR(1,1)) # 0



