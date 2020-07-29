
class Car: # 자료형 선언
    def __init__(self):   # 생성자 :  함수로 정의 / (self) 필수 - java의 this 와 동일 - 생략 불가
        self.color = 0xFF0000     # 차량색상(헥사 코드(Red)) /  self.변수 = x : 필드 선언
        self.wheel_size = 16     # 바퀴크기 --
        self.displacement = 2000 # 엔진 배기량
        # 값이 고정되어 범용성이 떨어진다.

    def forward(self): # 전진 / method 정의 - 함수 정의하는 방법과 동일
        pass # error 발생하지 않고, 의미만 담아줄 때 사용

    def backward(self): # 후진
        pass

    def turn_left(self): # 좌회전
        pass

    def turn_right(self): # 우회전
        pass

if __name__=='__main__': # 시작 지점
    car = Car()

    print(car.color) # 10진수 출력A
    print('0x{:02X}'.format(car.color)) # car 멤버변수 접근
                                        # {:02x}  => 정수를 2자리의 16진수로 출력하되,
                                        # 2자리 안되면 빈자리를 0으로 채워서 출력하라는 의미.

    print(car.displacement)


    car.forward() # car 멤버 메서드 접근
    car.backward()
    car.turn_left()
    car.turn_right()






