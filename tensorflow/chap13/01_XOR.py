import tensorflow as tf
import numpy as np

tf.set_random_seed(777)

# xor gate
x_data = [[0,0],[0,1],[1,0],[1,1]] # 입력 데이터
y_data = [  [0],  [1],  [1],  [0]] # 출력 데이터

x_data = np.array(x_data, dtype= np.float32) # 자료형 리스트 -> 배열 , 자료형 = float
y_data = np.array(y_data, dtype= np.float32)

X = tf.placeholder(tf.float32, [None, 2]) # 입력 데이터 - 2개의 특징
Y = tf.placeholder(tf.float32, [None, 1]) # 출력 데이터 - 1개 출력

W = tf.Variable(tf.random_normal([2,1]))
b = tf.Variable(tf.random_normal([1]))

# 가설함수 설정
hyposthesis = tf.sigmoid(tf.matmul(X,W)+b)

# 손실함수 설정
loss = -tf.reduce_mean(Y * tf.log(hyposthesis) + (1 - Y) * tf.log(1 - hyposthesis))

# 경사하강법 적용
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss)

predicted = tf.cast(hyposthesis > 0.5, dtype= tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

# tensorflow 흐름
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        sess.run(train, feed_dict={X:x_data, Y:y_data})

        if step % 200 == 0:
            print(step, sess.run(loss, feed_dict={X:x_data, Y:y_data}), sess.run(W))
            # 학습이 될수록 loss 값이 주는지 확인, W 값의 변화 확인

    # Accuracy
    h, c, a = sess.run([hyposthesis,predicted,accuracy], feed_dict={X:x_data, Y:y_data})
    print("\nHypothesis:", h, "\nCorrect:", c, "\nAccuracy:", a)













