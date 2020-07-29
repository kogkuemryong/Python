# @decorator

class MyDecorator:
    def __init__(self, f): # __init__() 메서드의 매개변수를 통해서 함수를 받아들이고 데이터 속성에 저장해 둠
        print("Initializing MyDecorator...")
        self.func = f # MyDecorator의 func 데이터 속성이 print_hello를 받아둠.

    def __call__(self):
        print("Begin:{0}".format(self.func.__name__))

        self.func() # __call()__ 메서드가 호출되면 생상자에서 저장해둔 함수(데이터 속성)를 호출.

        print("End:{0}".format(self.func.__name__))

@MyDecorator # 함수의 이름이 self.func에 등록이 되어진다.
def print_hello():
    print("Hello.")

if __name__ == '__main__':

    print_hello() # 함수의 이름을 통해서 Mydecorator와 연동되어 수행하도록 한다.


