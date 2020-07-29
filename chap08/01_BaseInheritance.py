class Base:
    def __init__(self):
        print(self)
        self.message = "Hello, World"

    def print_message(self):
        print(self.message)

class Derived(Base): # Base 클래스 상속
    pass

if __name__ == '__main__':
    base = Base()
    dervied = Derived()

    base.print_message()
    dervied.print_message() # 부모 클래스의 메서드를 그대로 사용.


