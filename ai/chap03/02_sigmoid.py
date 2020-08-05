import numpy as np

# - sigmoid(활성화) 함수의 특징
# 1) 음수 입력 값의 경우 양수로 변환
# 2) 0 < y < 1 사이의 연속적인 실수 값으로 변환

def sigmoid(x):
    return  1 / (1 + np.exp(-x)) # np.exp(-x) : 배열로 전달 받아도 전처리 과정 없이 한번에 수행된다

if __name__ == "__main__":
    x = np.array([-1, 0, 1, 2])
    y = sigmoid(x)
    print(y) # [0.26894142 0.5 0.73105858 0.88079708] - 실수 값으로 출력.
