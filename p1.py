class demo:
    a=15
    b=25
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self)
obj1=demo(10,20)
obj2=demo(30,40)
print('-'*50)
print('obj1.a->',obj1.a,'obj1.b->',obj1.b)
print('obj2.a->',obj2.a,'obj2.b->',obj2.b)