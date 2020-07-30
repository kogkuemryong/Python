list = [1,2,3]
for i in list: # for 반복문 사용
    print(i)

# Iterator 와 순회 가능한 객체
iterator = range(3).__iter__()  # 0~2 , 입력 받은 값을 iterator가 관리한다.
print(iterator.__next__()) # next 값을 하나씩 꺼내온다.
print(iterator.__next__())
print(iterator.__next__())
# print(iterator.__next__()) # 데이터가 없는데 추가적으로 출력을 하려고 하면 error를 일으킨다.

range(3) # 내부에 iterator가 탑재 되어 있는 자료형으로,
         # iterator는 __next__()가 정의 되어 있어서
         # 하나씩 값을 반환해주는 것이다.

########################################################################################################################

class MyRange: # rage() 함수와 같은 일을 하는 클래스 정의.
    def __init__(self,start,end):
        self.current = start
        self.end = end

    def __iter__(self): # iterator 사용
        return self

    def __next__(self): # iterator 를 사용하기 위해서는 반드시 정의 되어야 한다.
        if self.current < self.end:
            current = self.current
            self.current+=1
            return current

        else:
            raise StopIteration() # iterator 예외처리

if __name__ == '__maine__':
    for i in MyRange(0,5):
        print(i)












