# 정규식을 이용해서 숫자, 공백 지우고, 필요한 것만 빼오고 ...

import re


# 문자열에서 숫자 제거
#data = 'ejrlk423jfkjlfjsd0f2lkqwa0394239roefd'
#newdata = re.sub(r'[0-9]+','',data)
# newdata = re.빼주기(r'[숫자를 찾아서]','이걸로 바꿔줌',이 데이터에서)
#print(newdata)

# 문자열에서 숫자만 가져오기
data = 'ejrlk423jfkjlfjsd0f2lkqwa0394239roefd'
newdata = re.sub(r'[^0-9]+','',data)
# newdata = re.빼주기(r'[숫자를 제외한 나머지를 찾아서]','이걸로 바꿔줌',이 데이터에서)
print(newdata)

# 문자열에서 특수문자 제거
data2 = 'rjkl;23[u9wfgij3$%@#^^T(WR#WEUPAFJsdjglh3wt9gsckh'
newdata2 = re.sub('[~!@#$%^&*()_+-=`]','', data2)
print(newdata2)

# 문자열에서 한글만 가져오기
data3 = 'sfwelkfdㄴ안welf녕ewkl;f하elkf세qkwjhqawsd요we@'
newdata3 = re.sub('[^ㄱ-ㅣ가-힣]','',data3)
print(newdata3)

print(re.sub('[-]','','123456-4567897'))