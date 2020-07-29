# Overriding

class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

if __name__=='__main__':
    A().method() # A

    B().method() # B - 동일한 이름의 emthod가 있을 때, 부모의 method는 은닉화 되어지고 자식의 method가 출력 된다.
                 # 가장 가까운 것을 출력

    C().method() # C - 동일한 이름의 emthod가 있을 때, 부모의 method는 은닉화 되어지고 자식의 method가 출력 된다.
                 # 가장 가까운 것을 출력






