import tensorflow as tf
import numpy as np

tf.set_random_seed(777)

# hello 다음을 추천해주게끔 하는...
# 스펠링은 각각의 독립적인 의미를 가지고 있지만
# 'he'를 입력 했을 때, 서로의 연관성을 가지고 추천하게끔 만들어준다.
# 컴퓨터 선택의 최적화 되어 있는 수치로 표현 해야한다.

# h:0 , e:1 , l:2 , o:3 임의의 수를 넣어준다.
# One Hot Encoding

h = [1,0,0,0]
e = [0,1,0,0]
l = [0,0,1,0]
o = [0,0,0,1]

# RNN input_dim(4) -> output_dim(2), hidden_size(2)
hidden_size = 2

cell = tf.contrib.rnn.BasicRNNCell(num_units=hidden_size) # contrib : 상당수 많은 개발자들이 미리 구현해서 오픈하거나 공개하는 경우가 많다.
# print("cell:", cell.output_size, cell.state_size)

x_data = np.array([[h,e,l,l,o]],dtype=np.float32)
# print("x_data:", x_data)

output, _states = tf.nn.dynamic_rnn(cell, x_data, dtype=tf.float32)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    print('output: ',output.eval()) # eval() : 내부에서 자동적으로 tensor들의 동작이 되어지고 출력되지는 결과값 들을 return 시킨다.




