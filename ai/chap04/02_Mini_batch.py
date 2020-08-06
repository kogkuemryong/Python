import numpy as np
from dataset.mnist import load_mnist


# 60000개 데이터      10000개 데이터
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True) # normalize= True : 정규화 , flatten= , one_hot_label= True : 원핫인코딩 방식으로 처리

print(x_train.shape) # (60000, 784) 60000개 데이터, 784 입력 개수
print(t_train.shape) # (60000, 10) one_hot_label=True - 1이 아닌 10으로 불러온다.

print(t_train.shape[0]) # 60000 : 전체 데이터의 개수를 출력한다.
print(t_train.shape[1]) # 10 : one_hot_label=True 에 의해서 10으로 출력.
batch_size = 100 # 60000개 중에서 batch 100

# 지정한 범위의 수 중에서 무작위로 원하는 개수만 선택(batch_size = 100).
batch_mask = np.random.choice(t_train.shape[0], batch_size)  # (범위,출력개수)  - 60000개 중에서 100개 index를 출력
print(batch_mask)

x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]




