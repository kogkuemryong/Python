import numpy as np
import matplotlib.pyplot as plt

def relu(x): #  입력이 0을 넘으면 그 입력을 그대로 출력하고, 0 이하이면 0을 출력
    return np.maximum(0, x) # np.maximum : 두 입력 중 큰 값을 선택해 반환하는 함수


if __name__=="__main__":
    print(relu(5)) #5
    print(relu(-5)) #0

    x = np.arange(-5,5,0.1) # 배열형
    y = relu(x)
    print(y)

    plt.plot(x,y)
    plt.ylim(-1.0,5.5)
    plt.show()



