class A:
    pass
class B:
    pass
class C:
    pass
class D(A,B,C): # 다중 상속
    pass


#########################################################################

# 다중 상속시 주의 사항 - 죽음의 다이아몬드

class K:
    def method(self):
        print("K")

class L(K):
    def method(self):
        print("L")

class M(K):
    def method(self):
        print("M")

class N(L,M):
    pass

if __name__ == '__main__':

    obj = N()
    obj.method() # 가장 먼저 상속으로 입력된 L을 출력합니다.







