# 방법 1
from Module import plus
from Module import minus
from Module import multiply
from Module import divide

# 방법 2
# from module import plus,minus, multiply, divide
# 콤마( , )를 이용해서 연속적으로 여러 함수(변수) 사용

# 방법 3

# from chap06.module import *
# ( * ) 모든 함수, 변수 사용할 수 있도록 지원
# (권고하지 않음 - 1. 실직적으로 이 코드를 만나면 모든 내용을 읽어와서 배치하는 것과 같으므로 용량을 많이 차지하게 된다)
#                2. 어떤 함수를 사용하고 있는지 명확하지 않다.(가독성을 떨어뜨림)

result = plus(10,5)
print(result)

result = minus(10,5)
print(result)

result = multiply(10,5)
print(result)

result = divide(10,5)
print(result)