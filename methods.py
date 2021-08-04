class Student:
    branch = 'mech'
    def __init__(self,name,id,email):
        self.name=name
        self.id=id
        self.email=email


    @classmethod
    def getclass(cls):
        print(cls.branch)

    @classmethod
    def setclass(cls):
        modify = input("enter yes if branch needed to change")
        if modify == 'yes':
            cls.branch=input("enter the branch")
            cls.getclass()
        else:
            print("no data to be modified")

    def getobj(self):
        print(self.name)
        print(self.branch)
        print(self.id)
        print(self.email)

    def setobj(self):
        self.name=input("enter name:")
        self.getobj()

    @staticmethod
    def callstatic():
        print("static method called")

s1=Student('balayya',9,'balu@gmail')
#Student.setclass()
Student.setobj(s1)

s1.callstatic()
Student.callstatic()
