class Person:
    def __init__(self,name,job): #초기화자 - instance 생성 시 자동 호출 함수
        self.name = name
        self.job = job

    #클래스 속성 (초기값)
    # name = '홍길동'
    # gender = ' 성별'
    # age = 0

    company = "삼성"


    #method (멤버 함수)
    def name_print(self):
        print('내 이름 출력2 :', self.name)
        #self는 초기값 객체 , class를 가지고 있는 이름없는  instance 이름 = self

class Student(Person):
    def __init__(self, name, job , phoneNumber, studentID):
       self.name = name
       self.job = job
       self.phoneNumber = phoneNumber
       self.studentID = studentID


    def name_print2(self):
        print("내이름 출력2:", self.name)


st1 = Student('권율','회사원','1234-1234','1234567')

st1.name_print2()
st1.name_print()
print(st1.company)
print(st1.job)

# class student:
#     name ='학생이름'
#     grade ='학년'
#     school ='학교종류'
#     gender = '성별'
#     age=0

#per1 = Person('김유신') #instance 생성
#print(per1.name)
# #print(per1.name)
# per2 = Person('이순신', '장군')
# print(per2.name)
# print(per2.job)
# print(per2.company)


#per1.name_print() #method 호출

