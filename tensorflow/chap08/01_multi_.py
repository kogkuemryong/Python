# 다차원배열
import tensorflow as tf

tf.set_random_seed(777)

# 중간고사 점수를 가지고 기말고사 점수 예측 하기

# 데이터 정리
quiz1 = [73.,93.,89.,96.,73.] # 실수형으로 저장
quiz2 = [80.,88.,91.,98.,66.]
midterm = [75.,93.,90.,100.,70.]

finalterm = [152.,185.,180.,196.,142]

x1 = tf.placeholder(tf.float32) # tf.placeholder : (변수선언) 선언된 변수는 tensor를 활성화 시킬 때(run 호출) 입력. - 자료형의 크기를 할당(float32 - 4byte)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)

Y = tf.placeholder(tf.float32) # 결과데이터 , 정답 데이터

w1 = tf.Variable(tf.random_normal([1]), name='weight1') # 변수의 초기값을 넣어주는데 tf.random_normal() 을 넣어서 정규분포를 따르는 값 중에서 하나만 들어가게 함.
w2 = tf.Variable(tf.random_normal([1]), name='weight2')
w3 = tf.Variable(tf.random_normal([1]), name='weight3')

b = tf.Variable(tf.random_normal([1]), name='bias') # 편향


# 1) 가설 함수 정의 / H(x) = Wx + b
hypothesis = x1 * w1 + x2 * w2 + x3 * w3 + b

# 2) 손실 함수 정의(MSE)
loss = tf.reduce_mean(tf.square(hypothesis - Y)) # 정답값 - 예측값 의 제곱들의 평균값

# 3) 경사하강법 알고리즘
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.00001) # learning_rate=0.01 : 얼만큼 이동하면서 찾을 것인지 정의
train = optimizer.minimize(loss) # 손실함수(loss) 값을 기준으로 minimize()를 통해 최소값을 찾는다. - 학습

# 4) tensorflow 실행
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(15001):
    loss_val, hy_val, _ = sess.run([loss, hypothesis, train], feed_dict= {x1:quiz1, x2:quiz2, x3:midterm, Y:finalterm})
    # 리스트 형태로 전달(x의 값이 들어있지 않기 때문에 값을 입력(feed_dict : 를 통해서 맵핑)

    if step % 100 == 0: # 100번에 한번씩 출력
        print(step, "Loss:", loss_val, "\n예측값:\n", hy_val)





