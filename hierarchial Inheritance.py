class Parent:
    def function1(self):
        print('This is parent class method')

class Child1(Parent):
    def function2(self):
        print('This is Child1 Class Method')

class Child2(Parent):
    def function3(self):
        print('This is Child2 Class method')

c1 = Child1()
c1.function1()
c1.function2()

c2 = Child2()
c2.function1()
c2.function3()
