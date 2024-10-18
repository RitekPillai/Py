"""
import geometry

num=5
square = geometry.square_are(5)
circle = geometry.circle_area(5)
print(square)
print(circle)
"""
def dividenum(num,num1):
    try:
        return num/num1
    except ZeroDivisionError:
        print("zero division error")
    except TypeError:
        print("Type error")
    except Exception as e:
        print("Exception error",{e})


num=0
num1=0
dividenum(num,num1)