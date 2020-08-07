import numpy as np
from common.functions import *
from common.gradient import numerical_gradient

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01): # 생성자 생성
                       # 입력 데이터 개수 , 은닉층 개수 , 출력 개수 , 초기값
        # 가중치 초기화
        self.param = {}
        self.param['W1'] = weight_init_std * np.random.randn(input_size, hidden_size) # randn : 정규분포를 따르는 실수 값을 랜덤하게 값을 꺼내옴
        self.param['b1'] = np.zeros(hidden_size)
        self.param['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.param['b2'] = np.zeros(output_size)
        # 입력층 , 은닉층, 출력층

    def predict(self, x): # predict - 데이터의 흐름에 대한 기능 구현
        W1, W2 = self.param['W1'], self.param['W2']
        b1, b2 = self.param['b1'], self.param['b2']

        a1 = np.dot(x, W1) + b1 # 입력층 -> 은닉층
        z1 = sigmoid(a1) # 은닉층 -> 출력층

        a2 = np.dot(z1, W2) +b2 # 출력층
        y = softmax(a2) # 출력(확률 처럼 사용할 수 있도록 비율 값으로 출력)

        return y

    # 손실함수 활용
    def loss(self, x,t): # x : 입력데이터 , t : 정답 레이블
        y = self.predict() # y = 예측값

        return cross_entropy_error(y,t)  # t = 정답 값

    # 정확도 체크 함수 정의
    def accuracy(self, x,t): # accuracy - 정확도 체크 계산 함수 정의
        y = self.predict(x)  # y = 예측값
        y = np.argmax(y,axis=1) # argmax : y가 0~9까지 인덱스로 비율값이 출력되는데 거기에서 가장 큰 값을 찾아서 인덱스 값을 return 해준다.
                                # axis=1 - 열단위에서 기준으로 인덱스 값을 출력.
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])  # 맞은 값 / 총합 : x.shape[0] - 전체 데이터의 개수 출력.
        return accuracy

    # 경사 하강법

    # 미분 함수의 정의 - 중앙 차분
    def numerical_gradient(self,x,t): # x: 입력데이터, t : 정답 레이블
        loss_W = lambda W: self.loss(x,t)
        """
        lambda : 코드를 간략하게 구성하도록 해준다. 
        
        동일 코드 
        loss_W(W): 
            return self.loss(x,t) 
        """
        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.param['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.param['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.param['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.param['b2'])

        return grads

        # common 밑에 있는 함수를 호출 한 것인데, 자신 안에 자신과 동일한 이름의 함수가 사용된다면 어떻게 구분할까?
        # class 안의 함수나 메서드를 선어하려면 self.을 붙여야지만 선언이 가능한데 같은 자료형 안이어도
        # self.으로 호촐해야지 내가 선언한 함수를 사용되므로 외부의 정의 되어 있는 함수를 찾아서 수행한다.






















