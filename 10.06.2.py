class Mobile:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(self.name)

class mobile_model1(Mobile):
    def __init__(self,name,model):
        super().__init__(name)
        self.model = model
    def display(self):
        super().display()
        print(self.model)

class mobile_model2(Mobile):
    def __init__(self,name,model):
        super().__init__(name)
        self.model = model
    def display(self):
        super().display()
        print(self.model)

class


