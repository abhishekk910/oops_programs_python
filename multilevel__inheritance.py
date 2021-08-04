class University:
    def __init__(self,university_name):
        self.university = university_name

class College(University):
    def __init__(self,university_name,college_name):
        self.college = college_name
        super().__init__(university_name)


class Branch(College):
    def __init__(self,university_name,college_name,branch_name):
        self.branch = branch_name
        super().__init__(university_name,college_name)

class Semester(Branch):
    def __init__(self,university_name,college_name,branch_name,semester):
        self.semester = semester
        super().__init__(university_name,college_name,branch_name)

    def display(self):
        print(self.university)
        print(self.college)
        print(self.branch)
        print(self.semester)


obj = Semester(university_name='VTU',college_name='CMRIT',branch_name='MECHANICAL',semester=7)
obj.display()




