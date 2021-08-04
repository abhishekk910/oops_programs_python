'''class Student:

    def sum(self,a=None,b=None,c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s

s = Student()
print(s.sum(1,9,10))'''
class Methodoverload:
    def add(self,a=None,b=None):
        if a!=None and b!=None:
            print(a+b)
        elif a!=None:
            print(a)
s=Methodoverload()
s.add()
s.add(10)
s.add(10,20)

