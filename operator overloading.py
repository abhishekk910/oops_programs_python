class Student:

    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        total = self.marks+other.marks
        s = Student(total)
        return s

    def __mul__(self, other):
        total = self.marks*other.marks
        s = Student(total)
        return s



    def __str__(self):
        return 'The marks got by student is : ' + str(self.marks)

s1 = Student(91)
s2 = Student(97)
s3 = Student(98)
s4 = Student(90)

print(s1+s2+s3+s4)
print(s1*s2+s3*s4)

