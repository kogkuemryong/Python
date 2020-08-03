import numpy as np
'''
# NAND Gate - AND의 반대
def NAND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7 # bias

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
'''

def OR(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    
    tmp = np.sum(w * x) + b
    if tmp <=0:
        return 0
    else: 
        return 1


if __name__ == "__main__":
    result = OR(0,0)
    print(result)  # 0
    result = OR(1, 0)
    print(result)  # 1
    result = OR(0, 1)
    print(result)  # 1
    result = OR(1, 1)
    print(result)  # 1





