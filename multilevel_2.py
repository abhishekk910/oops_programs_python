class Grandfather():
    def __init__(self,gname):
        self.grandfather = gname

class Father(Grandfather):
    def __init__(self,gname,fname):
        self.father = fname
        super().__init__(gname)

class Son(Father):
    def __init__(self,gname,fname,son):
        self.son = son
        super().__init__(gname,fname)

    def display_name(self):
        print('son name-->',self.son,'Father name -->',self.father,'Grandfather name-->',self.grandfather)

obj = Son('Rajayya','RajaKumara','Rajs')
obj.display_name()

