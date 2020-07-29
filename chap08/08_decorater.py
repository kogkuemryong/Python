# 데코레이터(Decorator)

class Callable:
    def __call__(self): # (self , *arg(가변인자 매재변수) - 개수의 제한 x,
        print("I am called.")

if __name__ == '__main__':

    obj = Callable()
    obj() # 인스턴스 뒤에 괄호()를 호출하면, 내부적으로는 __call__ 메서드 호출


