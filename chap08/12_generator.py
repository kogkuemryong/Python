
def generator():
    yield 0 # yield : return과 동일한 기능이지만 차이점은 복귀 하지않고 값만 가지고 대기하고 있는다.
    yield 1 # 하나의 자료형으로 생각하는 것이 좋다.
    yield 2 # 반환하고 싶은 값을 yield 뒤에 넣으면 iterator를 통해서 출력 받을 수 있다.
    yield 3

iterator = generator()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
# print(iterator.__next__()) error : 입력 받는 값 보다 많은 값을 출력 하려고 하기 때문.

#####################################################################################################

# 위의 동일 기능 정의
def YourRange(start,end):
    current = start
    while current < end:
        yield current # 대기
        current += 1
    return

for i in YourRange(0,4):
    print(i)
