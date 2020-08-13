import tensorflow as tf

tf.set_random_seed(777)

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

X = tf.placeholder(tf.float32, shape=[None]) # 입력하는 순간 현재는 shape을 고정시키지 않겠다.
Y = tf.placeholder(tf.float32, shape=[None])

# 1) 가설함수 H(x) 정의

hypothesis = X * W + b

# 2) 손실 함수 정의
loss = tf.reduce_mean(tf.square(hypothesis - Y))

# 3) 경사하각법
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(loss)

session = tf.Session()
session.run(tf.global_variables_initializer())

for step in range(2001):
    loss_val, w_val , b_val, _ = session.run([loss, W, b, train], feed_dict={X:[1,2,3], Y:[1,2,3]})
    # 4개의 포맷으로 지정은 하되 마지막 값을 쓸이링 없으면 _로 지정해서 return 되는 값을 버리는 형식으로 작성

    if step % 20 == 0:
        print(step, loss_val, w_val, b_val)

print(session.run(hypothesis, feed_dict={X:[5]}))
print(session.run(hypothesis, feed_dict={X:[2.5]}))
print(session.run(hypothesis, feed_dict={X:[1.5,3.5]}))



