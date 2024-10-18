"""
class Student:
    def __init__(self,name,age,rollno,marks):
        self.name=name
        self.age=age,
        self.rollno=rollno
        self.marks=marks
        
    def display(self):
        print("Student Information:")
        print("Name:",self.name)
        print("Rollno:",self.rollno)
        print("Marks:",self.marks)
        print("Age:",self.age)
        print(self)

s=Student("ritek",19,36,1000)

s2=Student("ritek",19,36,1000)
s.display()
7b
class room:
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
class Area(room):
    def __init__(self,l,b,h):
        super().__init__(l,b,h)
        print("Area of the room is",self.l*self.b)

class Volume(Area):
    def __init__(self,l,b,h):
       
        super().__init__(l,b,h)
        print("Volume of a room is",self.l*self.b*self.h)

v=Volume(10,20,30)

"""
class Numbers:
    mulitpler=5
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    @classmethod
    def mul(cls,a):
        return cls.mulitpler*a
    @staticmethod
    def subtract(b,c):
        return b-c

n=Numbers(10,20)
print(n.add())
print(n.mul(5))
print(Numbers.subtract(10,2))
