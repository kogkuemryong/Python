import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist # 데이터 읽어 올 파일
from ex06_two_layer_neuralnetwork import TwoLayerNet

# 데이터 읽기
# 60000개 이미지 데이터, 60000개 정답 데이터, 10000개 이미지 데이터, 10000개 정답 데이터
(x_train, t_train),(x_test, t_test) = load_mnist(normalize= True, one_hot_label= True)
# normalize= True (0 ~ 255 사이의  값 -> 정규화 = 0과 1사이의 범위 값으로 변화)
# one_hot_label= True / 읽어 올때 부터 펼쳐서 가져도록 한다.

# 인스턴스화
network = TwoLayerNet(input_size = 784, hidden_size = 50, output_size=10)

# 하이퍼 파라미터 - 설정할 수 있는 파라미터
learning_rate = 0.1 # 학습률
train_size = x_train.shape[0] # 60000 / x_train.shape[1] = 784
batch_size = 100 # 배치 크기 (한번에 처리할 크기).
iters_num = 10000 # 반복 횟수를 적절히 설정(전체 데이터 반복).

# 학습하면서 나오는 손실값 - 값이 작아지는 것을 확인
train_loss_list = []
train_acc_list = []
test_acc_list = []

# 1. 에폭당 반복 수 : 1에폭 = 처음 끝까지 학습하는 단위 = train_size / batch_size = 600회
iter_per_epoch = max(train_size / batch_size,1) # 값이 1보다 크면 train_size / batch_size = 갑이 출력, 1보다 작으면 1 출력

# 미니 배치 방식으로 빠르게 값을 찾아가게 만들어준다.
for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size) # np.random.choice : 0 ~ 59999 값에서 100개의 index 출력.
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]


    # 기울기 계산(미분)
    grad = network.numerical_gradient(x_batch, t_batch) # 매개변수 - 입력 데이터, 정답 데이터

    # 매개변수(가중치, 편향) 보정
    for key in ('W1','b1','W2','b2'):
        network.param[key] -= learning_rate * grad[key]

    # 학습 경과 기록 - 시각화 사용.
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    # 1epoch 당 정확도 계산
    if i % iter_per_epoch == 0: # 600번에 한번씩 출력.
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print("train acc, test acc |" + str(train_acc)+", "+str(test_acc))


# 그래프 그리기
markers = {'train': 'o', 'test' :'s'}
x = np.arange(len(train_acc_list))
plt.plot(x, train_loss_list, lable = 'train acc')
plt.plot(x, test_acc_list, label = 'test acc', linesstyle = '--')
plt.xlabel('epochs') # 에폭
plt.ylabel('accuracy') # 정확도
plt.ylim(0,1.0)
plt.legend(loc = 'lower right')
plt.show()


















