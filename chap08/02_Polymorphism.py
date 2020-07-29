# 다형성 (Polymorephism)

class ArmorSuite:
    def armor(self):
        print('amored.')

class IronMan(ArmorSuite):
    pass

def get_armored(suite):
    suite.armor()

if __name__ == '__main__':

    suite = ArmorSuite() # 인스턴스화
    get_armored(suite) # 인스턴스화 - suite 참조 변수를 매개변수로 사용하여 메서드 호출

    iron_man = IronMan()
    get_armored(iron_man) # 상속 받은 자녀 클래스(다형성) - suite 참조 변수를 매개변수로 사용하여 메서드 호출


















