# 데코레이터 사용 용도(생성자)

class MyDecorator:
    def __init__(self, f): # __init__() 메서드의 매개변수를 통해서 함수를 받아들이고 데이터 속성에 저장해 둠
        print("Initializing MyDecorator...")
        self.func = f # MyDecorator의 func 데이터 속성이 print_hello를 받아둠.

    def __call__(self):
        print("Begin:{0}".format(self.func.__name__))

        self.func() # __call()__ 메서드가 호출되면 생상자에서 저장해둔 함수(데이터 속성)를 호출.

        print("End:{0}".format(self.func.__name__))

def print_hello():
    print("Hello.")

if __name__ == '__main__':

    mydecorator = MyDecorator(print_hello)
    mydecorator() # 참조변수를 함수를 호출하듯 괄호()를 넣어주면 등록되었던 함수를 호출해준다.





