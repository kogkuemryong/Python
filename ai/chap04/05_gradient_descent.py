import numpy as np
import matplotlib.pyplot as plt

# 경사하강법 (손실을 최소화)

def  numerical_gradient_no_batch(f,x): # 배치단위가 아닌 미분 값을 구현되어지게 만듦. - 중앙차분(미분)
     h = 1e-4
     grad = np.zeros_like(x) # _like를 가진 함수의 공통점 : _like(배열) 지정한 배열과 동일한 shape의 행렬을 만듦
                             # 입력으로 전달되는 shape 과 같은 shape를 초기값을 0으로 생성

     for idx in range(x.size):
         tmp_val = x[idx] # x값을 꺼내와서 변수에 담아주었다.

         # f(x+h) 계산
         x[idx] = float(tmp_val) + h
         fxh1 = f(x)

         # f(x-h) 계산
         x[idx] = float(tmp_val) - h
         fxh2 = f(x)

         grad[idx] = (fxh1 - fxh2) / (2 * h)  # 중앙차분
         x[idx] = tmp_val

     return grad


def numerical_gradient(f,x): # 편미분 정의 함수  (함수,입력값(단항,다항))

    if x.ndim == 1 : # 단항
        return numerical_gradient_no_batch(f,x)

    else:
        grade = np.zeros_like(x) # _like를 가진 함수의 공통점 : _like(배열) 지정한 배열과 동일한 shape의 행렬을 만듦
                                 # 입력으로 전달되는 shape 과 같은 shape를 초기값을 0으로 생성

        for idx, z in enumerate(x): # enumerate() : 입력으로 전달 받은 값을 자돟으로 인덱스 값을 0부터 증가하면서 x의 담긴 값을 반환
            grade[idx] = numerical_gradient_no_batch(f, x)

        return grade


def gradient_descent(f, init_x, lr, step_num): # 함수, 초기값, learning rate, 횟수 - 경사하강법
    x = init_x # 초기값
    x_history = [] # 학습을 통해서 나온 값들을 저장하여, 시각화 할 때 사용

    for i in range(step_num): # 20번 반복
        x_history.append(x.copy()) # 초기값을 가져와 저장한 이후 입력으로 전달되는 데이터 추가.

        grad = numerical_gradient(f,x) # 편미분
        x -= lr * grad

    return x, np.array(x_history) # 반복이 끝난 이후!!!!
                                  # 튜플의 가로 생략 된것이지 2개가 return이 되는 것이 아니다.

def function_2(x): # f(x0, x1) = x0^2 + x1^2
    return x[0]**2 + x[1]**2

if __name__ =="__main__":
    init_x = np.array([-3.0, 4.0]) # 초기값 셋팅(내부에서 처리 될 때, float으로 처리 되기 때문에 float형(실수)로 넣어줘야한다.

    lr = 0.1 # learning rate(학습률)
    step_num = 20 # 경사하강법의 학습을 시킬 때, 학습시킬 횟수의 값(20회)

    x, x_history = gradient_descent(function_2, init_x, lr, step_num)   # 함수, 초기값, learning rate, 회수 / 튜플로 반환해서 튜플로 받은 것(변수 2개x)


    plt.plot([-5,5],[0,0],'--b')
    plt.plot([0, 0], [-5, 5], '--b')
    plt.plot(x_history[:,0], x_history[:,1], 'o')

    plt.xlim(-3.5, 3.5)
    plt.ylim(-4.5, 4.5)
    plt.xlabel("X0")
    plt.ylabel("X1")
    plt.show()






