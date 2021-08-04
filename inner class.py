class College:

    def __init__(self,dept,student):
        self.dept = dept
        self.student = student
        self.faculty = self.Faculty()


    def display(self):
        print(self.student,self.dept)
        self.faculty.display()


    class Faculty:
        def __init__(self):
            self.id = 110
            self.salary = 50000

        def display(self):
            print(self.id,self.salary)

s1 = College('cse','balu')

s1.display()