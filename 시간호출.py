import datetime

#현재 시간 불러오기
now = datetime.datetime.now()
# print(now)
#
# now1 = now.strftime('%y-%m-%d') # 내가 원하는 형식으로, 년도를 22만
# print(now1)
# now2 = now.strftime('%Y-%m-%d') # 내가 원하는 형식으로, 년도를 2022로
# print(now2)
# now3 = now.strftime('%H:%M:%S') # 내가 원하는 형식으로, 현재 시간
# print(now3)

now4 = now.strftime('%y/%m/%d/%A %I:%M %p') # %H 24시를 기준으로, %I 12시를 기준으로, %A 요일, %a 요일 축약
print(now4)