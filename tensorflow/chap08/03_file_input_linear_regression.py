import tensorflow as tf
import numpy as np

tf.set_random_seed(777)

xy = np.loadtxt('data-01-test-score.csv', delimiter= ',' ,dtype=np.float32)
    # 데이터 읽어오기 np.loadtxt('파일이름', delimiter= 데이터 셋의 구별 단위 , dtype = 데이터 타입)
# print(xy) 잘 읽어오는지 확인.


score = xy[:,0:-1] # 행은 전체 열을 마지막 하나 빼고 읽어오기(# 96,93,95,192 - 마지막 항목이 final)

final_term = xy[:,[-1]] # 마지막 하나의 데이터를 읽어오기


X = tf.placeholder(tf.float32, shape = [None, 3]) # 자료형 선언 [None, 3] , None 자리에 들어간 값 만큼을 출력.
Y = tf.placeholder(tf.float32, shape = [None, 1]) # 자료형 선언

W = tf.Variable(tf.random_normal([3,1]), name='weight') # 변수 선언
b = tf.Variable(tf.random_normal([1]), name= 'bias')


# 1) 가설 함수 정의 / H(x) = Wx + b
hypothesis = tf.matmul(X, W) + b # .matmul(X, W) : 내적의 곱 계산(dot와 동일)

# 2) 손실 함수 정의(MSE)
loss = tf.reduce_mean(tf.square(hypothesis - Y)) # 정답값 - 예측값 의 제곱들의 평균값

# 3) 경사하강법 알고리즘
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.00001) # learning_rate=0.01 : 얼만큼 이동하면서 찾을 것인지 정의
train = optimizer.minimize(loss) # 손실함수(loss) 값을 기준으로 minimize()를 통해 최소값을 찾는다. - 학습

# 4) tensorflow 실행
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(20001):
    loss_val, hy_val, _ = sess.run([loss, hypothesis, train], feed_dict= {X:score, Y:final_term})
    # 리스트 형태로 전달(x의 값이 들어있지 않기 때문에 값을 입력(feed_dict : 를 통해서 맵핑)

    if step % 100 == 0: # 100번에 한번씩 출력
        print(step, "Loss:", loss_val, "\n예측값:\n", hy_val)

# 모델 확인하기
print("Test-set:", sess.run(hypothesis, feed_dict={X:[[75.,70.,72.]]}))
# Test-set: [[148.60616]]
sess.close()

# 20000 Loss: 6.1789813 / 많은 학습에도 로스값이 높에 나타나고 있다.
# 해설 : 실제값이 오차를 줄일 수 없는 한계의 값을 찾은 것이다. 실제 데이터가 조금 더 넓게 분포 되어 있고, 더이상 줄지 않게 되었다.
# 이론의 문제가 아닌, 데이터의 문제로, 정확한 데이터를 수집하는 것이 매우 중요하다.
# keypoint는 데이터로 매우 중요하다. 올바른 데이터를 사용해야지 높은 예측률을 기록 할 수 있다.
# 데이터의 특징을 파악했는데 분산이 광범위하게 퍼져 있을 때는 어떤 알고리즘을 넣어도 높은 예측을 구할 수 없다.
# 그렇기 때문에 탐색적 분석(EDA)가 매우 중요하다!! - 데이터의 이해를 통해 특징을 파악하는 것이 중요하다.

# 개선점 : 선형성을 가지고 있는 데이터가 더 많이 수집이 되어야 한다.




