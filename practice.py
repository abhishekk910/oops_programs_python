class Student:

    def __init__(self,marks):
        self.marks=marks

    def __gt__(self, other):
        if self.marks > other.marks:
            return True
        else:
            return False

    def __str__(self):
        return str(self.marks)


s1 = Student(96)
s2 = Student(97)

if s1 > s2:
    print('s1 is greater')
else:
    print('s2 is greater')


print(s1)
print(s2)
