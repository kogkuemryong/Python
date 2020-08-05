# 251 클래스, 객체, 인스턴스
# 클래스, 객체, 인스턴스에 대해 설명해봅시다.
# 클래스 : 매개 변수 만들기
# 객체 : 매개 변수의 자리값을 저장
# 인스턴스 : heap 영역에 할당( 메모리 할당 )


# 252 클래스 정의
# 비어있는 사람 (Human) 클래스를 "정의" 해보세요.
# class Human:
#     pass

# 253 인스턴스 생성
# 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.
# class Human:
#     pass

#areum = Human

# 254 클래스 생성자-1
# 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.
# class Human:
#     def __init__(self):
#         print("응애응애")

# areum = Human()
# areum

# 255 클래스 생성자-2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.
# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
# areum = Human("홍길동", 25 ,"남")


# 256 인스턴스 속성에 접근
# 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.
#class Human:
#    def __init__(self, name, age, gender):
#        self.name = name
#        self.age = age
#        self.gender = gender

#hong = Human("홍길동" , 25 , "남")
#print(hong.name)
#print(hong.age)
#print(hong.gender)

# 257 클래스 메소드 - 1
# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print("이름 : {0} , 나이 : {1} , 성별 : {2}".format(self.name,self.age,self.gender))
hong = Human("홍길동",25,"남")
hong.who()


# 258 클래스 메소드 - 2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.

class Human:
    def __init__(self, name, age , gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print("이름 : {0}, 나이 : {1} 성별 : {2}".format(self.name, self.age, self.gender))

    def setInfo(self, name, age , gender):
        self.name = name
        self.age = age
        self.gender = gender


wm=Human("몰라",12,"여")
wm.who()

wm.setInfo("홍길동", 25 , "남")
wm.who()

# 259 클래스 소멸자
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.
# >>> areum = Human("아름", 25, "여자")
# >>> del areum
# 나의 죽음을 알리지 말라

class human:
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def __del__(self):
        print("나의 죽음을 알리지마라")

hong = human("호길동",25,"남")


# 260 에러의 원인
# 아래와 같은 에러가 발생한 원인에 대해 설명하세요.
# class OMG :
#     def print() :
#         print("Oh my god")
#
# >>> >>> myStock = OMG()
# >>> myStock.print()

# TypeError Traceback (most recent call last)
# <ipython-input-233-c85c04535b22> in <module>()
# ----> myStock.print()
#
# TypeError: print() takes 0 positional arguments but 1 was given
# 답: 객체에 저장해줬기 때문에 객체로 함수를 호출해야한다. /  OMG.print(mystock)











