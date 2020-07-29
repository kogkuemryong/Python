# 클래스 생성자 호출 / java 에서 static ( class 변수 )

class ClassVar:
    text_list = []  # 생성자 함수 안에서 선언 x, (self)x
                    # 변수를 바로 선언 = 클래스 생성자(클래스 멤버), [] : 리스트의 자료형으로 선언(리스트로 자료형 관리)
                    # 인스턴스가 공유하는 멤버로 사용

    def add(self, text): # 인스턴스 멤버
        self.text_list.append(text) # self.변수이름 (내부에서 사용될 때는 self. 이 무조건 들어가야 한다.)
                                    # append(text) : 입력으로 가져오는 데이터를 내가 가지고 있는 데이터 마지막에 추가

    def print_list(self): # 인스턴스 멤버
        print(self.text_list)


if __name__ == '__main__':
    a = ClassVar()
    a.add('a')
    a.print_list() # ['a'] 출력을 기대.

    b = ClassVar()
    b.add('b')
    b.print_list() # # ['a','b'] 출력을 기대 -> ( append에 의해서 추가가 되어서 출력 )


