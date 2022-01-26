#
# from moduletest import square
# from math import pow
# import pandas
# import numpy
#
# import moduletest as md
#
# print(square(10,20))
# pow(10,3)
#
#
# md.square(3.4)
#
a = '대한민국'
try:
    b=10/a
except ZeroDivisionError:
    print('0나누기 에러')
except TypeError:
    print('문자로 나누기 에러')
except:
    print('모든 에러:',e.args[0])

import pandas
