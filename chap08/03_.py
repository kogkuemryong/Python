# 데이터 속성(field) 상속(명시적으로 표현해 주어야 함)

'''
class A:
    def __init__(self):
        print("A.__inint__()")
        self.message = "Hello"

class B(A):
    def __init__(self):
        print("B.__init__()")

if __name__ == '__main__':

    obj = B() # B의 생성자만 호출되고 A는 호출되지 않는다. - 자식 클래스가 부모 클래스의 생성자를 생성하지 않는다.
              # (java - 상속에서 자식의 생성자 안에서는 부모의 생성자까지 생성되도록 super 사용)

    print(obj.message) # error : message는 A의 __init__() 메서드 안에서 생성되는데, B의 인스턴스를 생성하면서 B.__init__()만 호출하고,
                       # A.__inint__() 메서드는 호출되지 않기 때문.
'''


# super() : 부모클래스의 객체 역할을 하는 프록시(Proxy)를 반환하는 내장 함수

class A:
    def __init__(self):
        print("A.__inint__()")
        self.message = "Hello"

class B(A):
    def __init__(self):
        super().__init__() # A.__inint__() - 명시적으로 표현
        print("B.__init__()")
        print("self.message is "+self.message)

if __name__ == '__main__':


    obj = B()
    print(obj.message)























