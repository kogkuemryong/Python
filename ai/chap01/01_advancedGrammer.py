# 데이터 분석에 유용한 기능들 ...
# - list comprehension 기본 구조

numbers = [1,2,3,4,5]
square1 = [] # list 형태 초기화

for i in numbers:
    square1.append(i**2) # append : 가지고 있는 데이터 마지막에 추가
                         # square에 numbers의 값을 제곱해서 저장.
print(square1)

########## 위의 코드와 동일 ################

square2 = [i**2 for i in numbers]
print(square2)

###################################################################################
square3 = []
for i in numbers:
    if i >= 3:
        square3.append(i**2)

print(square3)

########### 위의 코드와 동일 #################
square4 = [i**2 for i in numbers if i >= 3]
print(square4)


# - split(구분자) : 구분자로 구분, 기본값은 공백
test_text = "the-joen-computer-with-python"
result = test_text.split("-")
print(result) # ['the', 'joen', 'computer', 'with', 'python']


# 구분자.join(리스트): split 함수와 반대와 구분자를 붙인다.
test_text = ['the', 'joen', 'computer', 'with', 'python']
print(test_text)
result = '-'.join(test_text)
print(result) # the-joen-computer-with-python

# split()와 join 의 응용
result = '-'.join('345.234.6789'.split('.')) # replace 와 동일
print(result) # 345-234-6789


# enumerate(list): 인덱스와 값을 함께 반환
for i, name in enumerate(['a','b','c','d']):  # 변수가 2개
    print(i, name) # 인덱스와 함께 값을 반환

seq = ['mon','tue','wed','thu','fri','sat','sun']
print(dict(enumerate(seq))) # {0: 'mon', 1: 'tue', 2: 'wed', 3: 'thu', 4: 'fri', 5: 'sat', 6: 'sun'}


# zip(key, value) : key, value 형태로 연결해준다.
key_seq = 'abcdefg'
value_seq = ['mon','tue','wed','thu','fri','sat','sun']
dict = dict(zip(key_seq,value_seq))
print(dict)

day = ['mon','tue','wed','thu','fri','sat','sun']
print([x for x in day])

data = [35,56,-53,45,27,-28,8,-12]
print([x for x in data if x>=0])
print([x**2 for x in data if x>=0])

# Counter 를 이용한 카운팅
#   - Countsms 아이템의 개수를 자동으로 카운팅.


from collections import Counter # Counter 이름만으로 사용 가능

message = """
대통령은 조국의 평화적 통일을 위한 성실한 의무를 진다. 
비상계엄이 선포된 때에는 법률이 정하는 바에 의하여 영장제도, 언론·출판·집회·결사의 자유, 
정부나 법원의 권한에 관하여 특별한 조치를 할 수 있다. 군인·군무원·경찰공무원 기타 법률이 정하는 자가 전투·훈련등 
직무집행과 관련하여 받은 손해에 대하여는 법률이 정하는 보상외에 국가 또는 공공단체에 공무원의 직무상 불법행위로 인한 
배상은 청구할 수 없다. 모든 국민은 자기의 행위가 아닌 친족의 행위로 인하여 불이익한 처우를 받지 아니한다. 
국민의 자유와 권리는 헌법에 열거되지 아니한 이유로 경시되지 아니한다. 모든 국민은 보건에 관하여 국가의 보호를 받는다."""

counter = Counter(message.split()) # split의 default = 공백
print(counter) # dictionary 형태로 반환
print(type(counter)) # Counter로 수행되어지기 때문에 collections.Counter 로 출력.
# 텍스트 마이닝과 유사. 여백으로 나뉜 값에서 동일한 text의 개수를 출력.

# Counter(dict) -> list 형태로 반환.
print(counter.most_common())
# tuple의 자료형 list 자료형 안에서 관리 된다.

print(type(counter.most_common()))
# list -> dict 형태로 반환.
# print(dict(counter.most_common())) -- error

















