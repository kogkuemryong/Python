import numpy as np

a = np.array([0.3,2.9,4.0])
exp_a = np.exp(a)
print(exp_a) # [ 1.34985881 18.17414537 54.59815003] - [0.3,2.9,4.0] : 분자

sum_exp_a = np.sum(exp_a)
print(sum_exp_a) # 74.1221542101633 : 분모

y = exp_a / sum_exp_a
print(y) # [0.01821127 0.24519181 0.73659691] : 비율 ( 1.8% , 24.5% ,73.6% )


