'''class Person:
    def __init__(self,name,id):
        self.name= name
        self.id = id
    def display(self):
        print(self.id)
        print(self.name)

class Student(Person):
    def __init__(self,name,id,college,marks):
        super().__init__(id,name)
        self.college= college
        self.marks = marks
    def display(self):
        super().display()
        print(self.marks)
        print(self.college)

class Employee(Person):
    def __init__(self,name,id,company,salary):
        super().__init__(id,name)
        self.company = company
        self.salary = salary
    def display(self):
        super().display()
        print(self.company)
        print(self.salary)


obj = Student(1,'balu','vtu',95)
obj.display()
obj = Employee(2,'ramu','tcs',34000)
obj.display()'''

'''def display(*a):
    print(a)
display(1,2,3)
display(2,'hello')
display([1,2,3],(1,2,3),{'a':1,'b':2})'''

class Vehicle:
    def __init__(self,company_name):
        self.company_name = company_name
    def display(self):
        print('company name : ',self.company_name)

class Car(Vehicle):
    def __init__(self,company_name,model,fuel_type,price):
        super().__init__(company_name)
        self.model = model
        self.fuel_type = fuel_type
        self.price = price
    def display(self):
        super().display()
        print('model : ',self.model)
        print('fuel_type : ',self.fuel_type)
        print('price : ',self.price)

class Bike(Vehicle):
    def __init__(self,company_name,model,fuel_type,price):
        super().__init__(company_name)
        self.model = model
        self.fuel_type = fuel_type
        self.price = price
    def display(self):
        super().display()
        print('model : ',self.model)
        print('fuel_type : ',self.fuel_type)
        print('price : ',self.price)

car1 = Car('Maruti','Swift','Petrol',600000)
bike1 = Bike('Yamaha','MT 15','Petrol',140000)
car1.display()
bike1.display()




