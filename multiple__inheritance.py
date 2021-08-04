class Addition:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def calculate(self):
        print(self.a + self.b)

class Subtraction:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def calculate(self):
        print(self.a-self.b)

class Result(Subtraction,Addition):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def calculate(self):
        print(self.a*self.b)
        super().calculate()

res = Result(20,10)
res.calculate()


