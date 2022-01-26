#while 문
#a = 10
#while a >= 5:
#  print(a)
#  a = a-1

#for문 연습
#List1= [10,100,1000,2000] # 시퀀스형 객체(리스트)

#for i in List1: # 시퀀스 객체인 List1에 원소를 순서대로 (회전시 ) 빼서 i에 저장 10-100-1000-2000
#  print(i)

#dic1={'apple':100,'orange':200,'banana':300} # 시퀀스형 객체(사전타입)

#for i,j in dic1.items(): #.items 시 변수 하나 추가 가능
 # print(j)

#for i in range(1,6):
# print(i)


#list2 = list(range (5,11,2)) # 5~10까지 숫자 중 2를 step으로 출력
#print(list2)

#tup1 = tuple(ragne(1,11)) #1~10까지 튜플로  출력
#print(tup1)

#for i in range(2,10):
#  print('구구단수:' , i)
#  for j in range(1,10): # 1~9까지 반복
#   print(f"{i} * {j} = {i*j}")

#a = 10.123456
#b = 100
#c = 1000
#print('a={0}, b={1}, c={2}'.format(a,b,c))
#print(f'a={a:.3f}, b={b}, c={c:,}원')

#for i in range(1,11):
# print(i)
# if i == 5:
#    print('i = ', i)
#    break


#a=10
#while a < 20:
#  a = a+1
#  print(a)
#  if a == 15:
#    break

#for i in range(1,11):
#    if i % 2 ==0:
#       continue
#    print(i)

List3 = List(range(1,6)) #1~5

List4 = [i**2 for i in list3]

print(list4)

List 4 =['apple','orange','banana']
List 5 =[len(i) for i in list4]