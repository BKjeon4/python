
# import datetime
# today = datetime.date.today()
# print('today is ', today)

from datetime import date, timedelta
today = date.today()
print('today is ', today)

# 날짜 구하기
print('년도 : ', today.year)
print('월 : ', today.month) # 월
print('일 : ', today.day)# 일
a=['월','화','수','목','금','토','일']
print('요일 : ', a[today.weekday()]) # 요일

# 날짜 계산
print('어제 : ', today + timedelta(days=-1))

# 일주일 전 날짜
print('일주일 전 : ', today + timedelta(weeks=-1))

# 10일 후 날짜
print('10일 후 날짜 : ', today + timedelta(days=10))

from datetime import datetime
day = datetime.today()
print(day)

import datetime
day = datetime.datetime.today()
print(day)

# Y : Year
# m : month
# d : day
# H : HOUR
# M : Minute
# S : Second
# h : 1월 부터 12월까지의 월 표기 세글자 (Jan ~ Dec)

# 날짜를 문자열 형태로 (strftime() 이용 )
print(day.strftime('%Y년 %m월 %d일 %H:%M'))

# 문자열을 날짜형태 (strptime() 이용)
naljja = '2022-12-25 12:50:59'
print(type(naljja))
mydate = datetime.datetime.strptime(naljja, '%Y-%m-%d %H:%M:%S')
print(mydate)
print(type(mydate))