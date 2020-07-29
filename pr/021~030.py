# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = "python"
print(letters[0], letters[2]) # 파이썬 문자열에서 한 글자를 가져오는 것을 인덱싱이라고 부릅니다. 파이썬 인덱싱은 0부터 시작합니다.


# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
# 실행 예: 2210
print(license_plate[-4:])


# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
string = "홀짝홀짝홀짝"
print(string[::2]) # 시작인덱스:끝인덱스:오프셋


# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
# 실행 예:NOHTYP
print(string[::-1])


# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
#실행 예 : 010 1111 2222
phone_number = phone_number.replace("-", " ")
print(phone_number)
# 파이썬 문자열에서 replace 메서드를 사용하면 문자열을 일부를 치환할 수 있습니다.
# 문자열은 수정할 수 없는 자료형이므로 기존 문자열은 그대로 두고 치환된 새로운 문자열이 리턴됩니다.


# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
phone_number1 = "010-1111-2222"
# 실행 예 :  01011112222
phone_number1 = phone_number1.replace("-", "")
print(phone_number1)


# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = "http://sharebook.kr"
# 실행 예: kr
print(url[-2:])
# 문자열로 표현된 url에서 .을 기준으로 분리합니다. 분리된 url 중 마지막을 인덱싱하면 도메인만 출력할 수 있습니다.
url = url.split('.')
print(url[-1])


# 028 문자열은 immutable
#아래 코드의 실행 결과를 예상해보세요.
lang = 'python'
# lang[0] = 'P'
# print(lang) # Python
# 문자열은 수정할 수 없습니다. 실행 결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.


# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
# 실행 예:
# Abcdfe2A354A32A
string = string.replace("a", "A")
print(string)


# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
string = 'abcd'
string.replace('b', 'B')
print(string) # abcd
