import numpy as np
from common.util import im2col

x = np.random.rand(10,1,28,28)#(배치이미지,채널,행,열)
print(x.shape) # (10, 1, 28, 28)
print(x[0].shape) # (1, 28, 28)

# print(x[0,0])

x1 = np.random.rand(1,3,7,7)
col1 = im2col(x1,5,5)
print(col1.shape) # (9, 75)

x2 = np.random.rand(10,3,7,7)
col2 = im2col(x2,5,5)
print(col2.shape) # (90, 75)