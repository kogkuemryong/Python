import tensorflow as tf

tf.set_random_seed(777)

# matrix
      # quiz1 quiz2 midterm
score = [[73.,80.,75.],
         [93.,88.,93.],
         [89.,91.,90.],
         [96.,98.,100.],
         [73.,66.,70.]]

final_term = [[152.],
              [185.],
              [180.],
              [196.],
              [142.]]

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

for step in range(15001):
    loss_val, hy_val, _ = sess.run([loss, hypothesis, train], feed_dict= {X:score, Y:final_term})
    # 리스트 형태로 전달(x의 값이 들어있지 않기 때문에 값을 입력(feed_dict : 를 통해서 맵핑)

    if step % 100 == 0: # 100번에 한번씩 출력
        print(step, "Loss:", loss_val, "\n예측값:\n", hy_val)

# 모델 확인하기
print("Test-set:", sess.run(hypothesis, feed_dict={X:[[75.,70.,72.]]}))
# Test-set: [[148.60616]]
sess.close()
