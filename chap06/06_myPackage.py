# 폴더의 위치가 다른 모듈의 함수를 호출
from my_package import calculator2

#  패키지 안에 패키지 안에 모듈 호출 
from my_package.package2 import calc

if __name__=='__main__':
    print(calc.plus(20,5))
    print(calc.minus(20,5))
    print(calc.multiply(20,5))
    print(calc.divide(20,5))

if __name__=='__main__':
    print(calculator2.plus(20,5))
    print(calculator2.minus(20,5))
    print(calculator2.multiply(20,5))
    print(calculator2.divide(20,5))
