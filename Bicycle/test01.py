# 노트북이 간결해 보이도록 경고 문구는 출력되지 않도록 함 .  - 오류 문구는 나옵니다.
import warnings
warnings.simplefilter(action='ignore', category = FutureWarning)

#  시각화 도구 설치 R에서 사용하는 시각화 문법을 편하게 사용할 수 있도록 맵핑 - 그래프
import plotnine # R에서 사용하는 graphic 패키지를 python에서 그래프 그리기 할 때 사용
import missingno as msno # 결측치 시각화
import folium # 지도 시각화 (위치 표시)

# 기본 글꼴 변경하기
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


# 사용할 도구 가져오기
import pandas as pd # python에서 사용하는 exel과 유사한 기능을 가짐
import numpy as np # python에서 계산기로 수치 계산을 할 때 사용
from plotnine import * # 시각화 도구


# 데이터 확인
df = pd.read_csv("C:/workspaces/titanic/bi.csv", encoding='cp949') # 파일 자체를 인코딩 할 때는 'cp949' 사용
# print(df.shape) # (1755046, 11)
# print(df.head(10))
# print(df.tail) 뒤에 부터 옴
# print(df.info()) # 데이터의 컬럼 정보, 개수, 데이터 타입을
"""
[10 rows x 11 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1755046 entries, 0 to 1755045
Data columns (total 11 columns):
 #   Column    Dtype  
---  ------    -----  
 0   자전거번호     object 
 1   대여일시      object 
 2   대여 대여소번호  int64  
 3   대여 대여소명   object 
 4   대여거치대     int64  
 5   반납일시      object 
 6   반납대여소번호   int64  
 7   반납대여소명    object 
 8   반납거치대     int64  
 9   이용시간      int64  
 10  이용거리      float64
dtypes: float64(1), int64(5), object(5)
memory usage: 147.3+ MB
None
"""
# 분석을 위한 전처리

# 컬럼에 있는 '를 제거
df.columns = df.columns.str.strip("'")

# 불필요하게 '가 들어가 있다. 스트링 타입으로 되어 있는 데이터에서 '을 제거하자.
df = df.apply(lambda x: x.str.strip("'") if x.dtype == np.dtype('object') else x)
# strip - "'" 의 값을 삭제. / np의 데이터 타입이 object일때 제거하도록 사용.

# 결측치 보기
df.isnull().sum  # null 값을 합하도록
# 데이터프레임의 isnull 또는 isna 메서드를 사용하면 누락 데이터의 위치를 알 수 있다.

# 결측치 시각화 하기
# missingno는 별도로 설치해야하는 시각화 도구라고 하는데 pycharm에서는 그냥 사용 가능, 결측치를 시각화
msno.matrix(df, figsize=(12,5))
# plt.show()

# 대여소별 대여|반납 현황
# print('#대여소 수')
# print('대여 대여소:', df['대여 대여소번호'].unique().shape[0]) # 대여 대여소: 2031
# print('반납 대여소:', df['반납대여소번호'].unique().shape[0]) # 반납 대여소: 2030
# 그냥 shape[0] - 행 총 몇개인지 출력 // unique().shape[0] - 대여 대여소가 몇개 인지 출력.

# 대여 대여소번호로 상위 10개 출력
# print(df['대여 대여소번호'].value_counts().head(10))
# value_counts()를 이용해서 대여 대여소번호로 그룹바이를 해서 카운트하는 것이다.
# 어떤 대여소에서 몇건이 을 대여해갔는지 출력. head(10) - 상위 10개
"""
207     10682
502     10504
152      7710
2102     7382
2701     6053
2219     5950
2177     5322
1160     5297
1906     5147
583      5144
"""
# 번호로 출력되어서 어느 장소인지 알 수 없다.

# 대여대여소명으로 상위 10개 출력
# print(df['대여 대여소명'].value_counts().head(10))
"""
여의나루역 1번출구 앞               10682
뚝섬유원지역 1번출구 앞              10504
마포구민체육센터 앞                  7710
봉림교 교통섬                     7382
마곡나루역 5번출구 뒤편               6053
고속터미널역 8-1번, 8-2번 출구 사이     5950
신대방역 2번 출구                  5322
양천향교역 7번출구앞                 5297
신도림역 1번 출구 앞                5147
청계천 생태교실 앞                  5144
"""

# 반납량이 많은 상위 대여소 10개 출력
# print(df['반납대여소명'].value_counts().head(10))
"""
뚝섬유원지역 1번출구 앞              11424
여의나루역 1번출구 앞               10876
마포구민체육센터 앞                  8323
봉림교 교통섬                     7407
고속터미널역 8-1번, 8-2번 출구 사이     6229
마곡나루역 5번출구 뒤편               5960
신대방역 2번 출구                  5416
청계천 생태교실 앞                  5309
옥수역 3번출구                    5305
당산육갑문                       5273
"""

# 1. 대여반납이 많은 상위 대여소인 뚝썸, 여의나루역, 마포구민 센터등 모두 강이나 호수를 인근에 두고 있다.
# 2. 고속터미널, 신도림 역 같은 경우 사람들의 출퇴근이 또는 많이 사람들이 오가는 곳?

# 평균 이용거리가 긴 상위 대여소
df_ds_long = df.groupby(['대여 대여소명'])['이용거리'].mean().\
    reset_index().sort_values(by = '이용거리', ascending=False).head(10)
# mean - 평균 이용거리 ,sum 으로 구하게 되면 이용한 횟수가 많아지면 이용거리가 많이 나오는 것처럼 보일 수 있다.
# 만약 mean 대신 max를 이용하게 되면 제일 멀리간 사람의 값 하나만 출력되기 때문에 잘못된 결과가 나올 수 있다.
# reset_index : 기존의 행 인덱스를 제거하고 인덱스를 데이터 열로 추가
# sort_values(by = '이용거리', ascending=False).head(10) : 이용거리의 값을 기준으로 내림 차순으로 상위 10개 출력.

# print(df_ds_long)

"""
              대여 대여소명         이용거리
113               강남센터  6314.800000
426             능안마을입구  6027.500000
522   독산보도육교 앞 자전거 보관소  5587.796635
1354            안골마을입구  4992.727917
685           망원초록길 입구  4677.213210
2023          흑석역 1번출구  4511.513777
1497           옥수동성당 옆  4507.450980
1728         종암사거리 분수대  4443.333333
560    동작역 5번출구 동작주차공원  4403.272286
1908       한남초교 앞 보도육교  4372.122997

"""

# 평균 이용거리가 짧은 대여소
df_ds_short = df.groupby(["대여 대여소명"])['이용거리'].mean()\
    .reset_index().sort_values(by='이용거리',ascending=True).head(10)
# print(df_ds_short)
# sort_values(by = '이용거리', ascending=False).head(10) : 평균이 짧은 것 (올림 차순)
"""
      대여 대여소명         이용거리
295        구의7단지현대아파트   0.0
1080    서울특별시 남부교육지원청   0.0
1065           서울역 서부   0.0
1062       서울안천초등학교 옆   0.0
1527          용마지구대 옆   0.0
1538      우리은행 낙성대역지점   0.0
1540   우리은행 시흥남자동화점 앞   0.0
1057     서울식물원 식물문화센터   0.0
84    sk신내 주유소앞(용마산로)   0.0
168              개화정비   0.0
"""

# 평균 이용시간이 적은 상위 대여소
df_tm_long = df.groupby(['대여 대여소명'])['이용시간'].mean()\
    .reset_index().sort_values(by='이용시간',ascending=False).head(10)
# print(df_tm_long)
"""
대여 대여소명       이용시간
560     동작역 5번출구 동작주차공원  63.232439
1040         서울숲 공영주차장앞  61.479121
783            반포경남쇼핑 앞  59.869565
1441       연신초등학교옆 마을마당  59.714286
1639          이촌역5번출구 앞  59.642857
1638           이촌역2번 출구  59.609756
1196       송파 파인타운 11단지  59.000000
1373          약수역 6번 출구  57.800000
1943    항동지구 3단지 311동 앞  57.772727
1114  석수역1번출구 앞 (SK주유소)  57.543033
"""
# 이용시간이 긴 대여소와 대여수가 많은 대여소가 다르다. - 대부분 데이트 코스로 보이는 장소?!

# 평균 이용시간이 적은 상위 대여소
df_tm_short = df.groupby(['대여 대여소명'])['이용시간'].mean()\
    .reset_index().sort_values(by='이용시간',ascending=True).head(10)
# print(df_tm_short)
"""
    대여 대여소명       이용시간
168           개화정비   2.000000
965         상암단말정비   2.000000
559   동작상떼빌 103동 앞   3.000000
1280       신림동주민센터   3.000000
1183    소피아 관광호텔 앞   3.000000
1454       영남단말기정비   4.833333
1455    영남주차장 정비센터   6.000000
1577           위트콤  10.103774
505           도봉센터  11.000000
163     개포고등학교 정문앞  12.0000
"""

# 시계열 데이터 보기
# 대여일시와 반납일시 dtype을 object -> datetime 으로 변환
df['대여일시'] = pd.to_datetime(df['대여일시'])
df['반납일시'] = pd.to_datetime(df['반납일시'])
# print(df.dtypes)
#datetime으로 변환하면 dt.함수를 사용할 수 있다.

"""
자전거번호               object
대여일시        datetime64[ns]
대여 대여소번호             int64
대여 대여소명             object
대여거치대                int64
반납일시        datetime64[ns]
반납대여소번호              int64
반납대여소명              object
반납거치대                int64
이용시간                 int64
이용거리               float6
"""

df['대여년'] = df['대여일시'].dt.year
df['대여월'] = df['대여일시'].dt.month
df['대여일'] = df['대여일시'].dt.day
df['대여시'] = df['대여일시'].dt.hour
df['대여분'] = df['대여일시'].dt.minute
df['대여요일'] = df['대여일시'].dt.dayofweek
df.columns

df['반납년'] = df['반납일시'].dt.year
df['반납월'] = df['반납일시'].dt.month
df['반납일'] = df['반납일시'].dt.day
df['반납시'] = df['반납일시'].dt.hour
df['반납분'] = df['반납일시'].dt.minute
df['반납요일'] = df['반납일시'].dt.dayofweek
df.columns

# print(df.dtypes)

# 년, 월, 일, 시, 분 , 요일 단위로 구분 할 수 있어졌다.
"""
자전거번호               object
대여일시        datetime64[ns]
대여 대여소번호             int64
대여 대여소명             object
대여거치대                int64
반납일시        datetime64[ns]
반납대여소번호              int64
반납대여소명              object
반납거치대                int64
이용시간                 int64
이용거리               float64
대여년                  int64
대여월                  int64
대여일                  int64
대여시                  int64
대여분                  int64
대여요일                 int64
반납년                  int64
반납월                  int64
반납일                  int64
반납시                  int64
반납분                  int64
반납요일                 int64
"""

# 일자별 대여|반납 현황
# 일자별 대여 현황
df_day_1 = df['대여일'].value_counts().reset_index() # 인덱스 값 재설정
df_day_1.columns = ['day','count'] # 컬럼명 설정
# print(df_day_1)

# 몇일에 몇개를 빌렸는지를 출력.
"""
    day  count
0     3  75601
1     5  75291
2     1  73199
3     6  72711
4     8  71003
5     7  70452
6     4  69489
7    12  69189
8     9  67896
9    15  67641
10   18  65493
11   16  65401
12   17  65106
13   11  64806
14   19  64038
15   27  63017
16   23  59220
17   14  58484
18    2  57781
19   26  57741
20   28  57412
21   20  56748
22   22  56582
23   13  56409
24   21  54983
25   29  40340
26   10  37716
27   25  27502
28   30  22456
29   24  11339
"""

# 대여반납 - 대여 추가
df_day_1 = df_day_1.sort_values('day') # count -> day : sort
df_day_1['대여반납'] = '대여' # 대여반납이라는 컬럼 생성, 대여일은 대여로 출력.
# print(df_day_1)

# 일자별 반납 현황
df_day_2 = df['반납일'].value_counts().reset_index() # 인덱스 값 재설정
df_day_2.columns = ['day','count'] # 컬럼명 설정
# print(df_day_2)

# 대여반납 - 반납 추가
df_day_2 = df_day_2.sort_values('day') # count -> day : sort
df_day_2['대여반납'] = '반납' # 대여반납이라는 컬럼 생성, 반납일은 반납으로 출력.
# print(df_day_2)

df_day = pd.concat([df_day_1,df_day_2]) # pd.concat : 2개의 data 결합
# print(df_day)

# 시각화
"""
print((ggplot(df_day)
 + aes(x='day', y='count', fill='대여반납') # 축
 + geom_bar(stat='identity', position='dodge')
 + labs(x = '대여일', y = '대여수', title = '일별 자전거 대여수') # 각축 이름, 타이틀
 + theme(text= element_text(family=font_name),figure_size=(12,6)))) # 한글을 출력하기 위함.
"""


# 요일별 대여|반남 현황
# 요일별 대여 현황
df_dow_1 = df['대여요일'].value_counts().reset_index()
df_dow_1.columns = ['dayofweek','count']
# print(df_dow_1)

# 대여반납 추가 - 대여
df_dow_1 = df_dow_1.sort_values('dayofweek')
df_dow_1['대여반납'] = '대여'
# print(df_dow_1)

# 요일별 반납 현황
df_dow_2 = df['반납요일'].value_counts().reset_index()
df_dow_2.columns = ['dayofweek', 'count']
# print(df_dow_2)

# 대여반납 추가 - 반납
df_dow_2 = df_dow_2.sort_values('dayofweek')
df_dow_2['대여반납'] = '반납'
# print(df_dow_2)

# 데이터 결합 (요일별 대여|반납 현황)
df_dow = pd.concat([df_dow_1, df_dow_2])
# print(df_dow)

weekday_map ={0 :'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}

# 시각화
"""
print((ggplot(df_dow)
 + aes(x='dayofweek', y='count', fill='대여반납') # 축
 + geom_bar(stat='identity', position='dodge')
 + geom_point()
 + geom_line(color='blue')
 + labs(x = '대여요일', y = '대여수', title = '요일별 자전거 대여수') # 각축 이름, 타이틀
 + theme(text= element_text(family=font_name),figure_size=(12,6)))) # 한글을 출력하기 위함.
"""

# 시간대열 대여|반납량
# 시간대열 대여 현황
df_hour_1 = df['대여시'].value_counts().reset_index()
df_hour_1.columns = ['hour', 'count']
# print(df_hour_1)

# 대여반납 추가 - 대여
df_hour_1 = df_hour_1.sort_values('hour')
df_hour_1['대여반납'] = '대여'
# print(df_hour_1)

# 시간대열 반납 현황
df_hour_2 = df['반납시'].value_counts().reset_index()
df_hour_2.columns = ['hour', 'count']
# print(df_hour_2)

# 대여반납 추가 - 반납
df_hour_2 = df_hour_2.sort_values('hour')
df_hour_2['대여반납'] = '반납'
# print(df_hour_2)

# 시간별 대여반납 데이터 결합
df_hour = pd.concat([df_hour_1, df_hour_2])
# print(df_hour)

# 시각화
"""
print((ggplot(df_hour)
 + aes(x='hour', y='count', fill='대여반납') # 축
 + geom_bar(stat='identity', position='dodge')
 + geom_point()
 + geom_line(color='blue')
 + labs(x = '시간', y = '대여/반납', title = '사간별 자전거 대여수') # 각축 이름, 타이틀
 + theme(text= element_text(family=font_name),figure_size=(12,6)))) # 한글을 출력하기 위함.
"""

# 새벽 시간대로 갈수록 대여/반납 수가 줄어든다.
# 출퇴근 시간에 대여/반납이 많은데, 특히 퇴근시간에 가장 많은 대여/반납의 수를 보인다.
# 10 ~ 18시까지 대여가 반납 보다 많다 (대여 > 반납)
# 19 ~ 05시까지 반납이 대여 보다 많다 (반납 > 대여)


# 분별 대여|반납 현황
# 분별 대여량
df_minute_1 = df['대여분'].value_counts().reset_index()
df_minute_1.columns = ['minute', 'count']
# print(df_minute_1)

# 대여반납 추가 - 대여
df_minute_1 = df_minute_1.sort_values('minute')
df_minute_1['대여반납'] = '대여'
# print(df_minute_1)

# 분별 반납량
df_minute_2 = df['반납분'].value_counts().reset_index()
df_minute_2.columns = ['minute', 'count']
# print(df_minute_2)

# 대여반납 추가 - 반납
df_minute_2 = df_minute_2.sort_values('minute')
df_minute_2['대여반납'] = '반납'
# print(df_minute_2)

# 분별 대여|반납 데이터 결합
df_minute = pd.concat([df_minute_1, df_minute_2])
# print(df_minute)

# 시각화
"""
print((ggplot(df_minute)
 + aes(x='minute', y='count', fill='대여반납') # 축
 + geom_bar(stat='identity', position='dodge')
 + geom_point()
 + geom_line(color='blue')
 + labs(x = '분', y = '대여/반납', title = '시간대별(분) 자전거 대여수') # 각축 이름, 타이틀
 + theme(text= element_text(family=font_name),figure_size=(12,6)))) # 한글을 출력하기 위함.
"""
# 대여/반납이 거의 비슷하게 이루어지고 있지만 0~20분 사이에 더 많이 일어나며 반납은 40~60분 사이에 더 많이 일어난다.


# 대여와 바납은 같은 곳에서 이루어지고 있을까?

# print(df.dtypes)

# 같은대여반납소 데이터 생성 - 대여 대여소명 = 반납대여소명이 동일 할 때, True, False 값이 저장
df['같은대여반납소'] = df['대여 대여소명'] == df['반납대여소명']
# print(df['같은대여반납소']) # True, False 값으로 출력.

# .value_counts().reset_index()을 넣어서 새로운 변수에 저장
#
df_location_diff = df['같은대여반납소'].value_counts().reset_index()
df_location_diff.columns = ['일치여부','대여반납수']
# print(df_location_diff)
"""
   일치여부 대여반납
0  False  1548125
1   True   206921
"""
# 다른 곳에서 반납하는 경우가 훨씬 더 많다.

# 비율로 출력
location_diff_ration = df_location_diff['대여반납수'][0]/df_location_diff['대여반납수'][1]
# print('같은 곳에서 대여반납 하는 것보다 다른 곳에서 대여반납 하는 것이{0:.2f}배 많다.'.format(location_diff_ration))
# 소수점 두자리까지 출력.
# 같은 곳에서 대여반납 하는 것보다 다른 곳에서 대여반납 하는 것이7.48배 많다.

# print(location_diff_ration)
# # 7.481720076744264

# 시각화
"""
print(ggplot(df_location_diff)
 + geom_col(mapping=aes(x='일치여부', y = '대여반납수', fill = '대여반납수'))
 + labs(title = '대여반납소 일치여부')
 + theme(text= element_text(family=font_name),figure_size=(12,6)))
"""
# 같은 고세서 대여반납을 하는 것보다 다른 곳으로의 대여반납이 훨씬 많은 것을 확인할 수 있다.

# 같은 곳에서 대여반납을 하는 곳
df_same_loc = df.loc[df['같은대여반납소'] == True] # .loc 메서드는 기본적으로 레이블을 사용하여 행에 접근하는 메서드이다.
# print(df_same_loc.head())

# print(df_same_loc['대여 대여소명'].value_counts().head(20))
"""
뚝섬유원지역 1번출구 앞              2945
여의나루역 1번출구 앞               2775
마포구민체육센터 앞                 2185
봉림교 교통섬                    1598
월드컵공원                      1512
옥수역 3번출구                   1507
고속터미널역 8-1번, 8-2번 출구 사이    1230
청계천 생태교실 앞                 1188
당산육갑문                      1159
독산보도육교 앞 자전거 보관소           1103
서울숲 관리사무소                  1076
응봉역 1번출구                   1000
흑석역 1번출구                    992
노들역 1번출구                    969
홍은사거리                       917
동방1교                        867
신대방역 2번 출구                  843
CJ 드림시티                     837
양천향교역 7번출구앞                 820
한신16차아파트 119동 앞             767
Name: 대여 대여소명, dtype: int64
"""
# 강이나 호수 근처.

# print(df.dtypes)
# 같은 대여반납소의 이용시간
same_loc_mean_time = df_same_loc['이용시간'].mean()
# print('같은곳에서 대여, 반납이 이루어지는 자건거의 평균 이용 시간 :' , same_loc_mean_time)
# 같은곳에서 대여, 반납이 이루어지는 자건거의 평균 이용 시간 : 53.854350210950074
# 주변에서 타는 것으로 취미, 놀이

df_same_mean = df_same_loc.groupby(['대여 대여소명', '반납대여소명'])['이용시간'].mean().reset_index()
df_same_count = df_same_loc.groupby(['대여 대여소명', '반납대여소명']).size().reset_index()
df_same_count.columns = ['대여 대여소명', '반납대여소명', '이용횟수']
df_same_loc2 = df_same_mean.merge(df_same_count, left_on=['대여 대여소명', '반납대여소명'], right_on=['대여 대여소명', '반납대여소명'])
# print(df_same_loc2.sort_values(by='이용시간', ascending=False).head(10))
"""
             대여 대여소명          반납대여소명        이용시간  이용횟수
180         경문고등학교 앞        경문고등학교 앞  188.700000    10
377        남태령역 2번출구       남태령역 2번출구  152.000000     1
906          삼일수영장 앞         삼일수영장 앞  135.333333     3
1381   역삼동 sk뷰 501동앞   역삼동 sk뷰 501동앞  122.000000     8
1918        혜화역 1번출구        혜화역 1번출구  118.000000     1
758        반석교회(쌍문동)       반석교회(쌍문동)  117.000000     1
288       구의7단지현대아파트      구의7단지현대아파트  116.000000     1
1052       서울특별시 교육청       서울특별시 교육청  114.000000     1
734      문정·가락 대여소 앞     문정·가락 대여소 앞  103.500000     2
1265  신영동삼거리(북악터널방향)  신영동삼거리(북악터널방향)  102.000000     1

"""

# 이용횟수가 많은 곳의 평균 이용시간
# print(df_same_loc2.sort_values(by = '이용횟수', ascending=False).head(10))

"""
                    대여 대여소명                   반납대여소명       이용시간   이용횟수
568             뚝섬유원지역 1번출구 앞            뚝섬유원지역 1번출구 앞  58.456367  2945
1372             여의나루역 1번출구 앞             여의나루역 1번출구 앞  66.649369  2775
648                마포구민체육센터 앞               마포구민체육센터 앞  61.212815  2185
822                   봉림교 교통섬                  봉림교 교통섬  57.451189  1598
1524                    월드컵공원                    월드컵공원  60.522487  1512
1456                 옥수역 3번출구                 옥수역 3번출구  61.099536  1507
204   고속터미널역 8-1번, 8-2번 출구 사이  고속터미널역 8-1번, 8-2번 출구 사이  75.922764  1230
1767               청계천 생태교실 앞               청계천 생태교실 앞  51.898148  1188
434                     당산육갑문                    당산육갑문  64.081967  1159
507          독산보도육교 앞 자전거 보관소         독산보도육교 앞 자전거 보관소  67.539438  1103
"""
# 이용횟수의 시각화
# print(df_same_loc2['이용횟수'].plot.hist())  -- 다시 해보자

# 다른 대여|반납소
df_diff_loc = df.loc[df['같은대여반납소']== False]
# print(df_diff_loc.shape)


diff_loc_mean_time = df_diff_loc['이용시간'].mean()
# print('다른곳에서 대여, 반납이 이루어지는 자전거의 평균 이용시간 : ', diff_loc_mean_time)
# 다른곳에서 대여, 반납이 이루어지는 자전거의 평균 이용시간 :  27.80103544610416
# - 교통수단으로 이돟

df_diff_mean = df_diff_loc.groupby(['대여 대여소명', '반납대여소명'])['이용시간'].mean().reset_index()
df_diff_count = df_diff_loc.groupby(['대여 대여소명', '반납대여소명']).size().reset_index()
df_diff_count.columns = ['대여 대여소명', '반납대여소명', '이용횟수']
df_diff_loc2 = df_diff_mean.merge(df_diff_count, left_on=['대여 대여소명', '반납대여소명'], right_on=['대여 대여소명', '반납대여소명'])
# print(df_diff_loc2.sort_values(by='이용시간', ascending=False).head(10))

"""
     대여 대여소명             반납대여소명    이용시간  이용횟수
51932         녹사평역 광장          상월곡역 4번출구  2423.0     1
97760       밀리아나2빌딩 앞           어린이대공원정문  1306.0     1
64172            도원맨션        신월6차보람아파트 앞   949.0     1
233971     청구역 2번출구 앞            서울시립대 앞   920.0     1
92112    몽촌토성역 1번출구 옆  삼성타운(삼성생명) A동 맞은편   869.0     1
157899   신도림역 1번 출구 앞           중앙유통단지 앞   770.0     1
152819   스타즈호텔독산 빌딩 앞         혜명양로원 담장 옆   754.0     1
6850       LG베스트샵 종암점       동대문롯데캐슬아파트 앞   743.0     1
212844  잠실새내역 5번 출구 뒤        반포1동 서초빌딩 앞   735.0     1
219575       종각역 5번출구          LG서비스 역촌점   728.0     1
"""

# 다른 대여|반납소 중 이용횟수가 가장 많은 상위 10곳
# print(df_diff_loc2.sort_values(by='이용횟수', ascending=False).head(10))
"""
대여 대여소명            반납대여소명       이용시간  이용횟수
106134            봉림교 교통섬              동방1교  20.555024   836
68392                동방1교           봉림교 교통섬  19.763441   744
73870       뚝섬유원지역 1번출구 앞  건대입구역 사거리(롯데백화점)  24.929099   677
21205    건대입구역 사거리(롯데백화점)     뚝섬유원지역 1번출구 앞  36.906977   516
243582      하늘채코오롱아파트 건너편      홍대입구역 2번출구 앞  13.753456   434
210794            자양중앙나들목     뚝섬유원지역 1번출구 앞  14.319899   397
74347       뚝섬유원지역 1번출구 앞           자양중앙나들목  17.101828   383
160568          신방화역환승주차장       마곡엠밸리4단지 정문   9.358639   382
81105       마곡역 교차로(NH농협)     마곡나루역 5번출구 뒤편   5.498667   375
215944  장한평역 1번출구 (국민은행앞)           장안동 사거리  13.309973   371

"""
# 서로 오고가고 한 교통수단으로 이용한 것을 볼 수 있다.

rent_mean_time = same_loc_mean_time - diff_loc_mean_time
print('같은 곳에서 대여반납이 이루어지는 자전거의 이용시간이 다른 대여소의 대여반납 이용시간보다 {:,.2f} 분 많다.'.format(rent_mean_time))
# 같은 곳에서 대여반납이 이루어지는 자전거의 이용시간이 다른 대여소의 대여반납 이용시간보다 26.05 분 많다.

# - 이용횟수가 많은 대여소라고 해서 평균이용시간이 평균보다 높지 않다.

# 해당 기간동안 가장 많이 이용된 자전거는 몇 회 대여 되었을까?
bike_describe = df['자전거번호'].describe() # .describe() : 요약 통계량 - ean(), max(), median()등 개별 함수를 사용하여 통계량을 계산할 수도 있습니다.
# print(bike_describe)
# print('대여된 자전거 수 :', bike_describe[1]) # 대여된 자전거 수 : 13850
# print('가장 많이 대여된 자전거 번호 :', bike_describe[2]) # 가장 많이 대여된 자전거 번호 : SPB-31583


bike_rent_counts = df['자전거번호'].value_counts().reset_index()
bike_rent_counts.columns = ['자전거번호', '대여수']
# print('해당 기간동안 자전거 하나당 평균 대여 수:', bike_rent_counts['대여수'].mean()) # 해당 기간동안 자전거 하나당 평균 대여 수: 126.71812274368231
# print('자전거 하나당 가장 많이 대여된 횟수:', bike_rent_counts['대여수'].max()) # 자전거 하나당 가장 많이 대여된 횟수: 407
# print('자전거 하나당 가장 적게 대여된 횟수:', bike_rent_counts['대여수'].min()) # 자전거 하나당 가장 적게 대여된 횟수: 1

# 시각화
# bike_rent_counte.plot.hist()

