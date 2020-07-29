

class InstanceVar:
    def __init__(self):
        self.text_list = [] # 생성자가 호출되는 순간 메모리에 할당.

    def add(self, text): # 인스턴스 멤버
        self.text_list.append(text) # self.변수이름 (내부에서 사용될 때는 self. 이 무조건 들어가야 한다.)
                                    # append(text) : 입력으로 가져오는 데이터를 내가 가지고 있는 데이터 마지막에 추가

    def print_list(self): # 인스턴스 멤버
        print(self.text_list)


if __name__ == '__main__':

    a = InstanceVar()
    a.add('a')
    a.print_list() # ['a'] 출력을 기대.

    b = InstanceVar()
    b.add('b')
    b.print_list() #  ['b']  출력을 기대 -> 개별적으로 메모리에 할당 되어 지기 때문입니다.