class Student:
    def __init__(self,sname,sage,sid):
        self.sname = sname
        self.sage = sage
        self.sid = sid

class Test(Student):

    def getmarks(self):
        self.sclass = input('Enter the class')
        self.python = int(input("Enter marks :"))
        self.web = int(input('Enter marks :'))
        self.django = int(input('Enter marks:'))
        self.sql = int(input('Enter marks:'))

class Marks(Test):

    def display(self):
        print('name:',self.sname)
        print('age:',self.sage)
        print('id:',self.sid)
        print('total marks:',self.python+self.sql+self.web+self.django)

obj = Marks('Balu',25,'ba001')
obj.getmarks()
obj.display()
