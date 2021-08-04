class A:
    def __init__(self):
        print('A init')
    def feature1(self):
        print('feature 1 A')
    def feature2(self):
        print('feature 2 A')

class B:
    def __init__(self):

        print('B init')

    def feature1(self):
        print('feature 1 B')
    def feature2(self):
        print('feature 2 B')


class C(B,A):
    def __init__(self):
        super().__init__()
        print('C init')

    def feature(self):
        super().feature2()
        super().feature1()


c1 = C()
c1.feature()





