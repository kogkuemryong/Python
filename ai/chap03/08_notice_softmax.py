import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([0.3, 2.9, 4.0])

y = softmax(a)
print(y) # [0.01821127 0.24519181 0.73659691]

a = np.array([1010,1000,990])
"""
y = softmax(a)
print(y)
"""
max = np.max(a) # 입력으로 전달되는 a 값의 최대값


result = np.exp(a-max) / np.sum(np.exp(a-max)) # 0의 가까운수로 변경
print(result) # [9.99954600e-01 4.53978686e-05 2.06106005e-09]

def softmax_computer(a):
    max =  np.max(a)
    exp_a = np.exp(a-max) # 오버플로 처리 - 작은 값으로 바꿈.
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

y = softmax_computer(a)
print(y) # [9.99954600e-01 4.53978686e-05 2.06106005e-09]




