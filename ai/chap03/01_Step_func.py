# 계단 함수(Step Function)

import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

def step_func_ndarray(x):
    y = x > 0
    # print(y)
    return y.astype(np.int)


if __name__ =="__main__":
    x = step_function(3)
    print(x) # 1

    x = step_function(-3)
    print(x) # 0

    z = np.array([-1,1,2]) # error : if 을 통해서 하나의 값이 비교가 되어야 하는데 배열로 다수의 값이 오기 때문에 처리 되지 않는다.
    # x = step_function(z)
    # print(x)
    print(step_func_ndarray(z))

    x = np.arange(-5,5,0.1) # -5 ~ 4.9 까지.
    y = step_func_ndarray(x)

    plt.plot(x,y)
    plt.ylim(-0.1, 1.1)
    plt.show()
