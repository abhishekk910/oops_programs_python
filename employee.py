class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary




class TimeSheet:

    def __init__(self,name,days):
        self.name=name
        self.days=days

    def __mul__(self, other):
        return self.days * other.salary

    def __str__(self):
        return self.name

e1 = Employee('balu',1000)
t1 = TimeSheet('balu',25)

print('Total Salary of Month is : ',t1*e1)

print(t1)

