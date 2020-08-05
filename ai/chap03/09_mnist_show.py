# MNIST(Modified National Institude of Standards and Technology)
# - 손으로 직접 쓴 숫자(필기체 숫자)들로 이루어진 데이터 셋
# - 0 ~ 9까지의 숫자 이미지로 구성되며, 60,000개의 트레이닝 데이터와
#   10,000개의 테스트 데이터로 이루어져 있음.
# - 28x28 size

import numpy as np
from dataset.mnist import load_mnist
from PIL import Image # Image 패키지는 Anaconde Prompt를 통해서 받아야 한다.

def img_show(img):
    pil_img=Image.fromarray(np.uint8(img)) # uint8  : java에서 byte
    pil_img.show()

# (이미지, 레이블)
(x_train, t_train),(x_test, t_test) = \
    load_mnist(flatten=True, normalize=False, one_hot_label=False)

img = x_train[100]
print(img.shape) # (784,)

for i in range(10):
    img = x_train[i]
    label = t_train[i]
    print(label)
    print(img.shape)

img.reshape(28,28) # 형상을 원래 이미지의 크기로 변형
img_show(img)


