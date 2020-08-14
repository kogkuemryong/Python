import tensorflow as tf

tf.set_random_seed(777)

x_data = [[1,2],[2,3],[3,1],[4,3],[5,3],[6,2]]
        # 1시간 수업 2시간 공부 ,2시간 수업 3시간 공부 ,3시간 수업듣고 1시간 공부,
        # 4시간 수업 3시간 공부 ,5시간 수업 3시간 공부 ,6시간 수업듣고 2시간 공부,

y_data = [[0], [0], [0] ,[1] ,[1], [1]] # 0 불학격, 1 합격

X = tf.placeholder(tf.float32, shape = [None, 2]) # 특징 2개 (수업, 스스로 공부)
Y = tf.placeholder(tf.float32, shape = [None, 1]) # yes or no - 1개 출력

W = tf.Variable(tf.random_normal([2,1]), name='weight') # X의 열의 값과 행의 값이 동일(Nonex2) -2 , 결과(6x1) - 1
b = tf.Variable(tf.random_normal([1]), name='bias') # Y의 열의 값과 행의 값이 동일해야한다.

# W = tf.Variable(tf.random_normal([3,1]), name='weight')

# 1) 가설함수 정의 : logistic regression 적용
hypothesis = tf.sigmoid(tf.matmul(X,W) + b) # 시그모이드(tf.sigmoid)에 입력(tf.matmul(X,W) + b)


# 2) 손실함수 정의(CEE) - ylog(H(x)) - (1-y)log(1-H(x)) , H(x) : 가설함수
loss = - tf.reduce_mean((Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))) # tf.log:로그함수()

# 3) 경사하강법 알고리즘
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01) # 필수!! learning_rate=0.01
train = optimizer.minimize(loss) # 손실함수를 지표로 하여 최소값을 찾도록 훈련

# 기준치 제공 - 0.5 이상이면 합격, 0.5 미만이면 불합격
predict = tf.cast(hypothesis > 0.5, dtype = tf.float32) # 0초과 1미만 값
                                                        # dtype = tf.float32 : True = 1.0, False = 0.0 출력
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, Y), dtype = tf.float32))
# tf.equal(예측값 , 정답값): 두 값이 같은지 확인하고, 그 값으 같으면 True 반환, 다르면 False 반환

with tf.Session() as sess: # sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        _, loss_val = sess.run([train, loss], feed_dict={X:x_data, Y:y_data})
        # 학습을 시키고, 손실값은 줄어드는지 확인(train만 수행해도 문제 없이 진행)

        if step % 200 == 0:
            print(step, loss_val)

    h,p,a = sess.run([hypothesis,predict,accuracy], feed_dict={X:x_data, Y:y_data})


    print("\n 예측값 :", h , "\n prdict:", p , "\n accuracy:" , a)

    print("4시간 수업, 2시간 자율 학습 ", sess.run(predict, feed_dict={X:[[4,2]]}))







