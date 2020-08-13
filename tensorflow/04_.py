import tensorflow as tf
import matplotlib,pylab as plt

tf.set_random_seed(777)

X =[1,2,3]
Y =[2,4,6]

W = tf.placeholder(tf.float32) # 입력하는 순간 현재는 shape을 고정시키지 않겠다.

# 가설 함수 정의
hypothesis = X * W

# 2) 손실 함수 정의
loss = tf.reduce_mean(tf.square(hypothesis - Y))

sess = tf.Session()

W_history = []
loss_history = []

for i in range(-30, 81):
    curr_W = i * 0.1
    curr_loss = sess.run(loss, feed_dict={W:curr_W})
    W_history.append((curr_W))
    loss_history.append(curr_loss)

plt.plot(W_history, loss_history)
plt.show()