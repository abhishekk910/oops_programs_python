from abc import ABC,abstractmethod

class Calculation(ABC):
    def __init__(self,value):
        self.value = value

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

class A(Calculation):
    def add(self):
        print(self.value+100)

class B(A):
    def add(self):
        print(self.value+200)
        super().add()
    def sub(self):
        print(self.value-10)

obj = B(200)
obj.add()
obj.sub()