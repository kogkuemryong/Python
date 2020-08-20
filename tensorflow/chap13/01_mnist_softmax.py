import tensorflow as tf
import random
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

tf.set_random_seed(777)

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

X = tf.placeholder(tf.float32, shape=[None,784]) # 학습시 데이터를 전달 받아서 학습이 전달 되어져야 된다는 데이터가 사용될 떄 처리 되어지게 끔 정의되어 있는 것
Y = tf.placeholder(tf.float32, shape=[None,10])

W = tf.Variable(tf.random_normal([784,10])) # tf.Variable :  변수 선언
b = tf.Variable(tf.random_normal([10]))

hypothesis = tf.matmul(X,W) + b

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels=Y))

train = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

training_epochs = 15
batch_size = 100

for epoch in range(training_epochs):
    avg_cost = 0
    total_batch = int(mnist.train.num_examples / batch_size)

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)

        feed_dict = {X:batch_xs, Y:batch_ys}
        c, _ = sess.run([cost, train], feed_dict=feed_dict)
        avg_cost += c / total_batch

    print('Epoch:', '%04d' % (epoch+1), 'cost=','{:.9f}'.format(avg_cost))

print('Learning Finished!')

correct_prediction = tf.equal(tf.argmax(hypothesis,1), tf.argmax(Y,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

feed = {X:mnist.test.images, Y:mnist.test.labels}
print('Accuracy:',sess.run(accuracy,feed_dict=feed))

r = random.randint(0, mnist.test.num_examples-1)
print("Label:",sess.run(tf.argmax(mnist.test.labels[r:r+1],1)))
print("Prediction:", sess.run(tf.argmax(hypothesis,1),
                              feed_dict={X:mnist.test.images[r:r+1]}))

plt.imshow(mnist.test.images[r:r+1].reshape(28,28),
           cmap='Greys', interpolation='nearest')
plt.show()





