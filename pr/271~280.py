# 271 Account 클래스
# 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다.
# Account 클래스를 생성한 후 생성자를 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다.
# 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
# 은행이름: SC은행
# 계좌번호: 111-11-111111
import random
"""
class Account():
    def __init__(self,name, firstmoney):
        self.name = name
        self.firstmoney = firstmoney
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.number = num1 + '-' + num2 + '-' + num3

kong = Account("공금령",100000000000)
print(kong.name)
print(kong.firstmoney)
print(kong.bank)
print(kong.number)
"""
# 272 클래스 변수
# 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요
"""
class Account():
    account_number = 0

    def __init__(self,name, firstmoney):
        self.name = name
        self.firstmoney = firstmoney
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.number = num1 + '-' + num2 + '-' + num3

        Account.account_number += 1

kong = Account("공금령",100000000000000000)
print(Account.account_number)

kim = Account("김슬기",100000000000000000000)
print(Account.account_number)
"""

# 273 클래스 변수 출력
# Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.
"""
class Account():
    account_number = 0

    def __init__(self,name, firstmoney):
        self.name = name
        self.firstmoney = firstmoney
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.number = num1 + '-' + num2 + '-' + num3

        Account.account_number += 1

    @classmethod
    def get_account_num(num):
        print(num.account_number)


hong = Account("홍길동",100)
lee = Account("이순신",100)
hong.get_account_num()
"""

# 274 입금 메서드
# Account 클래스에 입금을 위한 depost 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.

"""
class Account():
    account_number = 0

    def __init__(self,name, firstmoney):
        self.name = name
        self.firstmoney = firstmoney
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.number = num1 + '-' + num2 + '-' + num3

        Account.account_number += 1

    @classmethod
    def get_account_num(num):
        print(num.account_number)

    def deposit(self, amount):
        if amount >= 1:
            self.firstmoney += amount

hong = Account("홍길동",100)
hong.deposit(100)

print(hong.firstmoney)
"""

# 275 출금 메서드
# Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.
"""
class Account():
    account_number = 0

    def __init__(self,name, firstmoney):
        self.name = name
        self.firstmoney = firstmoney
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.number = num1 + '-' + num2 + '-' + num3

        Account.account_number += 1

    @classmethod
    def get_account_num(num):
        print(num.account_number)

    def deposit(self, amount):
        if amount >= 1:
            self.firstmoney += amount

    def withdraw(self,money):
        if money < self.firstmoney:
            self.firstmoney -= money

hong = Account("홍길동",100)
hong.withdraw(50)
print(hong.firstmoney)
"""

# 276 정보 출력 메서드
# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.
"""
class Account():
    account_number = 0

    def __init__(self,name, firstmoney):
        self.name = name
        self.firstmoney = firstmoney
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.number = num1 + '-' + num2 + '-' + num3

        Account.account_number += 1

    @classmethod
    def get_account_num(num):
        print(num.account_number)

    def deposit(self, amount):
        if amount >= 1:
            self.firstmoney += amount

    def withdraw(self,money):
        if money < self.firstmoney:
            self.firstmoney -= money

    def display_info(self):
        print(self.name)
        print(self.firstmoney)
        print(self.bank)
        print(self.account_number)

hong = Account("홍길동",100)
hong.display_info()
"""

# 277 이자 지급하기
# 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.
"""
class Account():
    account_number = 0

    def __init__(self,name, firstmoney):
        self.deposit_count = 0

        self.name = name
        self.firstmoney = firstmoney
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.number = num1 + '-' + num2 + '-' + num3

        Account.account_number += 1

    @classmethod
    def get_account_num(num):
        print(num.account_number)


    def deposit(self, amount):
        if amount >= 1:
            self.firstmoney += amount

            self.deposit_count += 1
            if self.deposit_count % 5 ==0: # 5,10,15
                self.firstmoney = (self.firstmoney * 1.01)

    def withdraw(self,money):
        if money < self.firstmoney:
            self.firstmoney -= money

    def display_info(self):
        print(self.name)
        print(self.firstmoney)
        print(self.bank)
        print(self.account_number)

hong = Account("파이썬", 10000)

hong.deposit(10000)
hong.deposit(10000)
hong.deposit(10000)
hong.deposit(10000)
hong.deposit(10000)
print(hong.firstmoney)
"""
# 278 여러 객체 생성
# Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.]
"""
class Account():
    account_number = 0

    def __init__(self,name, firstmoney):
        self.deposit_count = 0

        self.name = name
        self.firstmoney = firstmoney
        self.bank = "SC은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        # 3 - 2 - 6
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.number = num1 + '-' + num2 + '-' + num3
        Account.account_number += 1

    @classmethod
    def get_account_num(num):
        print(num.account_number) # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.firstmoney += amount

            self.deposit_count += 1
            if self.deposit_count % 5 ==0: # 5,10,15
                # 이자 지급
                self.firstmoney = (self.firstmoney * 1.01)

    def withdraw(self,money):
        if money < self.firstmoney:
            self.firstmoney -= money

    def display_info(self):
        print(self.name)
        print(self.firstmoney)
        print(self.bank)
        print(self.account_number)

data = []
kong = Account("홍길동", 100100000000000)
lee = Account("이순신", 10000000000)
kang = Account("강감찬",100)

data.append(kong)
data.append(lee)
data.append(kang)

data
"""

# 279 객체 순회
# 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.

"""
class Account():
    account_number = 0

    def __init__(self,name, firstmoney):
        self.deposit_count = 0

        self.name = name
        self.firstmoney = firstmoney
        self.bank = "SC은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        # 3 - 2 - 6
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.number = num1 + '-' + num2 + '-' + num3
        Account.account_number += 1

    @classmethod
    def get_account_num(num):
        print(num.account_number) # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.firstmoney += amount

            self.deposit_count += 1
            if self.deposit_count % 5 ==0: # 5,10,15
                # 이자 지급
                self.firstmoney = (self.firstmoney * 1.01)

    def withdraw(self,money):
        if money < self.firstmoney:
            self.firstmoney -= money

    def display_info(self):
        print(self.name)
        print(self.firstmoney)
        print(self.bank)
        print(self.account_number)

data = []
kong = Account("홍길동", 100100000000000)
lee = Account("이순신", 10000000000)
kang = Account("강감찬",100)

data.append(kong)
data.append(lee)
data.append(kang)

for i in data:
    if i.firstmoney >= 1000000:
        i.display_info()

"""

# 280 입출금 내역
# 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.
class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount):
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)


k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()
print(k.balance)