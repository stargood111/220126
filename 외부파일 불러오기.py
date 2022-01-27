#텍스트 파일 쓰기
# f = open('data/test.txt','w')
# f.write('hello world!')
# f.close()

#텍스트 파일 내용 불러오기
try:
    f = open('data/test111.txt','r')
    test = f.read()
    f.close()

    test = test[5:10]
    print(test)
    if test == '123456789':
        print('비밀번호 체크 완료')
    else:
        print('비밀번호가 다릅니다')

except:
        print('불러오려는 파일이 없습니다')
