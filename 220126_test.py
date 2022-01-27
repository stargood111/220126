# 원을 나타 내는 Circle 이라는 클래스를 설계하고,
# 반지름 radius와 중심좌표 x,y 를 입력 받아
# 원의 넓이를 반환 하는 메소드 area와 원의 중심을 반환 하는 메소드 center를 구현하시오.
# (단, pi는 math 모듈에서 호출한다.)

# 클래스를 완성한 후 객체 circle1을 생성하여
# 임의의 원의 반지름과 그 중심좌표 x,y를 입력 받아 원의 넓이와 그 중심좌표값을 화면애 출력하시오.

import math

from numpy import double


class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def area(self):
        return self.radius * self.radius * math.pi

    def center(self):
        return self.x, self.y

print("원의 정보를 입력하세요.")
radius = double(input('반지름 입력:'))
cx = int(input('중심좌표 x 입력 :'))
cy = int(input('중심좌표 y 입력 :'))
circle1 = Circle(radius,cx,cy)

print("원의 넓이 : ", circle1.area())
print("중심 좌표 : ", circle1.center())