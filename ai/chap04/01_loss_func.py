import  numpy as np

# Loss Function

# MSE(Mean Squared Error)
def mean_squared_error(y, t): # p와 y 자리가 바뀌어도 제곱을 할것이기 때문에 문제 없다.
    return np.sum((y-t) ** 2) # 제곱

# CEE(Cross Entropy Error)
def cross_entropy_error(t, y):
    delta = 1e-7 # NaN 값이 나오지 않기 위함
    return -np.sum(t * np.log(y+delta))

# 2 : 정답
t = [0,0,1,0,0,0,0,0,0,0] # 답 2 : 원핫인코딩(One-Hot Encording)

# 예측 결과 : 2
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
msq = mean_squared_error(np.array(t),np.array(y)) # 리스트 형태 -> 배열로 변환

print(msq)
# 출력값 : 0.19500000000000006

# 예측 결과 : 7
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
msq = mean_squared_error(np.array(t),np.array(y)) # 리스트 형태 -> 배열로 변환
print(msq) # 1.195




# 예측 결과 : 2
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
cee = cross_entropy_error(np.array(t),np.array(y)) # 리스트 형태 -> 배열로 변환
print(cee)
# 출력값 : 0.44250000000000006

# 예측 결과 : 7
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
cee = cross_entropy_error(np.array(t),np.array(y)) # 리스트 형태 -> 배열로 변환
print(cee) # 2.302584092994546
