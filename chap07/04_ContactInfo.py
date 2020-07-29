
class ContactInfo: # class 생성
    def __init__(self, name, email): # 생성자 생성 - 범용적 사용(메모리에 할당 되었을 때, 매개변수로 값을 넣을 수 있게 한다)
        self.name = name # 생성자 안에서 필드 생성(self.이름)
        self.email = email

    def print_info(self):
        print('{0}:{1}'.format(self.name,self.email))


if __name__ == '__main__': # 메인에서만 출력 (시작 포인트와 같은 효과)
    hongkildong = ContactInfo('홍길동', 'sss@aaa.com')
    Leesunshin = ContactInfo('이순신', 'sss@aaa.com')

    hongkildong.print_info() # 메서드 호출
    Leesunshin.print_info()

    # 1) class 를 만나면 ContactInfo( ) 라는 메서드가 정의된 것을 확인
    # 2) 밑으로 내려와서 if 문을 확인
    # 3) ContactInfo() 안에 들어가서 heap 영역에 메모리 할당
    # 4) 할당 된 시작 주소값을 self에 저장을 해준다.
    # 5) 생성자 호출







