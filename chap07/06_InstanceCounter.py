
class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count += 1 # 같은 영역이여도 self. 생략 불가능 / 인스턴스가 생성될 때마다 카운트

    @classmethod # 데코레이션
    def print_instance_count(cls): # cls : 클래스를 나타낸다.
        print(cls)
        print(cls.count) # = InstanceCounter.count

if __name__ == '__main__':
    a = InstanceCounter()
    InstanceCounter.print_instance_count()

    b = InstanceCounter()
    InstanceCounter.print_instance_count()

    c = InstanceCounter()
    InstanceCounter.print_instance_count()

    InstanceCounter.count = 10
    print(InstanceCounter.count)

    # class method임을 알리기 위해서 class 이름으로 사용하는 것을 권고한다.


