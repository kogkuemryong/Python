import tensorflow as tf
import numpy as np
from numpy.core._multiarray_umath import dtype

tf.set_random_seed(777)

xy = np.loadtxt('data-04-zoo.csv', delimiter=',', dtype = float)

x_train_data = xy[:-10, :-1]
y_train_data = xy[:-10, [-1]]

x_test_data = xy[-10:, :-1]
y_test_data = xy[-10:, [-1]]

X = tf.placeholder(tf.float32, [None, 16])
Y = tf.placeholder(tf.int32, [None, 1]) # 0~6 : 7 class - one_hot incoding 방식으로 사용할 때는 자료형 - 정수형!

Y_one_hot = tf.one_hot(Y, 7) # 인덱스 위치의 값만 1로 채워주고 나머지 자리는 0으로 채움.
Y_one_hot = tf.reshape(Y_one_hot, [-1, 7])

W = tf.Variable(tf.random_normal([16,7]))
b = tf.Variable(tf.random_normal([7]))


# 가설함수 설정
hypothesis = tf.nn.softmax(tf.matmul(X,W)+b)

# 손실함수 설정
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=tf.matmul(X,W)+b, labels= Y_one_hot))

# 경사하강법 알고리즘
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss)

pridiction = tf.argmax(hypothesis,1)
accuracy = tf.reduce_mean(tf.cast(tf.equal(pridiction, tf.argmax(Y_one_hot,1)), dtype=tf.float32))

# ML
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(2001):
        sess.run(train, feed_dict={X:x_train_data, Y:y_train_data})

        if step % 200 == 0:
            loss_val, a = sess.run([loss, accuracy], feed_dict={X:x_train_data, Y:y_train_data})

        print("\nstep:{:5}\tLoss:{:.3f}\taccuracy{:.2%}".format(step, loss_val, a))


    pred = sess.run(pridiction, feed_dict={X:x_train_data})

    for p,y in zip(pred, y_train_data.flatten()):
        print("[{}] Prediction:{}, Y:{}".format(p==int(y),p,int(y)))

    print("===== \n 테스트 데이터 적용.")
    pred = sess.run(pridiction, feed_dict={X:x_test_data})
    for p, y in zip(pred, y_train_data.flatten()):
        print("[{}] Prediction:{}, Y:{}".format(p == int(y), p, int(y)))







