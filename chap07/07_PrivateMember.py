
class YourClass:
    pass

class MyClass:
    def __init__(self):
        self.message = "Hello" # 속성 = public

    def some_method(self):
        print(self.message)

#obj = MyClass()
#obj.some_method()

###########################################################

class HasPrivate:
    def __init__(self):
        self.public = "Public." # 속성 = public
        self.__private = "Private."
        self.__public__  = "__Public__" # 앞에 __ 가 있어도 변수 이름 뒤에 _가 2개 이상 오면 public이 된다.
        # 함부로 접근하지 못하도록 하고 싶을 때(정보은닉)
        # __필드명 = private의 속성을 가지도록 한다(변수의 이름으로 은닉화)

    def print_from_internal(self):
        print(self.public)
        print(self.__private) # 클래스 안에에서만 접근 가능, 외부에서는 접근 불가


if __name__ == '__main__':
    obj = HasPrivate()  # 인스턴스화
    obj.print_from_internal() # method 호출에 있어서 문제 없다.

    print(obj.public)
  # print(obj.__private) # error , 자동완성 기능도 수행되지 않는다.
    print(obj.__public__)


