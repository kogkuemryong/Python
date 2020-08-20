import tensorflow as tf
import numpy as np

tf.set_random_seed(777)

# Teach hihello : hihell -> ihello
idx2char = ['h','i','e','l','o']

x_data = [[0,1,0,2,3,3]] # hihell
x_one_hot = [[[1,0,0,0,0], # h -> 0
              [0,1,0,0,0], # i -> 1
              [1,0,0,0,0], # h -> 0
              [0,0,1,0,0], # e -> 2
              [0,0,0,1,0], # l -> 3
              [0,0,0,1,0]  # l -> 3
              ]]

y_data = [[1,0,2,3,3,4]] # ihello

input_dim = 5
hidden_size = 5
batch_size =  1
sequence_lenth = 6 # 6개 글자가 인가된다.
learning_rate = 0.1

X = tf.placeholder(tf.float32,[None, sequence_lenth, input_dim]) # x_one_hot
Y = tf.placeholder(tf.float32,[None, sequence_lenth]) # Y label

cell = tf.contrib.rnn.BasicRNNCell(num_units= hidden_size)

initial_state = cell.zero_state(batch_size, tf.float32)
output, _state = tf.nn.dynamic_rnn(cell, X, initial_state, dtype=tf.float32)

# FC layer
X_for_fc = tf.reshape(output, [-1, hidden_size])
"""
fc_w = tf.get_variable("fc_w", [input_dim, 5])
fc_b = tf.get_variable('fc_b', [5])

# 가설함수 지정
hypothesis = tf.matmul(X_for_fc, fc_w) +  fc_b
"""

hypothesis = tf.contrib.layers.fully_connected(input=X_for_fc,
                                               num_outputs=hidden_size,
                                               activation_fn= None)

outputs = tf.reshape(hypothesis,[batch_size,sequence_lenth, 5])

weights = tf.ones([batch_size, sequence_lenth])
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits = outputs,
                                                 targets = Y,
                                                 weights = weights)

loss = tf.reduce_mean(sequence_loss)
train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

prediction = tf.argmax(outputs, axis = 2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(50):
        l, _ = sess.run([loss, train], feed_dict={X:x_data, Y:y_data})
        result = sess.run(prediction, feed_dict={X:x_one_hot})
        print(i, "loss:", l, "prediction :", result, "Y_data:", y_data)

        result_str = [idx2char[c] for c in np.squeeze(result)]
        print("\nPrediction str:", ''.join(result_str))

        # [idx2char[c] for c in np.squeeze(result)] - for문을 반복해서 결과값을 가져와서 반환해준다.








