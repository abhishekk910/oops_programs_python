#Hybrid Inheritance
'''class A:
    def function1(self):
        print('This function is in class A ')

class B(A):
    def function2(self):
        print('This function is in class B')

class C(A):
    def function2(self):
        print('This function is in class C')

class D(C,B):
    def function4(self):
        super().function1()
        super().function2()
        print('This function is in class D')

d1 = D()
d1.function4()'''
class Company:
    def __init__(self,req):
        self.req = req

class Development(Company):
    def __init__(self,req,dev_id):
        self.dev_id = dev_id
        super().__init__(req)

class Testing(Company):
    def __init__(self,req,test_id):
        self.test_id = test_id

class Project(Development,Testing):
    def __init__(self,project_id,project_name,dev_id,req):
        self.project_id = project_id
        self.project_name = project_name
        super().__init__(req,dev_id)
    def display(self):
        print(self.project_id)
        print(self.project_name)
        print(self.req)
        print(self.dev_id)


c = Project('1','abc','2',2)
c.display()



