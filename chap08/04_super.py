
class Base:
    def __init__(self):
        print("Base")

class Derived(Base):
    pass

if __name__ == '__main__':

    d = Derived() # 자녀 클래스가 별도 생성자를 생성하지 않으면 default로 생성자를 만들어준다.
                  # def __init__(self):
                  #     super.__init__(self)

