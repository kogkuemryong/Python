# tensorflow 를 이용한 Linear Regression(선형회귀) - tensor / 행렬, 배열의 데이터를 의미 , flow/ 흘러가는 구조
                                                  # tensorflow = 배열이나 행렬의 데이터가 흘러간다

import tensorflow as tf

tf.set_random_seed(777) # 항상 같은 결과를 나오게 하기 위해서 random의 seed값을 고정한다.

# X and X data  - 데이터를 학습시켜 피드백을 받도록 한다.
x_train = [1,2,3] # 입력 데이터
y_train = [1,2,3] # 결과 데이터

# 1) 가설함수 정의 : y = wx + b
W = tf.Variable(tf.random_normal([1]), name = 'weight')
                                                              # tf.Variable - 변수로 만들어주는 함수, 이 변수는 학습이 되어질 때마다 변경되어 질 수 있게 한다.
                                                              # tf.random_normal  - 랜덤 값으로 초기값 생성
b = tf.Variable(tf.random_normal([1]), name = 'bias')

hypothesis = x_train * W + b # 스칼라 함수 일 때 w와 x 값은 교환법칙이 가능하다. - 예측값

# 2) 손실(Loss or Cost) 함수 정의
# MSC 사용
loss = tf.reduce_mean(tf.square(hypothesis - y_train)) # tf.square : 제곱 , tf.reduce_mean: 평균
                                                       # 실제값 과 예측 값의 차이에서 제곱을 한 값에 평균 값

# 손실이 계산 될 때마다 경사하강법을 넣어서 최적의 w, b 값을 찾도록 학습

# 3) 경사하강법(Gradient descent) algorithm 사용
optimizar = tf.train.GradientDescentOptimizer(learning_rate= 0.01)
            # tf.train.GradientDescentOptimizer : 경사하강법의 최적의 값을 찾아가는 함수
            # learning_rate= 0.01 : 0.01 간격으로 찾아간다.

train = optimizar.minimize(loss) # minimize(loss) :  손실함수(loss) 값을 기준으로 최소값을 찾아라

# session을 구동시키 위한 필수
session = tf.Session() # Session() : 데이터를 흘려주는 함수
session.run(tf.global_variables_initializer()) # tf.global_variables_initializer : 위의 별수로 선언된 모든 데이터를 초기화 시킴

for step in range(2001): # 마지막 메세지를 출력하기 위해서 2001(0~2000)번 반복
    session.run(train) #  run() : 데이터를 흘려보내주는 동작을 하는 함수

    if step % 20 == 0: # 20의 배수 출력(20번 마다 한번씩 출력) / 손실함수가 최소가 되어지면서 w, b 값은 최적의 파라메타 값으로 접근하고 있는지 확인
        print(step, session.run(loss), session.run(W), session.run(b))

