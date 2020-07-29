class Calculator:

    @staticmethod # 데코레이션
    def plus(a,b):       # static 메서드는 self를 사용하지 않는다.
        return a + b     # static은 미리 메서드에 할당되어야하고 , self 는 인스터스 생성이 되어야 메모리에
                         # 할당이 되어야 하기 때문에 사용하지 않는다.

    @staticmethod
    def minus(a,b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b

if __name__ == '__main__':

    print('{0} + {1} = {2}'.format(7, 4, Calculator.plus(7,4))) # class의 이름으로 호출
    print('{0} - {1} = {2}'.format(7, 4, Calculator.minus(7, 4)))  # class의 이름으로 호출
    print('{0} * {1} = {2}'.format(7, 4, Calculator.multiply(7, 4)))  # class의 이름으로 호출
    print('{0} / {1} = {2}'.format(7, 4, Calculator.divide(7, 4)))  # class의 이름으로 호출




