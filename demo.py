class A:
    def __init__(self,b):
        self.b=b
        print('In A Constructor',self.b)

class B(A):
    x=10
    def __init__(self):
        print('In B Constructor')
        A.__init__(self,'x') #classname
        super().__init__('10')

obj = B()


