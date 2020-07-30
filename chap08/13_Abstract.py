from abc import ABCMeta
from abc import abstractmethod

class AbstractDuck(metaclass=ABCMeta): # 추상 클래스

    @abstractmethod # 추상 메서드
    def Quack(self):
        pass


class Duck(AbstractDuck):
    # pass
    def Quack(self):
        print("메세지 출력")

if __name__ == '__main__':

    duck = Duck() #추상 메서드가 존재하는데 오버라이딩 하지 않아서 error를 낸다.
    duck.Quack()

